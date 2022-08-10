from httpx import post as httpx_post
from pywebio.output import (put_html, put_loading, put_markdown, put_table,
                            toast)

from utils.html_format_helper import html_link
from utils.url_params_helper import get_params

DATA_HEADER_MAPING = [
    ("上榜日期", "date"),
    ("排名", "ranking"),
    ("文章", "article_title"),
    ("作者收益", "reward_to_author"),
    ("总收益", "reward_total"),
    ("链接", "article_url")
]


def result():
    """查询结果
    """
    params = get_params()

    with put_loading(color="success"):
        response = httpx_post("http://backend:8081/api/query_record",
                              json={"name": params["name"]})
        response.raise_for_status()
        data = response.json()

        if not data["code"] == 200:
            toast(data["message"], color="warn")
        else:
            for item in data["data"]:
                item["article_url"] = put_html(html_link("点击跳转", item["article_url"]))

            put_markdown(f"# {params['name']} 的上榜记录")

            put_table(
                tdata=data["data"],
                header=DATA_HEADER_MAPING
            )
