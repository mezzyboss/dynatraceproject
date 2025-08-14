# stress_test.py
import requests
import random

for _ in range(50):
    side = random.choice(["BUY", "SELL"])
    try:
        res = requests.post("http://localhost:8000/order", json={
            "symbol": "AAPL",
            "qty": random.randint(1, 100),
            "side": side
        })
        print(res.json())
    except Exception as e:
        print("Error:", e)