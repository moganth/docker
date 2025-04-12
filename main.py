from fastapi import FastAPI
import uvicorn
from routes.docker_routes import router as docker_router

app = FastAPI(title="Docker Controller API")
app.include_router(docker_router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=1243, reload=True)
