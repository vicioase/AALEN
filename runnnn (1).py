import tkinter as tk
from tkinter import ttk
import xlrd
from Plat import Ngecheck

Font_judul = ("Times New Roman", 48)
Font_text = ("Times New Roman", 12)

class tkinterApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side= "top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (Home, Nomor1, Nomor2, Nomor3, Nomor4, Nomor5, Nomor6, Nomor7) :
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row = 0, column = 0, sticky = "nsew")
            frame.configure(background="black")

        self.show_frame(Home)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class Home(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text="Kelompok AALEN", font=Font_judul, foreground="white", background="black")
        label.grid(row=0, column=0, padx=10, pady=10)

        anggota = ttk.Label(self, text="""1. Purinda Karolin\t\t\t(L200220203)
2. Pramudya Amara Setyaningtyas\t(L200220207)
3. Abila Prastika Navilata\t\t(L200220251)
4. Hilda Nasywa Nurhaliza\t\t(L200220225)
5. Aminah Esti Utami\t\t(L200220226)
6. Fatimah Azzahro\t\t\t(L200220228)
7. Vici Oase\t\t\t(L200220271)""",
                            font=Font_judul, foreground='white', background='black')
        anggota.grid(row=1, column=0, padx=10, pady=10)

        button1 = tk.Button(self, text="Next", command= lambda : controller.show_frame(Nomor1), background='black', foreground='white')
        button1.grid(row=3, column=0, padx=10, pady=10)

class Nomor1(tk.Frame):
    def __init__(self, parent, controlling):
        tk.Frame.__init__(self, parent)

        self.a = xlrd.open_workbook(filename='Kendaraan dan plat.xlsx')
        self.b = self.a.sheet_by_index(0)

        JenisKendaraan = []
        for i in range(1, self.b.nrows):
            JenisKendaraan.append(self.b.cell_value(i, 1))
        kategori = []
        for i in range(1, self.b.nrows):
            kategori.append(self.b.cell_value(i, 2))
        plat = []
        for i in range(1, self.b.nrows):
            plat.append(self.b.cell_value(i, 3))

        checking = Ngecheck(f"{plat[0]}")
        hasil = checking.check()

        Judul = ttk.Label(self, text="Data nomor 1", background='black', foreground='white', font=Font_judul)
        Judul.grid(row=0, column=0, pady=10, padx=10)

        teks = ttk.Label(self, text=f"""Kendaraan berjenis {JenisKendaraan[0]}
Kendaraan berkategori {kategori[0]}
Dan memiliki plat nomor {plat[0]}
{hasil}""", background='black', foreground='white', font=Font_judul)
        teks.grid(row=1, column=0, padx=10, pady=10)

        button1 = tk.Button(self, text="Prev", background='black', foreground='white', command=lambda : controlling.show_frame(Home))
        button1.grid(row=2, column=0, pady=10, padx=10)

        button2 = tk.Button(self, text="Next", background='black', foreground='white', command=lambda : controlling.show_frame(Nomor2))
        button2.grid(row=2, column=1, padx=10, pady=10)

class Nomor2(tk.Frame):
    def __init__(self, parent, controlling):
        tk.Frame.__init__(self, parent)

        self.a = xlrd.open_workbook(filename='Kendaraan dan plat.xlsx')
        self.b = self.a.sheet_by_index(0)

        JenisKendaraan = []
        for i in range(1, self.b.nrows):
            JenisKendaraan.append(self.b.cell_value(i, 1))
        kategori = []
        for i in range(1, self.b.nrows):
            kategori.append(self.b.cell_value(i, 2))
        plat = []
        for i in range(1, self.b.nrows):
            plat.append(self.b.cell_value(i, 3))

        checking = Ngecheck(f"{plat[1]}")
        hasil = checking.check()

        Judul = ttk.Label(self, text="Data nomor 2", background='black', foreground='white', font=Font_judul)
        Judul.grid(row=0, column=0, pady=10, padx=10)

        teks = ttk.Label(self, text=f"""Kendaraan berjenis {JenisKendaraan[1]}
Kendaraan berkategori {kategori[1]}
Dan memiliki plat nomor {plat[1]}
{hasil}""", background='black', foreground='white', font=Font_judul)
        teks.grid(row=1, column=0, padx=10, pady=10)

        button1 = tk.Button(self, text="Prev", background='black', foreground='white', command=lambda : controlling.show_frame(Nomor1))
        button1.grid(row=2, column=0, pady=10, padx=10)

        button2 = tk.Button(self, text="Next", background='black', foreground='white', command=lambda : controlling.show_frame(Nomor3))
        button2.grid(row=2, column=1, padx=10, pady=10)


