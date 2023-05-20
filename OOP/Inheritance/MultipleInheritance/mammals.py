class Mammals:
    def mam_info(self):
        print("Mammals can give birth")

class Wingedmammals:
    def winged_info(self):
        print("Winged mammals can fly and flap")

class Bats(Mammals,Wingedmammals):
    pass
#Object of the Bat class
b1=Bats()
b1.winged_info()
b1.mam_info()
    