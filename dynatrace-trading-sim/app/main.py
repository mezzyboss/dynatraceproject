import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from .simulator import TradingSimulator

app = FastAPI(title="Dynatrace Trading Simulator")

# Read from env vars with defaults
FAULT_RATE = float(os.getenv("FAULT_RATE", 0.2))
LATENCY_MS = int(os.getenv("LATENCY_MS", 100))

sim = TradingSimulator(fault_rate=FAULT_RATE, latency_ms=LATENCY_MS)

class OrderRequest(BaseModel):
    symbol: str
    qty: int
    side: str

@app.get("/price/{symbol}")
def price(symbol: str):
    return {"symbol": symbol, "price": sim.get_price(symbol)}

@app.post("/order")
def order(req: OrderRequest):
    try:
        result = sim.place_order(req.symbol, req.qty, req.side)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))