'''
Input Harga: 370000
Input Diskon: 15
Output: harga yang harus dibayar adalah Rp. 314.500
'''

def hitung_harga_akhir(harga_awal, diskon):
    harga_diskon = (diskon / 100) * harga_awal
    harga_akhir = harga_awal - harga_diskon
    return harga_akhir

def main():
    try:
        harga_awal = float(input("Masukkan harga awal: "))
        diskon = float(input("Masukkan persentase diskon: "))
        if diskon < 0 or diskon > 100:
            print("Persentase diskon harus berada antara 0 dan 100.")
        else:
            harga_akhir = hitung_harga_akhir(harga_awal, diskon)
            print("Harga akhir setelah diskon adalah: ", harga_akhir)
    except ValueError:
        print("Masukan tidak valid. Pastikan Anda memasukkan angka.")

if __name__ == "__main__":
    main()