"""
FastAPI application that reflects the request.

"""

import typing

import fastapi
import fastapi.middleware.cors

from . import __version__


app = fastapi.FastAPI(
    title="Example",
    description=__doc__,
    version=__version__,
    license_info={"name":"GPLv3", "url":"https://www.gnu.org/licenses/gpl-3.0.en.html"},
    openapi_url="/api/v1/openapi.json",
    docs_url="/api",
)

app.add_middleware(
    fastapi.middleware.cors.CORSMiddleware,
    allow_origins=[
        "*",
    ],
    allow_credentials=True,
    allow_methods=[
        "GET",
        "HEAD",
    ],
    allow_headers=[
        "*",
    ],
)

def request_to_response(request: fastapi.Request) -> typing.Dict[str, typing.Any]:
    response = {
        "url": request.url._url,
        "method": request.method,
        "headers": request.headers
    }
    return response

@app.get("/favicon.ico", include_in_schema=False)
async def get_favicon():
    raise fastapi.HTTPException(status_code=404, detail="Not found")

@app.get("/")
def echo_get(request:fastapi.Request):
    return request_to_response(request)

@app.head("/")
def echo_head(request:fastapi.Request):
    return request_to_response(request)

@app.post("/")
def echo_post(request:fastapi.Request):
    return request_to_response(request)
