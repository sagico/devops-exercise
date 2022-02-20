from pydantic import BaseSettings


class CoinMasterSettings(BaseSettings):
    exchange_api_key: str
    exchange_base_url: str

    class Config:
        env_file = ".env"
