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
            print("1. Input saldo")
            print("2. Pemasukan")
            print("3. Pengeluaran")
            print("4. Rekap data")
            print("5. Lihat daftar transaksi")
            print("6. Keluar")
            choice = input("Pilih menu: ")

            if choice == "1":
                saldo = body.input_saldo(saldo, list_transaksi)
            elif choice == "2":
                saldo = body.pemasukan(saldo, list_transaksi)
            elif choice == "3":
                saldo = body.pengeluaran(saldo, list_transaksi)
            elif choice == "4":
                print("\nMenu Rekap Data:")
                print("1. Rekap data berdasarkan tanggal")
                print("2. Rekap data berdasarkan bulan")
                print("3. Rekap data berdasarkan tahun")
                pilihan_rekap = input("Pilih menu rekap data: ")
                body.rekap_data(list_transaksi, pilihan_rekap)
            elif choice == "5":
                body.TampilanList(list_transaksi)
            elif choice == "6":
                print("Terima kasih!")
                break
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")
    else:
        print("Login gagal. Program berhenti.")

if __name__ == "__main__":
    main()
