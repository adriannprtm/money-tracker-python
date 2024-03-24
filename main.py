"""
FITUR FITUR
- login
- input saldo
- Pemasukan
  - tanggal
  - katagori
  - nama kebutuhan
  - nominal 
  - saldo akhir
- Pengeluaran
  - tanggal
  - katagori
  - nama kebutuhan
  - nominal 
  - saldo akhir
- Pengurutan
  - tanggal
  - bulan
  - tahun
- menampilkan list pemasukan/pengeluaran

"""

import body

def main():
    logged_in = body.login()
    if logged_in:
        print("Login berhasil!")
        saldo = 0  # Saldo awal
        # Membaca data transaksi dari file eksternal saat memulai program
        list_transaksi = body.baca_data("dataPemasukan.txt") + body.baca_data("dataPengeluaran.txt")
        while True:
            print("\nMenu:")
            print("1. Pemasukan")
            print("2. Pengeluaran")
            print("3. Rekap data")
            print("4. Lihat daftar transaksi")
            print("5. Keluar")
            print("6. Tampilkan Chart")
            choice = input("Pilih menu: ")

            if choice == "1":
                saldo = body.pemasukan(saldo, list_transaksi)
            elif choice == "2":
                saldo = body.pengeluaran(saldo, list_transaksi)
            elif choice == "3":
                print("\nMenu Rekap Data:")
                print("1. Rekap data berdasarkan tanggal")
                print("2. Rekap data berdasarkan bulan")
                print("3. Rekap data berdasarkan tahun")
                print("0. Kembali ke Menu")
                pilihan_rekap = input("Pilih menu rekap data: ")
                body.rekap_data(list_transaksi, pilihan_rekap)
            elif choice == "4":
                body.TampilanList(list_transaksi)
            elif choice == "5":
                print("Terima kasih!")
            elif choice == "6":
                body.tampilkan_grafik(list_transaksi)
                break
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")
    else:
        print("Login gagal. Program berhenti.")

if __name__ == "__main__":
    main()
