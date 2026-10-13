
import tkinter as tk
from tkinter import messagebox
from kalkulator import tambah, kurang, kali, bagi


# Warna tampilan
BG = "#F3F6FC"
PUTIH = "#FFFFFF"
BIRU = "#2563EB"
TEKS = "#1F2937"
ABU = "#E8EEF8"


class Kalkulator:
    def __init__(self, root):
        self.root = root
        self.root.title("Kalkulator Modern")
        self.root.geometry("350x480")
        self.root.resizable(False, False)
        self.root.configure(bg=BG)

        self.ekspresi = ""

        # Judul aplikasi
        tk.Label(
            root,
            text="KALKULATOR MODERN",
            font=("Segoe UI", 16, "bold"),
            bg=BG,
            fg=BIRU
        ).pack(pady=(18, 4))

        tk.Label(
            root,
            text="Hitung dengan mudah",
            font=("Segoe UI", 10),
            bg=BG,
            fg=TEKS
        ).pack()

        # Layar kalkulator
        layar = tk.Frame(root, bg=PUTIH)
        layar.pack(fill="x", padx=18, pady=18)

        self.layar = tk.Label(
            layar,
            text="0",
            font=("Segoe UI", 28, "bold"),
            bg=PUTIH,
            fg=TEKS,
            anchor="e",
            padx=12,
            pady=22
        )
        self.layar.pack(fill="x")

        # Tombol kalkulator
        area_tombol = tk.Frame(root, bg=BG)
        area_tombol.pack(fill="both", expand=True, padx=14, pady=(0, 14))

        tombol = [
            ["C", "⌫", "%", "÷"],
            ["7", "8", "9", "×"],
            ["4", "5", "6", "−"],
            ["1", "2", "3", "+"],
            ["±", "0", ".", "="]
        ]

        for baris, isi_baris in enumerate(tombol):
            area_tombol.grid_rowconfigure(baris, weight=1)

            for kolom, teks_tombol in enumerate(isi_baris):
                area_tombol.grid_columnconfigure(kolom, weight=1)

                warna = ABU
                warna_teks = TEKS

                if teks_tombol == "=":
                    warna = BIRU
                    warna_teks = PUTIH

                tombol_buat = tk.Button(
                    area_tombol,
                    text=teks_tombol,
                    font=("Segoe UI", 14, "bold"),
                    bg=warna,
                    fg=warna_teks,
                    activebackground="#D4DFF2",
                    relief="flat",
                    cursor="hand2",
                    command=lambda nilai=teks_tombol: self.klik(nilai)
                )

                tombol_buat.grid(
                    row=baris,
                    column=kolom,
                    sticky="nsew",
                    padx=4,
                    pady=4,
                    ipady=7
                )

    def klik(self, nilai):
        if nilai == "C":
            self.ekspresi = ""
            self.layar.config(text="0")

        elif nilai == "⌫":
            self.ekspresi = self.ekspresi[:-1]
            self.layar.config(text=self.ekspresi or "0")

        elif nilai == "=":
            self.hitung()

        elif nilai == "%":
            try:
                hasil = float(self.ekspresi) / 100
                self.ekspresi = str(hasil)
                self.layar.config(text=self.rapikan(hasil))
            except ValueError:
                messagebox.showerror(
                    "Input tidak valid",
                    "Masukkan angka terlebih dahulu."
                )

        elif nilai == "±":
            if self.ekspresi:
                if self.ekspresi.startswith("-"):
                    self.ekspresi = self.ekspresi[1:]
                else:
                    self.ekspresi = "-" + self.ekspresi
                self.layar.config(text=self.ekspresi)

        else:
            simbol = {
                "÷": "/",
                "×": "*",
                "−": "-"
            }.get(nilai, nilai)

            self.ekspresi += simbol
            self.layar.config(text=self.ekspresi)

    def hitung(self):
        try:
            teks = self.ekspresi

            # Proses operasi dasar tanpa menggunakan eval()
            for operator in ["+", "-", "*", "/"]:
                if operator in teks[1:]:
                    posisi = teks.rfind(operator)
                    angka1 = float(teks[:posisi])
                    angka2 = float(teks[posisi + 1:])

                    if operator == "+":
                        hasil = tambah(angka1, angka2)
                    elif operator == "-":
                        hasil = kurang(angka1, angka2)
                    elif operator == "*":
                        hasil = kali(angka1, angka2)
                    else:
                        hasil = bagi(angka1, angka2)

                    self.ekspresi = self.rapikan(hasil)
                    self.layar.config(text=self.ekspresi)
                    return

            self.layar.config(text=self.rapikan(float(teks)))
            self.ekspresi = self.rapikan(float(teks))

        except (ValueError, ZeroDivisionError):
            messagebox.showerror(
                "Tidak dapat menghitung",
                "Periksa angka dan operasi yang kamu masukkan."
            )

    @staticmethod
    def rapikan(angka):
        if angka == int(angka):
            return str(int(angka))
        return str(round(angka, 8))


if __name__ == "__main__":
    jendela = tk.Tk()
    aplikasi = Kalkulator(jendela)
    jendela.mainloop()
