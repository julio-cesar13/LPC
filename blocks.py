def blocks(num_arena):
    doc = open(f"templates/arena_{num_arena}", "r")
    lista = doc.readlines()
    lista_cor = []

    for i in range(26):
        for j in range(38):
            if lista[i][j] == 'X' or lista[i][j] == 'x':
                lista_cor.append((i + 1, j + 1))
    return lista_cor
