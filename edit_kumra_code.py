def merge(a, l, m, r):
    print("merge: m, l r: ", m, l, r)

    n1 = m - l + 1
    n2 = r - m
    left = [0]*n1
    right = [0]*n2
    for i in range(0, n1):
        left[i] = a[l + i]
    for j in range(0, n2):
        right[j] = a[m + j + 1]

    i = 0
    j = 0
    k = l

    while i < n1 and j < n2:
        if left[i] <= right[j]:
            a[k] = left[i]
            i += 1
        else:
            a[k] = right[j]
            j += 1
        k += 1
    print("L: ", end=" ")
    print(left)
    print("R: ", end=" ")
    print(right)
    print("a: ", end='')
    print(a)

    while i < n1:
        a[k] = left[i]
        i += 1
        k += 1

    while j < n1:
        a[k] = right[j]
        j += 1
        k += 1

    print("a: ", end='')
    print(a)

def mergesort(a, l, r):
    print("r (last m value): ", r)
    if l < r:
        m = (l + r) // 2
        print("pre-mergesort1: m, l, r: ", m, l, r)
        mergesort(a, l, m)
        print("pos-mergesort1: m, l, r: ", m, l, r)
        mergesort(a, m+1, r)
        print("pos-mergesort2: m, l, r: ", m, l, r)
        merge(a, l, m, r)


a = [7, 6, 5, 4, 3, 2, 2, 1]
mergesort(a, 0, len(a)-1)
print(a)
