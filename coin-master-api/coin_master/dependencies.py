import aiohttp

from fastapi import Depends

from .coin_exchange import CoinExchange, ExchangeRateAPI
from .config import CoinMasterSettings


def coin_master_settings() -> CoinMasterSettings:
    return CoinMasterSettings()


async def coin_exchange(settings: CoinMasterSettings = Depends(coin_master_settings)) -> CoinExchange:
    async with aiohttp.ClientSession(base_url=settings.exchange_base_url) as session:
        yield ExchangeRateAPI(session=session, api_key=settings.exchange_api_key)
