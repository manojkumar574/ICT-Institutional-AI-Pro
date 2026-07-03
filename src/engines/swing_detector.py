import pandas as pd

class SwingDetector:

    def detect_swings(self, df, lookback=2):

        df = df.copy()

        df["High"] = pd.to_numeric(df["High"])
        df["Low"] = pd.to_numeric(df["Low"])

        swing_highs = []
        swing_lows = []

        for i in range(lookback, len(df) - lookback):

            high = df["High"].iloc[i]
            low = df["Low"].iloc[i]

            if high == max(df["High"].iloc[i-lookback:i+lookback+1]):
                swing_highs.append((i, high))

            if low == min(df["Low"].iloc[i-lookback:i+lookback+1]):
                swing_lows.append((i, low))

        return swing_highs, swing_lows