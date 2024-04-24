# Task5: Write any 5 timezones using datetime module example

# Egypt

import pytz
from datetime import datetime 
t1 = pytz.timezone('Egypt')
t2 = datetime.now(t1)
print('Date and time in Egypt: ', t2.strftime('%d/%m/%Y , %I:%M:%S %p'))