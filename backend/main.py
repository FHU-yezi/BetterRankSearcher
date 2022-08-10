from apscheduler.schedulers.background import BackgroundScheduler
from sanic import Sanic

from api import api
from data_fetcher import main_fetcher
from utils.cron_helper import CronToKwargs

scheduler = BackgroundScheduler()
scheduler.add_job(main_fetcher, "cron", **CronToKwargs("0 0 8 1/1 * *"))

app = Sanic(__name__)
app.blueprint(api)

app.run(host="0.0.0.0", port=8081, access_log=False)
