from fastapi import FastAPI, Path, Query
from typing import Optional, Dict, Any

app = FastAPI()

accounts_db: Dict[int, Dict[str, Any]] = {
  501: {"owner": "Alice", "balance": 1200.00},
  502: {"owner": "Bob", "balance": 450.50}
}

@app.delete("/accounts/{acc_id}")
async def delete_account(
  acc_id: int = Path(..., gt=0)
):
  if acc_id not in accounts_db:
    return {"error": "JSON object not found"}
  del accounts_db[acc_id]
  return {"status": "deleted", "all_accounts": accounts_db}
