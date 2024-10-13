class pacote:
    def __init__(self,param):
        self._param=param


    def exibir(self):
        print(f"param {self._param}")


class pacote_extendido(pacote):
    def __init__(self, parami,adicional):
        super().__init__(parami)
        self.acidional=adicional

    def exibir(self):
        super().exibir()
        print(f"paramet {self._param} {self.acidional}")

        




pacote1 = pacote(1544)
pacote1.exibir()
pacote1_ad = pacote_extendido(871,"foidd")
pacote1_ad.exibir()
