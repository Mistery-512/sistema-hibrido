import secrets
import string

def gerar_senha_completa(tamanho=12):
    # Verifica se o tamanho é válido
    if not isinstance(tamanho, int) or tamanho < 5:
        return "O tamanho deve ser um número inteiro maior ou igual a 5."

    # Conjuntos de caracteres
    letras_maiusculas = string.ascii_uppercase
    letras_minusculas = string.ascii_lowercase
    numeros = string.digits
    simbolos = "!@#$%&*()-/[]{},.+*<>;:?="

    # Garante pelo menos um de cada tipo
    senha = [
        secrets.choice(letras_maiusculas),
        secrets.choice(letras_minusculas),
        secrets.choice(numeros),
        secrets.choice(simbolos),
    ]

    # Preenche o restante da senha com caracteres aleatórios
    caracteres_disponiveis = letras_maiusculas + letras_minusculas + numeros + simbolos
    senha += [secrets.choice(caracteres_disponiveis) for _ in range(tamanho - 4)]

    # Embaralha a senha
    secrets.SystemRandom().shuffle(senha)

    return ''.join(senha)

# Testando a função
senha_completa = gerar_senha_completa(12)
print("Senha gerada (completa):", senha_completa)