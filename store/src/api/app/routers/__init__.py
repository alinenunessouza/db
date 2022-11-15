"""
    API routers.
    (FastAPI routers)
"""

from typing import Union

from fastapi import FastAPI

app = FastAPI()

from . import utils

def include_routers(app: FastAPI) -> None:
    """
    Registers (Including) FastAPI routers for FastAPI app.
    """

    for module in [utils]:
        app.include_router(module.router)
