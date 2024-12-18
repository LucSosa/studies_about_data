#%%
emptyList = []
print(emptyList)

emptyList = ["Lucas", "Sosa", 27, 1.70]
print(emptyList)

emptyList[0]
emptyList[0:2]
emptyList[::-2]

#%% 
for i in "Lucas Sosa":
    
    if i == "L":
        continue

    elif i == " ":
        continue
    
    print(i)

# %%
qtde = int(input("Quantas vezes deve repetir?"))

for i in range(qtde):
    print("repete")

# %%
qtde = int(input("Quantos vezes deve repetir?"))

count = 1
while count <= qtde:
    print("repete!")
    count += 1     
    
# %%
while True:
    
    senha = input("Entre com a senha: ")
    
    if senha == "testesinho":
        break
    
    elif senha == "teste":
        print("quase...")
        continue

    print("teste")


print("Saia!")