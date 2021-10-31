def sum(a, b, c=0, d=None, e=0):
    print(f"a: {a}, b: {b}, c: {c}, d: {d}, e: {e}")
    total = a + b + c + e
    if d is not None:
        total += d
    return total

x = int(input())
# y = int(input())
# z = int(input())
# print(sum(a=x, c=z, e=y, b=None, d=None))

print(sum(1, 2))
print(sum(1, 2, 3))
print(sum(1, 2, 3, 4))
print(sum(1, 2, 3, 4, 5))
