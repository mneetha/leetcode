#Hashset

s= set()
print(s)
#Add O(1)
s.add(1)
s.add(3)
s.add(5)
print(s)

#lookup O(1)
if 1 not in s:
    print(True)

#remove O(1)
s.remove(3)
print(s)

#set construction -O(s) where s is the length of the str
string = 'qqqqqweeeaaaaabbbbrrr'
sett = set(string)
print(set)


#loop over items in set O(n)
for x in s:
    print(x)

#hashmap - dictionaries

d = {
    'greg': 1,
    'steve': 2,
    'rob':3
}

print(d)

##check value to a key in the dictionary O(1)
d['arsh'] = 4
print(d)

#check for presence of key O(1)
if 'greg' in d:
    print(True)

print(d['greg'])

#loop over the key val pairs of the dictionary O(n)
for key,val in d.items():
    print(f'key {key}: val {val}')

#default dict

from collections import defaultdict
default = defaultdict(list)
default[2]
print(default)

from collections import Counter

counter = Counter(string)
print(counter)

words = ["apple", "banana", "apple", "cherry"]
count = Counter(words)

print(count["apple"])

nums = [1, 2, 3, 4, 2]

seen = set()
has_dupe = False

for num in nums:
    if num in seen:
        has_dupe = True
        break
    seen.add(num)

print(has_dupe)
