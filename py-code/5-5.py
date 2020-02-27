# -*- coding: UTF-8 -*-

try:
    dollar = float(raw_input("Enter a money that is letter than 1 dollar:"))
    if dollar > 1:
        print "You input is too large."
    elif dollar>0 and dollar<1:
        dollarTocents = int(dollar*100)
        (numTo25,dollarTocents) = divmod(dollarTocents,25)
        print '%d 25 coins.'%numTo25
        (numTo10,dollarTocents) = divmod(dollarTocents,10)
        print '%d 10 coins.'%numTo10
        (numTo5,dollarTocents) = divmod(dollarTocents,5)
        print '%d 5 coins.'%numTo5
        numTo1 = dollarTocents/1
        print '%d 1 coins.'%numTo1
    else:
        print 'you input must large than 0.'
except ValueError,v:
    print 'you must enter a digits.'
