from defCore.Exercicios import ObjExercicios


class Validate:
    def validar(self, active, securityName):
        self.active = active
        self.securityName = securityName
        self.on = True
        while self.on:
            try:
                self.recebe = input(": -> ")
                if self.recebe not in '0123456789Ss':
                    return ValueError("Números ou S")
                if self.recebe in 'Ss':
                    self.active = False
                    return self.active, self.securityName
                else:
                    if 0 < int(self.recebe) < 9 and (len(self.recebe) == 2):
                        print(ObjExercicios.exercicio(str(self.recebe[1]), self.securityName))
                        return self.active, self.securityName
                    
                    if 0 < int(self.recebe) < 9 and (len(self.recebe) == 1):
                        print(ObjExercicios.exercicio(str(self.recebe), self.securityName))
                        return self.active, self.securityName

            except ValueError as e:
                print('', e)
    

ObjValidate = Validate()
