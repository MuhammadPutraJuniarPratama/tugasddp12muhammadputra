from animal import animal


class singa(animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak):
        super().__init__(nama, makanan, hidup, berkembang_biak)
    def info_singa(self):
        print("nama \t\t\t :", self.nama,
              "\nmakanan\t\t\t :", self.makanan,
              "\nhidup\t\t\t :", self.hidup,
               "\nberkembang_biak \t\t\t :", self.berkembang_biak)
        

print("================================")
singa_afrika = singa("afrika","daging","savana","melahirkan")
singa_asia = singa("asia","daging","hutan tropis","melahirkan")
singa_afrika.info_singa()
print("================================")
singa_asia.info_singa() 