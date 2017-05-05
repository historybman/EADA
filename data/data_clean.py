#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  2 20:07:26 2017

@author: rmorriss
"""

fname = input('enter the file name: ')
new_name = 'new_' + fname
fout = open(new_name, 'w')
file_in = open(fname)
string = file_in.read().replace('\n', ' ')
string = string.replace('"', '')
fout.write(string)
fout.close()
file_in.close()


#for line in lines:
#    line = ''.join(line.strip())
#    print(line)
#inp = fout.read()
#stripped = inp.strip('\n')
#print(stripped)

#count = 0
#for line in fout:
#    line = line.strip()
#    line.replace('\n', ' ').replace('\r', '')
#    count += 1
#    print(line, count)


#def text_prep(file):
#	fout = open(file, 'w')
#	for line in fout:
#		line = line.strip()
#		fout.write(line)
#	fout.close()

#text_prep(fname)