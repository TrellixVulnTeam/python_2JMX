import shutil
import os
import pytz
import datetime
from datetime import datetime

pacific = pytz.timezone('America/Los_Angeles')
local_date = pacific.localize(datetime.now())
print(local_date)
print(local_date.hour)
Portland = (local_date.hour)
print(Portland)

source = '/Users/Sarah/Desktop/foldera/'

destination = '/Users/Sarah/Desktop/folderb/'
files = os.listdir(source)


if 8 <= Portland:
    for i in files:
        shutil.move(source+i, destination)
