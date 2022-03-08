terms=int(input("how many terms:"))
n1,n2=0,1
count=0
if terms<=0:
    print("please enter a positive number:")
elif terms==1:
    print("series sequence upto",terms,":")
    print(n1)
else:
    print("sequence:")
    while count<terms :
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth 
        count+=1
