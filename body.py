import matplotlib.pyplot as plt
from datetime import datetime

def login():
    print("\t=======================================================")
    print("\t|                 MONEY TRACKER                       |")
    print("\t=======================================================")
    print("\t|     ooooooooooooooo  LOGIN  oooooooooooooooo        |")
    print("\t=======================================================")
    username = input("\t              Masukkan username: ")
    password = input("\t              Masukkan password: ")
    print("\t=======================================================")

    # Validasi username dan password
    if username == "admin" and password == "admin123":
        print("\t            Login berhasil! Selamat datang, Admin!")
        return True
    else:
        print("\t    Username atau password salah. Silakan coba lagi.")
        return False

def menu():
    print("\t=======================================================")
    print("\t|     ooooooooooooooo  MENU  oooooooooooooooo         |")
    print("\t=======================================================")
    print("\t|                1. Input saldo                       |")
    print("\t|                2. Pemasukan                         |")
    print("\t|                3. Pengeluaran                       |")
    print("\t|                4. Rekap Data                        |")
    print("\t|                5. Lihat daftar transaksi            |")
    print("\t|                6. Keluar                            |")
    print("\t=======================================================")
    choice = input("\t        Pilih menu: ")

def input_saldo(saldo, list_transaksi):
    tanggal_input = input("Masukkan tanggal pemasukan (dd-mm-yyyy): ")
    tanggal = datetime.strptime(tanggal_input, "%Y-%m-%d").date()
    nominal = float(input("Masukkan saldo baru: "))
    saldo += nominal
    list_transaksi.append([tanggal, "Isi Saldo", "Isi Saldo", nominal, saldo])
    print("Data saldo berhasil disimpan.")
    # Menulis data transaksi ke file eksternal
    with open("dataPemasukan.txt", "a") as file:
        file.write(f"{tanggal},{"Isi Saldo"},{"Isi Saldo"},{nominal},{saldo}\n")
    return saldo


def pemasukan(saldo, list_transaksi): 
    tanggal_input = input("Masukkan tanggal pemasukan (dd-mm-yyyy): ")
    tanggal = datetime.strptime(tanggal_input, "%d-%m-%Y").date()
    nama_kebutuhan = input("Masukkan nama pemasukan: ")
    nominal = float(input("Masukkan nominal pemasukan: "))
    saldo += nominal
    list_transaksi.append([tanggal, "Pemasukan", nama_kebutuhan, nominal, saldo])
    print("Data pemasukan berhasil disimpan.")
    # Menulis data transaksi ke file eksternal
    with open("dataPemasukan.txt", "a") as file:
        file.write(f"{tanggal},{"Pemasukan"},{nama_kebutuhan},{nominal},{saldo}\n")
    return saldo


def pengeluaran(saldo, list_transaksi):
    tanggal_input = input("Masukkan tanggal pengeluaran (dd-mm-yyyy): ")
    tanggal = datetime.strptime(tanggal_input, "%d-%m-%Y").date()
    nama_kebutuhan = input("Masukkan nama kebutuhan: ")
    nominal = float(input("Masukkan nominal pengeluaran: "))
    saldo -= nominal
    list_transaksi.append([tanggal, "Pengeluaran", nama_kebutuhan, nominal, saldo])
    print("Data pengeluaran berhasil disimpan.")
    # Menulis data transaksi ke file eksternal
    with open("dataPengeluaran.txt", "a") as file:
        file.write(f"{tanggal},{"Pengeluaran"},{nama_kebutuhan},{nominal},{saldo}\n")
    return saldo


def TampilanList(list_transaksi):
    print("                            <<<<  PEMASUKAN/PENGELUARAN  >>>                        ")
    print('===========================================================================================')
    print('|    Tanggal      |    Katagori     |     Nama Kebutuhan      |   Nominal   |    Saldo    |')
    print('===========================================================================================')

    for transaksi in list_transaksi:
        tanggal, kategori, nama_kebutuhan, nominal, saldo = transaksi
        print(f"|  {tanggal.strftime('%d-%m-%Y'):<13}  | {kategori:<15} | {nama_kebutuhan:<23} | {nominal:>11} | {saldo:>11} |")

