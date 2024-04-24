# Task5: Write any 5 timezones using datetime module example

# Singapore

import pytz
from datetime import datetime 
t1 = pytz.timezone('Singapore')
t2 = datetime.now(t1)
print('Date and time in Singapore: ', t2.strftime('%d/%m/%Y , %I:%M:%S %p'))