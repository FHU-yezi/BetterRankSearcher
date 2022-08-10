from datetime import date, datetime


def GetTodayInDatetimeObj() -> datetime:
    return datetime.fromisoformat(date.today().strftime(r"%Y-%m-%d"))
