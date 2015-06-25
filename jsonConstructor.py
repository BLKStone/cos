#!/usr/bin/env python
# -*- coding:utf-8 -*-

import codecs
import sys
import re

reload(sys)
# Set Shell Encoding Format to UTF-8
sys.setdefaultencoding("utf-8")
print sys.getdefaultencoding()

file_object = open("mainCharacter.txt","r") 
try:
     all_the_text = file_object.read().decode('utf-8')
finally:
     file_object.close()

#print all_the_text

watchers = all_the_text.split("\n")
#print watchers

content = ""

for watcher in watchers:
    content = content +"{category:1, name:\'"+watcher+"\',value: 1},"+"\n"

content = content.encode('utf-8')
file_object = open('jsonNode.txt', 'w')
file_object.write(content)
file_object.close( )


