class No:
    def __init__(self,chave=None,valor=None,direita=None,esquerda=None):
        self.chave = chave
        self.valor = valor
        self.direita = direita
        self.esquerda = esquerda

class Arvore:
    def __init__(self):
        self.raiz = None
    def vazia(self):
        return self.raiz == None
    def inserir(self,self.raiz,chave,valor):
        nodo = self.raiz
        if self.vazia():
            nodo = No(chave,valor)
            return
        if nodo.valor > valor:
            nodo.direita  = inserir(nodo.direita,chave,valor)
        if nodo.valor < valor:
            nodo.esquerda = inserir(nodo.esquerda,chave,valor)
        else:
            nodo.valor = valor
        return nodo
