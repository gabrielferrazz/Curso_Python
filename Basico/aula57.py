"""
Lista dentro de lista
"""

salas = [ ['Maria', 'Helena', ],
         ['Elaine', ],
         ['Luiz', 'João', 'Eduarda',],
         ]



# print(salas[0][1])
# print(salas[2][2])
# print(salas[2][3][2])

for sala in salas:
    print(sala)
    for aluno in sala:
        print(aluno)

