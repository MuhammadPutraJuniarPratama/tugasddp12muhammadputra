#Buat class animal sebagai parent class. class animal mempunyai properti 4 properti (name, makanan, hidup, berkembang biak)
#buat minimal 3 class child (burung, ikan, ular, dll) setiap class child itu memiliki 2 properti dan method 
#buat minimal 2 objek untuk setiap class childnya. 

from animal import animal

class burung(animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, paruh, warna_bulu ):
        super().__init__(nama, makanan, hidup, berkembang_biak),
        self.paruh = paruh
        self.warna_bulu = warna_bulu   


    def info_burung(self) :
        super().info_animal(),
        print("Paruh \t\t\t :",self.paruh,
              "\nWarna Bulu \t\t :",self.warna_bulu)
print("===================================")
    
burung_beo = burung("Beo", "jagung", "udara", "bertelur", "panjang", "hitam")
burung_kutilang = burung("kutilang", "biji-bijian", "udara", "bertelur", "pendek", "abu-abu")
burung_beo.info_burung()
print()
print("===================================")
burung_kutilang.info_burung()
