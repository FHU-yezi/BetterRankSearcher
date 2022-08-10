from sanic import Blueprint
from sanic.response import json

api = Blueprint("api", url_prefix="/api")


@api.get("/hello_world")
async def hello_world_handler(request):
    return json({
        "code": 200,
        "message": "Hello World!"
    })
