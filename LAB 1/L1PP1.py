import stats
num = int(input("Enter a list of numbers (999 to Cancel): \n"))
l = []
while num != 999:
    l.append(num)
    num = int(input())
print ("List = ")
print (l)
print("Median = ", stats.median(l))
print("Mode = ", stats.mode(l))
print("Mean = ", stats.mean(l))
