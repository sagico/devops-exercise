from fastapi import FastAPI

from .config import CoinMasterSettings
from .router import router


def validate_configuration():
    CoinMasterSettings()


def create_app() -> FastAPI:
    validate_configuration()
    app = FastAPI()
    app.include_router(router=router)
    
    return app
