import random

# def part3(A, f, l):
#     cur = A[f][1]
#     left = []
#     mid = []
#     right = []
#     j = 0
#     count = 0
#     for i in range(f, l+1):
#         if A[i][1] < cur:
#             left.append(A[i])
#             j += 1
#         elif A[i][1] == cur:
#             mid.append(A[i])
#             count += 1
#         else:
#             right.append(A[i])
#     A[f:l+1] = left + mid + right
#     return f+j, f+j+count-1
#
# def randomized_quick_sort(A, f, l):
#     if f < l:
#         k = random.randint(f, l)
#         A[f], A[k] = A[k], A[f]
#         m1, m2 = part3(A, f, l)
#         randomized_quick_sort(A, f, m1-1)
#         randomized_quick_sort(A, m2+1, l)

def height(unit):
    global tree
    h = 1
    if tree[unit][1] == 0:
        h_el = 1
        while tree[unit][0] != -1:
            unit = tree[unit][0]
            h_el = height(unit)
            h = max(h, 1 + h_el)
        tree[unit][1] = h_el
    else:
        h += tree[unit][1] - 1
    return h

with open('input.txt') as f:
    with open('output.txt', 'w') as f1:
        n = int(f.readline())
        arr = list(map(int, f.readline().split()))
        tree = []
        for i in range(n):
            tree.append([arr[i], 0])
        max_h = 1
        for i in range(n):
            max_h = max(max_h, height(i))
        f1.write(str(max_h))