#!/usr/bin/env python
# -*- coding:utf-8 -*-

import codecs
import sys
import re



file_object = open("relations.txt","r") 
try:
     all_the_text = file_object.read().decode('utf-8')
finally:
     file_object.close()

content = ""

lines = all_the_text.split("\n")

for line in lines:
    #print line.encode('utf-8')
    couple = line.split(":")
    #print line
    if len(couple)!=2:
        pass
    else:
        print couple[0].encode('utf-8')
        print couple[1].encode('utf-8')
        content = content +"{source :\'"+couple[0] +"\', target: \'"+couple[1]+u"\',weight: 1,name: \'关注\'},"+"\n"


content = content.encode('utf-8')
file_object = open('jsonLinks.txt', 'w')
file_object.write(content)
file_object.close( )
