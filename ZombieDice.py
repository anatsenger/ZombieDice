import random
from random import shuffle

#ALUNA: Ana Thais Senger
#CURSO: TECNOLOGIA EM ANÁLISE E DESENVOLVIMENTO DE SISTEMAS.
    
#Criando as informações
dado_verde = ("C","P","C","T","P","C")
dado_amarelo = ("T","P","C","T","P","C")
dado_vermelho = ("T","P","T","C","P","T")

cerebrosJogadores = []
def initCerebrosJogadores(novaPontuacao):
    cerebrosJogadores.append(novaPontuacao)

tirosJogadores = []
def initTirosJogadores(novaPontuacao):
    tirosJogadores.append(novaPontuacao)

passosJogadores = []
def initPassosJogadores(novaPontuacao):
    passosJogadores.append(novaPontuacao)

nome_jogadores=[]
def addJogador(jogador):
    nome_jogadores.append(jogador)

def getVencedor(pontuacoes):
    vencedor="Ninguem"
    pontuacaoVencedor = 13
    for i in range(0, len(pontuacoes)):
        if pontuacoes[i] < pontuacaoVencedor:
            vencedor = vencedor
        else:
            vencedor = getNomeJogador(i)
            pontuacaoVencedor = pontuacoes[i]
    return vencedor

def verificaSeJogoNaoTerminou(pontuacoes):
    print("A pontuação dos Zombies é " + str(pontuacoes))
    jogoNaoTerminou = True

    for i in range(0, len(pontuacoes)):
        if pontuacoes[i] < 13:
            jogoNaoTerminou = True
        else:
            jogoNaoTerminou = False
            break
    return jogoNaoTerminou

def verificaEmpate(pontuacoes):
    maiorPontuacao = 0
    maiorPontuacaoOcorrencia = 0
    empate = False

    if (verificaSeJogoNaoTerminou == False):
        for i in range(0, len(pontuacoes)):
            if pontuacoes[i] > maiorPontuacao:
                maiorPontuacao = pontuacoes[i]

        for i in range(0, len(pontuacoes)):
            if pontuacoes[i] == maiorPontuacao:
                maiorPontuacaoOcorrencia += 1
        
        if(maiorPontuacaoOcorrencia >= 2):
            print("O jogo empatou, portanto os Zombies devem jogar mais um turno")
            empate = True

    return empate

def resetCerebrosJogador(posJogador):
    cerebrosJogadores[posJogador] = 0

def addCerebrosJogador(posJogador):
    cerebros = cerebrosJogadores[posJogador] + 1
    cerebrosJogadores[posJogador] = cerebros

def getCerebrosJogador(posJogador):
    return cerebrosJogadores[posJogador]

def addTirosJogador(posJogador):
    tiros = tirosJogadores[posJogador] + 1
    tirosJogadores[posJogador] = tiros

def getTirosJogador(posJogador):
    return tirosJogadores[posJogador]

def resetTirosJogador(posJogador):
    tirosJogadores[posJogador] = 0

def addPassosJogador(posJogador):
    passos = passosJogadores[posJogador] + 1
    passosJogadores[posJogador] = passos

def getPassosJogador(posJogador):
    return passosJogadores[posJogador]

def resetPassosJogador(posJogador):
    passosJogadores[posJogador] = 0

def getNomeJogador(posJogador):
    return nome_jogadores[posJogador]

def getDadoSorteado(lista):
    shuffle(lista)
    return (random.choice(lista))

def removeDadoSorteadoDoCopo(dadoSorteado):
    lista.remove(dadoSorteado) 

def mostraCorDadoSorteado(pos, corDado):
    print("A cor do dado " + str(pos+1) + " foi: " + corDado) 

def mostraFaceDadoSorteado(pos, faceDado):
    print ("A face do dado " + str(pos+1) + " foi: " + faceDado)

def setCorDadoSorteado(cor):
    corDado = ''
    if cor=="dado_verde":
        corDado = "verde"
    elif cor=="dado_amarelo":
        corDado = "amarelo"
    elif cor=="dado_vermelho":
        corDado = "vermelho"
    return corDado

def setFaceDadoSorteado(cor):
    faceDado = ''
    if cor=="verde":
        faceDado = (random.choice(dado_verde))
    elif cor=="amarelo":
        faceDado = (random.choice(dado_amarelo))
    else:
        faceDado = (random.choice(dado_vermelho))
    return faceDado

lista=[]
def setDadosCopo(dadosCopo):
    for i in range(0, len(dadosCopo)):
        lista.append(dadosCopo[i])

def mostraDadosCopo(lista):
    print(lista)

