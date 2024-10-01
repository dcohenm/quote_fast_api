from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.routes import router
from app.database import create_index

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: create index
    await create_index()
    yield
    # Shutdown: you can add cleanup code here if needed

app = FastAPI(lifespan=lifespan)

app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
