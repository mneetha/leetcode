"""
 Bit Manipulation Cheat Sheet (Python)

This cheat sheet covers essential bit manipulation concepts and patterns in Python, with examples and common use cases.


Bitwise Operators

| Operation       | Symbol | Description             | Example (`a = 5`, `b = 3`) |
|-----------------|--------|-------------------------|-----------------------------|
| AND             | `&`    | 1 if both bits are 1    | `a & b` → `1`               |
| OR              | `\|`   | 1 if either bit is 1    | `a | b` → `7`               |
| XOR             | `^`    | 1 if bits differ        | `a ^ b` → `6`               |
| NOT             | `~`    | Flip all bits           | `~a` → `-6`                 |
| Left Shift      | `<<`   | Multiply by `2^n`       | `a << 1` → `10`             |
| Right Shift     | `>>`   | Divide by `2^n` (floor) | `a >> 1` → `2`              |

---

## 🔹 Bit Tricks

| Task                         | Expression                         | Example (for `n = 13`)      |
|------------------------------|------------------------------------|------------------------------|
| Check k-th bit is set        | `n & (1 << k)`                     | Bit 2: `n & (1 << 2)` → `True` |
| Set the k-th bit             | `n | (1 << k)`                     | Set bit 1 → `n = 15`         |
| Clear the k-th bit           | `n & ~(1 << k)`                    | Clear bit 2 → `n = 9`        |
| Toggle the k-th bit          | `n ^ (1 << k)`                     | Toggle bit 0 → `n = 12`      |
| Check if power of two        | `n > 0 and (n & (n - 1)) == 0`     | `16 → True`, `18 → False`    |
| Count 1s (set bits)          | `bin(n).count('1')` or loop        | `13 → 3`                     |
| Get lowest set bit           | `n & -n`                           | `n = 12` → `4`               |
| Remove lowest set bit        | `n & (n - 1)`                      | `13 → 12`                    |



 Practice Problems

1. **Count 1s in a number's binary form**
2. **Check if a number is power of two**
3. **Find the single number** (All elements appear twice except one)
4. **Reverse bits of a 32-bit unsigned integer**
5. **Count bits from 0 to n** → Leetcode #338
6. **Bitwise AND of all numbers in range [m, n]** → Leetcode #201
7. **Swap even and odd bits in an integer**

---

Python Notes

- `bin(n)` → binary string
- `int('1010', 2)` → convert binary string to int
- Bit positions are usually 0-indexed from the **rightmost bit**

---

 Reference

- Python Docs: https://docs.python.org/3/library/stdtypes.html#bitwise-operations-on-integer-types
- Leetcode Bit Manipulation tag: https://leetcode.com/tag/bit-manipulation/
"""