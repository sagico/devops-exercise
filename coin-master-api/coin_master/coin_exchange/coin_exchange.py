from abc import ABC, abstractmethod


class CoinExchange(ABC):
    @abstractmethod
    async def check_rate(self, from_currency: str, to_currency: str) -> float:
        raise NotImplementedError()

    @abstractmethod
    async def check_health(self) -> bool:
        raise NotImplementedError()
