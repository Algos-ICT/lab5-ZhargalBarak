import math

def left(i):
    return 2*i + 1

def right(i):
    return 2*i + 2

def min_heapify(A, i):
    lf = left(i)
    rt = right(i)
    global heap_size
    if lf <= heap_size and A[lf] < A[i]:
        small = lf
    else:
        small = i
    if rt <= heap_size and A[rt] < A[small]:
        small = rt
    if small != i:
        global m, swaps
        m += 1
        swaps.append([i, small])
        A[i], A[small] = A[small], A[i]
        min_heapify(A, small)

def build_min_heap(A):
    global heap_size
    heap_size -= 1
    for i in range(math.floor(heap_size/2), -1, -1):
        min_heapify(A, i)

m = 0
swaps = []
with open('input.txt') as f:
    with open('output.txt', 'w') as f1:
        n = int(f.readline())
        heap_size = n
        pyr = list(map(int, f.readline().split()))
        build_min_heap(pyr)
        f1.write(str(m) + '\n')
        for i in range(len(swaps)):
            f1.write(str(swaps[i][0]) + ' ' + str(swaps[i][1]) + '\n')