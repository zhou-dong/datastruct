import datetime 

begin = datetime.datetime.now()
sum = 0 ;
for x in range(1,101):
    sum += x
interval = datetime.datetime.now() - begin ;
print sum, interval.microseconds

# Guassian
begin = datetime.datetime.now()
sum = (1 + 100) * 100 / 2
interval = datetime.datetime.now() - begin ;
print sum, interval.microseconds
