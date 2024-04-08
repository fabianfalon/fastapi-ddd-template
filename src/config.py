from pydantic.v1 import BaseSettings


class CommonSettings(BaseSettings):
    app_title: str = "DDD Fastapi Microservice"
    app_name: str = "fastapi"
    debug: bool = False
    swagger_url: str = "/docs"


class ServerSettings(BaseSettings):
    """
    Gunicorn server settings
    """

    host: str = "127.0.0.1"
    port: int = 5000
    workers_per_core: int = 1
    max_workers: int | None = None
    log_level: str = "warning"
    graceful_timeout: int = 120
    timeout: int = 120
    keep_alive: int = 5


class LocationSettings(BaseSettings):
    timezone: str = "Europe/Madrid"


class Settings(CommonSettings, ServerSettings, LocationSettings): ...


settings = Settings()
