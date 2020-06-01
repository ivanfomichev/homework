
class NinjaTurtle:
    def __init__(self, band_color, weapon):
        self.band_color = band_color
        self.weapon = weapon

class Leonardo(NinjaTurtle): 
    pass

class Michelangelo(NinjaTurtle):
    pass

class Donatello(NinjaTurtle):
    pass

class Raphael(NinjaTurtle):
    pass
  

class NinjaFactory:
    def get_ninja(self, ninja_type):
        if ninja_type == "Leonardo":
            return Leonardo('blue', 'katana')
        elif ninja_type == "Michelangelo":
            return Michelangelo('orange','nunchaku')
        elif ninja_type == "Donatello":
            return Donatello('purple','staff')
        else:
            return Raphael('red','sai')

factory = NinjaFactory()
Leonardo = factory.get_ninja('Leonardo')
Michelangelo = factory.get_ninja('Michelangelo')
Donatello = factory.get_ninja('Donatello')
Raphael = factory.get_ninja('Raphael')

print('Leonardo band color is', Leonardo.band_color, 'and weapon is', Leonardo.weapon)
print('Michelangelo band color is', Michelangelo.band_color, 'and weapon is', Michelangelo.weapon)
print('Donatello band color is', Donatello.band_color, 'and weapon is', Donatello.weapon)
print('Raphael band color is', Raphael.band_color, 'and weapon is', Raphael.weapon)

names = ['Leonardo', 'Michelangelo', 'Donatello', 'Raphael']
ninjas = [Leonardo, Michelangelo, Donatello, Raphael]

class Splinter:

    @staticmethod  
    def get_student_band_color(student_name, names, ninjas):
        students = dict(zip(names, ninjas))
        student = students.get(student_name, 'wrong name')
        return student.band_color
        
    @staticmethod  
    def get_student_weapon(student_name, names, ninjas):
        students = dict(zip(names, ninjas))
        student = students.get(student_name, 'wrong name')
        return student.weapon


master = Splinter()
master.get_student_band_color('Leonardo', names, ninjas)
master.get_student_weapon('Leonardo', names, ninjas)
master.get_student_band_color('Michelangelo', names, ninjas)
master.get_student_weapon('Michelangelo', names, ninjas)
master.get_student_band_color('Donatello', names, ninjas)
master.get_student_weapon('Donatello', names, ninjas)
master.get_student_band_color('Raphael', names, ninjas)
master.get_student_weapon('Raphael', names, ninjas)