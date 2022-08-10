from typing import Dict
from urllib import parse

from pywebio.session import eval_js


def get_url() -> str:
    result = eval_js("window.location.href").split("?")[0]

    if result[-1] == "/":
        return result
    else:
        return result + "/"


def get_params() -> Dict[str, str]:
    params_str = eval_js("window.location.href").split("?")[1]
    key_value_pair_list = params_str.split("&")
    key_value_pair_tuples = [x.split("=") for x in key_value_pair_list]
    # 对中文进行 URL 解码
    key_value_pair_tuples = [(key, parse.unquote(value)) for key, value in key_value_pair_tuples]
    return dict(key_value_pair_tuples)


def set_url_with_params(app_name: str, params: Dict[str, str]):
    base_url = get_url()
    params_str = "&".join([f"{key}={value}" for key, value in params.items()])
    full_url = base_url + "?app=" + app_name + "&" + params_str

    eval_js(f"window.location.href='{full_url}'")
