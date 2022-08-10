from httpx import post as httpx_post
from pywebio.output import put_button, put_markdown, put_row, toast
from pywebio.pin import put_input

from config import REMOTE_ADDRESS


def on_search_button_clicked():
    pass


def index():
    put_markdown("# 简书排行榜搜索")

    put_row([
        put_input("name", placeholder="请输入简书昵称进行搜索"),
        put_button("搜索", color="success", onclick=on_search_button_clicked)
    ], size=r"60% 40%")

    response = httpx_post(f"http://{REMOTE_ADDRESS}:8081/api/data_info")
    response.raise_for_status()

    put_markdown("\n".join([
        "- 数据每天早晨 8:00 自动更新",
        "- 数据范围：2021-09-18 - 现在",
        "- 简书昵称以上榜时昵称为准",
        "- 最多显示 100 条上榜记录"
    ]))

    data = response.json()
    if data["code"] != 200:
        toast(data["message"], color="warning")
    else:
        put_markdown("\n".join([
            f"数据更新时间：{data['newest_data_date']}",
            f"总数据量：{data['data_count']}",
            "数据来源：简书"
        ]))
