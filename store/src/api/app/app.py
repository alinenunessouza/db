"""
    API server application entry point.
    Provides FastAPI server.
    Should be run from external process (Manual uvicorn or by default as docker).
"""

from fastapi import FastAPI

from .routers import include_routers

if __name__ == "__main__":
    # You are not supposed to run this directly.
    # Raise error if tried to run from CLI directly.
    print(
        "ERROR: This application should be run with `Uvicorn` manually, or by Docker (Docker-Compose).\n"
    )
    print(
        "ERROR: Please use methods above, or search FastAPI application inside `/app.py`"
    )
    exit(1)


def _construct_app() -> FastAPI:
    """
    Returns FastAPI application ready to run.
    Creates base FastAPI instance with registering all required stuff on it.
    """

    app_instance = FastAPI(
        # Custom settings.
        # By default, modified by setters (below), or empty if not used.
        routes=None,
        middleware=None,
        exception_handlers=None,
        dependencies=None,
        responses=None,
        callbacks=None,
        # Event handlers.
        on_shutdown=None,
        on_startup=None,
        # Open API.
        title="title",
        version="1.0",
        description="description",
        # Other.
        root_path="/",
        root_path_in_servers=True,
    )
    
    # Initializing database connection and all ORM stuff.
    #TO DO

    # Register all internal stuff as routers/handlers/middlewares etc.
    include_routers(app_instance)

    return app_instance


# Root application for uvicorn runner or whatever else.
# (Docker compose is running with app.app:app, means that this application instance
# will be served by uvicorn, and will be constructed at import).
app = _construct_app()
