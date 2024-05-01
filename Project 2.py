import csv
import os
import time
from datetime import datetime
from prettytable import PrettyTable as pt
from tqdm import tqdm 
database_user = []
database_produk = []
namaproduk = []
hargaproduk = []
hargaprodukfix = []
databasefix = []
database_fix = []
keranjang = []
keranjang_cetak = []
login_ = [0]
user_login = []
kategori = []
cari = [0]
transaksi = []
rute = []
tujuan = []

with open ("C:/Code/Algo Pemro 2/Final Project 2/DATA PRODUK.csv") as file :
    baca = csv.reader(file, delimiter=",")
    for row in baca :
        database_produk.append(row)

with open ("C:/Code/Algo Pemro 2/Final Project 2/User.csv", 'r') as file :
    baca = csv.reader(file)
    for i in baca :
        database_user.append(i)
        
def masukkan_barang (database, nama_produk, harga_produk):
    for i in range(1, (len(database)-1)) :
        nama = database[i][2]
        harga = int(database [i][3])
        nama_produk.append(nama)
        harga_produk.append(harga)

def tambah_nomor (database, database_fix):
    for i in range (len(database)) :
        x = [f"{database_produk[i+1][0]}", f"{database[i][0]}", f"{database[i][1]}"]
        database_fix.append(x)
        
def menambahkan_rp (harga_produk, harga_produk_fix):
    for i in range(len(harga_produk)):
        x = f"Rp.{harga_produk[i]}"
        harga_produk_fix.append(x)
    
def menyatukan (nama_produk, harga_produk_fix, database_fix):
    for i in range (len(harga_produk_fix)):
        x = [f"{nama_produk[i]}", f"{harga_produk_fix[i]}"]
        database_fix.append(x)

def loading () :
  for i in tqdm(range(100)): 
    time.sleep(0.001) 
      
def bersih ():
    os.system('cls')

def judul ():
    print ("=" * 54)
    print ("|       'ATERAE' Solusi Belanja Kebutuhan Harian      |")
    print ("=" * 54)

def keluar ():
    bersih()
    judul()
    print("TERIMAKASIH TELAH MENGGUNAKAN SOFTWARE ANTERAE")
    exit()

def kosong ():
    for i in user_login :
        user_login.pop ()
    for i in range(len(keranjang)) :
        keranjang.pop ()
    login_[0] = 0

def mahal ():
    tanpa_rp = []
    tanpa_rp_fix = []
    ada_rp = []
    ada_rp_fix = []
    menyatukan(namaproduk, hargaproduk, tanpa_rp)
    tambah_nomor(tanpa_rp, tanpa_rp_fix)
    def harga_mahal (database1):
        if len(database1) <= 1:
            return database1
        mid = len(database1) // 2
        left_half = database1[:mid]
        right_half = database1[mid:]
        left_sorted = harga_mahal(left_half)
        right_sorted = harga_mahal(right_half)
        return merge_mahal(left_sorted, right_sorted)
    def merge_mahal(left, right):
        result = []
        left_index = right_index = 0
        while left_index < len(left) and right_index < len(right):
            left_value = left[left_index]
            right_value = right[right_index]
            if int(left_value[2]) >= int(right_value[2]):
                result.append(left_value)
                left_index += 1
            else:
                result.append(right_value)
                right_index += 1
        result.extend(left[left_index:])
        result.extend(right[right_index:])
        return result
    ada_rp = harga_mahal(tanpa_rp_fix)
    for i in range (len(ada_rp)) :
        no = ada_rp[i][0]
        merek = ada_rp[i][1]
        harga = ada_rp[i][2]
        hasil = [f'{no}',f'{merek}',f'Rp.{harga}']
        ada_rp_fix.append(hasil)
    lihat_produk(ada_rp_fix)

def murah ():
    tanpa_rp = []
    tanpa_rp_fix = []
    ada_rp = []
    ada_rp_fix = []
    menyatukan(namaproduk, hargaproduk, tanpa_rp)
    tambah_nomor(tanpa_rp, tanpa_rp_fix)
    def harga_mahal (database1):
        if len(database1) <= 1:
            return database1
        mid = len(database1) // 2
        left_half = database1[:mid]
        right_half = database1[mid:]
        left_sorted = harga_mahal(left_half)
        right_sorted = harga_mahal(right_half)
        return merge_mahal(left_sorted, right_sorted)
    def merge_mahal(left, right):
        result = []
        left_index = right_index = 0
        while left_index < len(left) and right_index < len(right):
            left_value = left[left_index]
            right_value = right[right_index]
            if int(left_value[2]) <= int(right_value[2]):
                result.append(left_value)
                left_index += 1
            else:
                result.append(right_value)
                right_index += 1
        result.extend(left[left_index:])
        result.extend(right[right_index:])
        return result
    ada_rp = harga_mahal(tanpa_rp_fix)
    for i in range (len(ada_rp)) :
        no = ada_rp[i][0]
        merek = ada_rp[i][1]
        harga = ada_rp[i][2]
        hasil = [f'{no}',f'{merek}',f'Rp.{harga}']
        ada_rp_fix.append(hasil)
    lihat_produk(ada_rp_fix)

def terjual ():
    def data_120 ():
        terjual_ = []
        for i in range(len(database_fix)):
            isi = database_produk[i+1][5]
            isi_fix = [f'{database_fix[i][0]}',f'{database_fix[i][1]}',f'{database_fix[i][2]}',f'{isi}']
            terjual_.append(isi_fix)
        def shorting_terjual(data):
            if len(data) <= 1:
                return data
            mid = len(data) // 2
            left_half = data[:mid]
            right_half = data[mid:]
            left_sorted = shorting_terjual(left_half)
            right_sorted = shorting_terjual(right_half)
            return merge_terjual(left_sorted, right_sorted)
        def merge_terjual(left, right):
            result = []
            left_index = right_index = 0
            while left_index < len(left) and right_index < len(right):
                left_value = left[left_index]
                right_value = right[right_index]
                if left_value[3] >= right_value[3]:
                    result.append(left_value)
                    left_index += 1
                else:
                    result.append(right_value)
                    right_index += 1
            result.extend(left[left_index:])
            result.extend(right[right_index:])
            return result
        banyak_terjual = shorting_terjual(terjual_)
        def tabel_terjual (database):
            x = pt(["No ID Barang","Nama Produk","Harga Produk","Terjual/Bulan"])
            for i in range(len(database)): 
                 x.add_row(database[i])
            print(x)
        tabel_terjual(banyak_terjual)
    if len(database_produk) <= 120 :
        data_120()
    elif len(database_produk) > 120 :
        mahal()
    
