from datetime import datetime

def login():
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    if username == "kelompokB6" and password == "123":
        return True
    else:
        return False


def input_saldo(saldo, list_transaksi):
    tanggal_input = input("Masukkan tanggal pemasukan (yyyy-mm-dd): ")
    tanggal = datetime.strptime(tanggal_input, "%Y-%m-%d").date()
    nominal = float(input("Masukkan saldo baru: "))
    saldo += nominal
    list_transaksi.append([tanggal, "Isi Saldo", "Isi Saldo", nominal, saldo])
    print("Data saldo berhasil disimpan.")
    # Menulis data transaksi ke file eksternal
    with open("dataPemasukan.txt", "a") as file:
        file.write(f"{tanggal},{'Isi Saldo'},{'Isi Saldo'},{nominal},{saldo}\n")
    return saldo  # Mengembalikan saldo baru


def pemasukan(saldo, list_transaksi): 
    tanggal_input = input("Masukkan tanggal pemasukan (yyyy-mm-dd): ")
    tanggal = datetime.strptime(tanggal_input, "%Y-%m-%d").date()
    nama_kebutuhan = input("Masukkan nama pemasukan: ")
    nominal = float(input("Masukkan nominal pemasukan: "))
    saldo += nominal
    list_transaksi.append([tanggal, 'Pemasukan', nama_kebutuhan, nominal, saldo])
    print("Data pemasukan berhasil disimpan.")
    # Menulis data transaksi ke file eksternal
    with open("dataPemasukan.txt", "a") as file:
        file.write(f"{tanggal},{'Pemasukan'},{nama_kebutuhan},{nominal},{saldo}\n")
    return saldo  # Mengembalikan saldo baru


def pengeluaran(saldo, list_transaksi):
    tanggal_input = input("Masukkan tanggal pengeluaran (yyyy-mm-dd): ")
    tanggal = datetime.strptime(tanggal_input, "%Y-%m-%d").date()
    nama_kebutuhan = input("Masukkan nama kebutuhan: ")
    nominal = float(input("Masukkan nominal pengeluaran: "))
    saldo -= nominal
    list_transaksi.append([tanggal, "Pengeluaran", nama_kebutuhan, nominal, saldo])
    print("Data pengeluaran berhasil disimpan.")
    # Menulis data transaksi ke file eksternal
    with open("dataPengeluaran.txt", "a") as file:
        file.write(f"{tanggal},{'Pengeluaran'},{nama_kebutuhan},{nominal},{saldo}\n")
    return saldo  # Mengembalikan saldo baru



def TampilanList(list_transaksi):
    print("                            <<<<  PEMASUKAN/PENGELUARAN  >>>                        ")
    print('===========================================================================================')
    print('|    Tanggal      |    Katagori     |     Nama Kebutuhan      |   Nominal   |    Saldo    |')
    print('===========================================================================================')
    

    for transaksi in list_transaksi:
        tanggal, kategori, nama_kebutuhan, nominal, saldo = transaksi
        print(f"|  {tanggal.strftime('%Y-%m-%d'):<13}  | {kategori:<15} | {nama_kebutuhan:<23} | {nominal:>11} | {saldo:>11} |")

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
        tanggal_input = input("Masukkan tanggal rekap (yyyy-mm-dd): ")
        tanggal = datetime.strptime(tanggal_input, "%Y-%m-%d").date()
        data_rekap = [transaksi for transaksi in list_transaksi if transaksi[0] == tanggal]
    elif pilihan == "2":  # Rekap data berdasarkan bulan
        bulan_input = input("Masukkan bulan rekap (mm-yyyy): ")
        bulan, tahun = bulan_input.split("-")
        data_rekap = [transaksi for transaksi in list_transaksi if transaksi[0].month == int(bulan) and transaksi[0].year == int(tahun)]
    elif pilihan == "3":  # Rekap data berdasarkan tahun
        tahun_input = input("Masukkan tahun rekap (yyyy): ")
        data_rekap = [transaksi for transaksi in list_transaksi if transaksi[0].year == int(tahun_input)]
    elif pilihan == "0":  # Kembali ke halaman menu
        return
    else:
        print("Pilihan tidak valid.")
        return
    if data_rekap:
        TampilanList(data_rekap)
    else:
        print("Tidak ada data untuk direkap.")


