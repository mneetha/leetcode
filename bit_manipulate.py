
x = 7


x<<1 #x * 2^1

x<<2 #x * 2^2

x<<3 #x * 2^3

y = 200

y>>1 #y // 2^0
y>>2 #y // 2^1
y>>3 #y // 2^2


def count_ones(n):
    count = 0
    print(f'Value: {n}')
    while n:
        count = count + n&1
        n = n>>1
    return count


def swap_int(a,b):
    print(f'a,b: {a},{b}')
    a^=b
    b^=a
    a^=b
    print(f'a,b: {a},{b}')


def is_kth_bit_set(n,k):
    print(f'n, k : {n} {k}')
    mask_bit = 1 << k
    return (n & mask_bit) !=0

def set_kth_bit(n,k):
    print(f'n, k : {n} {k}')
    mask_bit = 1 << k
    return (n | mask_bit)

def clear_kth_bit(n, k):
    print(f'n, k : {n} {k}')
    mask_bit = ~(1<<k)
    return n & mask_bit

def toggle_kth_bit(n,k):
    print(f'n, k : {n} {k}')
    return n ^ (1<<k)


READ, WRITE, EXECUTE, ADMIN = 0, 1, 2, 3

permissions = 0
#user has read and write permission
permissions = set_kth_bit(permissions, READ)
permissions = set_kth_bit(permissions, WRITE)

#check permissions
print(is_kth_bit_set(permissions, READ))
print(is_kth_bit_set(permissions, WRITE))

#revoke permissions
permissions = clear_kth_bit(permissions, WRITE)
print(bin(permissions))