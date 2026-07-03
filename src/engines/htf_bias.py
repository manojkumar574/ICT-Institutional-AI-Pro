import pandas as pd

class HTFBiasEngine:

    def get_bias(self, df):

        close = float(df["Close"].iloc[-1])

        sma20 = pd.to_numeric(df["Close"]).tail(20).mean()

        if close > sma20:
            return "BULLISH"

        elif close < sma20:
            return "BEARISH"

        else:
            return "NEUTRAL"