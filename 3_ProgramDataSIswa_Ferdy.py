import tkinter as tk
from tkinter import messagebox

def simpan_data():
    nama_lengkap = entry_nama_lengkap.get()
    tanggal_lahir = entry_tanggal_lahir.get()
    asal_sekolah = entry_asal_sekolah.get()
    nisn = entry_nisn.get()
    nama_ayah = entry_nama_ayah.get()
    nama_ibu = entry_nama_ibu.get()
    nomor_telepon = entry_nomor_telepon.get()
    alamat = entry_alamat.get("1.0", tk.END)

    if not nama_lengkap or not tanggal_lahir or not asal_sekolah or not nisn or not nama_ayah or not nama_ibu or not nomor_telepon or not alamat:
        messagebox.showerror("Error", "Harap isi semua field.")
        return

    data_siswa.insert(tk.END, f"Nama: {nama_lengkap}\nTanggal Lahir: {tanggal_lahir}\nAsal Sekolah: {asal_sekolah}\nNISN: {nisn}\nNama Ayah: {nama_ayah}\nNama Ibu: {nama_ibu}\nNomor Telepon: {nomor_telepon}\nAlamat: {alamat}\n")
    messagebox.showinfo("Info", "Data siswa berhasil disimpan.")

def hapus_data():
    data_siswa.delete(1.0, tk.END)
    entry_nama_lengkap.delete(0, tk.END)
    entry_tanggal_lahir.delete(0, tk.END)
    entry_asal_sekolah.delete(0, tk.END)
    entry_nisn.delete(0, tk.END)
    entry_nama_ayah.delete(0, tk.END)
    entry_nama_ibu.delete(0, tk.END)
    entry_nomor_telepon.delete(0, tk.END)
    entry_alamat.delete("1.0", tk.END)

root = tk.Tk()
root.title("Data Siswa")

frame_input = tk.Frame(root)
frame_input.pack()

label_nama_lengkap = tk.Label(frame_input, text="Nama Lengkap:")
label_nama_lengkap.grid(row=0, column=0)
entry_nama_lengkap = tk.Entry(frame_input)
entry_nama_lengkap.grid(row=0, column=1)

label_tanggal_lahir = tk.Label(frame_input, text="Tanggal Lahir:")
label_tanggal_lahir.grid(row=1, column=0)
entry_tanggal_lahir = tk.Entry(frame_input)
entry_tanggal_lahir.grid(row=1, column=1)

label_asal_sekolah = tk.Label(frame_input, text="Asal Sekolah:")
label_asal_sekolah.grid(row=2, column=0)
entry_asal_sekolah = tk.Entry(frame_input)
entry_asal_sekolah.grid(row=2, column=1)

label_nisn = tk.Label(frame_input, text="NISN:")
label_nisn.grid(row=3, column=0)
entry_nisn = tk.Entry(frame_input)
entry_nisn.grid(row=3, column=1)

label_nama_ayah = tk.Label(frame_input, text="Nama Ayah:")
label_nama_ayah.grid(row=4, column=0)
entry_nama_ayah = tk.Entry(frame_input)
entry_nama_ayah.grid(row=4, column=1)

label_nama_ibu = tk.Label(frame_input, text="Nama Ibu:")
label_nama_ibu.grid(row=5, column=0)
entry_nama_ibu = tk.Entry(frame_input)
entry_nama_ibu.grid(row=5, column=1)

label_nomor_telepon = tk.Label(frame_input, text="Nomor Telepon:")
label_nomor_telepon.grid(row=6, column=0)
entry_nomor_telepon = tk.Entry(frame_input)
entry_nomor_telepon.grid(row=6, column=1)

label_alamat = tk.Label(frame_input, text="Alamat:")
label_alamat.grid(row=7, column=0)
entry_alamat = tk.Text(frame_input, height=4, width=30)
entry_alamat.grid(row=7, column=1)

simpan_button = tk.Button(frame_input, text="Simpan", command=simpan_data)
simpan_button.grid(row=8, column=0, columnspan=2)

frame_data_siswa = tk.Frame(root)
frame_data_siswa.pack()

label_data_siswa = tk.Label(frame_data_siswa, text="Data Siswa:")
label_data_siswa.pack()

data_siswa = tk.Text(frame_data_siswa, height=10, width=50)
data_siswa.pack()

hapus_button = tk.Button(root, text="Hapus Data", command=hapus_data)
hapus_button.pack()

root.mainloop()