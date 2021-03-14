def missing_number(n, arr):
    l = len(arr)
    if l != (n-1): return -1
    total = (l + 1)*(l + 2)/2
    sum_arr = sum(arr)
    return int(total - sum_arr)


if __name__ == "__main__":
    n = int(input("Enter n:"))
    arr = list(map(int, input().split()))
    result = missing_number(n, arr)
    print(result)
