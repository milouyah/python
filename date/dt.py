import datetime

def now():
    x = datetime.datetime.now()
    return x.strftime("%Y-%m-%d")


if __name__ == "__main__":
    print(now())