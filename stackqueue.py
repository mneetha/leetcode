#Stacks
stk = []
print(stk)

#O(1)
stk.append(4)
stk.append(3)
print(stk)

#O(1)
x = stk.pop()
print(stk)

#peek O(1)
print(stk[-1])

#ask if stk is empty O(1)

if stk:
    print(True)


#Queues

from collections import deque
q=deque() #double ended queue

print(q)

#enqueue - add to the right O(1)
q.append(5)
q.append(6)
q.append(7)
print(q)

#deque = pop left O(1)
print(q.popleft())

print(q)

#peek from right side O(1)
q[-1]

#peek from left side O(1)
q[0]
