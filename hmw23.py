hrs = input("enter hours:")
rate = input("enter a rate")
h = float(hrs)
r = float(rate)
if h<=40:
    pay=h*r
else:
    pay=40*r+(h-40)*r*1.5
print(pay)
