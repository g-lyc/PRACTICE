# -*- coding: UTF-8 -*-

import math
def Square_and_cube(length):
  print "The area of the square is %d"%pow(length,2)
  print "The volume of a cube is %d"%pow(length,3)
def Circle_and_sphere(length):
  print "The area of the Circle is %f"%pow(length,2)*math.pi
  print "The volume of a sphere is %f"%pow(length,3)*math.pi*(4/3)

if __name__=="__main__":
  print """
  (1)Calculate square and cube
  (2)Calculate Circle and sphere
  (3)exit()
  """
  length=input("please enter the length:")
  choice=input("please make the choice number:")
  if choice==1:
    Square_and_cube(length)
  if choice==2:
    Circle_and_sphere(length)
  if choice==3:
    exit
