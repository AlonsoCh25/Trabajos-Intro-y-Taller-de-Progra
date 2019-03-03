def fibon_sec (n):
    if n <= 1:
        return 1
    else:
        return fibon_sec (n-1) + fibon_sec (n-2)
