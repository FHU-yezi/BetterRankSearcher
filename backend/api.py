from sanic import Blueprint
from sanic.response import json

from utils.db_manager import data

api = Blueprint("api", url_prefix="/api")


@api.post("/data_info")
async def data_info_handler(request):
    newest_data_date = list(
        data.find({}, {"_id": 0, "date": 1})
        .sort("date", -1)
        .limit(1)
    )[0]["date"]
    newest_data_date = str(newest_data_date).split()[0]

    data_count = data.count_documents({})

    return json({
        "code": 200,
        "newest_data_date": newest_data_date,
        "data_count": data_count
    })


@api.post("/query_record")
async def query_record_handler(request):
    if not request.json:
        return json({
            "code": 400,
            "message": "请求必须带有 JSON Body"
        })

    body = request.json
    name = body.get("name")

    if not name:
        return json({
            "code": 400,
            "message": "缺少参数"
        })

    if data.count_documents({"author.name": name}) == 0:
        return json({
            "code": 400,
            "message": "用户不存在或无上榜记录"
        })

    data_list = []
    for item in data.find({"author.name": name}).sort("date", -1).limit(100):
        data_list.append({
            "date": str(item["date"]).split()[0],
            "ranking": item["ranking"],
            "article_title": item["article"]["title"],
            "article_url": item["article"]["url"],
            "reward_to_author": item["reward"]["to_author"],
            "reward_total": item["reward"]["total"],
        })

    return json({
        "code": 200,
        "data": data_list
    })
