from fastapi import FastAPI,Response,status
from api.v1.api import api_router as api_v1

app = FastAPI(title="Character Engine API")

@app.get("/health",status_code=status.HTTP_204_NO_CONTENT)
def status_check():
    return Response(status_code=status.HTTP_204_NO_CONTENT)

app.include_router(api_v1, prefix="/api/v1")

