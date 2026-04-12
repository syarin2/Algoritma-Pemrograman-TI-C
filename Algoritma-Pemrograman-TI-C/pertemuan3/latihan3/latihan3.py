class Vehicle:
    def __init__(self, jenis, merk, tahun_rilis):
        self.jenis = jenis
        self.merk = merk
        self.tahun_rilis = tahun_rilis
    def sound(self):
        return("suara")
    
class Motor(Vehicle):
    def __init__(self, merk, tahun_rilis):
        self.__tahun_rilis = tahun_rilis
        super().__init__(self, merk, tahun_rilis)
    def get_tahun_rilis(self):
        return self.__tahun_rilis
    def set_tahun_rilis(self):
        return self.__tahun_rilis
    def sound(self):
        return ("Brumm")
    
class Car(Vehicle):
    def __init__(self, merk, tahun_rilis):
        self.__tahun_rilis = tahun_rilis
        super().__init__(self, merk, tahun_rilis)

    def get_tahun_rilis(self):
        return self.__tahun_rilis
    
    def set_tahun_rilis(self):
        return self.__tahun_rilis
    def sound(self):
        return ("Brumm")

v1 = Vehicle("Mobil", 2006, "Innova")
c1 = Car(2007, "Reborn")
m1 = Motor(2008, "Beat")

print(m1.sound())
print(c1.get_tahun_rilis())