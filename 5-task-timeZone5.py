# Task5: Write any 5 timezones using datetime module example

# Europe/Paris

import pytz
from datetime import datetime 
t1 = pytz.timezone('Europe/Paris')
t2 = datetime.now(t1)
print('Date and time in Paris: ', t2.strftime('%d/%m/%Y , %I:%M:%S %p'))