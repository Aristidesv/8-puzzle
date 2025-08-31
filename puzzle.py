import os

# Estado final desejado
estado_objetivo = [[1,2,3],
                   [4,5,6],
                   [7,8,'_']]

# Movimentos 
movimentos = {
    'CIMA': (-1, 0),
    'BAIXO': (1, 0),
    'ESQUERDA': (0, -1),
    'DIREITA': (0, 1)
}

def imprimir_tabuleiro(tabuleiro):
    os.system("clear")  
    for linha in tabuleiro:
        print(linha)
    print()

def encontrar_vazio(tabuleiro):
    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] == '_':
                return i, j

def movimentos_validos(tabuleiro):
    i, j = encontrar_vazio(tabuleiro)
    possiveis = []
    for mov, (di, dj) in movimentos.items():
        novo_i, novo_j = i + di, j + dj
        if 0 <= novo_i < 3 and 0 <= novo_j < 3:
            possiveis.append(mov)
    return possiveis

def aplicar_movimento(tabuleiro, mov):
    i, j = encontrar_vazio(tabuleiro)
    di, dj = movimentos[mov]
    novo_i, novo_j = i + di, j + dj
    novo_tabuleiro = [linha[:] for linha in tabuleiro]
    novo_tabuleiro[i][j], novo_tabuleiro[novo_i][novo_j] = novo_tabuleiro[novo_i][novo_j], novo_tabuleiro[i][j]
    return novo_tabuleiro

def objetivo_alcancado(tabuleiro):
    return tabuleiro == estado_objetivo

# Jogo
def jogar():
    historico = []
    # Estado incial embaralhado
    estado = [[1,2,3],[4,6,'_'],[7,5,8]]
    
    while True:
        imprimir_tabuleiro(estado)
        
        for idx, t in enumerate(historico):
            print(f"Passo {idx+1}:")
            for linha in t:
                print(linha)
            print()
        
        if objetivo_alcancado(estado):
            print("Parabens!venceu!")
            break

        mov = input("Movimento (CIMA, BAIXO, ESQUERDA, DIREITA): ").upper()
        if mov in movimentos_validos(estado):
            #historico.append([linha[:] for linha in estado])  # salva estado anterior
            estado = aplicar_movimento(estado, mov)
        else:
            print("Movimento invalido!")

if __name__ == "__main__":
    jogar()
