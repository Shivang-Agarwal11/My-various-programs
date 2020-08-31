# thickness = int(input())  # This must me an odd number
# c = 'H'

# # Top Cone
# for i in range(thickness):
#     print((c * i).rjust(thickness - 1) + c + (c * i).ljust(thickness - 1))

# # Top Pillars
# for i in range(thickness + 1):
#     print((c * thickness).center(thickness * 2) +
#           (c * thickness).center(thickness * 6))

# # Middle Belt
# for i in range((thickness + 1) / 2):
#     print((c * thickness * 5).center(thickness * 6))

# # Bottom Pillars
# for i in range(thickness + 1):
#     print((c * thickness).center(thickness * 2) +
#           (c * thickness).center(thickness * 6))

# # Bottom Cone
# for i in range(thickness):
#     print(((c * (thickness - i - 1)).rjust(thickness) + c +
#           (c * (thickness - i - 1)).ljust(thickness)).rjust(thickness * 6))
# c=1
# n= int(input())
# s='.|.'
# d=n-2
# for i in range (n//2):
#     print((s*c).center(n*3,'_'))
#     c=c+2
# print('WELCOME'.center(n*3,'-'))
# for i in range (n//2):
#     print((s*d).center(n*3,'-'))    
#     d=d-2
# n=int(input())
# s=len(bin(n)[2:])


# for i in range(1,n+1):
#     print(str(i).rjust(s," "),end="")
#     print((oct(i).upper())[2:].rjust(s," "),end="")
#     print((hex(i).upper())[2:].rjust(s," "),end="")
#     print((bin(i).upper())[2:].rjust(s," "),end="")
    
#     print()

# string=input()
# flag=0
# c=0
# x=0
# for i in range (0,len(string)):
        
#         if((string[i]) in ['A','E','I','O','U']):
#             c+=1
#             for j in range (i+1,len(string)):
#                if((string[i:j])[0] in ['A','E','I','O','U']):
#                  c+=1 
#                else:
#                      flag+=1
#         else:
#             flag+=1 
#             for j in range (i+1,len(string)):
#                    if((string[i:j])[0] not in  ['A','E','I','O','U']):
#                      flag+=1
# print(flag,c)              

# arr = list(map(int, input().rstrip().split()))   
# print(arr)           
# n = int(input())
# arr = list(map(int, input().rstrip().split()))
# for i in range (len(arr)-1,0,-1):
#   print(arr[i],end=" ")

# n=int(input())
# l=[]
# for i in range (n):
#     s=input()
#     l.append((s.split("  ")))
# # di=dict(zip(l,l))
# print(l)
# it=iter(l)
# di=dict(zip(it,it))
# print(di)

# n = int(input())
# stri=""
# while n>0:
#         c=n%2
#         print(str(c))
#         stri=stri.replace(stri,(stri+str(c)))
#         n=n//2
# print(stri)

# flag=0
# arr = []
# i=0
# sum1=0
# sum2=0
# c=0
# for i in range(6):
#         arr.append(list(map(int, input().rstrip().split())))
# i=0
# j=0
# while j<=5:
        
#         sum2=0
#         if (j+2)>5:
#                 break
#         else:
#                 while i<3:
#                         sum2=sum2+arr[j+2][i+0+c]
#                         i=i+1        
#                 c=c+1
#                 sum2=sum2+arr[j+1][c]
#                 # print(sum2)
#                 if sum1<sum2:
#                  sum1=sum2
#                 if c<4:
#                     j=j-1    
#         if c>=4:
#                 c=0
#         i=0      
#         while i<3:
#                 sum2=sum2+arr[j+0][i+0+c]
#                 i=i+1
#         i=0
#         flag=flag+1
#         j=j+1       
# print(sum1)
# print(flag)
# HOURGLASS DAY 11 HACLERRANK
# sum = 0
# tarr = []
# for l in range(0,4):
#         for k in range(0,4):
#             for i in range(l,l+3):
#                 for j in range(k,k+3):
#                     if i == l+1 and ( j == k or j == k+2):
#                         continue
#                     else:
#                         sum += arr[i][j]
#             tarr.append(sum)
#             sum = 0
# print(max(tarr))



