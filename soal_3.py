def hitung_total_harga():
    total_harga = 0
    jumlah_barang = int(input("Masukkan Jumlah Barang : "))

    for i in range(jumlah_barang):
        harga = float(input(f"Masukkan Harga Barang ke-{i+1} : "))
        total_harga += harga
    
    return total_harga

total = hitung_total_harga()
print(f"Total Belanjaan : Rp {total:.2f}")
