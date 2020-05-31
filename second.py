
class Fighter:
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        if type(name) is str:
            self.__name = name
        else:
            raise Exception ('Error: not str type')
    @property
    def defence(self):
        return self.__defence
    @defence.setter
    def defence(self, defence):
        if type(defence) is int:
            self.__defence = defence
        else:
            raise Exception ('Error: not int type')
    @property
    def strenth(self):
        return self.__strenth
    @strenth.setter
    def strenth(self, strenth):
        if type(strenth) is int:
            self.__strenth = strenth
        else:
            raise Exception ('Error: not int type')
    def fight(self, other):
        if other.__strenth > self.__defence:
            if self.__strenth > other.__defence:
                print('ничья') 
            else:
                print("победитель", other.__name)
        else:
            if self.__strenth > other.__defence:
                print("победитель", self.__name)
            else:
                print('ничья') 


class Fighter_Builder:
    def __init__(self):
        self.fighter = None
    def create_new_fighter(self,name,defence,strenth):
        self.fighter = Fighter()
        self.fighter.name = name
        self.fighter.defence = defence
        self.fighter.strenth = strenth
        return self.fighter


builder = Fighter_Builder()
A = builder.create_new_fighter('One',4,5)
B = builder.create_new_fighter('Two',3,7)
C = builder.create_new_fighter('Three',2,4)
D = builder.create_new_fighter('Four',20,4)
E = builder.create_new_fighter('Five',20,41)


class Championship:
    @staticmethod
    def championship(list):
        for i in range(len(list)):
            for j in range(len(list)):
                if j + 1 != len(list):
                    list[0].fight(list[j+1])
                else:
                    del list[0]


competitors = [A, B, C, D, E]              
fighting = Championship()
fighting.championship(competitors)
print('check')
A.fight(B)
A.fight(C)
A.fight(D)
A.fight(E)
B.fight(C)
B.fight(D)
B.fight(E)
C.fight(D)
C.fight(E)
D.fight(E)




 