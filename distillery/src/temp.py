#
# temp.py - This file contains the temperature sensor functionality
# Date Created: 12/01/2024
# Author: Justin Ackermann
#
#

from MAX6675 import MAX6675

cs = 22
sck = 18
so = 16

max = MAX6675.MAX6675(cs, sck, so)

try:
    while 1:
        a = MAX6675.read_temp(cs)
        print(a)

        MAX6675.time.sleep(2)

except KeyboardInterrupt:
    pass