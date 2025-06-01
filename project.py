import tkinter as tk
from tkinter import ttk

class KonverterApp:
    def __init__(self, master):
        self.master = master
        master.title("Konversi Panjang & Berat")
        master.geometry("360x500")

        self.panjang_list = ["mm", "cm", "dm", "m", "dam", "hm", "km"]
        self.berat_list = ["mg", "cg", "dg", "g", "dag", "hg", "kg"]

        self.judul = tk.Label(master, text="Konversi Panjang / Berat", font=("Arial", 16, "bold"))
        self.judul.pack(pady=15)

        self.frame = tk.Frame(master)
        self.frame.pack(pady=10)

        self.buat_form()
        self.update_satuan()

    def buat_form(self):
        tk.Label(self.frame, text="Jenis Konversi:").grid(row=0, column=0, sticky="w", pady=5)
        self.jenis_var = tk.StringVar(value="Panjang")
        self.jenis_dropdown = ttk.Combobox(self.frame, textvariable=self.jenis_var, values=["Panjang", "Berat"], state="readonly")
        self.jenis_dropdown.grid(row=0, column=1)
        self.jenis_dropdown.bind("<<ComboboxSelected>>", lambda e: self.update_satuan())

        tk.Label(self.frame, text="Masukkan Angka:").grid(row=1, column=0, sticky="w", pady=5)
        self.entry_input = tk.Entry(self.frame)
        self.entry_input.grid(row=1, column=1)

        tk.Label(self.frame, text="Satuan Asal:").grid(row=2, column=0, sticky="w", pady=5)
        self.satuan_asal_var = tk.StringVar()
        self.satuan_asal_dropdown = ttk.Combobox(self.frame, textvariable=self.satuan_asal_var, state="readonly")
        self.satuan_asal_dropdown.grid(row=2, column=1)

        tk.Label(self.frame, text="Satuan Tujuan:").grid(row=3, column=0, sticky="w", pady=5)
        self.satuan_tujuan_var = tk.StringVar()
        self.satuan_tujuan_dropdown = ttk.Combobox(self.frame, textvariable=self.satuan_tujuan_var, state="readonly")
        self.satuan_tujuan_dropdown.grid(row=3, column=1)

        self.label_hasil = tk.Label(self.master, text="Hasil Konversi:", font=("Arial", 12))
        self.label_hasil.pack(pady=(20, 5))
        self.hasil_text = tk.Label(self.master, text="", font=("Arial", 12))
        self.hasil_text.pack()

        self.btn_konversi = tk.Button(self.master, text="Konversi", command=self.konversi)
        self.btn_konversi.pack(pady=10)

    def update_satuan(self):
        jenis = self.jenis_var.get()
        if jenis == "Panjang":
            satuan_list = self.panjang_list
            self.satuan_asal_var.set("m")
            self.satuan_tujuan_var.set("cm")
        else:
            satuan_list = self.berat_list
            self.satuan_asal_var.set("g")
            self.satuan_tujuan_var.set("mg")

        self.satuan_asal_dropdown['values'] = satuan_list
        self.satuan_tujuan_dropdown['values'] = satuan_list

    def konversi(self):
        try:
            angka = float(self.entry_input.get())
            jenis = self.jenis_var.get()
            asal = self.satuan_asal_var.get()
            tujuan = self.satuan_tujuan_var.get()

            if jenis == "Panjang":
                satuan_list = self.panjang_list
            else:
                satuan_list = self.berat_list

            index_asal = satuan_list.index(asal)
            index_tujuan = satuan_list.index(tujuan)

            pangkat = index_asal - index_tujuan
            hasil = angka * (10 ** pangkat)

            self.hasil_text.config(text=f"{angka:.4f} {asal} = {hasil:.4f} {tujuan}")
        except:
            self.hasil_text.config(text="Masukkan angka dan satuan yang valid!")

if __name__ == "__main__":
    root = tk.Tk()
    app = KonverterApp(root)
    root.mainloop()
