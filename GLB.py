import os

def clearData():
    os.system('cls')

def garis():
    print('='*29)

def cover():
    clearData()
    garis()
    print('''
      SELAMAT DATANG Di   
     OPERASI PERHITUNGAN  
    GERAK LURUS BERATURAN 
    ''')
    garis()
    input("Tekan [Enter] Untuk Melanjutkan")
    loginData()

def loginData():
    clearData()
    username = input('Masukkan Username : ')
    password = input('Masukkan Password : ')
    if username == "admin" :
        if password == "admin" :
            garis()
            print('Selamat Anda Telah Berhasil Login')
            input('Tekan [Enter] Untuk Masuk ke Menu')
            menuData()
        else:
            input('Username atau Password Salah, Silahkan login Kembali')
            loginData()
    else:
        input('Username atau Password Salah Silahkan Login Kembali')
        loginData()
     
def menuData():
    print('''
    MENU OPERASI PERHITUNGAN
    GERAK LURUS BERATURAN
    1. Menghitungan Kecepatan Suatu Benda
    2. Menghitung Jarak Suatu Benda
    3. Menghitung Waktu
    ''')
    inputan = int(input('Pilih Menu : '))
    if inputan == 1 :
        kecepatanBenda()
    elif inputan == 2 :
        jarakBenda()        
    elif inputan== 3 :
        waktuBenda()
    else :
        input("Operasi Tidak Ada, Silahkan Pilih Menu yang Sesuai")
        menuData()

def kecepatanBenda():
    print('[Menu Mencari Kecepatan Benda]')
    s = int(input('Masukkan Jarak (m) : '))
    t = int(input('Masukkan Selang Waktu (s) : '))
    v = s/t
    print(f'Kecepatan Benda Tersebut adalah {v} m/s dengan jarak {s} meter dan selang waktu {t} sekon')

def jarakBenda():
    print('[Menu Mencari Jarak Suatu Benda]')
    v = int(input('Masukkan Kecepatan Suatu Benda (m/s) : '))
    t = int(input('Masukkan Selang Waktu (s) : '))
    s = v*t
    print(f'Jarak yang ditempuh benda tersebut {s} meter dengan kecepatan {v} m/s dan selang waktu {t} sekon ')

def waktuBenda():
    print('[Menu Mencari Selang Waktu]')
    s = int(input('Masukkan Jarak (m) : '))
    v = int(input('Masukkan Kecepatan Suatu Benda (m/s) : '))
    t = s/v
    print(f'Waktu yang ditempuh benda tersebut bergerak selama {t} sekon dengan kecepatan {v} m/s dan jarak {s} meter')

cover()