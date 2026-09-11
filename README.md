# Ecommerce Product API

A small HTTP API backed by the existing SQLite product database.

## Run

```bash
python -m ecommerce_api.main
```

The server listens on port `8000`.

## Endpoint

```http
GET /products?skip=0&limit=10&category=electronics
```

Query parameters:

- `skip` — number of matching products to skip (default: `0`)
- `limit` — maximum products to return (default: `10`)
- `category` — optional exact category filter

Successful requests return `200 OK` with a JSON array.

## Test

```bash
python -m unittest discover -s tests
```