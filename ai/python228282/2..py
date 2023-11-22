import random


class TicketMachine:
    price = 30

    def __init__(self, name, price, seat , piaofang):
        self.name = name
        self.price = price
        self.seat = seat
        self.piaofang = piaofang
    def goumaitongzhi(self):
        print("you chose {0},it is {1} yuan,here are {2} seats\n".format(self.name, self.price, self.seat))
        if self.seat == 0:
            print("here is no seat for you\n")

    def td(self):
        print("how many do you want to quit?\n")
        tuip = input()
        print("your quit {0} tickets", tuip)
        self.seat += tuip
        self.piaofang -= self.price*self.seat


zhanlang = TicketMachine("zhanlang", 30, 50, 8000)
harrypoter = TicketMachine("harrypoter", 50, 0, 111111)
family_guy = TicketMachine("family_guy", 20, 40, 9505)

ch00se = 0
c = 1
while c == 1:
    ch00se = input()
    if ch00se == "zhanlang":
        zhanlang.goumaitongzhi()
        if zhanlang.seat != 0:
            print("how many ticket do you want to buy?\n")
            piao = int(input())
            zhanlang.piaofang += int(zhanlang.price * piao)
            zhanlang.seat -= piao
            ch00se = 1
    elif ch00se == "harrypoter":
        if harrypoter.seat != 0:
            print("how many ticket do you want to buy?\n")
            piao = int(input())
            harrypoter.piaofang += int(harrypoter.price*piao)
            harrypoter.seat -= piao
            ch00se = 1
    elif ch00se == "family_guy":
        if family_guy.seat != 0:
            print("how many ticket do you want to buy?\n")
            piao = int(input())
            family_guy.piaofang += int(family_guy.price*piao)
            family_guy.seat -= piao
            ch00se = 1
    else:
        print("here is not a film name is\n", ch00se)
        ch00se = 0
    print("if you want to buy another ticket please put in 1,else put in 0\n")
    c = int(input())

sold_out = random.randint(1, 8080)
sold_out2 = random.randint(1, 8080)
sold_out3 = random.randint(1, 8080)

m = 0

if ch00se == 1:
    print("are you sure you choose these film?give in 'yes' or 'no'\n")
    answer = input()
    e = int(random.randint(1, 50))
    if answer == "yes":
        print("have a good time your seat is", e, "\n")
    else:
        while m == 0:
            tui = input()
            if tui == "zhanlang":
                zhanlang.td()
            elif tui == "harrypoter":
                harrypoter.td()
            elif tui == "family_guy":
                family_guy.td()
            print("ok?put in 1 or 0")
            m = input()


zhanlang.piaofang += sold_out * int(zhanlang.price)
harrypoter.piaofang += sold_out2 * int(harrypoter.price)
family_guy.piaofang += sold_out3 * int(family_guy.price)

print("new news of films:\n")
print("zhanlang has sold", zhanlang.piaofang, "yuan", "here are still", zhanlang.seat, "seats")
print("harrypoter has sold", harrypoter.piaofang, "yuan", "here are still", harrypoter.seat, "seats")
print("family_guy has sold", family_guy.piaofang, "yuan", "here are still", family_guy.seat, "seats")
