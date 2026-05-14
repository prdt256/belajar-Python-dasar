#====================================
#Belajar Python Dasar - Episode 3
#====================================

import time
start_time = time.time()

angka = 0
print("Halo, saya sedang belajar cara kerja Python!")
for i in range(100):
    for j in range(100):
        angka += j

while angka < 100:
    angka += 1

# Script ini buat bikin file python yang isinya 50.000 baris kode sampah
with open("raksasa.py", "w") as f:
    for i in range(50000):
        f.write(f"var_{i} = {i}\n")
    f.write("print('File raksasa siap!')")

# Python bekerja dengan cara:
# 1. Source Code (.py) -> 2. Bytecode (.pyc) -> 3. PVM (Python Virtual Machine)

print(time.time() - start_time, "detik")

# Catatan: 
# Untuk meng-compile manual ke bytecode, ketik di terminal:
# python -m py_compile main.py