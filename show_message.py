#!/usr/bin/python
import sys
# arg1 is the script name
# arg2 is what we want
if len(sys.argv) != 2:
  raise ValueError('Argument missing or too many');

from sense_hat import SenseHat
sense = SenseHat()
sense.show_message(sys.argv[1])
