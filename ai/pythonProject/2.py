import eare
Id = input("please give in your identity number: ")
if len(Id) != 18:
    print("number of Number is wrong")

if not Id[0:-1].isdigit():
    print("wrong,is not number")

if len(Id) == 18:
    year = Id[6:10]
    month = Id[10:12]
    day = Id[12:14]
    if int(Id[17]) % 2 == 0:
        gender = "male"
    else:
        gender = "female"
    ar = eare.area.panduan(int(Id[0:2]))
    print(year)
    print(month)
    print(day)
    print(gender)
    print(ar)
