N=int(input())
D = dict(input().split() for _ in range(N))
while True:
    try:
        name = input()
    except EOFError as e:
        break
    if name not in D.keys():
        print("Not found")
    else:
        print(name+"="+D[name])
