from app.boostrap import settings
from estimator.entrypoints import api
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

origins = settings.cors.split(",")


app = FastAPI()

"""
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)"""

app.include_router(api.api_router)

from starlette.middleware.cors import CORSMiddleware

origins = ["*"]
app = CORSMiddleware(
    app=app,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=1212)
