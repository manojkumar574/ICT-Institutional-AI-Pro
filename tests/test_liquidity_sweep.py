import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))

from core.market_data import MarketData
from engines.swing_detector import SwingDetector
from engines.liquidity_sweep import LiquiditySweep


market = MarketData()

df = market.get_klines(
    symbol="BTCUSDT",
    interval="1h",
    limit=500
)

detector = SwingDetector()

highs, lows = detector.detect_swings(df)

engine = LiquiditySweep()

sweeps = engine.detect(df, highs, lows)

print("=" * 50)
print("LIQUIDITY SWEEP TEST")
print("=" * 50)

print("Total Sweeps:", len(sweeps))

if sweeps:
    print("Latest Sweep:", sweeps[-1])