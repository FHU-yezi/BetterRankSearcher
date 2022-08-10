from sanic import Sanic

from api import api

app = Sanic(__name__)
app.blueprint(api)

app.run(host="0.0.0.0", port=8081, access_log=False)
