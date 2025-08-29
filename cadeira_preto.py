# O cabeçalho de um arquivo Python é uma seção no início do arquivo que geralmente contém informações sobre o arquivo, como o nome do autor, a data de criação, uma descrição do que o arquivo faz e outras informações relevantes. Ele serve para documentar o código e fornecer contexto para quem está lendo o arquivo.

# A principal diferença entre um cabeçalho e uma docstring é que o cabeçalho é geralmente colocado no início do arquivo, enquanto a docstring é usada para documentar funções, classes e módulos específicos dentro do código. A docstring fornece uma descrição mais detalhada do que uma função ou classe faz, incluindo informações sobre os parâmetros de entrada, o valor de retorno e possíveis exceções.

# Uma docstring é uma string de documentação que é usada para descrever o propósito e o comportamento de uma função, classe ou módulo. Ela é escrita entre três aspas duplas e pode ser acessada programaticamente através do atributo `__doc__`. As docstrings são uma parte importante da documentação do código Python e ajudam os desenvolvedores a entender o que cada parte do código faz.

#ajuste um cabeçalho para o arquivo e complete os exercicios abaixo
import re

def limpa_texto(s: str) -> str:
    """Deixa minúsculo e remove pontuação comum."""
    # TODO: converta s para minúsculo e remova pontuações como ,.;:!?'"()-_
    ...

def conta_vogais(s: str) -> int:
    """Conta vogais (a,e,i,o,u) em s (desconsidere acentos)."""
    # TODO: conte as vogais simples
    ...

def palindromo(s: str) -> bool:
    """Retorna True se s é palíndromo ignorando espaços e pontuação."""
    # TODO: normalizar (minúsculo, remover não alfanumérico) e comparar com o reverso
    ...

def total_por_vendedor(vendas):
    """
    vendas: lista de tuplas (nome, valor).
    Retorna: dict {nome: soma_valores}
    """
    # TODO: inicialize um dict e vá somando
    ...

def melhor_vendedor(totais: dict):
    """
    Retorna (nome, total) com o maior total.
    Se dict vazio, levante ValueError.
    """
    # TODO: encontre o par com maior total (sem ordenar a lista inteira)
    ...

