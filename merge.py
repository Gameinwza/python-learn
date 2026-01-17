def merge(a, b, c):
    result = []

    i = j = 0
    k = len(c) - 1

    while i < len(a) or j < len(b) or k >= 0:
        av = a[i] if i < len(a) else float('inf')
        bv = b[j] if j < len(b) else float('inf')
        cv = c[k] if k >= 0 else float('inf')

        if av <= bv and av <= cv:
            result.append(av)
            i += 1
        elif bv <= av and bv <= cv:
            result.append(bv)
            j += 1
        else:
            result.append(cv)
            k -= 1

    return result


# def test_merge():
#     assert merge([1,3,5], [2,4], [9,7,6]) == [1,2,3,4,5,6,7,9]
#     assert merge([], [1,2], [4,3]) == [1,2,3,4]

#     print("✅ All tests passed")


print(merge([1,3,5], [2,4], [9,7,6]))
