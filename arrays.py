#Arrays, string
A= [1,2,3]
print(A)
A.append(5) #O(1)
print(A)
A.pop() #O(n)
print(A)
A.insert(2,5) #O(n)
print(A)
A[0] = 7 #O(1)
print(A)
print(A[3]) #O(1)
if 7 in A:#O(n)
    print(True)

print(len(A))#O(1)
s='hello'
b=s+'z' #O(n)
print(b)

if 'f' in s: #O(n)
    print(True)

print(s[2]) #O(n)
print(len(s)) #O(1)