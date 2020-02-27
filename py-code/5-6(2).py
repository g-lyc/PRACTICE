# -*- coding: UTF-8 -*-

def calculator(number1,i,number2):
  if i=='+':
    return number1+number2
  if i=='-':
    return number1-number2
  if i=='*':
    return number1*number2
  if i=='/':
    return number1/number2
  if i=='%':
    return number1%number2
  if i=='**':
    return number1**number2
caozuo=['+','-','**','/','%','*']
string = raw_input("Please enter the string:")
for obj in caozuo:
    if string.find(obj)>-1 and string.count(obj)<2:
        number = string.split(obj)
        list = []
        for i in number:
            list.append(i)
        number1=int(list[0])
        i=obj
        number2=int(list[1])
print calculator(number1,i,number2)
