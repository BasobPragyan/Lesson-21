a=[3,4,5,1,10,8,7,]
print("Original list is : ",a)
count=0
for i in a:
    count+=i
    avg=count/len(a)
print("Sum",count)
print("Average",avg)
a.sort()
print("Smallest element is  : ",a[0])
print("Largest element is : ",a[-1])