def remove_elements(list_to_remove_elements):
    lista = list_to_remove_elements
    if len(lista) > 5: # aca me fijo si es teiene 6 elelementos
        del lista [5] # elimino el 6to elemento si lo tiene
    if len(lista) > 4: # aca me fijo si es tiene 5 elelementos
        del lista [4] # elimino el 6to elemento si lo tiene
    if len(lista) > 0: 
        del lista [0] # elimino el 1er elemento si lo tiene
    return lista

def add_elements(list_to_add_elements):
    lista=list_to_add_elements
    lista.insert(0,'Pink')
    lista.append('Yellow')
    return lista  

def is_empty(list_to_check):
    return len(list_to_check) == 0

def check_lists(list_to_compare1, list_to_compare2):
    lista_1=list_to_compare1
    lista_2=list_to_compare2
    if len(lista_1) < 3 or len(lista_2) < 3:
        return False
    elif lista_1[2] == lista_2[2]:
        return True
    else: 
        return False
    return "ANSWER HERE" 


def list_of_lists(list_of_lists_to_modify):
    list_1=list_of_lists_to_modify
    list_1[0]= list_1[0][:2]
    list_1[1]= list_1[1][1:4]
    list_1[2]= list_1[2][-2:]
    return list_1  