def urut_abjad ():
    def shorting_abjad(data):
        if len(data) <= 1:
            return data
        mid = len(data) // 2
        left_half = data[:mid]
        right_half = data[mid:]
        left_sorted = shorting_abjad(left_half)
        right_sorted = shorting_abjad(right_half)
        return merge_abjad(left_sorted, right_sorted)
    def merge_abjad(left, right):
        result = []
        left_index = right_index = 0
        while left_index < len(left) and right_index < len(right):
            left_value = left[left_index]
            right_value = right[right_index]
            if left_value[1] <= right_value[1]:
                result.append(left_value)
                left_index += 1
            else:
                result.append(right_value)
                right_index += 1
        result.extend(left[left_index:])
        result.extend(right[right_index:])
        return result
    lihat_produk(shorting_abjad(database_fix))

def terbaru ():
    terbaru_fix = []
    def shorting_barangbaru(data):
        if len(data) <= 1:
            return data
        mid = len(data) // 2
        left_half = data[:mid]
        right_half = data[mid:]
        left_sorted = shorting_barangbaru(left_half)
        right_sorted = shorting_barangbaru(right_half)
        return merge_barangbaru(left_sorted, right_sorted)
    def merge_barangbaru(left, right):
        result = []
        left_index = right_index = 0
        while left_index < len(left) and right_index < len(right):
            left_value = left[left_index]
            right_value = right[right_index]
            if parse_date(left_value[3]) >= parse_date(right_value[3]):
                result.append(left_value)
                left_index += 1
            else:
                result.append(right_value)
                right_index += 1
        result.extend(left[left_index:])
        result.extend(right[right_index:])
        return result
    def parse_date(date_str):
        try:
            return datetime.strptime(date_str, '%d/%m/%Y')
        except ValueError:
            return None
    for i in range(len(database_fix)):
        tanggal = database_produk[i+1][6]
        isi = [f'{database_fix[i][0]}',f'{database_fix[i][1]}',f'{database_fix[i][2]}',f'{tanggal}']
        terbaru_fix.append(isi)
    terbaru_fix2 = shorting_barangbaru(terbaru_fix)
    def tabel_terjual (database):
        x = pt(["No ID Barang","Nama Produk","Harga Produk","Tanggal Masuk"])
        for i in range(len(database)): 
             x.add_row(database[i])
        print(x)
    tabel_terjual(terbaru_fix2)
    
def search (key):
    bersih()
    judul()
    cari[0]=0
    def searching(data, key):
        # Basis: jika data hanya memiliki satu elemen atau kosong, kembalikan data tersebut
        if len(data) == 0:
            return []
        if len(data) == 1:
            if key in data[0][1].lower():
                return [data[0]]
            else:
                return []
        # Langkah 1: Bagi data menjadi dua setengah
        mid = len(data) // 2
        left_half = data[:mid]
        right_half = data[mid:]
        # Langkah 2: Panggil rekursif pada kedua setengah data
        left_searching = searching(left_half, key)
        right_searching = searching(right_half, key)
        # Langkah 3: Gabungkan dan urutkan kembali kedua setengah data yang sudah diurutkan
        return merge(left_searching, right_searching)
    def merge(left, right):
        result = []
        left_index = right_index = 0
        while left_index < len(left) and right_index < len(right):
            if (left[left_index][0]) < (right[right_index][0]):
                result.append(left[left_index])
                left_index += 1
            else:
                result.append(right[right_index])
                right_index += 1
        # Menambahkan sisa elemen dari setengah data yang masih tersisa
        result.extend(left[left_index:])
        result.extend(right[right_index:])
        return result
    # Menampilkan semua data yang sudah terurut dari yang paling murah
    searching_data = searching(database_fix, key)
    if len(searching_data) > 0:
        bersih()
        judul()
        print("Hasil Pencarian:")
        lihat_produk(searching_data)
        cari[0] = 1
    else:
        print(">>>>>Tidak ditemukan barang dengan kata kunci tersebut<<<<<")

def lihat_produk (database):
    x = pt(["No ID Barang","Nama Produk","Harga Produk"])
    for i in range(len(database)): 
         x.add_row(database[i])
    print(x)

def kelompok_kategori () :
    for i in range(1,(len(database_produk))):
        if database_produk[i][1] not in kategori :
            kategori.append(database_produk[i][1])
    for i in range(len(kategori)):
        fix = [f"{i+1}", f"{kategori[i]}"]
        kategori[i] = fix
            
def tambah_produk (kategori):
    kelompok_kategori()
    bersih()
    judul()
    banyak = int(input("Banyak Data Yang Dimasukkan :"))
    for i in range(1, (banyak+1)) :
        bersih()
        judul()
        print (f"Barang Ke {i}")
        for i in range(len(kategori)) :
            print (f"[{kategori[i][0]}]. {kategori[i][1]}")
        print(f"[{len(kategori)+1}]. Tambah Kategori Baru")
        pilihan = int(input("Masukkan Pilihan Anda :"))
        if pilihan <= (len(kategori)) :
            kategori = kategori[pilihan]
            merek = input("Masukkan Nama Produk :")
            harga = int(input("Masukkan Harga Produk (Contoh : 15000) :"))
            stock = int(input("Masukkan Banyak Produk :"))
            waktu = datetime.now()
            isi = f"{(len(database_produk))+1};{kategori}";f"{merek}";f"{harga}";f"{stock}";f"{0}";f"{waktu.day}/{waktu.month}/{waktu.year}"
            database_produk.append(isi)
        elif pilihan == ((len(kategori))+1) :
            kategori = input("Masukkan Kategori Baru :")
            merek = input("Masukkan Nama Produk :")
            harga = int(input("Masukkan Harga Produk (Contoh : 15000) :"))
            stock = int(input("Masukkan Banyak Produk :"))
            waktu = datetime.now()
            isi = f"{(len(database_produk))+1};{kategori}";f"{merek}";f"{harga}";f"{stock}";f"{0}";f"{waktu.day}/{waktu.month}/{waktu.year}"
            database_produk.append(isi)
        else :
            def tidak_ada ():
                print (
                    "Masukkan Pilihan Yang Tersedia"
                    "Apakah Anda Ingin Mengulang ?"
                    "[1]. Ya"
                    "[2] Tidak"
                )
                pilih = int(input("Masukkan Pilihan Anda :"))
                if pilih == 1 :
                    tambah_produk (kategori)
                elif pilih == 2 :
                    homepage_pusat()
                else :
                    tidak_ada()
            tidak_ada()

