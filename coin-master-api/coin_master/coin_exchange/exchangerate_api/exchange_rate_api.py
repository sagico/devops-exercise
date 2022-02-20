import aiohttp

from ..coin_exchange import CoinExchange


class ExchangeRateAPI(CoinExchange):
    api_key: str
    base_url: str
    session: aiohttp.ClientSession

    def __init__(self, session: aiohttp.ClientSession, api_key: str):
        self.api_key = api_key
        self.session = session

    async def check_rate(self, from_currency: str, to_currency: str) -> float:
        return 0.1
