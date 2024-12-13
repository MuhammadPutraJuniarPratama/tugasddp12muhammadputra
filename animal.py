#Buat class animal sebagai parent class. class animal mempunyai properti 4 properti (name, makanan, hidup, berkembang biak)
#buat minimal 3 class child (burung, ikan, ular, dll) setiap class child itu memiliki 2 properti dan method 
#buat minimal 2 objek untuk setiap class childnya. 

class animal:
    def __init__(self, nama, makanan, hidup, berkembang_biak):
        self.nama = nama
        self.makanan = makanan
        self.hidup = hidup
        self.berkembang_biak = berkembang_biak

    def info_animal(self):
        print("nama \t\t\t :", self.nama,
              "\nmakanan\t\t\t :", self.makanan,
               "\nberkembang_biak \t\t\t :", self.berkembang_biak)
        

binatang = animal("Kucing","Daging", "Darat", "Melahirkan")
binatang.info_animal()
    
