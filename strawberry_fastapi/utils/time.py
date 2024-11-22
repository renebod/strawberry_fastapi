import pytz
from datetime import datetime 

def now():
    now = datetime.now(pytz.timezone('Europe/Amsterdam'))
    return datetime.strftime(now, '%Y-%m-%d %H:%M:%S')