def baca_data(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
        data = [line.strip().split(",") for line in lines]
        # Konversi tanggal menjadi objek datetime
        for entry in data:
            entry[0] = datetime.strptime(entry[0], "%Y-%m-%d").date()
    return data


def rekap_data(list_transaksi, pilihan):
    data_rekap = []
    if pilihan == "1":  # Rekap data berdasarkan tanggal
        tanggal_input = input("Masukkan tanggal rekap (dd-mm-yyyy): ")
        tanggal = datetime.strptime(tanggal_input, "%d-%m-%Y").date()
        if list_transaksi == "pemasukan":
            data_rekap = [transaksi for transaksi in baca_data("dataPemasukan.txt") if transaksi[0] == tanggal]
        elif list_transaksi == "pengeluaran":
            data_rekap = [transaksi for transaksi in baca_data("dataPengeluaran.txt") if transaksi[0] == tanggal]
    elif pilihan == "2":  # Rekap data berdasarkan bulan
        bulan_input = input("Masukkan bulan rekap (mm-yyyy): ")
        bulan, tahun = bulan_input.split("-")
        if list_transaksi == "pemasukan":
            data_rekap = [transaksi for transaksi in baca_data("dataPemasukan.txt") if transaksi[0].month == int(bulan) and transaksi[0].year == int(tahun)]
        elif list_transaksi == "pengeluaran":
            data_rekap = [transaksi for transaksi in baca_data("dataPengeluaran.txt") if transaksi[0].month == int(bulan) and transaksi[0].year == int(tahun)]
    elif pilihan == "3":  # Rekap data berdasarkan tahun
        tahun_input = input("Masukkan tahun rekap (yyyy): ")
        if list_transaksi == "pemasukan":
            data_rekap = [transaksi for transaksi in baca_data("dataPemasukan.txt") if transaksi[0].year == int(tahun_input)]
        elif list_transaksi == "pengeluaran":
            data_rekap = [transaksi for transaksi in baca_data("dataPengeluaran.txt") if transaksi[0].year == int(tahun_input)]
    else:
        print("Pilihan tidak valid.")
        return
    if data_rekap:
        TampilanList(data_rekap)
    else:
        print("Tidak ada data untuk direkap.")

def tampilan_rekap():
    print("\t=======================================================")
    print("\t|          <<<<  MENU REKAP DATA  >>>>                |")
    print("\t=======================================================")
    print("\t|       1. Rekap data berdasarkan tanggal             |")
    print("\t|       2. Rekap data berdasarkan bulan               |")
    print("\t        3. Rekap data berdasarkan tahun               |")
    print("\t=======================================================")
    pilihan_rekap = input("\t       Pilih menu rekap data: ")

from datetime import datetime

def tampilkan_grafik(list_transaksi):
    # Ambil tanggal dan nominal dari setiap transaksi
    tanggal = [transaksi[0] for transaksi in list_transaksi]
    nominal = [transaksi[3] for transaksi in list_transaksi]

    # Mengurutkan data berdasarkan tanggal
    tanggal, nominal = zip(*sorted(zip(tanggal, nominal)))

    # Konversi tanggal ke format yang dapat ditampilkan pada chart
    tanggal_str = [tgl.strftime('%d-%m-%Y') for tgl in tanggal]

    # Buat grafik
    plt.figure(figsize=(10, 6))
    plt.plot(tanggal_str, nominal, marker='o', linestyle='-')
    plt.title('Grafik Pemasukan/Pengeluaran')
    plt.xlabel('Tanggal')
    plt.ylabel('Nominal')
    plt.xticks(rotation=45)  # Putar label tanggal agar lebih mudah dibaca
    plt.grid(True)
    plt.tight_layout()

    # Tampilkan grafik
    plt.show()

