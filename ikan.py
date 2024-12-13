from animal import animal


class Ikan(animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak):
        super().__init__(nama, makanan, hidup, berkembang_biak)
    def info_ikan(self):
        print("nama \t\t\t :", self.nama,
              "\nmakanan\t\t\t :", self.makanan,
              "\nhidup\t\t\t :", self.hidup,
               "\nberkembang_biak \t\t\t :", self.berkembang_biak)

print("================================")

ikan_mujair = Ikan("Mujair","Pelet","Air","bertelur")
ikan_lele = Ikan("lele","Pelet","Air","bertelur")
ikan_mujair.info_ikan()
print("================================")
ikan_lele.info_ikan()




