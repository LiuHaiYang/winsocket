#-*- encoding：utf-8 -*-
import re

#test= "b'aa3'"
#test.split("'")
#if re.match(r'\w\'\w\w\d', test):
#    print('ok')
#else:
#    print('error')

import re

txt='[Data:2015-01-01 12:00:00|A]'
txt1='[Data:2015-01-01 12:00:01|000000|B|11一哈离开了]'
re1='(\\[)'	# Any Single Character 1
re2='((?:[a-z][a-z]+))'	# Word 1
re3='(:)'	# Any Single Character 2
re4='((?:2|1)\\d{3}(?:-|\\/)(?:(?:0[1-9])|(?:1[0-2]))(?:-|\\/)(?:(?:0[1-9])|(?:[1-2][0-9])|(?:3[0-1]))(?:T|\\s)(?:(?:[0-1][0-9])|(?:2[0-3])):(?:[0-5][0-9]):(?:[0-5][0-9]))'	# Time Stamp 1
re5='(\\|)'	# Any Single Character 3
re6='([a-z])'	# Any Single Word Character (Not Whitespace) 1
re7='([\u4e00-\u9fa5]{2,})'   #{2,}  表示至少两个汉字   ｛2,N｝ 2-N 个汉字
re8='(\\])'	# Any Single Character 4
re9='([0-9]{6})'
re10='([0-9]{1,})'
#rg = re.compile(re1+re2+re3+re4+re5+re6+re5+re7+re8,re.IGNORECASE|re.DOTALL)
rg = re.compile(re1+re2+re3+re4+re5+re9+re5+re6+re5+re10+re7+re8,re.IGNORECASE|re.DOTALL)
#m = rg.search(txt)
if re.match(rg, txt1):
	print ("OK")
else:
	print("Error")
