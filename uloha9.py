z = int(input("Zadaj z (zaciatok): "))
k = int(input("Zadaj k (koniec): "))
if z > k:
    z, k = k, z
print(','.join(str(i) for i in range(z, k+1) if i % 2 == 1))
