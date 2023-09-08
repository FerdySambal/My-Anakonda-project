import tkinter as tk


def hitung_biaya():
    waktu_masuk = entry_masuk.get()
    waktu_keluar = entry_keluar.get()

    # Hitung biaya parkir (di sini kita asumsikan biaya per jam)
    biaya_per_jam = 2000  # Ganti dengan biaya per jam yang sesuai
    try:
        waktu_masuk = float(waktu_masuk)
        waktu_keluar = float(waktu_keluar)
        waktu_parkir = waktu_keluar - waktu_masuk
        biaya = waktu_parkir * biaya_per_jam
        result_label.config(text=f"Biaya Parkir: Rp.{biaya:.2f}")
    except ValueError:
        result_label.config(text="Waktu masuk dan keluar harus berupa angka")


root = tk.Tk()
root.title("Program Parkir")

label_nopol = tk.Label(root, text="NoPol (Nomor Polisi): ")
label_nopol.grid(row=0, column=0)

entry_nopol = tk.Entry(root)
entry_nopol.grid(row=0, column=1)

label_plat = tk.Label(root, text="No Plat Polisi: ")
label_plat.grid(row=1, column=0)

entry_plat = tk.Entry(root)
entry_plat.grid(row=1, column=1)

label_masuk = tk.Label(root, text="Waktu Masuk (jam): ")
label_masuk.grid(row=2, column=0)

entry_masuk = tk.Entry(root)
entry_masuk.grid(row=2, column=1)

label_keluar = tk.Label(root, text="Waktu Keluar (jam): ")
label_keluar.grid(row=3, column=0)

entry_keluar = tk.Entry(root)
entry_keluar.grid(row=3, column=1)

biaya_label = tk.Label(root, text="Biaya Per Jam: Rp. 2.000", font=("Arial", 12), fg="red")
biaya_label.grid(row=0, column=2, rowspan=2)  # Menambahkan label biaya per jam

button_hitung = tk.Button(root, text="Hitung Biaya Parkir", command=hitung_biaya)
button_hitung.grid(row=4, columnspan=2)

result_label = tk.Label(root, text="")
result_label.grid(row=5, columnspan=2)

root.mainloop()