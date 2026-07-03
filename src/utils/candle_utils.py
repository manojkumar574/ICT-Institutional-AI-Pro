import pandas as pd


class CandleUtils:

    @staticmethod
    def to_numeric(df):
        columns = ["Open", "High", "Low", "Close", "Volume"]

        for col in columns:
            df[col] = pd.to_numeric(df[col])

        return df

    @staticmethod
    def last_close(df):
        return float(df["Close"].iloc[-1])

    @staticmethod
    def last_high(df):
        return float(df["High"].iloc[-1])

    @staticmethod
    def last_low(df):
        return float(df["Low"].iloc[-1])
        import pandas as pd


def prepare_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """
    Prepare Binance OHLC dataframe for analysis.
    """

    df = df.copy()

    numeric_columns = [
        "Open",
        "High",
        "Low",
        "Close",
        "Volume"
    ]

    for col in numeric_columns:
        df[col] = pd.to_numeric(df[col])

    return df
