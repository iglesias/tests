#!/usr/bin/python3

prefix = 'file'
extension = '.dat'
num_files = 10

for idx in range(1,num_files+1):
  fname = '{}{:02}{}'.format(prefix, idx, extension)
  print(fname)