def tambah_isi_keranjang ():
    nomor_barang = int(input("Masukkan Nomor Barang :"))
    def tambah ():
        keranjang.append(database_produk[nomor_barang])
        print(
            "Berhasil Ditambahkan\n"
            "Apakah Ingin Menambahkan Lagi?\n"
            "[1]. Ya\n"
            "[2]. Tidak"
        )
        konf = int(input("Pilihan :"))
        if konf == 1 :
            tambah_isi_keranjang()
        elif konf == 2 :
            homepage_pusat()
        else :
            def ulang ():
                print(
                    "Masukkan Pilihan Yang Ada"
                    "Apakah Ingin Menambahkan Lagi?\n"
                    "[1]. Ya\n"
                    "[2]. Tidak"
                )
                x = int(input("Masukkan Pilihan :"))
                if x == 1  :
                    tambah_isi_keranjang()
                elif x == 2 :
                    homepage_pusat()
                else :
                    ulang()
            ulang()   
    if len(keranjang) == 1 :
        tambah()
    else :
        for i in range(1, len(keranjang)) :
            if nomor_barang == int(keranjang[i][0]) :
                print("Barang Sudah Ada Di Keranjang")
                input(">>>>ENTER<<<<")
                print(
                    "Apakah Ingin Menambahkan Lagi?\n"
                    "[1]. Ya\n"
                    "[2]. Tidak"
                )
                konf = int(input("Pilihan :"))
                if konf == 1 :
                    tambah_isi_keranjang()
                elif konf == 2 :
                    homepage_pusat()
                else :
                    def ulang ():
                        print(
                            "Masukkan Pilihan Yang Ada"
                            "Apakah Ingin Menambahkan Lagi?\n"
                            "[1]. Ya\n"
                            "[2]. Tidak"
                        )
                        x = int(input("Masukkan Pilihan :"))
                        if x == 1  :
                            tambah_isi_keranjang()
                        elif x == 2 :
                            homepage_pusat()
                        else :
                            ulang()
                    ulang()   
            else :
                tambah()

def log_out (user, keranjang):
    with open (f'C:/Code/Algo Pemro 2/Final Project 2/Database User/{user[0]}.csv', 'w', newline='') as baru :
        tulis = csv.writer(baru)
        tulis.writerows(keranjang)
    
def register (database):
    user = input("Masukkan Username :")
    pas = input("Masukkan Password :")
    itera = 0 
    for i in range(len(database)):
        if user == database [i][0]:
            print("Username telah digunakan, silahkan gunakan yang lain")
            input("<<<<Pencet Enter>>>>")
            register(database)
        elif itera == (len(database)-1) :
            if (len(database_user)-1) < 5 :
                print (
                    "Data berhasil ditambahkan\n"
                    "Silahkan Login"
                    )
                baru = [user, pas]
                database.append(baru)
                file3 = f"C:/Code/Algo Pemro 2/Final Project 2/Database User/{user}.csv"
                with open(file3, 'w', newline='') as file :
                    new = csv.writer(file)
                    isi = ['Nomor ID Barang','Kategori','Merek','Harga','Stok','Terjual','Tanggal Masuk']
                    new.writerow(isi)
                input("<<<<Pencet Enter>>>>")
            elif (len(database_user)-1) >= 5 :
                print("User sudah ada 5, kami tidak menerima lagi")
        else :
            itera+=1
    with open ('C:/Code/Algo Pemro 2/Final Project 2/User.csv', 'w', newline='') as baru :
        tulis = csv.writer(baru)
        tulis.writerows(database)
        
def login (database):
    user = input("Masukkan Username :")
    pas = input("Masukkan Password :")
    loading()
    itera = 0 
    login__ = 0
    for i in range(len(database)):
        if user == database [i][0]:
            if pas == database[i][1] :
                print("Login Berhasil")
                input(">>>>>Tekan Enter<<<<<<")
                if user == "admin":
                    login__ += 2
                    login_[0]=login__
                    user_login.append(user)
                    with open ("C:/Code/Algo Pemro 2/Final Project 2/Riwayat Transaksi.csv") as file :
                        baca = csv.reader(file)
                        for i in baca :
                            transaksi.append(i)
                    homepage_pusat()
                else :
                    login__ += 1
                    login_[0]=login__
                    user_login.append(user)
                    file2 = f"C:/Code/Algo Pemro 2/Final Project 2/Database User/{user}.csv"
                    with open(file2, 'r') as file :
                        baca = csv.reader(file)
                        for i in baca:
                            keranjang.append(i)
                    homepage_pusat()         
            else :
                def salah ():
                    print("Password Salah")
                    print(
                        "Apakah Anda Ingin Mengulang?\n"
                        "[1]. Ya\n"
                        "[2]. Tidak"
                    )
                    x = int(input("Masukkan Pilihan Anda :"))
                    if x == 1 :
                        bersih()
                        judul()
                        login(database)
                    elif x == 2 :
                        homepage_pusat()
                    else :
                        print("Masukkan Pilihan Yang Tersedia")
                        input("<<<<Pencet Enter>>>>")
                        salah()
                salah()
        elif itera == (len(database)-1) :
            bersih()
            judul()
            print ("Data tidak ditemukan")
            print(
                "Apakah Anda Ingin Mengulang?\n"
                "[1]. Ya\n"
                "[2]. Tidak"
            )
            x = int(input("Masukkan Pilihan Anda :"))
            if x == 1 :
                bersih()
                judul()
                login(database)
            elif x == 2 :
                homepage_pusat()
        else :
            itera+=1

def cetak_kategori():
    bersih()
    judul()
    print("         Daftar Kategori Barang")
    for i in range (len(kategori)):
        print(f"[{kategori[i][0]}]. {kategori[i][1]}")
    print(f"[{len(kategori)+1}]. Kembali")

