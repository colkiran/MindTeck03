"""
Assignment
==========
1. months = ['dec', 'oct', 'aug', 'sep', 'jan', 'nov', 'mar', 'jul',  'feb', 'may', 'jun', 'apr']

sort it like calendar month

"""
months = ['dec', 'oct', 'aug', 'sep', 'jan', 'nov', 'mar', 'jul',  'feb', 'may', 'jun', 'apr']

print(f"Unsorted Months :{months}")

print("-" * 60)

from calendar import month_abbr

print(f"Calendar Month :{list(month_abbr)}")

print("-" * 60)
res = sorted(months, key=list(map(lambda mth: mth.lower(), list(month_abbr))).index)

print(f"Sorted Months :{res}")