class Nomor3(tk.Frame):
    def __init__(self, parent, controlling):
        tk.Frame.__init__(self, parent)

        self.a = xlrd.open_workbook(filename='Kendaraan dan plat.xlsx')
        self.b = self.a.sheet_by_index(0)

        JenisKendaraan = []
        for i in range(1, self.b.nrows):
            JenisKendaraan.append(self.b.cell_value(i, 1))
        kategori = []
        for i in range(1, self.b.nrows):
            kategori.append(self.b.cell_value(i, 2))
        plat = []
        for i in range(1, self.b.nrows):
            plat.append(self.b.cell_value(i, 3))

        checking = Ngecheck(f"{plat[2]}")
        hasil = checking.check()

        Judul = ttk.Label(self, text="Data nomor 3", background='black', foreground='white', font=Font_judul)
        Judul.grid(row=0, column=0, pady=10, padx=10)

        teks = ttk.Label(self, text=f"""Kendaraan berjenis {JenisKendaraan[2]}
Kendaraan berkategori {kategori[2]}
Dan memiliki plat nomor {plat[2]}
{hasil}""", background='black', foreground='white', font=Font_judul)
        teks.grid(row=1, column=0, padx=10, pady=10)

        button1 = tk.Button(self, text="Prev", background='black', foreground='white', command=lambda : controlling.show_frame(Nomor2))
        button1.grid(row=2, column=0, pady=10, padx=10)

        button2 = tk.Button(self, text="Next", background='black', foreground='white', command=lambda : controlling.show_frame(Nomor4))
        button2.grid(row=2, column=1, padx=10, pady=10)

class Nomor4(tk.Frame):
    def __init__(self, parent, controlling):
        tk.Frame.__init__(self, parent)

        self.a = xlrd.open_workbook(filename='Kendaraan dan plat.xlsx')
        self.b = self.a.sheet_by_index(0)

        JenisKendaraan = []
        for i in range(1, self.b.nrows):
            JenisKendaraan.append(self.b.cell_value(i, 1))
        kategori = []
        for i in range(1, self.b.nrows):
            kategori.append(self.b.cell_value(i, 2))
        plat = []
        for i in range(1, self.b.nrows):
            plat.append(self.b.cell_value(i, 3))

        checking = Ngecheck(f"{plat[3]}")
        hasil = checking.check()

        Judul = ttk.Label(self, text="Data nomor 4", background='black', foreground='white', font=Font_judul)
        Judul.grid(row=0, column=0, pady=10, padx=10)

        teks = ttk.Label(self, text=f"""Kendaraan berjenis {JenisKendaraan[3]}
Kendaraan berkategori {kategori[3]}
Dan memiliki plat nomor {plat[3]}
{hasil}""", background='black', foreground='white', font=Font_judul)
        teks.grid(row=1, column=0, padx=10, pady=10)

        button1 = tk.Button(self, text="Prev", background='black', foreground='white', command=lambda : controlling.show_frame(Nomor3))
        button1.grid(row=2, column=0, pady=10, padx=10)

        button2 = tk.Button(self, text="Next", background='black', foreground='white', command=lambda : controlling.show_frame(Nomor5))
        button2.grid(row=2, column=1, padx=10, pady=10)

