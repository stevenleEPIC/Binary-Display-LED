from gpiozero import LED
from time import sleep
# gpio 5 & 6 is broken :C oh well 

# LED are viewed as eight to one from left to right
one=LED(17)
two=LED(27)
three=LED(22)
four=LED(5)
five=LED(6)
six=LED(13)
seven=LED(19)
eight=LED(26)

#binary recursion thing idk
def tobin(d):
    if d==0:
        return 0
    else:
        return (d % 2 + 10 * tobin(d//2))

#binary to LED
d=int(input("give me number (0-255): "))
o=str(tobin(d)).zfill(8)
print(o)
l1, l2, l3, l4, l5, l6, l7, l8=[int(n)for n in str(o)] #l1-l8 goes to each individual leds

while True:
    if l1==1:
        one.on()
    if l2==1:
        two.on()
    if l3==1:
        three.on()
    if l4==1:
        four.on()
    if l5==1:
        five.on()
    if l6==1:
        six.on()
    if l7==1:
        seven.on()
    if l8==1:
        eight.on()