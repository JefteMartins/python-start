from abc import ABC, abstractmethod
import cv2
import os

class TreeADT(ABC):

    @abstractmethod
    def insert(self, value):
        """Insere <value> na Ã¡rvore"""
        pass

    @abstractmethod
    def empty(self):
        """Verifica se a Ã¡rvore estÃ¡ vazia"""
        pass

    @abstractmethod
    def root(self):
        """Retorna o nÃ³ raiz da Ã¡rvore"""
        pass


class Node:

    def __init__(self, data=None, parent=None, left=None, right=None):
        self._data = data
        self._parent = parent
        self._left = left
        self._right = right

    def empty(self):
        return not self._data

    def __str__(self):
        return self._data.__str__()


class BinaryTree(TreeADT):

    def __init__(self, data=None):
        self._root = Node(data)

    def empty(self):
        return not self._root._data

    def root(self):
        return self._root

    def insert(self, elem):
        node = Node(elem)
        if self.empty():
            self._root = node
        else:
            self.__insert_children(self._root, node)

    def __insert_children(self, root, node):
        if node._data <= root._data:    # modificar para o trabalho parte 2???
            if not root._left:
                root._left = node
                root._left._parent = root
            else:
                self.__insert_children(root._left, node)
        else:
            if not root._right:
                root._right = node
                root._right._parent = root
            else:
                self.__insert_children(root._right, node)

    def traversal(self, in_order=True, pre_order=False, post_order=False):
        result = list()
        if in_order:
            in_order_list = list()
            result.append(self.__in_order(self._root, in_order_list))
        else:
            result.append(None)

        if pre_order:
            pre_order_list = list()
            result.append(self.__pre_order(self._root, pre_order_list))
        else:
            result.append(None)

        if post_order:
            post_order_list = list()
            result.append(self.__post_order(self._root, post_order_list))
        else:
            result.append(None)

        return result

    def __in_order(self, root, lista):
        if not root:
            return
        self.__in_order(root._left, lista)
        lista.append(root._data)  # modificar para o trabalho parte 2???
        self.__in_order(root._right, lista)
        return lista

    def __pre_order(self, root, lista):
        if not root:
            return
        lista.append(root._data) # modificar para o trabalho parte 2???
        self.__pre_order(root._left, lista)
        self.__pre_order(root._right, lista)
        return lista

    def __post_order(self, root, lista):
        if not root:
            return
        self.__post_order(root._left, lista)
        self.__post_order(root._right, lista)
        lista.append(root._data) # modificar para o trabalho parte 2???
        return lista

    def print_binary_tree(self):
        if self._root:
            print(self.traversal(False, True, False)[1])


