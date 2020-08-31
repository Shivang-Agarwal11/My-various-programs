# # final='Lmao'
# # guess=[0,0,0,0]
# # for i in range (len(final)):
# #     guess[i]=hex(ord(final[i]))
# # # print(guess)
# # guess[3] = hex(int(guess[3],16) - 32)
# # # print(guess)
# # guess = [hex(int(g,16)) for g in guess][::-1]
# # # print(guess)
# # guess=[int(g,16) for g in guess]
# # # print(guess)
# # guess[0] -= int((ord('g') - ord('G')) / (ord('z') - ord('Z')) * ord('c') - ord('a'))
# # # print(guess)
# # guess[0] -= int((ord('j') - ord('J')) / (ord('E') - ord('e')));guess[2] -= ord('b')
# # # print(guess)
# # guess[0] /= 3;guess[1] += 18;guess[3] += 30
# # # print(guess)
# # guess[1] *= 2
# # # print(guess)
# # guess='1ae60b6a'
# # guess=int(guess,16)
# # # print(guess)
# # for tax5 in range(0,1000,5):
# #     for tax4 in range(10,40,10):
# #         guess += tax5 * tax4
# # # print(guess)
# # for tax4 in range(18,30,2):
# #     guess = int((str(hex(guess)[2:])[::-1]),16) + tax4 * 1000
# # # print(guess)
# # guess=hex(guess)
# # # print(guess)
# # guess=guess[2:]
# # # print(guess)
# # guess = str(guess[4:8]) + str(guess[0:4])
# # # print(guess)
# # guess=int(guess,16)
# # # print(guess)
# # for tax3 in range(0,1234):
# #     guess += 1337 + tax3
# # print(guess)


# from itertools import permutations
# l,b=input().split()
# li=list(permutations(l,int(b)))
# # li=sorted(li)
# # # print(li)
# # for i in range(len(li)):
# #     for j in range (2):
# #         print(li[i][j],end='')
# #     print()
# for i in sorted(li):
#     print(*i)
a='HELLO'
print(a.hash())