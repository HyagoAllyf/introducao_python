"""
Documentando funções com Docstrings
"""

# Exemplos

def diz_oi():
    """
    Uma função simples que retorna a string 'Oi!'
    """
    return 'Oi!'

def exponencial(numero, potencia=2):
    """
    Função que retorn por padrão o quadrado de 'numero' ou 'numero' à 'potencia' informada.

    : param numero: base
    : param potencia: expoente
    : return: base^expoente
    """
    return numero ** potencia