from http.client import INTERNAL_SERVER_ERROR, NOT_FOUND, SERVICE_UNAVAILABLE
from fastapi import APIRouter, Depends, HTTPException
from structlog import get_logger
from structlog.threadlocal import bound_threadlocal
from pydantic import BaseModel

from .coin_exchange import CoinExchange, CoinExchangeError, CurrencyNotFound
from .dependencies import coin_exchange


logger = get_logger()


class ExchangeRateResponse(BaseModel):
    rate: float


class ExchangeHealthResponse(BaseModel):
    healthy: bool


def make_error(message: str) -> dict[str, str]:
    return {
        "message": message
    }


router = APIRouter(tags=["Currency Rate"], responses={
    NOT_FOUND: make_error("currency not found"),
    INTERNAL_SERVER_ERROR: make_error("internal server error"),
    SERVICE_UNAVAILABLE: make_error("service is currently unavailable"),
})


@router.get("/rate/{from_currency}/{to_currency}", response_model=ExchangeRateResponse)
async def get_exchange_rate(
    from_currency: str,
    to_currency: str,
    exchange: CoinExchange = Depends(coin_exchange),
):
    with bound_threadlocal(from_currency=from_currency, to_currency=to_currency):
        try:
            rate = await exchange.check_rate(from_currency, to_currency)
            return ExchangeRateResponse(rate=rate)
        except CurrencyNotFound:
            raise HTTPException(NOT_FOUND)
        except CoinExchangeError:
            logger.exception("Failed to get rate from exchange")
            raise HTTPException(SERVICE_UNAVAILABLE)


@router.get("/health", response_model=ExchangeHealthResponse)
async def check_exchange_health(
    exchange: CoinExchange = Depends(coin_exchange),
):
    try:
        healthy = await exchange.check_health()
        return ExchangeHealthResponse(healthy=healthy)
    except CurrencyNotFound:
        raise HTTPException(NOT_FOUND)
    except CoinExchangeError:
        logger.exception("Health check failed for coin exchange")
        raise HTTPException(SERVICE_UNAVAILABLE)
