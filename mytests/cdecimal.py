import cdecimal
import memcache
import os
from decimal import *
getcontext().prec = 6
a =str('111')
if isinstance(a, str):
    a = a.replace(",", "")
try:
    print(Decimal(a))
except decimal.InvalidOperation:
    raise ValueError(
        "amount value could not be converted to Decimal(): '{}'".format(a),
    )
print(Decimal(1) / Decimal(7.8))
print(Decimal(a))
print(cdecimal.Decimal(a))