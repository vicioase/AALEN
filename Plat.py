class Ngecheck(object):
    """Plat harus berformat string Upper Case"""
    def __init__(self, plat_nomor):
        self.p = plat_nomor

    def check(self):
        if self.p == "AD":
            return("Untuk kendaraan berkaresidenan Surakarta")
        elif self.p == "B":
            return("Untuk kendaraan wilayah DKI Jakarta")
        elif self.p == "A":
            return("Untuk kendaraan wilayah Banten")
        elif self.p == "D":
            return("Untuk kendaraan wilayah Bandung")
        elif self.p == "T":
            return("Untuk kendaraan wilayah Purwakarta")
        elif self.p == "K":
            return("Untuk kendaraan wilayah Pati")
        elif self.p == "G":
            return("Untuk kendaraan wilayah Pekalongan")
        elif self.p == "H":
            return("Untuk kendaraan wilayah Semarang")
        elif self.p == "R":
            return("Untuk kendaraan wilayah Banyumas")
        elif self.p == "AB":
            return("Untuk kendaraan wilayah Yogyakarta")
        elif self.p == "AE":
            return("Untuk kendaraan wilayah Madiun")
        elif self.p == "S":
            return("Untuk kendaraan wilayah Bojonegoro")
        elif self.p == "N":
            return("Untuk kendaraan wilayah Malang")
        elif self.p == "M":
            return("Untuk kendaraan wilayah Madura")
        elif self.p == "L":
            return("Untuk kendaraan wilayah Surabaya")
        elif self.p == "W":
            return("Untuk kendaraan wilayah Sidoarjo")
        elif self.p == "AG":
            return("Untuk kendaraan wilayah Kediri")
        elif self.p == "Z":
            return("Untuk kendaraan wilayah Garut")
        elif self.p == "E":
            return("Untuk kendaraan wilayah Cirebon")
        else:
            return("Maaf plat kendaraan tidak terdaftar atau Input salah format")


ada = Ngecheck("B 88880 PT")
ada.check()
