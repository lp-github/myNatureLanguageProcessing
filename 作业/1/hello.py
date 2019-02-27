import re
import time

key = r"http://www.poshoaiu.com and https://iusdhbfw.com"
p1 = r"http://"
p2 = r"https://"
pattern1 = re.compile(p1)
pattern2 = re.compile(p2)
matcher1 = re.search(pattern1,key)
matcher2 = re.search(pattern2,key)
print matcher1.group(0)
print matcher2.group(0)
time.sleep(5)
