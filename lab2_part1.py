from fastapi import FastAPI, Query, Path

app = FastAPI()

prices_db: list[float] = [15.50, 99.99, 45.00, 250.00, 12.00, 500.25, 75.10]


@app.get("/prices")
async def get_price(
    min_price: float = Query(
        None,
        title="Minimum Prices",
        description="Prices that are at the minimum of the prices_db",
        ge=0.0,
    ),
    max_price: float = Query(
        None,
        title="Maximum Prices",
        description="Prices that are at the maximum of the prices_db",
        le=1000.00,
    ),
):
    filtered_prices = prices_db
    if min_price is not None:
        filtered_prices = [price for price in filtered_prices if price >= min_price]
    if max_price is not None:
        filtered_prices = [price for price in filtered_prices if price <= max_price]
    return {"filtered_prices": filtered_prices, "count": len(filtered_prices)}


employees_db: dict[int, str] = {
    1001: "Alice Johnson",
    1002: "Bob Smith",
    1003: "Charlie Davis",
}

@app.get("/employees/{emp_id}")
async def get_employee(
    emp_id: int = Path(
        title="Employee ID",
        description="4-digit internal employee code",
        ge=1000,
        lt=10000,
    ),
):
    if emp_id in employees_db:
        return {"emp_id": emp_id, "name": employees_db[emp_id]}
    else:
        return {"error": "Employee not found"}
