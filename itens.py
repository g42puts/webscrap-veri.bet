import ast
from format_datetime import get_formated_datetime

def get_itens(content) -> list:

    itens = []
    for item in content:
        # Usar split para separar o índice do conteúdo entre colchetes
        partes = item.split(sep=': ')

        if len(partes) == 2:

            # Usar ast.literal_eval para analisar a lista interna com segurança
            lista_interna = ast.literal_eval(node_or_string=partes[1])
            itens.append(lista_interna)
    
    return itens

def get_item(itens) -> list[str]:

    item = [' '.join(x) for x in itens]

    # retira o ODDS do period
    item[0] = ' '.join(item[0].split()[:2])
    item[13] = get_formated_datetime(item=item[13])
    
    return item

def get_value_list(itens) -> list:
    # obtem lista dos valores referente aos dados ML, SPREAD e TOTAL
    values = itens[5:8] + itens[9:12]

    # retira os paranteses da list de spreads
    value_list = [[item.replace('(', '').replace(')', '') for item in sublista] for sublista in values]

    # faz a remoção dos caracteres 'U' e 'O' dentro da value_list
    for x in value_list:
        if 'U' in x:
            x.remove('U')
        if 'O' in x:
            x.remove('O')
    return value_list