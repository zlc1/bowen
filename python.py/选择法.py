a = [30,28,77,16,98]
for i in range(len(a)-1):
    for j in range(i + 1,len(a)):
        if a[i] < a [j]:
            a[i],a[j ] = a[j],a[i]
    print(a)
