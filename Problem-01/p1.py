s = input().strip()
n = len(s)

# Duplicate string for cyclic traversal
t = s + s

left = 0
seen = set()
current_sum = 0
max_sum = 0

for right in range(len(t)):
    while t[right] in seen or (right - left + 1) > n:
        seen.remove(t[left])
        current_sum -= (ord(t[left]) - ord('a') + 1)
        left += 1

    seen.add(t[right])
    current_sum += (ord(t[right]) - ord('a') + 1)

    max_sum = max(max_sum, current_sum)

print(max_sum)
