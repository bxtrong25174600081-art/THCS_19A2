def kiem_tra_so_doi_xung(n):
    n = str(n)
    x = n[::-1]
    if n == x:
        return "True"
    else:
        return "False"
n = 121
print(kiem_tra_so_doi_xung(n))


