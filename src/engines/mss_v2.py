import pandas as pd


class MSSv2:

    def detect(self, df):

        df = df.copy()

        df["High"] = pd.to_numeric(df["High"])
        df["Low"] = pd.to_numeric(df["Low"])
        df["Close"] = pd.to_numeric(df["Close"])

        if len(df) < 5:
            return None

        last = df.iloc[-1]
        prev = df.iloc[-2]
        prev2 = df.iloc[-3]

        # Bullish MSS
        if (
            last["Close"] > prev["High"] and
            prev["Low"] > prev2["Low"]
        ):
            return {
                "direction": "BULLISH",
                "strength": "STRONG"
            }

        # Bearish MSS
        if (
            last["Close"] < prev["Low"] and
            prev["High"] < prev2["High"]
        ):
            return {
                "direction": "BEARISH",
                "strength": "STRONG"
            }

        return {
            "direction": "NONE",
            "strength": "NONE"
        }