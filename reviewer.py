from fastapi import FastAPI, Path, Query

app = FastAPI()

@app.post("/items/{item_id}")
async def create_item(item_id: int = Path(...,  gt=0), price: float = Query(..., gt=0.0)):
    return {"item_id": item_id, "price": price}

@app.get("/check")
async def check(flag: bool = Query(False)):
  return {"flag": flag} 