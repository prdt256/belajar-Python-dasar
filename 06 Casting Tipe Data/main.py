#====================================
#Belajar Python Dasar - Episode 6
#====================================

print("=== DATA AWAL (INTEGER) ===")
data_int = 9
print("data : ", data_int, ", tipe : ", type(data_int))

# Casting dari Integer
data_float = float(data_int)
data_str   = str(data_int)
data_bool  = bool(data_int) # Akan False jika int = 0, selain itu True
print("ke float : ", data_float, ", tipe : ", type(data_float))
print("ke str   : ", data_str, ", tipe : ", type(data_str))
print("ke bool  : ", data_bool, ", tipe : ", type(data_bool))

print("\n=== DATA AWAL (FLOAT) ===")
data_float = 9.9
print("data : ", data_float, ", tipe : ", type(data_float))

# Casting dari Float (Nilai akan dibulatkan ke bawah / dibuang komanya)
data_int = int(data_float)
print("ke int   : ", data_int, ", tipe : ", type(data_int))

print("\n=== DATA AWAL (BOOLEAN) ===")
data_bool = False
print("data : ", data_bool, ", tipe : ", type(data_bool))

# Casting dari Boolean
data_int   = int(data_bool)   # True -> 1, False -> 0
data_float = float(data_bool) # True -> 1.0, False -> 0.0
data_str   = str(data_bool)   # Menjadi teks "True" atau "False"
print("ke int   : ", data_int, ", tipe : ", type(data_int))
print("ke float : ", data_float, ", tipe : ", type(data_float))
print("ke str   : ", data_str, ", tipe : ", type(data_str))

print("\n=== DATA AWAL (STRING) ===")
data_str = "10" # String harus berupa angka bulat jika ingin ke int
print("data : ", data_str, ", tipe : ", type(data_str))

data_int   = int(data_str)
data_float = float(data_str)
print("ke int   : ", data_int, ", tipe : ", type(data_int))
print("ke float : ", data_float, ", tipe : ", type(data_float))

# Catatan penting untuk Boolean dari String:
# bool() hanya akan False jika String-nya kosong ""
data_kosong = ""
print("String kosong ke bool : ", bool(data_kosong))
print("String isi ke bool    : ", bool("Ucup"))

data_str = "10.5"
print ("Data : ", data_str)

# Cara 1: Langsung ke int (ERROR)
# data_int = int(data_str) 

# Cara 2: Lewat jembatan float (SUKSES)
data_float = float(data_str) # Ubah teks jadi angka desimal dulu (10.5)
data_int   = int(data_float) # Ubah angka desimal jadi angka bulat (10)

print(f"Hasil akhir: {data_int}")