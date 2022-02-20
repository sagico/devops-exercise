from fastapi import APIRouter, Depends
from pydantic import BaseModel

from .coin_exchange import CoinExchange
from .dependencies import coin_exchange

router = APIRouter(tags=["Currency Rate"])


class ExchangeRateResponse(BaseModel):
    rate: float


@router.get("/rate/{from_currency}/{to_currency}", response_model=ExchangeRateResponse)
async def get_exchange_rate(
    from_currency: str,
    to_currency: str,
    exchange: CoinExchange = Depends(coin_exchange),
):
    rate = await exchange.check_rate(from_currency, to_currency)
    return ExchangeRateResponse(rate=rate)
