#
# temp.py - This file contains the temperature sensor functionality
# Date Created: 12/01/2024
# Author: Justin Ackermann
#
#

import max6675

cs = 22
sck = 18
so = 16

max = max6675.set_pin(cs, sck, so, 2)

try:
    while 1:
        a = max6675.read_temp(cs)
        print(a)

        max6675.time.sleep(2)
        
except KeyboardInterrupt:
    pass