import xlrd

class excel(object):
    def __init__(self, file_name = "event ctfbersama (sementara).xlsx"):
        self.a = xlrd.open_workbook(file_name)
        self.b = self.a.sheet_by_index(0)
    def nama_event(self):
        nama = []
        for i in range (1, self.b.nrows):
            nama.append(self.b.cell_value(i, 1))
        for i in nama:
            i = nama.remove('')
        return nama
    def kategori(self):
        tingkat = []
        for i in range(1, self.b.nrows):
            tingkat.append(self.b.cell_value(i, 2))
        for i in tingkat:
            i = tingkat.remove('')
        return tingkat
    def tipe(self):
        tipe = []
        for i in range(1, self.b.nrows):
            tipe.append(self.b.cell_value(i, 3))
        for i in tipe:
            i = tipe.remove('')
        return tipe

tes = excel()
print(tes.nama_event())
print(tes.kategori())
print(tes.tipe())