import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))

from ai.decision_engine import DecisionEngine

engine = DecisionEngine()

result = engine.decide(
    bias="BULLISH",
    liquidity_sweep=True,
    mss={"direction": "BULLISH"},
    fvg=True,
    order_block=True,
    killzone=True,
)

print("=" * 50)
print("ICT AI DECISION TEST")
print("=" * 50)
print(result)