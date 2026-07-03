from binance.client import Client
import pandas as pd


class MarketData:

    def __init__(self):
        self.client = Client()

    def get_klines(self, symbol="BTCUSDT", interval="1h", limit=10):

        klines = self.client.get_klines(
            symbol=symbol,
            interval=interval,
            limit=limit
        )

        df = pd.DataFrame(
            klines,
            columns=[
                "Open Time", "Open", "High", "Low", "Close", "Volume",
                "Close Time", "Quote Asset Volume", "Trades",
                "Taker Buy Base", "Taker Buy Quote", "Ignore"
            ]
        )

        from utils.candle_utils import prepare_dataframe
        return df[
            ["Open Time", "Open", "High", "Low", "Close", "Volume"]
        ]

    def get_multi_timeframe_data(self, symbol="BTCUSDT", limit=500):

        timeframes = {
            "weekly": Client.KLINE_INTERVAL_1WEEK,
            "daily": Client.KLINE_INTERVAL_1DAY,
            "4h": Client.KLINE_INTERVAL_4HOUR,
            "1h": Client.KLINE_INTERVAL_1HOUR,
            "15m": Client.KLINE_INTERVAL_15MINUTE,
            "5m": Client.KLINE_INTERVAL_5MINUTE,
            "1m": Client.KLINE_INTERVAL_1MINUTE
        }

        data = {}

        for name, interval in timeframes.items():

            df = self.get_klines(
                symbol=symbol,
                interval=interval,
                limit=limit
            )

            data[name] = df

        return data
        df = prepare_dataframe(df)

return df[
    [
        "Open Time",
        "Open",
        "High",
        "Low",
        "Close",
        "Volume"
    ]
]
