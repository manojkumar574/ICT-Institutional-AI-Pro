import pandas as pd


class LiquiditySweep:

    def detect(self, df, swing_highs, swing_lows):

        sweeps = []

        df = df.copy()

        df["High"] = pd.to_numeric(df["High"])
        df["Low"] = pd.to_numeric(df["Low"])
        df["Close"] = pd.to_numeric(df["Close"])

        # Buy-side Liquidity Sweep
        for idx, price in swing_highs:

            if idx + 1 >= len(df):
                continue

            next_candle = df.iloc[idx + 1]

            if next_candle["High"] > price and next_candle["Close"] < price:

                sweeps.append({
                    "type": "BUY_SIDE",
                    "index": idx + 1,
                    "price": price
                })

        # Sell-side Liquidity Sweep
        for idx, price in swing_lows:

            if idx + 1 >= len(df):
                continue

            next_candle = df.iloc[idx + 1]

            if next_candle["Low"] < price and next_candle["Close"] > price:

                sweeps.append({
                    "type": "SELL_SIDE",
                    "index": idx + 1,
                    "price": price
                })

        return sweeps