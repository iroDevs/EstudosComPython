def calcular_area(base: float, altura: float) -> float:
    return base * altura

base = float(input("Valor da base: "))
altura = float(input("Valor da altura: "))

area = calcular_area(base, altura)

print(f"base {base} \naltura {altura} \narea é igual a: {area}")
