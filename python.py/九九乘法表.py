# a = 1
# while a <= 9:
#     i = 1
#     while i <= a:
#         print("%d * %d = %d" %(i,a,i*a),end="\t")
#         i += 1
#     print("")
#     a += 1
# for a in range(1,10):
#     for i in range(1,a+1):
#         print("%d * %d = %d" % (a, i, a * i), end="\t")
#     print("")
# a = 1
# while a <= 9:
#     b = 1
#     while b <= a:
#         print("%d*%d=%d" %(b,a,b*a),end = "\t")
#         i += 1
#     print("")
#     a += 1
def juijiu():
    for i in range(1,10):
        for j in range(1,i + 1):
            print('{} * {} = {}'.format(j,i,j * i))
            return print

juijiu()
