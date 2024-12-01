from fastapi import FastAPI, APIRouter
from fastapi.staticfiles import StaticFiles
import httpx
from contextlib import asynccontextmanager

from app.routes.home_routes import router as home_router
from app.routes.todo_routes import router as todo_router
from app.routes.product_routes import router as product_router

main_router = APIRouter()

main_router.include_router(home_router)
main_router.include_router(todo_router, prefix="/todo", tags=["todo"])
main_router.include_router(product_router, prefix="/product", tags=["product"])


# https://stackoverflow.com/questions/71031816/how-do-you-properly-reuse-an-httpx-asyncclient-within-a-fastapi-application
# https://medium.com/@benshearlaw/how-to-use-httpx-request-client-with-fastapi-16255a9984a4

@asynccontextmanager
async def lifespan(app: FastAPI):
    app.requests_client = httpx.AsyncClient()
    yield
    await app.requests_client.aclose()


# create app instance
app = FastAPI(lifespan=lifespan)


# add route for static files
app.mount(
    "/static",
    StaticFiles(directory="app/static"),
    name="static",
)

# include routes in app
app.include_router(main_router)
