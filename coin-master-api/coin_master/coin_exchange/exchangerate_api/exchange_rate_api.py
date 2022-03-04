import functools
from contextlib import asynccontextmanager
from http.client import BAD_REQUEST, FORBIDDEN, NOT_FOUND
from typing import Iterator

import aiohttp
from structlog import get_logger

from ...coin_exchange import CurrencyNotFound
from ..coin_exchange import CoinExchange
from .exceptions import ExceededAPIQuota, InvalidAPIKey, UnexpectedResponse

logger = get_logger()


def catch_unexpected_reponse(method):
    @functools.wraps(method)
    async def wrapped(*args, **kwargs):
        try:
            return await method(*args, **kwargs)
        except KeyError as e:
            missing = e.args[0]
            raise UnexpectedResponse(f'could not found key "{missing}"')

    return wrapped


class ExchangeRateAPI(CoinExchange):
    api_key: str
    session: aiohttp.ClientSession

    def __init__(self, session: aiohttp.ClientSession, api_key: str):
        self.api_key = api_key
        self.session = session

    @asynccontextmanager
    async def _get(self, url: str) -> Iterator[aiohttp.ClientResponse]:
        async with self.session.get(f"/v6/{self.api_key}{url}") as response:
            logger.debug(
                "Calling ExchangeRate API",
                exchange_rate_api_path=url,
                status=response.status,
            )
            if response.status == FORBIDDEN:
                raise InvalidAPIKey()

            yield response

    @catch_unexpected_reponse
    async def check_rate(self, from_currency: str, to_currency: str) -> float:
        async with self._get(f"/pair/{from_currency}/{to_currency}") as response:
            if response.status in [BAD_REQUEST, NOT_FOUND]:
                raise CurrencyNotFound()

            response_data = await response.json()

            return response_data["conversion_rate"]

    @catch_unexpected_reponse
    async def check_health(self) -> True:
        async with self._get("/quota") as response:
            response.raise_for_status()
            response_data = await response.json()

            if not response_data["requests_remaining"]:
                raise ExceededAPIQuota()

            return True
