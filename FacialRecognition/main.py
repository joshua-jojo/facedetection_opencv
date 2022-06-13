import os
from time import sleep
import FaceDataset
import FaceTraining
import FaceRecognition

bintang = 50
def clear():
    os.system("cls")

def judul(data):
    print("|"+("*")*bintang+"|")
    print("|"+data.center(bintang," ")+"|")
    print("|"+("*")*bintang+"|")

def submenu(menu):
    print("|"+(menu.center(bintang," "))+"|")

def penutup():
    print("|"+("*")*bintang+"|")

def perintah(data):
    value =  int(input(data))
    return value
    
def cek_siswa():
    path = "dataset"
    if os.path.isdir("dataset"):   
        ids = set()
        imagePaths = [os.path.join(path,f) for f in os.listdir(path)]
        for imagePath in imagePaths:
            id = int(os.path.split(imagePath)[-1].split(".")[1])
            ids.add(id)
        return ids
    else :
        return 0

def cek_data_siswa():
    clear()
    judul("Cek Data Siswa")
    submenu("0. Back")
    penutup()    
    if cek_siswa() == 0 :
        input("Data siswa masih kosong...")
        menu_siswa()
    else :
        nim = perintah("Masukan NIS : ")
        if nim == 0 :
            menu_siswa()
        if nim in cek_siswa() :
            print("Siswa Telah Terdaftar...\n")
            input("Press Any Key To Continue...")
        else :
            print("Siswa Belum Terdaftar...\n")
            input("Press Any Key To Continue...")

    cek_data_siswa()

def tampilkan_data_siswa(data):
    clear()
    judul("NIS YANG TELAH TERDAFTAR")
    if data :
        for x in data :
            submenu(str(x))
    else :
        submenu("Data Kosong")
    penutup()
    input("Press Any Key To Continue...")
    menu_siswa()

def tambah_data_siswa():
    FaceDataset.main()
    FaceTraining.main()
    print("Data Telah Siap...")
    sleep(1)
    menu_siswa()

def menu_siswa():
    clear()
    judul("MENU SISWA")
    submenu("1. Cek Data Siswa")
    submenu("2. Tambah Data Siswa")
    submenu("3. Tampilkan Data Siswa")
    submenu("0. Back")
    penutup()

    value = perintah("Masukkan Input : ")
    if value == 0 :
        main()
    elif value == 1 :
        cek_data_siswa()
    elif value == 2 :
        tambah_data_siswa()
    elif value == 3:
        tampilkan_data_siswa(cek_siswa())
    else :
        menu_siswa()

def daftar_absen():
    clear()
    judul("DAFTAR NIS ABSENSI") 
    absen = open("absen.txt","r")
    absen = list(absen.read())
    test = set()
    for x in absen :
        test.add(x)
    absen = list(test)
    absen.remove("{")
    absen.remove("}")
    absen.remove(",")
    absen.remove(" ")
    for x in absen :
        submenu(x)
    penutup()
    input("Press Any Key To Continue...")
    main()



def main():
    clear()
    judul("SISTEM ABSENSI")
    submenu("1. Menu Siswa")
    submenu("2. Deteksi Wajah")
    submenu("3. Daftar Absen")
    penutup()


    value = perintah("Masukkan Perintah : ")

    if value == 1 :
        menu_siswa()
    elif value == 2:
        FaceRecognition.main()
        main()
    elif value == 3:
        daftar_absen()

if __name__ == "__main__" :
    main()