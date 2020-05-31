class NinjaTurtle:
    name = ''
    band_color = ""
    weapon = ""

    # абстрактный метод, который переопределяется в дочернем классе
    def say(self):
        raise NotImplementedError("Subclass must implement abstract method")


class Leonardo(NinjaTurtle):
    name = 'Leonardo'
    band_color = "blue"
    weapon = "katana"
    def say(self):
        return "uhuuu!"


class Michelangelo(NinjaTurtle):
    name = 'Michelangelo'
    band_color = "orange"
    weapon = "nunchaku"
    def say(self):
        return "come on!"


class Donatello(NinjaTurtle):
    name = 'Donatello'
    band_color = "purple"
    weapon = "staff"
    def say(self):
        return "let's go!"


class Raphael(NinjaTurtle):
    name = 'Raphael'
    band_color = "red"
    weapon = "sai"
    def say(self):
        return "got it!"


class AbstractFactory:
    def get_ninja(self, ninja_type):
        raise NotImplementedError("Subclass must implement abstract method")


class NinjaFactory(AbstractFactory):
    def get_ninja(self, ninja_type):
        if ninja_type == 'Leonardo':
            return Leonardo()
        elif ninja_type == 'Michelangelo':
            return Michelangelo()
        elif ninja_type == 'Donatello':
            return Donatello()
        elif ninja_type == 'Raphael':
            return Raphael()
        else:
            print('wrong type')


factory = NinjaFactory()
Leonardo = factory.get_ninja('Leonardo')
Michelangelo = factory.get_ninja('Michelangelo')
Donatello = factory.get_ninja('Donatello')
Raphael = factory.get_ninja('Raphael')

Leonardo.say()
Michelangelo.say()
Donatello.say()
Raphael.say()

print('Leonardo band color is', Leonardo.band_color, 'and weapon is', Leonardo.weapon)
print('Michelangelo band color is', Michelangelo.band_color, 'and weapon is', Michelangelo.weapon)
print('Donatello band color is', Donatello.band_color, 'and weapon is', Donatello.weapon)
print('Raphael band color is', Raphael.band_color, 'and weapon is', Raphael.weapon)

names = ['Leonardo', 'Michelangelo', 'Donatello', 'Raphael']
ninjas = [Leonardo, Michelangelo, Donatello, Raphael]


class Splinter:
    students = {}

    def __init__(self, names, ninjas):
        self.names = names
        self.ninjas = ninjas
        Splinter.students = dict(zip(self.names, self.ninjas))

    @staticmethod
    def get_student_band_color(student_name):
        student = Splinter.students.get(student_name)
        if student is None:
            raise Exception('wrong_name')
        return student.band_color

    @staticmethod
    def get_student_weapon(student_name):
        student = Splinter.students.get(student_name)
        if student is None:
            raise Exception('wrong_name')
        return student.weapon


master = Splinter(names, ninjas)
master.get_student_band_color('Leonardo')
master.get_student_weapon('Leonardo')
master.get_student_band_color('Michelangelo')
print(master.get_student_band_color('Michelangelo'))
master.get_student_weapon('Michelangelo')
master.get_student_band_color('Donatello')
master.get_student_weapon('Donatello')
master.get_student_band_color('Raphael')
master.get_student_weapon('Raphael')

isinstance(Splinter.students['Leonardo'], NinjaTurtle)

issubclass(Leonardo, NinjaTurtle)