import os

def clear():
    os.system('cls')

def garis():
    print('-'*45)

def EP():
    clear()
    garis()
    print('''
    MENCARI ENERGI KINETIK SUATU BENDA
    ''')
    garis()
    print('')
    print('EK = 1/2.m.v2')
    print('')
    m = int(input('Masukkan Massa Suatu Benda : '))
    v = int(input('Masukkan Nilai Kecepatan Suatu Benda : '))
    ek = 1/2*m*v**2
    print('')
    print(f'Nilai Energi Kinetik Benda Tersebut {ek}Joule dengan Massa {m}kg dan Kecepatan {v}m/s')
    print('')
    input('Tekan [Enter] Untuk Kembali Ke Menu ')
    menu()

def login():
    clear()
    garis()
    print('''
                SELAMAT DATANG 
          DI OPERASI FISIKA SEDERHANA
                ENERGI KINETIK
    ''')
    garis()
    while True:
        user = 'admin'
        pas = 'admin'
        
        username = input('Masukkan Username : ')
        password = input('Masukkan Password : ')
        
        if username == user :
            if password == pas :
                garis()
                input('Selamat Anda Telah Berhasil Login, Tekan [Enter] Untuk Melanjutkan ')
                menu()
            else : 
                print('')
                print('Password Yang Anda Masukkan Salah, Silahkan Login Kembali')
                print('')
                input('Tekan [Enter] Untuk Login Kembali')
                clear()
                login()
        else :
            print('')
            print('Username Yang Anda Masukkan Salah, Silahkan Login Kembali')
            print('')
            input('Tekan [Enter] Untuk Login Kembali')
            clear()
            login()

def menu():
    clear()
    garis()
    print('''
        MENU OPERASI FISIKA
          ENERGI KINETIK
    ''')
    garis()
    print('''       
1. Mencari Energi Kinetik
2. Exit
    ''')
    pilih = int(input('Silahkan Pilih Salah Satu Menu Di Atas : '))
    if pilih == 1 :
        EP()
    elif pilih == 2 :
        exit()
    else :
        print('')
        input('Pilihan Menu Tidak Ada, Tekan [Enter] Untuk Memilih Kembali ')
        menu()

def exit():
    clear()
    garis()
    print('                TERIMA KASIH')
    garis()
    input()

login()

