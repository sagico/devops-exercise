from fastapi import FastAPI
from loguru import logger

from .config import CoinMasterSettings
from .router import router


def create_app() -> FastAPI:
    settings = CoinMasterSettings()
    logger.info(f"Starting Coin Master API URL={settings.exchange_base_url} API_KEY={settings.exchange_api_key}")
    app = FastAPI()
    app.include_router(router=router)
    
    return app
