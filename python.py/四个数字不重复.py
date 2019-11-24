# a = 1
# while a <= 4:
#     b = 1
#     while b <= 4:
#         c = 1
#         while c <= 4:
#             if a != b and b!= c and c != a:
#                 print("%d%d%d" %(a,b,c))
#             c += 1
#         b += 1
#     a += 1
for a in range(1,4):
    for b in range(1,4):
        for c in range(1,4):
            if a != b and b!= c and c != a:
                print("%d%d%d" %(a,b,c))


