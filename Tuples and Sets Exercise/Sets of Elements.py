n, m = [int(num) for num in input().split(" ")]
n_set = []
m_set = []
while n > 0:
    n_set.append(input())
    n -= 1
while m > 0:
    m_set.append(input())
    m -= 1
n_set = set(n_set)
m_set = set(m_set)

print("\n".join(sorted(n_set.intersection(m_set), key=lambda x: x)))
