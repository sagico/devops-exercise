from ...coin_exchange import CoinExchangeError


class ExchangeRateAPIError(CoinExchangeError):
    pass


class InvalidAPIKey(ExchangeRateAPIError):
    pass


class ExceededAPIQuota(ExchangeRateAPIError):
    pass


class UnexpectedResponse(ExchangeRateAPIError):
    pass
