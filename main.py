import csv

# https://www.cpubenchmark.net/

# CPU
# AMD Ryzen 3, 5, 7, 9
ryzen = {"AMD Ryzen 3": 13516, "AMD Ryzen 5": 28856, "AMD Ryzen 7": 36398, "AMD Ryzen 9": 63417}

# Intel Celeron
celeron = {"Intel Celeron": 4541}

# Intel Core i3, i5, i7, i9
core = {"Intel Core i3": 14914, "Intel Core i5": 38391, "Intel Core i7": 46877, "Intel Core i9": 62048}

# https://www.videocardbenchmark.net/gpu_list.php

# GPU
# GTX
# 1050, 1070, 1650, 1660
gtx = {"GTX 1050": 5043, "GTX 1070": 13507, "GTX 1650": 7858, "GTX 1660": 11727}

# RTX
# 2050, 2060, 2070, 2080
rtx2 = {"RTX 2050": 6948, "RTX 2060": 14113, "RTX 2070": 16170, "RTX 2080": 18819}

# 3050, 3060, 3070, 3080
rtx3 = {"RTX 3050": 12975, "RTX 3060": 17158, "RTX 3070": 22488, "RTX 3080": 25376}

# 4050, 4060, 4070, 4080, 4090
rtx4 = {"RTX 4050": 15128, "RTX 4060": 19388, "RTX 4080": 34870, "RTX 4090": 39041}

# A1000, A2000, A3000, A5500
rtxa = {"RTX A1000": 10203, "RTX A2000": 13813, "RTX A3000": 14653, "RTX A5500": 17829}

cpu = {**ryzen, **celeron, **core}
gpu = {**gtx, **rtx2, **rtx3, **rtx4, **rtxa}


file = open('laptops.csv', 'r', encoding="utf_8", errors="", newline="")
data = csv.reader(file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
header = next(data)
print(header)

f = open('laptops_data.csv', 'w', newline='')
wr = csv.writer(f)

wr.writerow(["Status", "CPU", "RAM", "Storage", "Storage type", "GPU", "Screen", "Touch", "Final Price"])

for row in data:
    new_row = []
    print(row[0]) # full name

    # Refurbished / New
    if row[1] == 'New':
        new_row.append(1)
    elif row[1] == 'Refurbished':
        new_row.append(0)
    else:
        continue

    print(row[2]) # brand name
    print(row[3]) # model name

    # CPU
    if row[4] in cpu:
        new_row.append(cpu[row[4]])
    elif row[4] == '':
        new_row.append(0)
    else:
        continue

    # RAM
    new_row.append(row[5])

    # Storage
    if int(row[6]) >= 256:
        new_row.append(row[6])
    else:
        continue

    # Storage Type
    if row[7] == "HDD":
        new_row.append(0)
    elif row[7] == "SSD":
        new_row.append(1)
    else:
        continue

    # GPU
    if row[8] in gpu:
        new_row.append(gpu[row[8]])
    elif row[8] == '':
        new_row.append(0)
    else:
        continue

    # Screen
    new_row.append(row[9])

    # Touch
    if row[10] == "No":
        new_row.append(0)
    if row[10] == "Yes":
        new_row.append(1)

    new_row.append(row[11])

    print(new_row)
    wr.writerow(new_row)

f.close()







