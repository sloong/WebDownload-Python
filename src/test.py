
import re

title = "<title>测试标题</title>"

reg = r'<title>(.*)</title>'

result = re.findall(reg,title)
if result :
    print(result[0])
else:
    print( "")
