class CoinExchangeError(Exception):
    pass


class CurrencyNotFound(CoinExchangeError):
    pass
