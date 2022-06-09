def  cd(p,r,y):
	if Y<=0:
		return p
	else:
		return cd(p+p*r/100,r,y-1)
p=int(input("enter the amount"))
r=int(input("enter the rate"))
y=int(input("enter the years"))
amount=cd(p,r,y)
print(amount)
