import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))

from core.market_data import MarketData
from engines.mss_v2 import MSSv2

market = MarketData()

df = market.get_klines(
    symbol="BTCUSDT",
    interval="1h",
    limit=500
)

engine = MSSv2()

result = engine.detect(df)

print("=" * 50)
print("MSS V2 TEST")
print("=" * 50)
print(result)