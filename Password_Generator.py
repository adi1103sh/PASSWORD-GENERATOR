import random
import sys
def gen():
    global c
    # FOR ALPHANUMERIC COMBINATIONS TO GENERATE DIFFERENT PASSWORDS
    s = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
         'w', 'x', 'y', 'z',
         '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
         'M', 'N', 'O', 'P', 'Q',
         'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', "!", "@", "#", "$", "%", "&", "_", "-"]
    for i in range(9) :
            g = ""
            for i in range(n) :
                # TO CHOOSE RANDOMLY ANY CHARACTER FROM s
                gl = s[random.randint(0,len(s)-1)]
                # CONCATENATING ALL THE CHARACTERS TO GENERATE A PASSWORD
                g = gl + g
                if(len(g)==n):
                    print(g)
                else:
                    pass
    print("To get more passwords enter 'MORE' and to exit enter 'DONE'")
    c = input("MORE or DONE?: ").upper()
print("WELCOME TO PASSWORD GENERATOR")
n=int(input("Enter length of password: "))
gen()
while(1):
    if(c=="MORE"):
        gen()
    elif(c=="DONE"):
        print("Thank You!!!")
        sys.exit()
    else:
        print("Invalid Choice....Thanks!!")
