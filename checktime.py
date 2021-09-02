from datetime import datetime

def check_time():
    format = '%H:%M %p'
    t = datetime.today().strftime(format)
    return t

