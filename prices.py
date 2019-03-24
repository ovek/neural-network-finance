import pandas_datareader.data as pdr
import fix_yahoo_finance as fix
fix.pdr_override()


def get_price(ticker, start_date, end_date):
    try:
        all_data = pdr.get_data_yahoo(ticker, start_date, end_date)
    except ValueError:
        print("ValueError, trying again")

    stock_data = all_data['Adj Close']
    stock_data.to_csv(ticker + ".csv")


if __name__ == "__main__":
    get_price("SPY", "2018-05-01", "2018-06-01")
