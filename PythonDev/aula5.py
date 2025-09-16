num1 = int(input("Digite o primeiro numero:\n"))
num2 = int(input("Digite o segundo numero:\n"))

sum = num1 + num2
sub = num1 - num2
div = num1 / num2
mult = num1 * num2
mod = num1 % num2
exp = num1 ** num2

print(sum)
print(f"Potência do número {num1} por {num2} é: {exp}")

#comparação
bigger = num1 > num2
smaller = num1 < num2
equal = num1 == num2
different = num1 != num2
bigger_equal = num1 >= num2
smaller_equal = num1 <= num2

print(bigger)
print(smaller)