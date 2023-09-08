import tkinter as tk
from tkinter import ttk

class KasirApp:
    def _init_(self, root):
        self.root = root
        self.root.title("Program Kasir")

        # Label dan input teks untuk harga
        self.label_harga = ttk.Label(root, text="Harga:")
        self.label_harga.grid(row=0, column=0)
        self.entry_harga = ttk.Entry(root)
        self.entry_harga.grid(row=0, column=1)

        # Label dan input teks untuk kuantitas
        self.label_kuantitas = ttk.Label(root, text="Kuantitas:")
        self.label_kuantitas.grid(row=1, column=0)
        self.entry_kuantitas = ttk.Entry(root)
        self.entry_kuantitas.grid(row=1, column=1)

        # Tombol "Hitung" untuk menghitung total harga
        self.button_hitung = ttk.Button(root, text="Hitung", command=self.hitung_total)
        self.button_hitung.grid(row=2, column=0, columnspan=2)

        # Label untuk menampilkan total harga
        self.label_total = ttk.Label(root, text="Total Harga: Rp 0")
        self.label_total.grid(row=3, column=0, columnspan=2)

    def hitung_total(self):
        try:
            harga = float(self.entry_harga.get())
            kuantitas = int(self.entry_kuantitas.get())
            total_harga = harga * kuantitas
            self.label_total.config(text=f"Total Harga: Rp {total_harga}")
        except ValueError:
            self.label_total.config(text="Masukkan harga dan kuantitas yang valid.")

if _name_ == "_main_":
    root = tk.Tk()
    app = KasirApp(root)
    root.mainloop()