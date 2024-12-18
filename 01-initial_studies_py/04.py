# %%
note = 7.75
notes = []

notes.append(note)
print(notes)

notes.append(10)
print(notes)

notes.extend([5.75, 6.24])
print(notes)

notes = notes + [10, 9.25]
print(notes)

notes.remove(10)
print(notes)

# %%
names = ("Lucas", "Martina", "Pitica", "Gatona")
print(names)

# %%
data =  {"name":"Lucas",
         "lastname":"Sosa",
         "age":28,
         "cats":[ {"name":"Pitica", "idade":1},
                  {"name":"Gatona", "idade":2}]
         }

name = data["name"]
print(name)

print(data.keys())
print(data.values())
print(data.items())
