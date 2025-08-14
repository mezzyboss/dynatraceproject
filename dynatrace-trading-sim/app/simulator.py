import logging
from pythonjsonlogger.json import JsonFormatter
import random
import time

logger = logging.getLogger("trading_sim")
logHandler = logging.StreamHandler()
formatter = JsonFormatter()
logHandler.setFormatter(formatter)
logger.addHandler(logHandler)
logger.setLevel(logging.INFO)

class TradingSimulator:
    def __init__(self, fault_rate=0.1, latency_ms=50):
        self.fault_rate = fault_rate
        self.latency_ms = latency_ms

    def get_price(self, symbol: str) -> float:
        time.sleep(self.latency_ms / 1000)
        return round(random.uniform(100, 200), 2)

    def place_order(self, symbol: str, qty: int, side: str) -> dict:
        start = time.time()
        fault = False

        if random.random() < self.fault_rate:
            fault = True
            logger.error({"event": "order_failed", "symbol": symbol, "side": side})
            raise Exception("Simulated trading engine failure")

        price = self.get_price(symbol)
        latency = (time.time() - start) * 1000

        logger.info({
            "event": "order_filled",
            "symbol": symbol,
            "qty": qty,
            "side": side,
            "price": price,
            "latency_ms": latency,
            "fault_occurred": fault
        })

        return {
            "symbol": symbol,
            "qty": qty,
            "side": side,
            "price": price,
            "status": "FILLED"
        }