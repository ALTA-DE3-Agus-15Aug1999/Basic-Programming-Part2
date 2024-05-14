# input
T = 20.0
r = 4.0


# kode disini
T = int(T)
r = int(r)

if r % 7 == 0:
    phi = 22/7
else :
    phi = 3.14

Lp = (2 * phi * r * (r + T) )
print("Luas Permukaan Tabung : ", (Lp))