class Nomor5(tk.Frame):
    def __init__(self, parent, controlling):
        tk.Frame.__init__(self, parent)

        self.a = xlrd.open_workbook(filename='Kendaraan dan plat.xlsx')
        self.b = self.a.sheet_by_index(0)

        JenisKendaraan = []
        for i in range(1, self.b.nrows):
            JenisKendaraan.append(self.b.cell_value(i, 1))
        kategori = []
        for i in range(1, self.b.nrows):
            kategori.append(self.b.cell_value(i, 2))
        plat = []
        for i in range(1, self.b.nrows):
            plat.append(self.b.cell_value(i, 3))

        checking = Ngecheck(f"{plat[4]}")
        hasil = checking.check()

        Judul = ttk.Label(self, text="Data nomor 5", background='black', foreground='white', font=Font_judul)
        Judul.grid(row=0, column=0, pady=10, padx=10)

        teks = ttk.Label(self, text=f"""Kendaraan berjenis {JenisKendaraan[4]}
Kendaraan berkategori {kategori[4]}
Dan memiliki plat nomor {plat[4]}
{hasil}""", background='black', foreground='white', font=Font_judul)
        teks.grid(row=1, column=0, padx=10, pady=10)

        button1 = tk.Button(self, text="Prev", background='black', foreground='white', command=lambda : controlling.show_frame(Nomor4))
        button1.grid(row=2, column=0, pady=10, padx=10)

        button2 = tk.Button(self, text="Next", background='black', foreground='white', command=lambda : controlling.show_frame(Nomor5))
        button2.grid(row=2, column=1, padx=10, pady=10)

class Nomor6(tk.Frame):
    def __init__(self, parent, controlling):
        tk.Frame.__init__(self, parent)

        self.a = xlrd.open_workbook(filename='Kendaraan dan plat.xlsx')
        self.b = self.a.sheet_by_index(0)

        JenisKendaraan = []
        for i in range(1, self.b.nrows):
            JenisKendaraan.append(self.b.cell_value(i, 1))
        kategori = []
        for i in range(1, self.b.nrows):
            kategori.append(self.b.cell_value(i, 2))
        plat = []
        for i in range(1, self.b.nrows):
            plat.append(self.b.cell_value(i, 3))

        checking = Ngecheck(f"{plat[5]}")
        hasil = checking.check()

        Judul = ttk.Label(self, text="Data nomor 6", background='black', foreground='white', font=Font_judul)
        Judul.grid(row=0, column=0, pady=10, padx=10)

        teks = ttk.Label(self, text=f"""Kendaraan berjenis {JenisKendaraan[5]}
Kendaraan berkategori {kategori[5]}
Dan memiliki plat nomor {plat[5]}
{hasil}""", background='black', foreground='white', font=Font_judul)
        teks.grid(row=1, column=0, padx=10, pady=10)

        button1 = tk.Button(self, text="Prev", background='black', foreground='white', command=lambda : controlling.show_frame(Nomor5))
        button1.grid(row=2, column=0, pady=10, padx=10)

        button2 = tk.Button(self, text="Next", background='black', foreground='white', command=lambda : controlling.show_frame(Nomor7))
        button2.grid(row=2, column=1, padx=10, pady=10)

class Nomor7(tk.Frame):
    def __init__(self, parent, controlling):
        tk.Frame.__init__(self, parent)

        self.a = xlrd.open_workbook(filename='Kendaraan dan plat.xlsx')
        self.b = self.a.sheet_by_index(0)

        JenisKendaraan = []
        for i in range(1, self.b.nrows):
            JenisKendaraan.append(self.b.cell_value(i, 1))
        kategori = []
        for i in range(1, self.b.nrows):
            kategori.append(self.b.cell_value(i, 2))
        plat = []
        for i in range(1, self.b.nrows):
            plat.append(self.b.cell_value(i, 3))

        checking = Ngecheck(f"{plat[6]}")
        hasil = checking.check()

        Judul = ttk.Label(self, text="Data nomor 7", background='black', foreground='white', font=Font_judul)
        Judul.grid(row=0, column=0, pady=10, padx=10)

        teks = ttk.Label(self, text=f"""Kendaraan berjenis {JenisKendaraan[6]}
Kendaraan berkategori {kategori[6]}
Dan memiliki plat nomor {plat[6]}
{hasil}""", background='black', foreground='white', font=Font_judul)
        teks.grid(row=1, column=0, padx=10, pady=10)

        button1 = tk.Button(self, text="Prev", background='black', foreground='white', command=lambda : controlling.show_frame(Nomor6))
        button1.grid(row=2, column=0, pady=10, padx=10)

        button2 = tk.Button(self, text="Next", background='black', foreground='white', command=lambda : controlling.show_frame(Home))
        button2.grid(row=2, column=1, padx=10, pady=10)


app = tkinterApp()
app.mainloop()
