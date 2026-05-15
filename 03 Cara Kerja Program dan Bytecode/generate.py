with open("raksasa.py", "w") as f:
    for i in range(100000): # 100 ribu baris!
        f.write(f"a{i} = {i}\n")
    f.write("print('File raksasa selesai dieksekusi')\n")