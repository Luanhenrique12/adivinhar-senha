import itertools
import string
import multiprocessing

def tentativa_senha(senha_alvo, combinacoes):
    for combinacao in combinacoes:
        tentativa = "".join(combinacao)
        if tentativa == senha_alvo:
            return tentativa
    return None

def adivinhar_senha_paralelo(senha_alvo):
    caracteres = string.ascii_lowercase + string.digits
    max_comprimento = len(senha_alvo)
    num_processos = multiprocessing.cpu_count()

    print(f"Tentando adivinhar a senha '{senha_alvo}' com {num_processos} núcleos...")

    for comprimento in range(1, max_comprimento + 1):
        combinacoes = list(itertools.product(caracteres, repeat=comprimento))

        # Divide a lista de combinações entre os processos
        chunks = [combinacoes[i::num_processos] for i in range(num_processos)]

        with multiprocessing.Pool(num_processos) as pool:
            resultados = pool.starmap(tentativa_senha, [(senha_alvo, chunk) for chunk in chunks])

        for resultado in resultados:
            if resultado:
                print(f"\n🎉 Senha encontrada! A senha é: {resultado}")
                return True

    print("\nSenha não encontrada neste conjunto.")
    return False

# Exemplo de uso
if __name__ == "__main__":
    senha_para_tentar = "pgfiu2"
    adivinhar_senha_paralelo(senha_para_tentar)
