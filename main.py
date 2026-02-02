import json

saldo = 0

def simpan_saldo():
    """Menyimpan saldo ke file JSON"""
    data = {"saldo": saldo}
    with open("saldo.json", "w") as file:
        json.dump(data, file)

def baca_saldo():
    """Membaca saldo dari file JSON"""
    global saldo
    try:
        with open("saldo.json", "r") as file:
            data = json.load(file)
            saldo = data["saldo"]
    except FileNotFoundError:
        saldo = 0

def tambah_pemasukan():
    global saldo
    jumlah = int(input("Masukkan jumlah pemasukan: "))
    saldo = saldo + jumlah
    print(f"Pemasukan sebesar Rp{jumlah:,} berhasil ditambahkan!")
    print(f"Saldo Anda sekarang: Rp{saldo:,}")
    simpan_saldo()

def tambah_pengeluaran():
    global saldo
    jumlah = int(input("Masukkan jumlah pengeluaran: "))
    if jumlah > saldo:
        print(f"⚠️ Peringatan: Saldo tidak cukup!")
        print(f"Saldo Anda: Rp{saldo:,}, Pengeluaran: Rp{jumlah:,}")
    else:
        saldo = saldo - jumlah
        print(f"Pengeluaran sebesar Rp{jumlah:,} berhasil dikurangi!")
        print(f"Saldo Anda sekarang: Rp{saldo:,}")
        simpan_saldo()

def lihat_saldo():
    print("=" * 35)
    print(f"💰 Saldo Anda: Rp{saldo:,}")
    print("=" * 35)

def menu():
    print("=== Aplikasi Pengelola Uang Saku ===")
    print("1. Tambah pemasukan")
    print("2. Tambah pengeluaran")
    print("3. Lihat saldo")
    print("4. Keluar")

baca_saldo()
while True:
    menu()
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tambah_pemasukan()
    elif pilihan == "2":
        tambah_pengeluaran()
    elif pilihan == "3":
        lihat_saldo()
    elif pilihan == "4":
        print("Terima kasih!")
        break
    else:
        print("Pilihan tidak valid")