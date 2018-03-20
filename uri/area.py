vez = 0
par = []
while vez < 1:
    x = input()
    lista = list(x)
    count = 0
    var = ''
    for l in lista:
        if l == " ":
            count += 1
            par.append(float(var))
            var = ''
        else:
            var += l
    par.append(float(var))
    vez += 1

a, b, c = par
pi = 3.14159
triangulo = (a * c) / 2
circulo = pi * (c**2)
trapezio = ((a+b)*c)/2
quadrado = b * b
retangulo = a * b

print("TRIANGULO: %.3f" %triangulo)
print("CIRCULO: %.3f" %circulo)
print("TRAPEZIO: %.3f" %trapezio)
print("QUADRADO: %.3f" %quadrado)
print("RETANGULO: %.3f" %retangulo)