from fastapi import FastAPI
import uvicorn
from main import pop_artist
from main import access
from main import pop_track
from main import pop_album
from fastapi.responses import PlainTextResponse

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello"}


@app.get("/topartist", response_class=PlainTextResponse)
async def topartist():
    """Print the top five artists"""

    result = pop_artist()
    print(result)
    return result.to_string()


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")