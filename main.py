from calculator import Calculator

calc = Calculator()
expr = input()#rentrez votre expression mathématique :
result = calc.evaluate_math_expression(expr)
print(f"Résultat : {result}")