def pengantaran () :
    graf = {
        'tumparejo': ['ambulu', 'jenggala', 'mumbul sari', 'silo'],
        'ambulu': ['tumparejo', 'wuluhan', 'jenggala'],
        'wuluhan': ['ambulu', 'puger', 'balung', 'rambi puji', 'jenggala'],
        'puger': ['wuluhan', 'gumuk mas', 'umbul sari', 'balung'],
        'gumuk mas': ['kencong', 'puger', 'umbul sari'],
        'kencong': ['gumuk mas', 'umbul sari', 'tanggul', 'sumber baru'],
        'umbul sari': ['kencong', 'gumuk mas', 'puger', 'balung', 'rambi puji', 'panti', 'tanggul'],
        'balung': ['umbul sari', 'puger', 'wuluhan', 'rambi puji'],
        'rambi puji': ['umbul sari', 'balung', 'wuluhan', 'jenggala', 'kaliwates', 'suko rambi', 'panti'],
        'jenggala': ['wuluhan', 'ambulu', 'tumparejo', 'mumbul sari', 'batang', 'sumber sari', 'kaliwates', 'suko rambi', 'rambi puji'],
        'mumbul sari': ['jenggala', 'tumparejo', 'silo', 'batang'],
        'silo': ['tumparejo', 'mumbul sari', 'batang', 'ledok ombo'],
        'batang': ['mumbul sari', 'silo', 'ledok ombo', 'kalis', 'pakusari', 'sumbersari', 'jenggala'],
        'sumber sari': ['batang', 'pakusari', 'arjasa', 'patrang', 'kaliwates', 'jenggala'],
        'pakusari': ['batang', 'kalis', 'arjasa', 'sumbersari'],
        'kaliwates': ['jenggala', 'sumbersari', 'patrang', 'suko rambi', 'rambi puji'],
        'patrang': ['kaliwates', 'sumbersari', 'arjasa', 'suko rambi'],
        'suko rambi': ['rambi puji', 'jenggala', 'kaliwates', 'patrang', 'arjasa', 'panti'],
        'panti': ['umbul sari', 'rambi puji', 'suko rambi', 'arjasa'],
        'tanggul': ['sumber baru', 'kencong', 'umbul sari'],
        'sumber baru': ['kencong', 'tanggul'],
        'arjasa': ['panti', 'suko rambi', 'patrang', 'sumbersari', 'pakusari', 'kalis', 'sukowono'],
        'kalis': ['arjasa', 'pakusari', 'batang', 'ledok ombo', 'sukowono'],
        'sukowono': ['arjasa', 'kalis', 'ledok ombo', 'sumber jambe'],
        'ledok ombo': ['kalis', 'batang', 'silo', 'sumber jambe', 'sukowono'],
        'sumber jambe': ['sukowono', 'ledok ombo']
    }
    def cari_jalan(graf, awal, akhir, jalur):
        jalur = jalur + [awal]
        if awal == akhir:
            return [jalur]
        if awal not in graf:
            return []
        semua_jalur = []
        for titik in graf[awal]:
            if titik not in jalur:
                jalur2 = cari_jalan(graf, titik, akhir, jalur.copy())  # Create a copy of jalur
                for jalur_baru in jalur2:
                    semua_jalur.append(jalur_baru)
        return semua_jalur
    def counter(data):
        rute = ' > '.join(data) 
        return rute
    start = 'tumparejo'
    finish = input('Masukkan Tujuan Anda: ').lower()
    tujuan.append(finish)
    data_x = cari_jalan(graf, start, finish, [])
    shortest_route = min(data_x, key=len)
    if len(shortest_route) <= 3 :
        rute.append(counter(shortest_route))
    else :
        rute.append("Jalur Tidak Ada Yang Kurang Dari 3")

def cetak_isi_kategori(x):
    key = kategori[x-1][1]
    produk = []
    bersih()
    judul()
    print(f"        Daftar Kategori {key}")
    for i in range(len(database_produk)) :
        if database_produk[i][1] == key :
            produk.append(database_fix[i-1])
    print(produk)
    lihat_produk(produk)
      
