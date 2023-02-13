# https://pythonaplicado.com/leer/capitulo-12/manipulacion-de-listas-y-tuplas


# método append
nombres_masculinos = ["Alvaro", "Jacinto", "Miguel", "Edgardo", "David"] 
nombres_masculinos.append("Jose") 
print(nombres_masculinos)

# metodo extend(outr_list)
nombres_masculinos.extend(["Jose", "Gerardo"]) 
print(nombres_masculinos)

# inserir um elemento numa posicao determinada
# metodo pop()
# retorno: o elemtno eliminado
print(nombres_masculinos.pop(3))

# elimina um elemento pelo seu valor
# metodo: .remove("valor")
nombres_masculinos.remove("Jose")
print(nombres_masculinos)