# import math
# n=int(input())
# lis=[]
# flag=0
# for i in range (n):
#     lis.append(list(map(int,input().split(' '))))
# for i in range (0,n-2):
#     if flag==1:
#         break
#     for j in range (i+1,n):
#         if flag==1:
#             break
#         for k in range (j+1,n):
#             dis1=math.sqrt(((lis[i+0][0]-lis[j+0][0])*(lis[i+0][0]-lis[j+0][0]))+((lis[i+0][1]-lis[j+0][1])*(lis[i+0][1]- lis[j+0][1])))
#             dis2=math.sqrt(((lis[i+0][0]-lis[k+0][0])*(lis[i+0][0]-lis[k+0][0]))+((lis[i+0][1]-lis[k+0][1])*(lis[i+0][1]-  lis[k+0][1])))
#             dis3=math.sqrt(((lis[k+0][0]-lis[j+0][0])*(lis[k+0][0]-lis[j+0][0]))+((lis[k+0][1]-lis[j+0][1])*(lis[k+0][1]-  lis[j+0][1])))
#             dis4=math.sqrt(((lis[n-1-i][0]-lis[n-j-1][0])*(lis[n-1-i][0]-lis[n-j-1][0]))+((lis[n-1-i][1]-lis[n-j-1][1])*(lis[n-1-i][1]-lis[n-j-1][1])))
#             dis5=math.sqrt(((lis[n-1-i][0]-lis[n-k-1][0])*(lis[n-1-i][0]-lis[n-k-1][0]))+((lis[n-1-i][1]-lis[n-k-1][1])*(lis[n-1-i][1]-lis[n-k-1][1])))
#             dis6=math.sqrt(((lis[n-1-k][0]-lis[n-j-1][0])*(lis[n-1-k][0]-lis[n-j-1][0]))+((lis[n-1-k][1]-lis[n-j-1][1])*(lis[n-1-k][1]-lis[n-j-1][1])))
#             if dis1==dis2==dis3 or dis5==dis6==dis4:
#                 flag=1
#                 break
#             n=n-1
# if flag>0:
#     print("VICTORY")
# else:
#     print("DEFEAT")
            
    

# n=int(input())
# left=[]
# right=[]
# location=[]
# for i in range (n):
#     bot=int(input())
#     for j in range (2,bot+1,2):
#         left.append(j)
        
#         right.append(j+1)
#     # print(left)
#     # print(right)    
#     if bot in left:
#         # location.append('L')
#         while bot>1:
#             # print(bot)
#             if bot in left:
#                 location.append('L')
#             else:
#                 location.append('R')    
#             bot=bot//2
#     else:
#         # location.append('R')
#         while bot>1:
#             # print(bot)
#             if bot in left:
#                 location.append('L')
#             else:
#                 location.append('R')    
#             bot=bot//2
#     # print(location) 
#     location.reverse()           
#     for j in range (len(location)):
#         print(location[j+0],end="")
#     print()    
#     location=[]
#     left=[]
#     right=[]
    # print(15//2)
                
# n= int(input())
# for i in range (n):
#     location=[]
#     bot=int(input())
#     while bot >1:
#         if bot%2==0:
#             location.append('L')
#         else:
#             location.append('R')
#         bot=bot//2
#     location.reverse()
#     for j in range (len(location)):
#         print(location[j+0],end="")
#     print()
    # location=[]                
# CODECHEF

# n=int(input())
# for i in range (n):
#     li=list(map(int,input().split(' ')))
#     sum=0
#     sum2=0
#     m=[]
#     # for j in range (li[0]):
#     m=list(map(int,input().split(' ')))
#     print(m)
#     for j in range (li[0]):     
#         sum2=m[j+0]+sum2
#         print(sum2)
#         if m[j+0]>li[1]:
#             sum=sum+li[1]
#         else:
#             sum=sum+m[j+0]
#     print(sum)        
#     if sum>sum2:
#         print(sum-sum2)
#     else:
#         print(0)


# n=int(input())
# for i in range(n):
#         s=input()
#         c=0
#         j=0
#         while j< len(s):
#             if 'xy' in s[j:j+2] or 'yx' in s[j:j+2]:
#                 c=c+1
#                 j=j+2
#             else:
#                 j=j+1    

#         # for j in range(0,len(s)-1,2):
#             # j=j+1        
#         print(c)        


# n=int(input())
# for i in range (n):
#         people=int(input())
#         coins=list(map(int,input().split(' ')))
#         other=0
#         if coins[0]>5:
#             print("NO")
#         else:
#             five=coins.count(5)
#             for j in range (people):
#                 other=other+coins[j]//5-1
#             if five>=other:
#                 print("YES")
#             else:
#                 print("NO")


# t=int(input())
# for i in range (t):
#     n=int(input())
#     li1=[]
#     li2=[]
#     c=1
#     flag=n*n
#     for j in range (n):
#         if j%2>0:
#             for k in range (n-1,-1,-1):
#                 li1.append(flag)
#                 print(flag,end="")
#                 flag=flag-1
#                 # c=c+11
#         else:
#             for k in range (n):
#                 li1.append(c)
#                 print(c,end="")
#                 # flag=flag-1
#                 c=c+1
#         li2.append(li1)
#         li1=[]  
#         print()      
#     # print(li2)



n=int(input())
for i in range (n):
    tu1=tuple(map(int,input().split(' ')))
    tu2=tuple(map(int,input().split(' ')))
    tu3=()
    c=0
    for j in range (3):
        tu3=tu3+(tu2[j]-tu1[j],)
    maxi=max(list(tu3))
    mini=min(list(tu3))
    same=tu3[0]
    for k in range (1,3):
        if same==tu3[k]:
                # same=k
            c=c+1
    if c>0:
        if maxi==same:
            print((maxi*2)//mini)
        else:
            print((mini*2)//maxi)
    elif tu3[1]==tu3[2]:
        if maxi==tu3[1]:
            print((maxi*2)//mini)
        else:
            print((mini*2)//maxi)
    else:
        print(mini-1)        
            
    
    