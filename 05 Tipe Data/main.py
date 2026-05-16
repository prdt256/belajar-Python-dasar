#====================================
#Belajar Python Dasar - Episode 5
#====================================

# 1. Integer (Angka bulat tanpa koma)
data_integer = 10
print("data : ", data_integer)
print("- bertipe : ", type(data_integer))

# 2. Float (Angka desimal dengan koma/titik)
data_float = 1.5
print("data : ", data_float)
print("- bertipe : ", type(data_float))

# 3. String (Kumpulan karakter/teks)
data_string = "Ucup"
print("data : ", data_string)
print("- bertipe : ", type(data_string))

# 4. Boolean (Nilai biner / True atau False)
data_bool = True
print("data : ", data_bool)
print("- bertipe : ", type(data_bool))

## TIPE DATA KHUSUS ##

# 5. Complex (Bilangan Kompleks: Real + Imajiner)
data_complex = complex(5, 6)
print("data : ", data_complex)
print("- bertipe : ", type(data_complex))

## TIPE DATA DARI BAHASA C ##
# Karena Python dibuat pakai bahasa C, kita bisa pinjam tipe datanya
from ctypes import c_double, c_char, c_long, c_float

data_c_double = c_double(10.5)
print("data : ", data_c_double)
print("- bertipe : ", type(data_c_double))

nilai_c_long = c_long(1000)
print("data : ", nilai_c_long)
print("- bertipe : ", type(nilai_c_long))

# 1. Kondisi Awal
nilai = "Ikan"
print("Data awal      : ", nilai)
print("- Bertipe      : ", type(nilai))

print("----------------------------") # Pembatas biar rapi

# 2. Kondisi Setelah Diganti (Re-assignment)
nilai = 1
print("Data sekarang  : ", nilai)
print("- Bertipe      : ", type(nilai))

# Cara yang lebih disukai di industri:
nama_hewan = "Ikan"
jumlah_hewan = 1

print(f"{nama_hewan} jumlahnya ada {jumlah_hewan}")