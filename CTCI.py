#Problem from: https://www.hackerrank.com/challenges/ctci-making-anagrams
def number_needed(a, b):
    a, b = sorted(a), sorted(b)
    count = 0
    for ch in a:
        if ch in b:
            a = a[:a.index(ch)] + a[a.index(ch) + 1:]
            b = b[:b.index(ch)] + b[b.index(ch) + 1:]
        else:
            count += 1

    count += len([c for c in b if c not in a])

    return count

"""
a = input().strip()
b = input().strip()

print(number_needed(a, b))
"""