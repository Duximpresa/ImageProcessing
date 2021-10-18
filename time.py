from datetime import datetime
import time

a = datetime.now()
time.sleep(1)
b = datetime.now()
c = b - a
print(c)