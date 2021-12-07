import math

def left(i):
    return 2*i + 1

def right(i):
    return 2*i + 2

def max_heapify(A, i):
    lf = left(i)
    rt = right(i)
    global heap_size
    if lf <= heap_size and A[lf] > A[i]:
        big = lf
        print(lf)
    else:
        big = i
    if rt <= heap_size and A[rt] > A[big]:
        big = rt
        print(rt)
    if big != i:
        A[i], A[big] = A[big], A[i]
        max_heapify(A, big)

def build_max_heap(A):
    global heap_size
    heap_size -= 1
    for i in range(math.floor(heap_size/2), -1, -1):
        print(i)
        max_heapify(A, i)
    return A

# def heapsort(A):
#     global heap_size
#     build_max_heap(A)
#     for i in range(len(A)-1, 0, -1):
#         A[0], A[i] = A[i], A[0]
#         heap_size -= 1
#         max_heapify(A, 0)
#     return A

with open('input.txt') as f:
    with open('output.txt', 'w') as f1:
        n = int(f.readline())
        arr = list(map(int, f.readline().split()))
        for i in range(math.floor(n/2)-1):
            if arr[i] > arr[left(i)] or arr[i] > arr[right(i)]:
                f1.write('NO')
                exit()
        f1.write('YES')