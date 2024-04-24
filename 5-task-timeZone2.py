# Task5: Write any 5 timezones using datetime module example

# Europe/London

import pytz
from datetime import datetime 
t1 = pytz.timezone('Europe/London')
t2 = datetime.now(t1)
print('Date and time in Londan: ', t2.strftime('%d/%m/%Y , %I:%M:%S %p'))