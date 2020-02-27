# -*- conding:utf-8 -*-
#Author:lyc
import os, sys

from itertools import compress

addresses=['5412NCLARK','5148NCLARK','5800E58TH','2122NCLARK','5645NRAVENSWOOD','1060WADDISON','4801NBROADWAY','1039WGRANVILLE']
counts=[0,3,10,4,1,7,6,1]

more5 = [n > 5 for n in counts]
#[False,False,True,False,False,True,True,False]
print(list(compress(addresses,more5)))
#['5800E58TH','1060WADDISON','4801NBROADWAY']


