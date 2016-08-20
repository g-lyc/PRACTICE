# -*- coding: UTF-8 -*-

day_rate=float(raw_input("please type the day rate:\n"))

year_rate=(1+day_rate)**365-1

print "Annuai return is %f"%year_rate
