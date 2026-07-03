import pandas as pd


class LiquidityEngine:

    def find_swing_highs(self, df, lookback=2):
        swings = []

        df = df.copy()
        df["High"] = pd.to_numeric(df["High"])

        for i in range(lookback, len(df) - lookback):
            current = df["High"].iloc[i]

            left = df["High"].iloc[i - lookback:i]
            right = df["High"].iloc[i + 1:i + lookback + 1]

            if current > left.max() and current > right.max():
                swings.append(i)

        return swings

    def find_swing_lows(self, df, lookback=2):
        swings = []

        df = df.copy()
        df["Low"] = pd.to_numeric(df["Low"])

        for i in range(lookback, len(df) - lookback):
            current = df["Low"].iloc[i]

            left = df["Low"].iloc[i - lookback:i]
            right = df["Low"].iloc[i + 1:i + lookback + 1]

            if current < left.min() and current < right.min():
                swings.append(i)

        return swings