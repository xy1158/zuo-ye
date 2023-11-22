import random
a = random.randint(1, 10)
b = int(input())
for i in range(1, 4):
    if a != b:
        if b > a:
            print("too big")
        elif b < a:
            print("too small")
        b = int(input())
    else:
        print("right")
