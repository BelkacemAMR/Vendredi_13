from datetime import date, timedelta
from calendar import monthrange


def is_friday_13th(date):
    return date.day == 13 and date.weekday() == 4


def max_days(date):
    return monthrange(date.year, date.month)[1]

def friday_the_13th():
    today = date.today()
    result = today

    if result.day < 13:
        result += timedelta(days=13 - result.day)

    found = is_friday_13th(result)

    while not found:
        result += timedelta(days=max_days(result) - result.day)
        result += timedelta(days=13)

        found = is_friday_13th(result)

    return f"{result.strftime('%Y-%m-%d')}"


if __name__ == "__main__":
    print(friday_the_13th())
