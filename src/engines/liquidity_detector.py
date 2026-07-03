import pandas as pd


class LiquidityDetector:

    def detect_equal_highs(self, df, tolerance=0.001):
        """
        Detect Equal Highs (EQH)
        """

        df = df.copy()
        df["High"] = pd.to_numeric(df["High"])

        equal_highs = []

        for i in range(1, len(df)):
            high1 = df["High"].iloc[i - 1]
            high2 = df["High"].iloc[i]

            if abs(high1 - high2) / high1 <= tolerance:
                equal_highs.append({
                    "index": i,
                    "price": high2
                })

        return equal_highs

    def detect_equal_lows(self, df, tolerance=0.001):
        """
        Detect Equal Lows (EQL)
        """

        df = df.copy()
        df["Low"] = pd.to_numeric(df["Low"])

        equal_lows = []

        for i in range(1, len(df)):
            low1 = df["Low"].iloc[i - 1]
            low2 = df["Low"].iloc[i]

            if abs(low1 - low2) / low1 <= tolerance:
                equal_lows.append({
                    "index": i,
                    "price": low2
                })

        return equal_lows