def homepage_pusat ():
    if (login_[0]) == 1 :
        def homepage_user():
            bersih()
            judul()
            print (f"         Selamat Datang {user_login[0]} di Software ANTERAE!!")
            print ("")
            waktu = datetime.now()
            print (f"{waktu.day}/{waktu.month}/{waktu.year}                                  {waktu.hour}:{waktu.minute}")
            print()
            print(
                "[1]. Lihat Semua Produk\n"
                "[2]. Cari Produk\n"
                "[3]. Kategori Produk\n"
                "[4]. Keranjang\n"
                "[5]. Logout"
                )
            print()
            konfirmasi = int(input("Masukkan Pilihan Anda :"))
            if konfirmasi == 1 :
                bersih()
                judul()
                print ("    Daftar Produk Yang Kami Miliki")
                lihat_produk(database_fix)
                print(
                    "[1]. Kembali\n"
                    "[2]. Tambahkan Produk Ke Keranjang\n"
                    "[3]. Urutkan Berdasarkan Abjad\n"
                    "[4]. Urutkan Berdasarkan Termahal\n"
                    "[5]. Urutkan Berdasarkan Termurah\n"
                    "[6]. Urutkan Berdasarkan Terlaris\n"
                    "[7]. Urutkan Berdasarkan Terbaru"
                )
                pilih = int(input("Masukkan Pilihan Anda :"))
                if pilih == 1 :
                    homepage_user()
                elif pilih == 2 :
                    tambah_isi_keranjang()
                elif pilih == 3 :
                    bersih()
                    judul()
                    print("         Daftar Produk Berdasarkan Abjad")
                    urut_abjad()
                    print(
                        "[1]. Kembali\n"
                        "[2]. Tambah Produk Ke Keranjang\n"
                    )
                    pilih_3 = int(input("Masukkan Pilihan Anda :"))
                    if pilih_3 == 1 :
                        homepage_user()
                    elif pilih_3 == 2 :
                        tambah_isi_keranjang()
                    else :
                        print("ERROR PILIHAN TIDAK DITEMUKAN SILAHKAN ULANGI")
                        input(">>>>>Pencet Enter<<<<<")
                        homepage_user()
                elif pilih == 4 :
                    bersih()
                    judul()
                    print("      Daftar Produk Berdasarkan Harga Termahal")
                    mahal()
                    print(
                        "[1]. Kembali\n"
                        "[2]. Tambah Ke Keranjang\n"
                    )
                    pilih4 = int(input("Masukkan Pilihan Anda :"))
                    if pilih4 == 1 :
                        homepage_user()
                    elif pilih4 == 2 :
                        tambah_isi_keranjang()
                    else :
                        print("ERROR PILIHAN TIDAK DITEMUKAN SILAHKAN ULANGI")
                        input(">>>>>Pencet Enter<<<<<")
                        homepage_user()
                elif pilih == 5 :
                    bersih()
                    judul()
                    print("      Daftar Produk Berdasarkan Harga Termurah")
                    murah()
                    print(
                        "[1]. Kembali\n"
                        '[2]. Tambah Ke Keranjang'
                    ) 
                    pilih5 = int(input("Masukkan Pilihan Anda :"))
                    if pilih5 == 1 :
                        homepage_user()
                    elif pilih5 == 2 :
                        tambah_isi_keranjang()
                    else :
                        print("ERROR PILIHAN TIDAK DITEMUKAN SILAHKAN ULANGI")
                        input(">>>>>Pencet Enter<<<<<")
                        homepage_user()
                elif pilih == 6 :
                    bersih()
                    judul()
                    print("      Daftar Produk Berdasarkan Terjual Per Bulan")
                    terjual()
                    print(
                        "[1]. Kembali\n"
                        '[2]. Tambah Ke Keranjang'
                    ) 
                    pilih6 = int(input("Masukkan Pilihan Anda :"))
                    if pilih6 == 1 :
                        homepage_user()
                    elif pilih6 == 2 :
                        tambah_isi_keranjang()
                    else :
                        print("ERROR PILIHAN TIDAK DITEMUKAN SILAHKAN ULANGI")
                        input(">>>>>Pencet Enter<<<<<")
                        homepage_user()
                elif pilih == 7 :
                    bersih()
                    judul()
                    print("      Daftar Produk Berdasarkan Tanggal Masuk Terbaru")
                    terbaru()
                    print(
                        "[1]. Kembali\n"
                        '[2]. Tambah Ke Keranjang'
                    ) 
                    pilih6 = int(input("Masukkan Pilihan Anda :"))
                    if pilih6 == 1 :
                        homepage_user()
                    elif pilih6 == 2 :
                        tambah_isi_keranjang()
                    else :
                        print("ERROR PILIHAN TIDAK DITEMUKAN SILAHKAN ULANGI")
                        input(">>>>>Pencet Enter<<<<<")
                        homepage_user()
                else :
                    bersih()
                    judul()
                    print("ERROR PILIHAN TIDAK DITEMUKAN SILAHKAN ULANGI")
                    input(">>>>>Pencet Enter<<<<<")
                    homepage_user()
            elif konfirmasi == 2 :
                bersih()
                judul()
                key = input("Masukkan Kata Kunci :")
                search(key)
                if cari[0] == 1 :
                    print (
                        "[1]. Kembali\n"
                        "[2]. Tambah Produk Ke Keranjang"
                    )
                    pilih_cari = int(input("Masukkan Pilihan Anda :"))
                    if pilih_cari == 1 :
                        homepage_user()
                    elif pilih_cari == 2 :
                        tambah_isi_keranjang()
                    else :
                        print("ERROR PILIHAN TIDAK DITEMUKAN SILAHKAN ULANGI")
                        input(">>>>>Pencet Enter<<<<<")
                        homepage_user()
            elif konfirmasi == 3 :
                def kon_3 ():
                    cetak_kategori()
                    x = int(input("Masukkan Pilihan Anda :"))
                    if x in range(1, len(kategori)) :
                        def x_1 ():
                            cetak_isi_kategori(x)
                            print(
                                "[1]. Tambahkan Produk Ke Keranjang\n"
                                "[2]. Lihat Kategori Lain\n"
                                "[3]. Kembali Ke Halaman Utama"
                            )
                            lanjut = int(input("Masukkan Pilihan Anda :"))
                            if lanjut == 1 :
                                tambah_isi_keranjang()
                            elif lanjut == 2 :
                                kon_3()
                            elif lanjut == 3 :
                                homepage_user()
                            else :
                                bersih()
                                judul()
                                print("Pilihan Tidak Ditemukan Silahkan Masukkan Pilihan Yang Disediakan!!")
                                input("<<<Tekan Enter>>>")
                                x_1()
                        x_1()
                    elif x == (len(kategori)+1) :
                        homepage_user()
                    else :
                        bersih()
                        judul()
                        print("Pilihan Tidak Ditemukan Silahkan Masukkan Pilihan Yang Disediakan!!")
                        input("<<<Tekan Enter>>>")
                        kon_3() 
                kon_3()
            elif konfirmasi == 4 :
                bersih()
                judul()
                print("           ISI KERANJANG ANDA")
                for i in range(len(keranjang)):
                    key = keranjang[i][0]
                    for i in range(len(database_produk)):
                        if key == database_produk[i][0]:
                            keranjang_cetak.append(database_fix[i-1])
                x = pt(["No ID Barang","Nama Produk","Harga Produk"])
                for i in range(len(keranjang_cetak)): 
                    x.add_row(keranjang_cetak[i])
                print(x)
                for i in range(len(keranjang_cetak)):
                    keranjang_cetak.pop ()
                print(
                    "[1]. Kembali\n"
                    "[2]. Hapus Barang Dari Keranjang\n"
                    "[3]. Pesan Barang"
                )  
                pilih4 = int(input("Masukkan Pilihan Anda :"))
                if pilih4 == 1 :
                    homepage_user()   
                elif pilih4 == 2 :
                    def hapus ():
                        hapus_isi = int(input("Masukkan Nomor Barang Yang Ingin Dihapus :"))
                        loading()
                        for i in range(1, (len(keranjang))) :
                            if hapus_isi == int(keranjang[i][0]) :
                                keranjang.pop(i)
                                print ("Data Berhasil Dihapus")
                                print(
                                    "[1]. Kembali\n"
                                    "[2]. Hapus Lagi"
                                )
                                konfirmasi_hapus = int(input("Masukkan Pilihan Anda :"))
                                if konfirmasi_hapus == 1 :
                                    homepage_user()
                                elif konfirmasi_hapus == 2 :
                                    hapus()
                            elif i == (len(keranjang)-1):
                                print(
                                    "Barang Tidak Berada Di Keranjang\n"
                                    "Apakah Anda Ingin Mengulang ?\n"
                                    "[1]. Ya\n"
                                    "[2]. Tidak"
                                )
                                konfirmasi_tidak_ditemukan = int(input("Masukkan Pilihan Anda :"))
                                if konfirmasi_tidak_ditemukan == 1 :
                                    hapus()
                                elif konfirmasi_tidak_ditemukan == 2 :
                                    homepage_user()
                                else :
                                    print("ERROR PILIHAN TIDAK DITEMUKAN SILAHKAN ULANGI")
                                    input(">>>>>Pencet Enter<<<<<")
                                    homepage_user()
                    hapus()
                elif pilih4 == 3 :
                    if len(keranjang) == 1 :
                        loading()
                        print("Keranjang Masih Kosong Harap Masukkan Barang Terlebih Dahulu")
                        input (">>>>ENTER<<<<")
                        homepage_user()
                    else :
                        def jumlah ():
                            beli = []
                            total = 0
                            for i in range(1, len(keranjang)):
                                jumlah = int(input(f"Masukkan Banyak Barang [{keranjang[i][2]}] (Tersedia {keranjang[i][4]}) ="))
                                if jumlah <= int(keranjang[i][4]):
                                    isi = [f'{keranjang[i][0]}',f'{keranjang[i][2]}',f'Rp.{keranjang[i][3]}',f'{jumlah}',f'Rp.{(int(keranjang[i][3]))*jumlah}']
                                    total += ((int(keranjang[i][3]))*jumlah)
                                    beli.append(isi)
                                else :
                                    print(
                                        "Jumlah Melebihi Stock Yang Tersedia, Apakah Anda Ingin Mengulang?\n"
                                        "[1]. Ya\n"
                                        "[2]. Tidak"
                                    )
                                    ulang = int(input("Masukkan Pilihan Anda :"))
                                    if ulang == 1 :
                                        jumlah()
                                    elif ulang == 2 :
                                        print("Mohon Maaf Atas Ketidaktersediaan Produknya")
                                        input(">>>>>Pencet Enter<<<<<")
                                        homepage_user()
                                    else :
                                        print("ERROR PILIHAN TIDAK DITEMUKAN SILAHKAN ULANGI")
                                        input(">>>>>Pencet Enter<<<<<")
                                        homepage_user()
                            x = pt(["No ID Barang","Nama Produk","Harga Produk","Jumlah Produk","Total"])
                            for i in range(len(beli)): 
                                x.add_row(beli[i])
                            print(x)
                            print(f"Total Transaksi Sebanyak : Rp.{total}")
                            print(
                                "Apakah Sudah Sesuai?\n"
                                "[1]. Ya\n"
                                "[2]. Tidak"
                            )
                            konfirmasi_order = int(input("Masukkan Pilihan Anda :"))
                            if konfirmasi_order == 1 :
                                for i in range (len(beli)):
                                    Id_barang = int(beli[i][0])
                                    berkurang = int(beli[i][3])
                                    waktu = datetime.now()
                                    for x in range(1, len(database_produk)) :
                                        if int(database_produk[x][0]) == Id_barang :
                                            stok = int(database_produk[x][4]) - berkurang
                                            database_produk[x] = [f'{database_produk[x][0]}', f'{database_produk[x][1]}', f'{database_produk[x][2]}', f'{database_produk[x][3]}', f'{stok}', f'{database_produk[x][5]}', f'{database_produk[x][6]}']
                                    pengantaran()
                                    
                                    print(f"Jalur Yang Akan Ditempuh : {rute}")
                                    checkout = [f'{waktu.day}/{waktu.month}/{waktu.year}',f'{waktu.hour}:{waktu.minute}',f'{beli[i][1]}',f'{beli[i][2]}',f'{beli[i][3]}',f'{beli[i][4]}',f'{tujuan[0]}',f'{rute[0]}']
                                    transaksi.append(checkout)
                                with open (f'C:/Code/Algo Pemro 2/Final Project 2/DATA PRODUK.csv', 'w', newline='') as baru :
                                    tulis = csv.writer(baru)
                                    tulis.writerows(database_produk)
                                with open ("C:/Code/Algo Pemro 2/Final Project 2/Riwayat Transaksi.csv", 'w', newline='') as file :
                                    tulis = csv.writer(file)
                                    tulis.writerows(transaksi)                                
                                for i in range(len(transaksi)-1) :
                                    transaksi.pop()
                                for i in range(len(rute)):
                                    rute.pop()
                                for i in range(len(tujuan)):
                                    tujuan.pop()                               
                                for i in range(len(keranjang)-1) :
                                    keranjang.pop()
                                with open (f"C:/Code/Algo Pemro 2/Final Project 2/Database User/{user_login[0]}.csv", 'w', newline='') as file :
                                    tulis = csv.writer(file)
                                    tulis.writerows(keranjang)
                                print("Terimakasih Telah Melakukan Transaksi Di ANTERAE, Barang Anda Akan Segera Kami Kirimkan")
                                print(input(">>>>ENTER<<<<"))
                                homepage_user()                        
                            elif konfirmasi_order == 2 :
                                jumlah()
                            else :
                                print("ERROR PILIHAN TIDAK DITEMUKAN SILAHKAN ULANGI")
                                input(">>>>>Pencet Enter<<<<<")
                                homepage_user()
                        jumlah()
            elif konfirmasi == 5 :
                bersih()
                judul()
                log_out(user_login, keranjang)
                kosong()
                loading()
                print("Terimakasih Telah Menggunakan ANTERAE")
                input(">>>>>>Log Out Berhasil Tekan Enter<<<<<<")
                homepage_pusat() 
            else :
                print("ERROR PILIHAN TIDAK DITEMUKAN SILAHKAN ULANGI")
                input(">>>>>Pencet Enter<<<<<")
                homepage_admin()
        homepage_user()
    elif (login_[0]) == 2 :
        def homepage_admin():
            bersih()
            judul()
            print (f"     Selamat Datang {user_login[0]} di Software Kami!!")
            print ("")
            waktu = datetime.now()
            print (f"{waktu.day}/{waktu.month}/{waktu.year}                                  {waktu.hour}:{waktu.minute}")
            print()
            print(
                "[1]. Lihat Database Produk\n"
                "[2]. Lihat Database Transaksi\n"
                "[3]. Lihat Database User\n"
                "[4]. Logout"
            )
            print()
            konfirmasi = int(input("Masukkan Pilihan Anda :"))
            if konfirmasi == 1 : 
                bersih()
                judul()
                print ("        Daftar Produk Yang Dimiliki")
                x = pt(["No ID Barang","Kategori","Nama Produk","Harga Produk","Stock","Tejual/Bulan","Tanggal Masuk"])
                for i in range(1, len(database_produk)): 
                    x.add_row(database_produk[i])
                print(x)
                print(
                    "[1]. Kembali\n"
                    "[2]. Ubah Harga Produk\n"
                    "[3]. Ubah Stock Produk\n"
                    "[4]. Ubah Kategori Produk\n"
                    "[5]. Ubah Nama Produk\n"
                )
                pilih = int(input("Masukkan Pilihan Anda :"))
                if pilih == 1 :
                    homepage_admin()
                elif pilih == 2 :
                    def ubah_harga () :
                        id_barang = int(input("Masukkan ID Barang Yang Akan Dirubah Harganya :"))
                        harga_baru = int(input("Masukkan Harga Baru (Hanya Angka):"))
                        for i in range(1, len(database_produk)):
                            if (int(database_produk[i][0])) == id_barang :
                                isi = [f'{database_produk[i][0]}',f'{database_produk[i][1]}',f'{database_produk[i][2]}',f'{harga_baru}',f'{database_produk[i][4]}',f'{database_produk[i][5]}',f'{database_produk[i][6]}']
                                database_produk[i] = isi
                        print(
                            "DATA BERHASIL DIRUBAH\n"
                            "Apakah Ingin Merubah Lagi?\n"
                            "[1]. Ya\n"
                            "[2]. Tidak"
                        )
                        pilih_lagi = int(input("Masukkan Pilihan Anda :"))
                        if pilih_lagi == 1 :
                            ubah_harga()
                        elif pilih_lagi == 2 :
                            homepage_admin()
                        else :
                            print(
                                "ERROR!!!!\n"
                                "Harap Pilih Menu Yang Disediakan"
                            )
                            input(">>>>ENTER<<<<")
                            homepage_admin()
                    ubah_harga()    
                elif pilih == 3 :
                    def ubah_stock () :
                        id_barang = int(input("Masukkan ID Barang Yang Akan Dirubah Stocknya :"))
                        stock_baru = int(input("Masukkan Jumlah Saat Ini :"))
                        for i in range(1, len(database_produk)):
                            if (int(database_produk[i][0])) == id_barang :
                                isi = [f'{database_produk[i][0]}',f'{database_produk[i][1]}',f'{database_produk[i][2]}',f'{database_produk[i][3]}',f'{stock_baru}',f'{database_produk[i][5]}',f'{database_produk[i][6]}']
                                database_produk[i] = isi
                        print(
                            "DATA BERHASIL DIRUBAH\n"
                            "Apakah Ingin Merubah Lagi?\n"
                            "[1]. Ya\n"
                            "[2]. Tidak"
                        )
                        pilih_lagi = int(input("Masukkan Pilihan Anda :"))
                        if pilih_lagi == 1 :
                            ubah_stock()
                        elif pilih_lagi == 2 :
                            homepage_admin()
                        else :
                            print(
                                "ERROR!!!!\n"
                                "Harap Pilih Menu Yang Disediakan"
                            )
                            input(">>>>ENTER<<<<")
                            homepage_admin()
                    ubah_stock()
                elif pilih == 4 :
                    def ubah_kategori () :
                        id_barang = int(input("Masukkan ID Barang Yang Akan Dirubah Kategorinya :"))
                        kategori_baru = input("Masukkan Kategori Baru :")
                        for i in range(1, len(database_produk)):
                            if (int(database_produk[i][0])) == id_barang :
                                isi = [f'{database_produk[i][0]}',f'{kategori_baru}',f'{database_produk[i][2]}',f'{database_produk[i][3]}',f'{database_produk[i][4]}',f'{database_produk[i][5]}',f'{database_produk[i][6]}']
                                database_produk[i] = isi
                        print(
                            "DATA BERHASIL DIRUBAH\n"
                            "Apakah Ingin Merubah Lagi?\n"
                            "[1]. Ya\n"
                            "[2]. Tidak"
                        )
                        pilih_lagi = int(input("Masukkan Pilihan Anda :"))
                        if pilih_lagi == 1 :
                            ubah_kategori()
                        elif pilih_lagi == 2 :
                            homepage_admin()
                        else :
                            print(
                                "ERROR!!!!\n"
                                "Harap Pilih Menu Yang Disediakan"
                            )
                            input(">>>>ENTER<<<<")
                            homepage_admin()
                    ubah_kategori()
                elif pilih == 5 :
                    def ubah_nama () :
                        id_barang = int(input("Masukkan ID Barang Yang Akan Dirubah Namanya :"))
                        nama_baru = input("Masukkan Nama Baru :")
                        for i in range(1, len(database_produk)):
                            if (int(database_produk[i][0])) == id_barang :
                                isi = [f'{database_produk[i][0]}',f'{database_produk[i][1]}',f'{nama_baru}',f'{database_produk[i][3]}',f'{database_produk[i][4]}',f'{database_produk[i][5]}',f'{database_produk[i][6]}']
                                database_produk[i] = isi
                        print(
                            "DATA BERHASIL DIRUBAH\n"
                            "Apakah Ingin Merubah Lagi?\n"
                            "[1]. Ya\n"
                            "[2]. Tidak"
                        )
                        pilih_lagi = int(input("Masukkan Pilihan Anda :"))
                        if pilih_lagi == 1 :
                            ubah_nama()
                        elif pilih_lagi == 2 :
                            homepage_admin()
                        else :
                            print(
                                "ERROR!!!!\n"
                                "Harap Pilih Menu Yang Disediakan"
                            )
                            input(">>>>ENTER<<<<")
                            homepage_admin()
                    ubah_nama()   
                else :
                   print(
                        "ERROR!!!!\n"
                        "Harap Pilih Menu Yang Disediakan"
                    )
                   input(">>>>ENTER<<<<")                        
                   homepage_admin()        
            elif konfirmasi == 2 :
                bersih()
                judul()
                print("     Daftar Transaksi Yang Terjadi")
                x = pt(["Tanggal Transaksi","Jam Transaksi","Nama Produk","Harga Produk","Jumlah Terjual","Total Harga","Alamat Tujan","Rute Pengantaran"])
                for i in range(1, len(transaksi)): 
                    x.add_row(transaksi[i])
                print(x)
                input(">>>>TEKAN ENTER UNTUK KEMBALI<<<<")
                homepage_admin()
            elif konfirmasi == 3 :
                bersih()
                judul()
                print("     Daftar Akun Yang Ada Di 'ANTERAE'")
                user_cetak = database_user.copy()
                for i in range(1, len(user_cetak)):
                    user_cetak[i][1] = ('*' * len(user_cetak[i][1]))
                x = pt(["Username","Password"])
                for i in range(1, len(user_cetak)): 
                    x.add_row(user_cetak[i])
                print(x)
                input(">>>>TEKAN ENTER UNTUK KEMBALI<<<<")
                homepage_admin()
            elif konfirmasi == 4 :
                bersih()
                judul()
                log_out(user_login, keranjang)
                kosong()
                loading()
                print("Terimakasih Telah Menggunakan ANTERAE")
                input(">>>>>>Log Out Berhasil Tekan Enter<<<<<<")
                homepage_pusat()
            else :
                print("ERROR PILIHAN TIDAK DITEMUKAN SILAHKAN ULANGI")
                input(">>>>>Pencet Enter<<<<<")
                homepage_admin()
        homepage_admin()
    else :
        def homepage ():
            bersih()
            judul ()
            print ("         Selamat Datang di Software Kami!!")
            print ("")
            waktu = datetime.now()
            print (f"{waktu.day}/{waktu.month}/{waktu.year}                                  {waktu.hour}:{waktu.minute}")
            print()
            print(
                "[1]. Lihat Semua Produk\n"
                "[2]. Cari Produk\n"
                "[3]. Kategori Produk\n"
                "[4]. Login\n"
                "[5]. Register\n"
                "[6]. Keluar"
                )
            print()
            konfirmasi = int(input("Masukkan Pilihan Anda :"))
            if konfirmasi == 1 :
                bersih()
                judul()
                print ("    Daftar Produk Yang Kami Miliki")
                lihat_produk(database_fix)
                print(
                    "[1]. Kembali\n"
                    "[2]. Tambahkan Produk Ke Keranjang\n"
                    "[3]. Urutkan Berdasarkan Abjad\n"
                    "[4]. Urutkan Berdasarkan Termahal\n"
                    "[5]. Urutkan Berdasarkan Termurah\n"
                    "[6]. Urutkan Berdasarkan Terlaris\n"
                    "[7]. Urutkan Berdasarkan Terbaru"
                )
                pilih = int(input("Masukkan Pilihan Anda :"))
                if pilih == 1 :
                    homepage()
                elif pilih == 2 :
                    bersih()
                    judul()
                    print(">>>>>Silahkan Login Terlebih Dahulu<<<<<<")
                    input("Tekan Enter")
                    homepage()
                elif pilih == 3 :
                    bersih()
                    judul()
                    print("         Daftar Produk Berdasarkan Abjad")
                    urut_abjad()
                    print(
                        "[1]. Kembali\n"
                        "[2]. Tambah Produk Ke Keranjang\n"
                    )
                    pilih_3 = int(input("Masukkan Pilihan Anda :"))
                    if pilih_3 == 1 :
                        homepage ()
                    elif pilih_3 == 2 :
                        bersih()
                        judul()
                        print(">>>>>Silahkan Login Terlebih Dahulu<<<<<<")
                        input("Tekan Enter")
                        homepage()
                    else :
                        print("ERROR PILIHAN TIDAK DITEMUKAN SILAHKAN ULANGI")
                        input(">>>>>Pencet Enter<<<<<")
                        homepage()
                elif pilih == 4 :
                    bersih()
                    judul()
                    print("      Daftar Produk Berdasarkan Harga Termahal")
                    mahal()
                    print(
                        "[1]. Kembali\n"
                        "[2]. Tambah Ke Keranjang\n"
                    )
                    pilih4 = int(input("Masukkan Pilihan Anda :"))
                    if pilih4 == 1 :
                        homepage()
                    elif pilih4 == 2 :
                        bersih()
                        judul()
                        print(">>>>>Silahkan Login Terlebih Dahulu<<<<<<")
                        input("Tekan Enter")
                        homepage()
                    else :
                        print("ERROR PILIHAN TIDAK DITEMUKAN SILAHKAN ULANGI")
                        input(">>>>>Pencet Enter<<<<<")
                        homepage()
                elif pilih == 5 :
                    bersih()
                    judul()
                    print("      Daftar Produk Berdasarkan Harga Termurah")
                    murah()
                    print(
                        "[1]. Kembali\n"
                        '[2]. Tambah Ke Keranjang'
                    ) 
                    pilih5 = int(input("Masukkan Pilihan Anda :"))
                    if pilih5 == 1 :
                        homepage()
                    elif pilih5 == 2 :
                        bersih()
                        judul()
                        print(">>>>>Silahkan Login Terlebih Dahulu<<<<<<")
                        input("Tekan Enter")
                        homepage()
                    else :
                        print("ERROR PILIHAN TIDAK DITEMUKAN SILAHKAN ULANGI")
                        input(">>>>>Pencet Enter<<<<<")
                        homepage()
                elif pilih == 6 :
                    bersih()
                    judul()
                    print("      Daftar Produk Berdasarkan Terjual Per Bulan")
                    terjual()
                    print(
                        "[1]. Kembali\n"
                        '[2]. Tambah Ke Keranjang'
                    ) 
                    pilih6 = int(input("Masukkan Pilihan Anda :"))
                    if pilih6 == 1 :
                        homepage()
                    elif pilih6 == 2 :
                        bersih()
                        judul()
                        print(">>>>>Silahkan Login Terlebih Dahulu<<<<<<")
                        input("Tekan Enter")
                        homepage()
                    else :
                        print("ERROR PILIHAN TIDAK DITEMUKAN SILAHKAN ULANGI")
                        input(">>>>>Pencet Enter<<<<<")
                        homepage()
                elif pilih == 7 :
                    bersih()
                    judul()
                    print("      Daftar Produk Berdasarkan Tanggal Masuk Terbaru")
                    terbaru()
                    print(
                        "[1]. Kembali\n"
                        '[2]. Tambah Ke Keranjang'
                    ) 
                    pilih6 = int(input("Masukkan Pilihan Anda :"))
                    if pilih6 == 1 :
                        homepage()
                    elif pilih6 == 2 :
                        bersih()
                        judul()
                        print(">>>>>Silahkan Login Terlebih Dahulu<<<<<<")
                        input("Tekan Enter")
                        homepage()
                    else :
                        print("ERROR PILIHAN TIDAK DITEMUKAN SILAHKAN ULANGI")
                        input(">>>>>Pencet Enter<<<<<")
                        homepage()
                else :
                    bersih()
                    judul()
                    print("ERROR PILIHAN TIDAK DITEMUKAN SILAHKAN ULANGI")
                    input(">>>>>Pencet Enter<<<<<")
                    homepage()
            elif konfirmasi == 2 :
                bersih()
                judul()
                key = input("Masukkan Kata Kunci :")
                search(key)
                if cari[0] == 1 :
                    print (
                        "[1]. Kembali\n"
                        "[2]. Tambah Produk Ke Keranjang"
                    )
                    pilih_cari = int(input("Masukkan Pilihan Anda :"))
                    if pilih_cari == 1 :
                        homepage()
                    elif pilih_cari == 2 :
                        bersih()
                        judul()
                        print(">>>>>Silahkan Login Terlebih Dahulu<<<<<<")
                        input("Tekan Enter")
                        homepage()
                    else :
                        print("ERROR PILIHAN TIDAK DITEMUKAN SILAHKAN ULANGI")
                        input(">>>>>Pencet Enter<<<<<")
                        homepage()
                else :
                    input(">>>>>Pencet Enter<<<<<")
                    homepage()
            elif konfirmasi == 3 :
                def kon_3 ():
                    cetak_kategori()
                    x = int(input("Masukkan Pilihan Anda :"))
                    if x in range(1, len(kategori)) :
                        def x_1 ():
                            cetak_isi_kategori(x)
                            print(
                                "[1]. Tambahkan Produk Ke Keranjang\n"
                                "[2]. Lihat Kategori Lain\n"
                                "[3]. Kembali Ke Halaman Utama"
                            )
                            lanjut = int(input("Masukkan Pilihan Anda :"))
                            if lanjut == 1 :
                                print()
                                bersih()
                                judul()
                                print(">>>>>Silahkan Login Terlebih Dahulu<<<<<<")
                                input("Tekan Enter")
                                homepage()
                            elif lanjut == 2 :
                                kon_3()
                            elif lanjut == 3 :
                                homepage()
                            else :
                                bersih()
                                judul()
                                print("Pilihan Tidak Ditemukan Silahkan Masukkan Pilihan Yang Disediakan!!")
                                input("<<<Tekan Enter>>>")
                                x_1()
                        x_1()
                    elif x == (len(kategori)+1) :
                        homepage()
                    else :
                        bersih()
                        judul()
                        print("Pilihan Tidak Ditemukan Silahkan Masukkan Pilihan Yang Disediakan!!")
                        input("<<<Tekan Enter>>>")
                        kon_3() 
                kon_3()     
            elif konfirmasi == 4 :
                bersih()
                judul()
                login(database_user)  
            elif konfirmasi == 5 :
                bersih()
                judul()
                register(database_user)   
                bersih()
                judul()
                login(database_user)
            elif konfirmasi == 6 : 
                keluar()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
        homepage()

masukkan_barang(database_produk, namaproduk, hargaproduk)
menambahkan_rp(hargaproduk, hargaprodukfix)
menyatukan(namaproduk, hargaprodukfix, databasefix)
tambah_nomor(databasefix, database_fix)
kelompok_kategori()
homepage_pusat()