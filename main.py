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
        saldo = 0  # Saldo awal
        # Membaca data transaksi dari file eksternal saat memulai program
        list_transaksi = body.baca_data("dataPemasukan.txt") + body.baca_data("dataPengeluaran.txt")
        while True:
            body.menu()
            choice = input("\t\t        Pilih menu: ")

            if choice == "1":
                saldo = body.pemasukan(saldo, list_transaksi)
            elif choice == "2":
                saldo = body.pengeluaran(saldo, list_transaksi)
            elif choice == "3":
                body.tampilan_rekap()
                pilihan_rekap = input("\t       Pilih menu rekap data: ")
                body.rekap_data(list_transaksi, pilihan_rekap)
            elif choice == "4":
                body.TampilanList(list_transaksi)
                print("\t===========================================================================================")
            elif choice == "5":
                body.tampilkan_grafik(list_transaksi)
            elif choice == "6":
                body.keluar()
                break
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")
    else:
        print("Login gagal. Program berhenti.")

if __name__ == "__main__":
    main()
