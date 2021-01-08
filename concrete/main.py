import uvicorn
from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def main():
    return {"test": "1234"}


def run_application():
    uvicorn.run('concrete.main:app', host='0.0.0.0', port=9001, log_level='debug', reload=True)

if __name__ == "__main__":
    run_application()
