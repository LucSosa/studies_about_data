# %%
name = "Lucas Sosa"
print(name)
print("Meu nome é ", name)

# %%
a = 10
b = 20
sum = a + b
print("A soma é ", sum)

# %%
condition = a > b
if condition:
    print("Isso é verdade")
else:
    print("Isso nunca vai acontecer")

# %%
age = int(input("Entre com a sua idade: "))
cnh = input("Você tem CNH? ")

if age >= 18 and cnh == "sim":
    print("Siga em frente")

else:
    print("Preso em nome da lei!")

qualification = age >= 18 and cnh == "sim"
print(qualification)

# %%
yourAge = int(input("Entre com a sua idade:"))

if yourAge < 18:
    print("Você é menor de idade!")
    print("Vá para casa beber leite!")

elif yourAge >= 90:
    print("Cuidado, você já tem certa idade!")

else:
    print("Você é maior de idade")
    print("Beba a vontade!")
