def computepay(h,r):
    if h<=40:
        pay=h*r
        return pay
    else:
        pay = 40*r+(h-40)*r*1.5
        return pay

hrs = input("Enter Hours:")
rate = input("a rate")
h = float(hrs)
r = float(rate)
pay = computepay(h,r)
print("Pay",pay)
