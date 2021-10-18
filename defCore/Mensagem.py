import time


class Mess:
    def __init__(self):
        ...

    def tratar(self, valor, logotype):
        self.valor = valor
        self.logotype = logotype
        print('-'*50)
        time.sleep(.5)
        self.vlr = 46 - len(self.logotype)
        print('| '+(' '*(self.vlr // 2))+(str(self.logotype))+(' '*(self.vlr // 2))+' |')
        time.sleep(.5)
        print('-'*50)

    def baner(self, valor):
        self.valor = valor
        self.logotype = 'DJTEST - INICIALIZANDO APLICAÇÂO'
        ObjMess.tratar(self.valor, self.logotype)

    def exerc(self, valor):
        self.valor = valor
        self.logotype = 'EXERCÍCIO '+str(self.valor)
        ObjMess.tratar(self.valor, self.logotype)


ObjMess = Mess()
