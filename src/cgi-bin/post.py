#!/usr/bin/python
# -*- coding: UTF-8 -*-

# CGI处理模块
import cgi, cgitb

# 创建 FieldStorage 的实例化
form = cgi.FieldStorage() 

# 获取数据
input = form.getvalue('input')

if (input == 'f'):
    ...
elif (input == 'l'):
    ...
elif (input == 'r'):
    ...
elif (input == 'b'):
    ...
else :
    exit()

print( "Content-type:text/html")
print()
print(input)
