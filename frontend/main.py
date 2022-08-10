from pywebio import start_server

from index_page import index
from result_page import result

start_server([index, result], host="0.0.0.0", port=8080)
