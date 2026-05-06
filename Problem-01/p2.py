n = int(input())
arr = list(map(int, input().split()))
k = int(input())

if len(arr) != n:
    print("Invalid input")
else:
    mods = [x % k for x in arr]

    if len(set(mods)) > 1:
        print(-1)
    else:
        arr.sort()
        target = arr[n // 2]

        operations = 0
        for x in arr:
            operations += abs(x - target) // k

        print(operations)
