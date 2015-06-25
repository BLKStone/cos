#!/usr/bin/env python
# -*- coding:utf-8 -*-

import codecs
import sys
import re

reload(sys)
# Set Shell Encoding Format to UTF-8
sys.setdefaultencoding("utf-8")
print sys.getdefaultencoding()




file_object = open("余弦100.txt","r") 
try:
     all_the_text = file_object.read().decode('gbk')
finally:
     file_object.close()

#print type(all_the_text)
#print all_the_text

str_list = all_the_text.split('\n')
print type(str_list)

result = ""
maincontent = ""
pattern = re.compile('\[([^\]]*)\]')

for s in str_list:
    q = s.split(':')
    watcher = q[0]
    watcher = watcher[1:-1]
    watcheeGroup = q[1]
    #print "test:",watcheeGroup
    #print type(watcheeGroup)
    watcheeList = pattern.findall(watcheeGroup)
    
    #print "content:",watcheeList
    
    for watchee in watcheeList:
        print "watcher:",watcher.encode('utf-8'),"watechee:",watchee.encode('utf-8')
        result = result + watcher+":"+watchee +"\n"
    
    maincontent = maincontent + watcher +"\n"
    #print watcher.encode('utf-8')

result = result.encode('utf-8')
file_object = open('relations.txt', 'w')
file_object.write(result)
file_object.close( )

maincontent = maincontent.encode('utf-8')
file_object = open('mainCharacter.txt', 'w')
file_object.write(maincontent)
file_object.close( )

