from datetime import datetime, date


def GetTodayInDatetimeObj() -> datetime:
    return datetime.fromisoformat(date.today().strftime(r"%Y-%m-%d"))
