# =======================================================
# Materi: Episode 09 - Operasi Komparasi
# Sumber: Kelas Terbuka
# =======================================================

a = 4
b = 2

print("=== 1. OPERATOR STANDAR ===")

# Lebih Besar Dari (>)
hasil = a > 3
print(f"{a} > 3  = {hasil}")

# Lebih Kecil Dari (<)
hasil = a < 3
print(f"{a} < 3  = {hasil}")

# Lebih Besar Sama Dengan (>=)
hasil = a >= 4
print(f"{a} >= 4 = {hasil}")

# Lebih Kecil Sama Dengan (<=)
hasil = b <= 2
print(f"{b} <= 2 = {hasil}")

# Sama Dengan (==) -> Hati-hati, pakai dua tanda sama dengan!
hasil = a == b
print(f"{a} == {b} = {hasil}")

# Tidak Sama Dengan (!=)
hasil = a != b
print(f"{a} != {b} = {hasil}")


print("\n=== 2. OPERATOR KHUSUS (IDENTITY COMPILER) ===")
# 'is' dan 'is not' digunakan untuk membandingkan posisi memori (Object Identity)
x = 5
y = 5
print(f"Nilai x = {x}, id memori = {hex(id(x))}")
print(f"Nilai y = {y}, id memori = {hex(id(y))}")

# x is y (Apakah x adalah y?)
hasil = x is y
print(f"x is y     = {hasil}")

# x is not y (Apakah x bukan y?)
hasil = x is not y
print(f"x is not y = {hasil}")