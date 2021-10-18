from defCore.Exercicios import ObjExercicios
from defCore.Validate import ObjValidate
import time
# from defCore.Mensagem import ObjMess


class Escolha:
    def __init__(self):
        self.active = True
        self.SECURITYNAME = input('INFORME NOME: -> ')
        time.sleep(.5)
        print(f"\nBEM VINDO {self.SECURITYNAME}!\n")

    def inicializar(self):
        while self.active:
            try:
                tab = 36 // 2
                listaExercicios = {1: 'exercicio01', 2: 'exercicio02', 3: 'exercicio03', 4: 'exercicio04', 5: 'exercicio05', 6: 'exercicio06', 7: 'exercicio07', 8: 'exercicio08', 9: 'exercicio09', 10: 'exercicio10'}
                print(f'\nNÚMERO OU S PARA SAIR: ->\n\n'+(' '*tab)+f' - GRUPO 01 -\n\n[1] - {listaExercicios[1]}\n[2] - {listaExercicios[2]}\n[3] - {listaExercicios[3]}\n[4] - {listaExercicios[4]}\n'+(' '*tab)+f' - GRUPO 2 - \n\n[5] - {listaExercicios[5]}\n[6] - {listaExercicios[6]}\n[7] - {listaExercicios[7]}\n[8] - {listaExercicios[8]}\n')

                self.active, self.SECURITYNAME = ObjValidate.validar(self.active, self.SECURITYNAME)
                if self.active is False:
                    raise ValueError("\n\nTERMINANDO APLICAÇÂO\n")

            except ValueError as e:
                print("", e)


ObjEscolha = Escolha()
