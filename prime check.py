x=int(input("Enter a number to check if Prime: "))
count=0
for i in range(1,x+1):
    if x%i==0:
        count+=1
if count==2:
    print("Prime")
else:
    print("Not Prime")
