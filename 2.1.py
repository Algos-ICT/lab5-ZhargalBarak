import time

with open('input.txt') as f:
    with open('output.txt', 'w') as f1:
        n = int(f.readline())
        arr = list(map(int, f.readline().split()))
        tree = set(range(n)) - set(arr)
        start = time.perf_counter()
        max_h = 0
        for i in tree:
            h = 1
            elem = i
            while arr[elem] != -1:
                h += 1
                elem = arr[elem]
            max_h = max(max_h, h)
        print(time.perf_counter() - start)
        f1.write(str(max_h))
