# Task5: Write any 5 timezones using datetime module example

# Asia/Kolkata

import pytz
from datetime import datetime 
t1 = pytz.timezone('Asia/Kolkata')
t2 = datetime.now(t1)
print('Date and time in India: ', t2.strftime('%d/%m/%Y , %I:%M:%S %p'))