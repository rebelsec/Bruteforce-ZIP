import zipfile

# Tipe tipe karakter
lowercase = 'abcdefghijklmnopqrstuvwxyz'
uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
number = '1234567890'
complete = []

print("""

Crack Zip :
 ____      _          _
|  _ \ ___| |__   ___| |___  ___  ___
| |_) / _ \ '_ \ / _ \ / __|/ _ \/ __|
|  _ <  __/ |_) |  __/ \__ \  __/ (__
|_| \_\___|_.__/ \___|_|___/\___|\___|

Karakter List :
1. Lowercase
2. Uppercase
3. Number
4. Lowercase + Uppercase 
5. Uppercase + Number
6. Lowercase + Number
""")

# pemilihan karakter
pilih_karakter = 0
while pilih_karakter < 1:
    inputan = input("Pilih Nomor Tipe Karakter :")
    if inputan == '1':
        charlist = lowercase
        pilih_karakter += 1
    elif inputan == '2':
        charlist = uppercase
        pilih_karakter += 1
    elif inputan == '3':
        charlist = number
        pilih_karakter += 1
    elif inputan == '4':
        charlist = lowercase + uppercase
        pilih_karakter += 1
    elif inputan == '5':
        charlist = uppercase + number
        pilih_karakter += 1
    elif inputan == '6':
        charlist = lowercase + number
        pilih_karakter += 1
    else:
        print("silahkan masukkan inputan yang benar")

# masukkan kombinasi karakter
kombinasi = input("Banyaknya kombinasi karakter ? :")
print('Please Wait  ...')

# penggabungan karakter
for current in range(int(kombinasi)):
    a = [i for i in charlist]
    for x in range(current):
        a = [y + i for i in charlist for y in a]
    complete = complete+a

# Proses Crack zip
file = input("File Zip ? :")
z = zipfile.ZipFile(file)
percobaan = 0
nama_file_sekarang = input(
    "Isi file yang ada di dalam zip ? : ")
for password in complete:
    try:
        percobaan += 1
        z.setpassword(password.encode('ascii'))
        z.extract(nama_file_sekarang)

        # Jika Sudah berhasil
        print(f"Percobaan sebanyak ", percobaan, "password adalah ", password)
        break
    # Jika ada yang salah
    except Exception as err:
        print(err)
        pass
