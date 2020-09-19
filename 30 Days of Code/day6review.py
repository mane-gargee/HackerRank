N=int(input())
for i in range(N):
    arr=input()
    for j in arr:
        even = slice(0,len(arr),2)
        odd = slice(1,len(arr),2)
    print(arr[even],arr[odd])
