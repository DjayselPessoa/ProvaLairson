from defCore.Mensagem import ObjMess
import time
import random


class Exercicios:
    def exercicio(self, valor, securityName):
        self.valor = int(valor)
        self.securityName = securityName
        self.numlist = []
        self.activeIn = True
        if self.valor == 1:
            # EXERCICIO 01
            ObjMess.exerc(1)
            while self.activeIn:
                try:
                    self.recebe = input('Informe um número positivo até 100! Números negativos realizarão o cálculo: ')
                    # print(self.recebe)
                    if 0 <= int(self.recebe) <= 100:
                        self.numlist.append(int(self.recebe))

                    if int(self.recebe) < 0:
                        self.cont = 0
                        for x in self.numlist:
                            if 0 <= x <= 25:
                                print(f'Posição {self.cont} da lista - Valor {self.numlist[self.cont]} está entre [0|25]')
                                self.cont += 1
                            if 26 <= x <= 50:
                                print(f'Posição {self.cont} da lista - O valor {self.numlist[self.cont]} está entre [26|50]')
                                self.cont += 1
                            if 51 <= x <= 75:
                                print(f'Posição {self.cont} da lista - O valor {self.numlist[self.cont]} está entre [51|75]')
                                self.cont += 1
                            if 76 <= x <= 100:
                                print(f'Posição {self.cont} da lista - O valor {self.numlist[self.cont]} está entre [76|100]')
                                self.cont += 1
                        self.activeIn = False
                        time.sleep(3)
                        raise ValueError("\nRETORNANDO!\n")
                    if int(self.recebe) > 100:
                        raise ValueError("Números de 0 a 100 ou negativo para executar!")

                except ValueError as e:
                    print("", e)
            return ""
        elif self.valor == 2:
            # EXERCICIO 02
            ObjMess.exerc(2)
            while self.activeIn:
                try:
                    self.recebe = input('Informe uma nota entre 0 e 10: ')
                    # print(type(self.recebe))
                    if self.recebe.find(','):
                        self.recebe = self.recebe.replace(',', '.')
                        print(self.recebe)
                    for x in self.recebe:
                        if x not in '0123456789.':
                            raise ValueError("DADO INCORRETO!\n")
                        else:
                            continue

                    if 0.0 <= float(self.recebe) <= 10.0:
                        print(f"A nota informada foi: {self.recebe}")
                        if 0.0 <= float(self.recebe) <= 6.5:
                            print(f"{self.securityName}, você foi reprovado!")
                            time.sleep(1)
                            self.activeIn = False
                            raise ValueError("\nREINICIANDO!")
                        elif 6.6 <= float(self.recebe) <= 10.0:
                            print(f"{self.securityName}, você foi aprovado!")
                            time.sleep(1)
                            self.activeIn = False
                            raise ValueError("\nREINICIANDO!")
                    else:
                        raise ValueError("Informe uma nota válida de 0 a 10!")
                except ValueError as e:
                    print("", e)
            return ""
        elif self.valor == 3:
            # EXERCICIO 03
            ObjMess.exerc(3)
            self.candidatosRJ = {}
            self.cont = 1
            while self.activeIn:
                try:
                    self.totalCandRJ = int(input('Informe a quantidade de candidatos do concurso no RJ: '))
                    for x in range(self.totalCandRJ):
                        self.criarnome = input(f"informe o nome do {self.cont}º candidato: ")
                        self.notaCand = input("Informe a nota do candidat@ "+self.criarnome+": ")
                        if self.notaCand.find(','):
                            self.notaCand = self.notaCand.replace(',', '.')
                            print(self.notaCand)

                        for x in self.notaCand:
                            if x in '0123456789.':
                                continue
                            else:
                                raise ValueError("VALOR INCORRETO!")

                        self.candidatosRJ[self.criarnome] = float(self.notaCand)
                        self.cont += 1
                    print(self.candidatosRJ)
                    for x in self.candidatosRJ:
                        if self.candidatosRJ[x] < 80:
                            time.sleep(.5)
                            print(f'Candidat@ {x} recebeu a nota {self.candidatosRJ[x]} e foi reprovado!')
                        elif self.candidatosRJ[x] > 80:
                            time.sleep(.5)
                            print(f'Candidat@ {x} recebeu a nota {self.candidatosRJ[x]} e foi aprovado!')
                    self.activeIn = False
                    raise ValueError("")
                except ValueError as e:
                    print("", e)
            return ""
        elif self.valor == 4:
            # EXERCICIO 04
            ObjMess.exerc(4)
            self.s = 0
            while (self.s) < 10:
                print(self.s + 1)
                self.s = self.s + 1
            print(f"fim do While! s = {self.s}")
            return ""
        elif self.valor == 5:
            # EXERCICIO 05
            ObjMess.exerc(5)
            ListaVazia = []
            for x in range(10):
                ListaVazia.append(x)
            print(ListaVazia)
            return ""
        elif self.valor == 6:
            # EXERCICIO 06
            ObjMess.exerc(6)
            self.listaVazia = []
            for x in range(10):
                self.listaVazia.append(0)
                print(self.listaVazia)
            for x in range(10):
                aleatorio = int(random.randrange(1, 100))
                self.listaVazia[x] = aleatorio
                print(self.listaVazia)
            print('Fim!')
            time.sleep(.5)
            return ""
        elif self.valor == 7:
            # EXERCICIO 07
            ObjMess.exerc(7)
            while self.activeIn:
                try:
                    self.listaV = {}
                    self.nomeAtleta = input("Informe o nome do atleta: ")
                    if self.nomeAtleta == "":
                        self.activeIn = False
                        raise ValueError("TERMINANDO!")
                    self.listaSaltos = []
                    self.media = 0
                    for x in range(5):
                        self.salto = float(input(f"Informe a nota do {x}º salto: "))
                        self.media = self.media + self.salto
                        self.listaSaltos.append(self.salto)
                    self.media = self.media / 5
                    self.listaV[self.nomeAtleta] = self.listaSaltos

                    print('-'*50+f'\nAtleta: {self.nomeAtleta}\n\nPrimeiro salto: {self.listaV[self.nomeAtleta][0]}\nSegundo salto: {self.listaV[self.nomeAtleta][1]}\nTerceiro salto: {self.listaV[self.nomeAtleta][2]}\nQuarto salto: {self.listaV[self.nomeAtleta][3]}\nQuito salto: {self.listaV[self.nomeAtleta][4]}\n\nResultado final:\nAtleta: {self.nomeAtleta}\nSaltos: {self.listaV[self.nomeAtleta]}\nMédia dos Saltos: {self.media}\n'+('-'*50))
                    # print('Fim!')
                    time.sleep(.5)
                except ValueError as e:
                    print("LOG -> ", e)
            return ""
        elif self.valor == 8:
            # EXERCICIO 08
            ObjMess.exerc(8)
            while self.activeIn:
                try:
                    valores = [] 
                    listaSO = ['Windows Server', 'Unix', 'Linux', 'NetWare', 'Mac OS', 'Outros']
                    print(f'Qual o melhor sistema operacional para uso em servidores?\n\nAs possívels respostas são:\n\n1 - {listaSO[0]}\n2 - {listaSO[1]}\n3 - {listaSO[2]}\n4 - {listaSO[3]}\n5 - {listaSO[4]}\n6 - {listaSO[5]}\n')
                    print(('-'*50)+'\n')
                    print('Sistema Operacional     Votos   %  \n'+('-'*18)+(' '*5)+('-'*5)+'   ---\n')
                    for x in range(6):
                        self.numRand = random.randrange(1, 10000)
                        valores.append(float(self.numRand))
                    self.cont = 0
                    # mediaValores = sum(valores) / len(valores)
                    # print(valores)
                    for x in listaSO:
                        if self.cont == len(listaSO):
                            break
                        porcentagem = float(valores[self.cont] * 100) / sum(valores)
                        self.vlr = 24 - len(str(listaSO[self.cont]))
                        self.vlr1 = 6 - len(str(valores[self.cont]))
                        print(f'{x}'+(' '*self.vlr)+(' '*self.vlr1)+f'{int(valores[self.cont])}   {round(porcentagem, 2)}%')
                        self.cont += 1
                    print(('-'*18)+(' '*5)+('-'*5)+'   ---')
                    total = int(sum(valores))
                    print(f'Total'+(' '*18)+str(round(total, 1))+'   100%')
                    self.activeIn = False
                    time.sleep(3)
                    raise ValueError("SAINDO!")
                except ValueError as e:
                    print("LOG -> ", e)
            return ""


ObjExercicios = Exercicios()
