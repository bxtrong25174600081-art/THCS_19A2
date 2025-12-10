def tim_so_fibonacci(n):
    if n < 0:
        return -1 
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return tim_so_fibonacci(n - 1) + tim_so_fibonacci(n - 2)
n = 6
kq = tim_so_fibonacci(n)
print(f"Số Fibonacci thứ {n} là: {kq}")
