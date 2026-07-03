import pandas as pd


class MarketStructure:

    def detect_bullish_mss(self, df):

        df = df.copy()

        df["High"] = pd.to_numeric(df["High"])
        df["Low"] = pd.to_numeric(df["Low"])

        recent_high = df["High"].iloc[-2]
        current_high = df["High"].iloc[-1]

        return current_high > recent_high

    def detect_bearish_mss(self, df):

        df = df.copy()

        df["High"] = pd.to_numeric(df["High"])
        df["Low"] = pd.to_numeric(df["Low"])

        recent_low = df["Low"].iloc[-2]
        current_low = df["Low"].iloc[-1]

        return current_low < recent_low