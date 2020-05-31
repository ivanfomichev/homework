#задание 0
import math
help(math)

math.log(25)
math.log(math.exp(3))
math.log10(1000)
math.pi**3
print(123**4)
math.sqrt(459)

#задание 1
a = 2
b = 5
a,b = b,a
print(a,b)

#задание 2
gdp = 501231234234
d = math.log(gdp)
print("Логарифм ВВП: %.2f" %d)

#задание 3
fh = 15
p = 4
Fr = 0.4*fh + 0.6*p
print(Fr)

#задание 4
n = int(input("введите день от 1 до 31:"))
print("Дней: %i" %n)
m = 1
i = 1
k = 3
while i <= n:
    if i != 1:
        m = m + k
    i = i + 1    
print("Минут на солнце: %i" %m)


