import sys
import re
for i in range(3):
    id = str(input('请输入身份证号：'))
    if len(id) != 18:
        print('错误，身份证必须是 18 位')
    elif not id[0:-1].isdigit():
        print('错误，非数字')
    else:
        break

def findArea(areaCode):

    areaList = []
    with open('./area.js', 'rb') as file:
            temp = file.readline()
            while temp:
                areaList.append(temp.decode('utf-8'))
                temp = file.readline()
    provinceCode = areaCode[0:2] + "0000"
    cityCode = areaCode[0:4] + "00"
    provinceVal = ''
    cityVal = ''
    areaVal = ''
    for item in areaList:
        if item.startswith(provinceCode):
            provinceVal = item.split(",")[1].strip("\n").strip("\r")
        if item.startswith(cityCode):
            cityVal = item.split(",")[1].strip("\n").strip("\r") + '市'
        if item.startswith(areaCode):
            areaVal = item.split(",")[1].strip("\n").strip("\r")
    return provinceVal + cityVal + areaVal



year=id[6:10]
month=id[11:12]
date=id[13:14]
if int(id[-2])%2==0:
    print("女性")
else:
    print("男性")
print('出生日期' + year + '年' + month + '月' + date + '日')
age=2023-int(year)
print("年龄="+str(age))
area=findArea(id[0:6])
print("籍贯是："+area)
print("校验码="+id[-1])