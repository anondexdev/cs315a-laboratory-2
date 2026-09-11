import json
import sqlite3
import tempfile
import threading
import unittest
from http.client import HTTPConnection
from http.server import ThreadingHTTPServer
from pathlib import Path
from unittest.mock import patch

from ecommerce_api.main import ProductAPIHandler


class ProductsEndpointTest(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.database_path = Path(self.temp_dir.name) / "products.db"
        with sqlite3.connect(self.database_path) as connection:
            connection.executescript(
                """
                CREATE TABLE product (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    description TEXT,
                    price REAL NOT NULL,
                    stock INTEGER NOT NULL,
                    category TEXT NOT NULL,
                    is_available BOOLEAN NOT NULL
                );
                INSERT INTO product VALUES
                    (1, 'Laptop', 'Portable computer', 999.0, 4, 'electronics', 1),
                    (2, 'Desk', 'Office desk', 250.0, 2, 'furniture', 1),
                    (3, 'Mouse', NULL, 25.0, 10, 'electronics', 0);
                """
            )

        self.path_patch = patch("ecommerce_api.main.DATABASE_PATH", self.database_path)
        self.path_patch.start()
        self.server = ThreadingHTTPServer(("127.0.0.1", 0), ProductAPIHandler)
        self.thread = threading.Thread(target=self.server.serve_forever, daemon=True)
        self.thread.start()

    def tearDown(self) -> None:
        self.server.shutdown()
        self.server.server_close()
        self.thread.join()
        self.path_patch.stop()
        self.temp_dir.cleanup()

    def request(self, path: str) -> tuple[int, object]:
        client = HTTPConnection("127.0.0.1", self.server.server_port)
        client.request("GET", path)
        response = client.getresponse()
        payload = json.loads(response.read())
        client.close()
        return response.status, payload

    def test_defaults_return_200(self) -> None:
        status, products = self.request("/products")
        self.assertEqual(status, 200)
        self.assertEqual(len(products), 3)

    def test_pagination_and_category_filter(self) -> None:
        status, products = self.request(
            "/products?skip=1&limit=1&category=electronics"
        )
        self.assertEqual(status, 200)
        self.assertEqual([product["name"] for product in products], ["Mouse"])

    def test_invalid_pagination_returns_422(self) -> None:
        status, payload = self.request("/products?skip=-1")
        self.assertEqual(status, 422)
        self.assertIn("skip", payload["detail"])


if __name__ == "__main__":
    unittest.main()