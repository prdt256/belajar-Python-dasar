# =======================================================
# Latihan: Konversi Satuan Temperatur
# Gabungan Episode 06, 07, dan 08
# =======================================================

print("\nPROGRAM KONVERSI TEMPERATUR\n")

# 1. Ambil input suhu dalam Celcius
# Kita pakai float karena suhu seringkali ada komanya
celcius = float(input('Masukkan suhu dalam celcius : '))
print("Suhu adalah : ", celcius, "Celcius")

# 2. Reamur (Rumus: 4/5 * C)
reamur = (4/5) * celcius
print("Suhu dalam reamur adalah : ", reamur, "Reamur")

# 3. Fahrenheit (Rumus: 9/5 * C + 32)
fahrenheit = ((9/5) * celcius) + 32
print("Suhu dalam fahrenheit adalah : ", fahrenheit, "Fahrenheit")

# 4. Kelvin (Rumus: C + 273)
kelvin = celcius + 273
print("Suhu dalam kelvin adalah : ", kelvin, "Kelvin")