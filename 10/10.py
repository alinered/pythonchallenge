import re
initNum = '1'
for each in range(30):
    initNum = "".join([str(len(i + j)) + i for i, j in re.findall(r"(\d)(\1*)", initNum)])
print len(initNum)
