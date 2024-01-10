
print("Olá, bem vindo a biblioteca virtual, segue abaixo a lista de ações possíveis")
print("0 – cadastrar livro")
print("1 – cadastrar usuário")
print("2 – consultar acervo")
print("3 – alugar livro")
print("4 – retornar livro")
print("9 – sair da aplicação")



listaDeLivros = []
listaDeCodigos = []
listaDeLivrosFinal = []
"""Biblioteca"""
class biblioteca:
    codigo = 0
    def __init__(self,nome,codigo):
        self.nome = nome
        self.codigo = codigo
    def setLivro(self,nome):
        self.nome = nome
        self.codigo = self.codigo +1
        listaDeLivros.append(self.nome)
        listaDeLivrosFinal.append(self.nome) #lista pra nao ser alterada
        listaDeCodigos.append(self.codigo)
    def listaDeLivros():
        print(listaDeLivros)
        
"""Pessoas"""
listaDeAlunos = []
matriculaDeAlunos = []
listaDeProfessores = []
matriculaDeProfessores = []
listaDeAlunosPendentes = []
listaDeProfessoresPendentes = []
class Aluno:
    aluguel=0
    def __init__ (self,nome,matricula):
        self.nome = nome
        self.matricula = matricula
    def setInfo(self,nome,matricula):
        self.nome = nome
        self.matricula = matricula
        listaDeAlunos.append(self.nome)
        matriculaDeAlunos.append(self.matricula)
class Professor:
    aluguel=0;
    def __init__ (self,nome,matricula):
        self.nome = nome
        self.matricula = matricula
    def setInfo(self,nome,matricula):
        self.nome = nome
        self.matricula = matricula
        listaDeProfessores.append(self.nome)
        matriculaDeProfessores.append(self.matricula)

"""começa biblioteca"""
biblioteca = biblioteca("nome",0)
"""começo aluno"""
aluno = Aluno("doido",0)
"""começo profeessores"""
professor = Professor("doido",0)

escolha = int(input("Pressione sua ação: "))



while(escolha<10):
    if(escolha == 0):
        novoLivro = input("Adicione um livro a biblioteca: ")
        biblioteca.setLivro(novoLivro)
    escolha = int(input("Pressione sua ação: "))
    if(escolha == 1):
        pessoinha = int(input("Caso seja aluno digite 1. Caso seja professor digite 2: "))
        if(pessoinha==1):
            nomeDoCoiso = input("Cadastre seu nome: ")
            matriculaDoCoiso = int(input("Digite a sua matricula: "))
            if (matriculaDoCoiso not in matriculaDeAlunos):
                aluno.setInfo(input("Digite seu nome para confirmar: "),int(input("Digite sua matricula para confirmar: ")))
            else:
                print("Matricula ja existente")

        if(pessoinha==2):
            nomeDoCoiso = input("Cadastre seu nome: ")
            matriculaDoCoiso = int(input("Digite a sua matricula: "))
            if (matriculaDoCoiso not in matriculaDeProfessores):
                professor.setInfo(input("Digite seu nome para confirmar: "),int(input("Digite sua matricula para confirmar: ")))

            else:
                print("Matricula ja existente")
    escolha = int(input("Pressione sua ação: "))
    if(escolha == 2):
        for i in range(len(listaDeLivros)):
               print("Nome do livro disponível: ",listaDeLivros[i])
               print("Código: ",listaDeCodigos[i])
    escolha = int(input("Pressione sua ação: "))
    if(escolha == 3):
        for i in range(len(listaDeLivros)):
               print("Nome do livro disponível: ",listaDeLivros[i])
               print("Código: ",listaDeCodigos[i])
  
        print("Código: ",listaDeCodigos[i])
        checando = int(input("Caso seja aluno digite 1. Caso seja professor digite 2: "))
        if(checando == 1):
            print("Aluno, digite sua matrícula")
            check = int(input("Matrícula:"))
            if(check in listaDeAlunosPendentes):
                print("você tem livros pendentes")
                
            if(check not in listaDeAlunosPendentes):            
                if(check in matriculaDeAlunos):
                        escolhaDoLivro = int(input("Escolha seu livro usando o codigo: "))
                        if(listaDeLivros[escolhaDoLivro-1]=='ALUGADO'):
                            print("Livro não disponível")
                        else:
                            if(escolhaDoLivro in listaDeCodigos):
                                print("livro alugado: ",listaDeLivros[escolhaDoLivro-1])
                                listaDeLivros.pop(escolhaDoLivro-1)
                                listaDeLivros.insert(escolhaDoLivro-1,"ALUGADO")
                                listaDeAlunosPendentes.append(check)
        if(checando == 2):
            print("Professor, digite sua matrícula")
            check = int(input("Matrícula:"))
            if(check in listaDeProfessoresPendentes):
                print("você tem livros pendentes")
            if(check in matriculaDeProfessores):
                    escolhaDoLivro = int(input("Escolha seu livro usando o codigo: "))
                    if(listaDeLivros[escolhaDoLivro-1]=='ALUGADO'):
                        print("Livro não disponível")
                    else:
                        if(escolhaDoLivro in listaDeCodigos):
                            print("livro alugado: ",listaDeLivros[escolhaDoLivro-1])
                            listaDeLivros.pop(escolhaDoLivro-1)
                            listaDeLivros.insert(escolhaDoLivro-1,"ALUGADO")
                            listaDeProfessoresPendentes.append(check)
    escolha = int(input("Pressione sua ação: "))
    if(escolha == 4):
        devolver = int(input("Caso seja aluno digite 1. Caso seja professor digite 2: "))
        if(devolver==1):
            matricula = int(input("Digite sua matrícula: "))
            if(matricula not in listaDeAlunosPendentes):
                print("Você não tem livros pendentes")
            if(matricula in listaDeAlunosPendentes):
                livrao = int(input("Digite a matrícula do livro que quer devolver: "))
                nomeDoLivrao = input("digite o nome do livro que quer devolver: ")
                listaDeLivros.pop(livrao-1)
                listaDeLivros.insert(livrao-1,nomeDoLivrao)
                listaDeAlunosPendentes.remove(matricula)
        if(devolver==2):
            matricula = int(input("Digite sua matrícula: "))
            if(matricula not in listaDeProfessoresPendentes):
                print("Você não tem livros pendentes")
            if(matricula in listaDeProfessoresPendentes):
                livrao = int(input("Digite a matrícula do livro que quer devolver: "))
                nomeDoLivrao = input("digite o nome do livro que quer devolver: ")
                listaDeLivros.pop(livrao-1)
                listaDeLivros.insert(livrao-1,nomeDoLivrao)
                listaDeProfessoresPendentes.remove(matricula)
                    
                    
    if(escolha == 9):
        print("Obrigado por usar a nossa biblioteca!")
        break
                        
    escolha = int(input("Pressione sua ação: "))
        
        
