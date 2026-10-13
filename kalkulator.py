
def tambah(a, b):
    return a + b


def kurang(a, b):
    return a - b


def kali(a, b):
    return a * b


def bagi(a, b):
    if b == 0:
        raise ValueError("Tidak bisa membagi dengan nol")
    return a / b


def main():
    print("=== KALKULATOR SEDERHANA ===")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")

    pilihan = input("Pilih operasi (1-4): ")

    if pilihan not in ["1", "2", "3", "4"]:
        print("Pilihan tidak valid")
        return

    try:
        a = float(input("Masukkan angka pertama: "))
        b = float(input("Masukkan angka kedua: "))

        if pilihan == "1":
            hasil = tambah(a, b)
        elif pilihan == "2":
            hasil = kurang(a, b)
        elif pilihan == "3":
            hasil = kali(a, b)
        else:
            hasil = bagi(a, b)

        print("Hasil:", hasil)

    except ValueError as error:
        print("Error:", error)


if __name__ == "__main__":
    main()
