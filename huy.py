x11=int(input())
for p in range(0,100):
	if x11==2**p:
		flag=0
		break
	else:
		flag=1
if flag==0:
	print("yes")
else:
	print("no")