if __name__ == '__main__':
    listaDeImagens = list()
    print("")
    print("Lista de imagens:")
    for i in range(1,16):
        i=str(i)
        listaDeImagens.append(i+".png") #criando o nome das imagens de vai de 1 a 15 .png
    print(listaDeImagens)
    print("")
    t = BinaryTree()
    # Leitura da imagem com a função imread()
    img = cv2.imread('Images/5.png', cv2.IMREAD_UNCHANGED)
    # convert to HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    for i in range(1, 16):
        # Leitura da imagem com a função imread()
        i = str(i)
        img = cv2.imread('Images/' + i + '.png', cv2.IMREAD_UNCHANGED)
        # convert to HSV
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        h, s, v = cv2.split(hsv)
        t.insert(h[0, 0])
    print("Lista da arvore pós inserção baseada na matiz das imagens:")
    t.print_binary_tree()
    print("")
    l = t.traversal(True, True, True)
    def mostraInOrder():
        lista2 = list()
        print("Ordem das imagens da lista in order")
        print(" 'a' para imagem anterior, 'd' para imagem posterior")
        print(" 'esc' para voltar ao menu")
        for i in range(0,len(l[0])):
            lista = list(l[1]) #referencia nao mudar
            lista1 = list(l[0]) #pega a primeira lista de l que é a pre order
            posicao = str(lista.index(lista1[i]) + 1) #faço uma string com as posições da lista pre order usando a original como parametro
            lista2.append(posicao + ".png")
        print(lista2)
        print("")
    def mostraPreOrder():
        lista2 = list()
        print("Ordem das imagens da lista pre order")
        print(" 'a' para imagem anterior, 'd' para imagem posterior")
        print(" 'esc' para voltar ao menu")
        for i in range(0,len(l[1])):
            lista = list(l[1]) #referencia nao mudar
            lista1 = list(l[1])
            posicao = str(lista.index(lista1[i])+1) #faço uma string com as posições da lista pre order usando a original como parametro
            lista2.append(posicao + ".png")
        print(lista2)
        print("")
    def mostraPostOrder():
        lista2 = list()
        print("Ordem das imagens da lista post order")
        print(" 'a' para imagem anterior, 'd' para imagem posterior")
        print(" 'esc' para voltar ao menu")
        for i in range(0,len(l[2])):
            lista = list(l[1]) #referencia nao mudar
            lista1 = list(l[2])
            posicao = str(lista.index(lista1[i]) + 1)
            lista2.append(posicao + ".png")
        print(lista2)
        print("")
        return  lista2

    print("-----------AHOY MARINHEIRO!-----------")
    print("-------------aqui voce verá-----------")
    print("-----------a lista de imagens---------")
    print("---------Organizada pela matiz--------")
    print("")
    print("---'a' = para ver a lista in order----")
    print("---'s' = para ver a lista pre order---")
    print("---'d' = para ver a lista post order--")
    print("--------------------------------------")
    print("-----------'f' = para sair------------")
    print("---em seguida 'a' e 'd' para passar---")
    print("------------ou voltar ----------------")
    print("-----e 'esc' para fechar a janela-----")
    key = None
    exibe = True
    while exibe:
        print("a = in order | s = pre order | d = post order | f = sair")
        key = input("tecle: ")
        if key == 'a':
            print("")
            mostraInOrder()
            lista3 = list()
            for i in range(0, len(l[0])):
                lista = list(l[1])  # referencia nao mudar
                lista1 = list(l[0])
                posicao = str(lista.index(lista1[i]) + 1)
                lista3.append(posicao + ".png")
            apresenta = True
            key = None
            idShow = 0
            while apresenta:
                strIDShow = str(idShow)
                img = cv2.imread('Images/' + lista3[idShow], cv2.IMREAD_COLOR)
                cv2.imshow('teste', img)
                key = cv2.waitKey(2000)
                if key == 97:
                    idShow += 1
                    if idShow == len(lista3):
                        idShow = 0
                    pass
                if key == 100:
                    idShow -= 1
                    if idShow < 0:
                        idShow = len(lista3) - 1
                    pass
                if key == 27:
                    print("Encerrar programa")
                    apresenta = False
                    cv2.destroyAllWindows()
            pass

        if key == 's':
            print("")
            mostraPreOrder()
            apresenta = True
            key = None
            idShow = 1
            while apresenta:
                strIDShow = str(idShow)
                img = cv2.imread('Images/' + strIDShow + '.png', cv2.IMREAD_COLOR)
                cv2.imshow('teste', img)
                key = cv2.waitKey(2000)
                if key == 97:
                    idShow += 1
                    if idShow == 16:
                        idShow = 1
                    pass
                if key == 100:
                    idShow -= 1
                    if idShow <= 0:
                        idShow = 15
                    pass
                if key == 27:
                    print("Encerrar programa")
                    apresenta = False
                    cv2.destroyAllWindows()
            pass

        if key == 'd':
            print("")
            mostraPostOrder()
            lista4 = list()
            for i in range(0, len(l[2])):
                lista = list(l[1])  # referencia nao mudar
                lista1 = list(l[2])
                posicao = str(lista.index(lista1[i]) + 1)
                lista4.append(posicao + ".png")
            apresenta = True
            key = None
            idShow = 0
            while apresenta:
                strIDShow = str(idShow)
                img = cv2.imread('Images/' + lista4[idShow], cv2.IMREAD_COLOR)
                cv2.imshow('teste', img)
                key = cv2.waitKey(2000)
                if key == 97:
                    idShow += 1
                    if idShow == len(lista4):
                        idShow = 0
                    pass
                if key == 100:
                    idShow -= 1
                    if idShow < 0:
                        idShow = len(lista4) - 1
                    pass
                if key == 27:
                    print("Encerrar programa")
                    apresenta = False
                    cv2.destroyAllWindows()
            pass
        if key == 'f':
            exibe = False





