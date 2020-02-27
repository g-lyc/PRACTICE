# -*- coding: UTF-8 -*-

def pay(paid,balance):
    print "Pymt# Paid Balance"
    print "----- ----- ------"
    i=0
    b=balance
    while(balance>paid):
        balance=balance - paid
        i +=1
        print "%d $%f $%f"%(i,paid,balance)
        i +=1
        print "%d $%d $%f"%(i,balance,0)
if __name__ == '__main__':
    balance=raw_input("please enter the balance:")
    paid=raw_input("please enter the paid:")
    balance=float(balance)
    paid=float(paid)
    pay(paid,balance)