def perguntaJogadorDesejaContinuarRodada(posJogador):
    print("=" * 80)
    print("O Zombie " + getNomeJogador(posJogador) + " possui " + str(getCerebrosJogador(posJogador)) + " cérebros")
    print("O Zombie " + getNomeJogador(posJogador) + " tomou " + str(getTirosJogador(posJogador)) + " tiros")
    print("=" * 80)
    return input("Jogador " + getNomeJogador(posJogador) + " deseja continuar a rodada? (s/n)")

print("|-----------------------------------------------------------------------------|")
print("|-------------------------------Zombie Dice-----------------------------------|")
print("|--------------------Seja bem-vindo ao jogo Zombie Dice!----------------------|")
print("|-----------------------------------------------------------------------------|")

setDadosCopo(["dado_verde", "dado_verde","dado_verde","dado_verde","dado_verde","dado_verde","dado_amarelo","dado_amarelo","dado_amarelo","dado_amarelo" ,"dado_vermelho","dado_vermelho","dado_vermelho"])

#Criando a quantidade de jogadores e verificando
numero_jogadores=int(input("Digite o número de Zombies jogando hoje: "))

while numero_jogadores < 2:
   print(" Aviso: O número mínimo para o jogo é de pelo menos 2 Zombies")
   numero_jogadores=int(input("Digite o número de Zombies: "))

#Adicionando o nome dos jogadores, de acordo com o número
if numero_jogadores>=2:  
    lista_nomes =[]  
    
    for i in range (numero_jogadores):
        nome=input("Digite o nome do Zombie: ")
        addJogador(nome)
        initCerebrosJogadores(0)
        initTirosJogadores(0)
        initPassosJogadores(0)

    print("Os nomes dos Zombies são: "+ str(nome_jogadores))


print("|-----------------------------------------------------------------------------|")
print("|---------------------------INICIANDO O JOGO----------------------------------|")
print("|-----------------------------------------------------------------------------|")

#Escolhendo quem começa o jogo
print("O jogador que falar cééééérebros da maneira mais zumbi poaaível, começa a jogar")
inicio=input("|                       [PRESS ENTER PARA INICIAR]                            |")
print("|-----------------------------------------------------------------------------|")
#O primeiro jogador deve iniciar

dadosSorteados=[]
while verificaSeJogoNaoTerminou(cerebrosJogadores) or verificaEmpate(cerebrosJogadores):

    #sorteio dos dados com suas respectivas faces e remoção dos dados já sorteados
    for i in range (0, numero_jogadores):
        rodadaCerebros = 0
        rejoga = True
        lista = lista + dadosSorteados
        dadosSorteados=[]
        print(getNomeJogador(i) + ", agite o tubo e pegue 3 dados, sem olhar e jogue os dados")

        while(rejoga):
            mostraDadosCopo(lista)
            for j in range (0,3 - rodadaCerebros):
                if (len(lista) == 0):
                    resetPassosJogador(i)
                    resetTirosJogador(i)
                    rejoga = False
                    break

                dadoSorteados=getDadoSorteado(lista)
                dadosSorteados.append(dadoSorteados)
                removeDadoSorteadoDoCopo(dadoSorteados) 

                corDado = setCorDadoSorteado(dadoSorteados)
                mostraCorDadoSorteado(j, corDado)

                faces_dado = setFaceDadoSorteado(dadoSorteados)
                mostraFaceDadoSorteado(j, faces_dado)

                if faces_dado== "C":
                    rodadaCerebros += 1
                    addCerebrosJogador(i)
                elif faces_dado=="T":
                    addTirosJogador(i)
                elif faces_dado=="P":
                    addPassosJogador(i)

            if (getTirosJogador(i) >= 3):
                print("O Zombie " + getNomeJogador(i) + " tomou 3 tiros e perdeu todos os cérebros")
                resetPassosJogador(i)
                resetTirosJogador(i)
                resetCerebrosJogador(i)
                print("=" * 80)
                rejoga = False
                break

            if (getPassosJogador(i) == 0):
                print("O Zombie " + getNomeJogador(i) + " não pegou nenhum dado com face de passos, portanto passa vez")
                resetTirosJogador(i)
                print("=" * 80)
                rejoga = False
                break
            
            resetPassosJogador(i)

            desejaRejogar = perguntaJogadorDesejaContinuarRodada(i)
            if (desejaRejogar != "s"):
                resetTirosJogador(i)
                rejoga = False

            if(rejoga == True):
                print("|--------O jogador " + getNomeJogador(i) + " irá rejogar--------|")

print("=" * 80)
print("O vencedor foi o Zombie " + getVencedor(cerebrosJogadores))
print("=" * 80)
print("|-------------------------------FIM DE JOGO----------------------------|")