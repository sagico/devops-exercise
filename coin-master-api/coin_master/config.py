from pydantic import BaseSettings


class CoinMasterSettings(BaseSettings):
    exchange_api_key: str
    exchange_base_url: str
    log_level: str = "INFO"
    json_logging: bool = False

    class Config:
        env_file = ".env"
