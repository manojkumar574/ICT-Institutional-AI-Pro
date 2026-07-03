import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))

from core.market_data import MarketData
from engines.swing_detector import SwingDetector
from core.market_data import MarketData
from engines.swing_detector import SwingDetector

market = MarketData()
df = market.get_klines(
    symbol="BTCUSDT",
    interval="1h",
    limit=500
)

detector = SwingDetector()

highs, lows = detector.detect_swings(df)

print("=" * 50)
print("SWING DETECTOR TEST")
print("=" * 50)

print(f"Swing Highs: {len(highs)}")
print(f"Swing Lows : {len(lows)}")

if highs:
    print("Latest Swing High:", highs[-1])

if lows:
    print("Latest Swing Low :", lows[-1])