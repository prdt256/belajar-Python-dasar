# =======================================================
# Materi: Episode 08 - Operasi Aritmatika
# Sumber: Kelas Terbuka
# =======================================================

a = 10
b = 3

print("=== 1. OPERASI DASAR ===")
# Penjumlahan (+)
hasil = a + b
print(f"{a} + {b} = {hasil}")

# Pengurangan (-)
hasil = a - b
print(f"{a} - {b} = {hasil}")

# Perkalian (*)
hasil = a * b
print(f"{a} * {b} = {hasil}")

# Pembagian (/) -> Hasil pembagian di Python OTOMATIS jadi Float
hasil = a / b
print(f"{a} / {b} = {hasil}")


print("\n=== 2. OPERATOR KHUSUS (SPESIAL PYTHON) ===")
# Eksponen / Pangkat (**)
hasil = a ** b
print(f"{a} pangkat {b} = {hasil}")

# Modulus / Sisa Hasil Bagi (%)
# 10 dibagi 3 itu dapet 3, sisa 1. Nah, 1 ini hasilnya le!
hasil = a % b
print(f"{a} mod {b} = {hasil}")

# Floor Division / Pembagian Dibulatkan ke Bawah (//)
# 10 / 3 kan 3.333..., kalau pakai // komanya langsung dibuang jadi 3
hasil = a // b
print(f"{a} // {b} = {hasil}")


print("\n=== 3. PRIORITAS OPERASI (KABATAKU) ===")
# Hati-hati urutan pengerjaan le!
# Python akan mengerjakan Perkalian (*) dulu baru Penjumlahan (+)
x = 3
y = 2
z = 4

hasil = x + y * z
print(f"{x} + {y} * {z} = {hasil} (Perkalian duluan)")

# Kalau mau penjumlahan duluan, wajib dikurung ()
hasil = (x + y) * z
print(f"({x} + {y}) * {z} = {hasil} (Kurung duluan)")