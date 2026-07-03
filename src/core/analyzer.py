from core.market_data import MarketData
from engines.htf_bias import HTFBiasEngine
from engines.liquidity_detector import LiquidityDetector
from engines.market_structure import MarketStructure


class Analyzer:

    def __init__(self):
        self.market = MarketData()
        self.bias_engine = HTFBiasEngine()
        self.liquidity = LiquidityDetector()
        self.structure = MarketStructure()

    def analyze(self, symbol="BTCUSDT"):

        df = self.market.get_klines(
            symbol=symbol,
            interval="1h",
            limit=500
        )

        bias = self.bias_engine.get_bias(df)

        eqh = self.liquidity.detect_equal_highs(df)
        eql = self.liquidity.detect_equal_lows(df)

        bullish = self.structure.detect_bullish_mss(df)
        bearish = self.structure.detect_bearish_mss(df)

        return {
            "symbol": symbol,
            "bias": bias,
            "equal_highs": len(eqh),
            "equal_lows": len(eql),
            "bullish_mss": bullish,
            "bearish_mss": bearish
        }