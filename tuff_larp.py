#!/bin/python

import time
import random

tuff = input("Enter Target: ")
print("\n")
for i in range(20):
  time.sleep(0.15)
  print("".join(random.choice("01") for _ in range(80)))
print("**Hack Successfull.**")
print( 
