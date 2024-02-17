from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette.middleware.cors import CORSMiddleware

from apps.config import settings
from apps.shared.urls import router
from src.shared.domain.exceptions.base import DomainException
from src.shared.infrastructure.dependency_injector import init as init_dependencies

init_dependencies()

app = FastAPI(
    title=settings.PROJECT_NAME, openapi_url=f"{settings.API_PREFIX}/openapi.json"
)

if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(router, prefix=settings.API_PREFIX)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    data = ({"source": err["loc"][1], "msg": err["msg"]} for err in exc.errors())
    return JSONResponse({"detail": tuple(data)}, status_code=422)


@app.exception_handler(DomainException)
async def base_error_handler(request, exception):
    return JSONResponse({"detail": [dict(exception)]}, status_code=exception.code)
