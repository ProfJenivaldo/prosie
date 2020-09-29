import math

def mols(i,t):
    #Converte valores de corrente em número de mols de elétrons.
    return (i * t) / 96500

def corrente(n,nox,t):
    return (n*nox*96500) / t

def tempo(n,nox,i):
    return (n*nox*96500) / i

def massa(n,nox,MM):
    return (n/nox) * MM

def massa_mol(m,MM):
    return m/MM

def resposta_corrosao01 (n,MM,nox):
    print()
    print("Número de mols de elétrons envolvidos:","%.5f" % n,"mol(s)")
    print("Massa molar:",MM,"g/mol")
    print("Número de oxidação:",nox)
    print()
    print("Variação de massa:","%.5f" % massa(n,nox,MM),"g")

def resposta_nmols(dm):
    print()
    print("Número de mols:")
    print(" - Alumínio:","%.5f" % massa_mol(dm,27),"mol(s)")
    print(" - Ferro:","%.5f" % massa_mol(dm,56),"mol(s)")
    print(" - Zinco:","%.5f" % massa_mol(dm,65),"mol(s)")
    print()

def lista_especies():
    print()
    print("  [1] Li+/Li")
    print("  [2] Zn2+/Zn")
    print("  [3] H+/H")
    print("  [4] Ag+/Ag")
    print("  [5] F/F-")
    print("  [6] K+/K")
    print("  [7] Pb2+/Pb")
    print("  [8] Cu2+/Cu")
    print("  [9] Cl/Cl-")
    print()
    
def potencial_padrao(x):
    plist = [-3.04, -0.76, 0.00, 0.8, 2.87, -2.92, -0.13, 0.34, 1.36]
    return float(plist[x-1])

def eletro_espec(x):
    elist = [1, 2, 2, 1, 2, 1, 2, 2, 2]
    return int(elist[x-1])

def eletro_cations():
    print()
    print("Escolha o cátion:")
    print()
    print("  [1] Hg2+")
    print("  [2] Ag+")
    print("  [3] Cd2+")
    print("  [4] Pb2+")
    print("  [5] Fe2+")
    print("  [6] Zn2+")
    print("  [7] Al3+")
    print("  [8] Na+")
    print("  [9] Ca2+")
    print()

def potencial_cations(x):
    clist = [0.85, 0.80, -0.40, -0.13, -0.44, -0.76, -1.66, -2.71, -2.87]
    return float(clist[x-1])

def eletro_anions():
    print()
    print("Escolha o ânion:")
    print("  [1] Cl-")
    print("  [2] I-")
    print("  [3] NO3 -")
    print("  [4] SO4 2-")
    print("  [5] F-")
    print()

def potencial_anions(x):
    anlist = [1.36, 0.53, 0.96, 0.2, 2.87]
    return float(anlist[x-1])

print()
print("==================================================================")
print("00000000   00000000     000000     00000000   000000000   00000000")
print("000000000  000000000   00000000    00000000   000000000   00000000")
print("000    00  000    00  000    000   000           000      000")
print("000   000  000   000  000    000   000           000      000")
print("00000000   00000000   000    000   00000000      000      000000")
print("0000000    0000000    000    000   00000000      000      000000")
print("000        000  000   000    000        000      000      000")
print("000        000   000  000    000        000      000      000")
print("000        000   000   00000000    00000000   000000000   00000000")
print("000        000   000    000000     00000000   000000000   00000000")
print("===================================================================")
print()
print("PROGRAMA PARA SIMULAÇÃO DE PROCESSOS ELETROQUÍMICOS")
#Versão 0.5.1
print("Produzido por: Jenivaldo Lisboa")
print()
print("Olá Mundo!!!")
print()
print("Escolha o módulo que será iniciado:")
print()
print("  [1] Básico")
print("  [2] Avançado")
print()
a = 0
while a < 1 or a > 2:
    a = int(input("Digite um número: "))
if a == 1:
    #Inicia o módulo básico.
    print()
    print("Escolha a simulação que deseja iniciar:")
    print()
    print("  [1] Pilha") #Determina a voltagem de uma pilha a partir da escolha das substâncias participantes.
    print("  [2] Eletrólise") #Apresenta os módulos ígnea e aquosa e determina o potencial e as espécies envolvidas no processo.
    print("  [3] Variação de massa") #Realiza cálculos simples de perda de massa para um determinado material escolhido - inserir opção comparativa.
    print()
    mod1 = 0
    while mod1 < 1 or mod1 > 3:
        mod1 = int(input("Digite um número: "))
    if mod1 == 1:
        #Inicia o módulo básico para cálculo do potencial de uma pilha.
        print()
        print("Escolha o ânodo:")
        print(" - A espécie que sofre oxidação.")
        lista_especies()
        anodo = 0
        while anodo < 1 or anodo > 9:
            anodo = int(input("Digite um número: "))
        print()
        print("Escolha o cátodo:")
        print(" - A espécie que sofre redução.")
        lista_especies()
        catodo = 0
        while catodo < 1 or catodo > 9:
            catodo = int(input("Digite um número: "))
        print()
        pcat = potencial_padrao(catodo)
        pand = potencial_padrao(anodo)
        potencial = float(pcat) - float(pand)
        if potencial < 0:
            print("O valor do potencial resultou em",potencial,"V, indicando que neste sentido o processo não é espontâneo e, consequentemente, representa uma eletrólise. Inverta as espécies do ânodo e do cátodo que foram selecionadas previamente e o resultado será positivo.")
        else:
            print("Potencial do ânodo", end='\t')
            print("Potencial do cátodo", end='\t')
            print("Potencial padrão")
            print('{:>10,.2f}'.format(potencial_padrao(anodo)),"V",'{:>22,.2f}'.format(potencial_padrao(catodo)),"V",'{:>20,.2f}'.format(potencial),"V")
    if mod1 == 2:
        #Inicia o módulo básico de eletrólise.
        print()
        print("Escolha o tipo de eletrólise.")
        print()
        print("  [1] Ígnea")
        print("  [2] Aquosa")
        print()
        eletro01 = 0
        while eletro01 < 1 or eletro01 > 2:
            eletro01 = int(input("Digite um número: "))
        print()
        if eletro01 == 1:
        #Realiza os cálculos para eletrólise ígnea.
            print()
            print("Escolha o ânodo:")
            print(" - A espécie que sofre oxidação.")
            lista_especies()
            anodo = 0
            while anodo < 1 or anodo > 9:
                anodo = int(input("Digite um número: "))
            print()
            print("Escolha o cátodo:")
            print(" - A espécie que sofre redução.")
            lista_especies()
            catodo = 0
            while catodo < 1 or catodo > 9:
                catodo = int(input("Digite um número: "))
            print()
            pcat = potencial_padrao(catodo)
            pand = potencial_padrao(anodo)
            potencial = float(pcat) - float(pand)
            print("Potencial do ânodo:",potencial_padrao(anodo),"V")
            print("Potencial do cátodo:",potencial_padrao(catodo),"V")
            if potencial > 0:
                print("O valor do potencial resultou em",potencial,"V, indicando que neste sentido o processo é espontâneo e, consequentemente, representa uma pilha. Inverta as espécies do ânodo e do cátodo que foram selecionadas previamente e o resultado será negativo.")
            else:
                print("Diferença de potencial:","%.2f" % potencial,"V")
        if eletro01 == 2:
        #Realiza os cálculos para eletrólise aquosa.
            eletro_cations()
            cation = 0
            while cation < 1 or cation > 9:
                cation = int(input("Digite um número: "))
            eletro_anions()
            anion = 0
            while anion < 1 or anion > 9:
                anion = int(input("Digite um número: "))
            if 0 < cation < 7 and 0 < anion < 3:
                print()
                print("Com base nas espécies selecionadas o ânion e cátion que irão descarregar durante a eletrólise serão aqueles indicados por você, seguem os dados do processo eletroquímico:")
                print()
                potencial = float(potencial_cations(cation)) - float(potencial_anions(anion))
                print("Potencial do ânodo:",potencial_anions(anion),"V.")
                print("Potencial do cátodo:",potencial_cations(cation),"V.")
                if potencial > 0:
                    print("O valor do potencial resultou em",potencial,"V, indicando que neste sentido o processo é espontâneo e, consequentemente, representa uma pilha. Inverta as espécies do ânodo e do cátodo que foram selecionadas previamente e o resultado será negativo.")
                else:
                    print("Diferença de potencial:","%.2f" % potencial,"V")
            if cation >= 7 and 0 < anion < 3:
                print()
                print("Com base nas espécies selecionadas apenas o ânion que você indicou irá descarregar, enquanto o cátion que participará da reação será o H+ (neste caso haverá a autoionização da água), seguem os dados do processo eletroquímico:")
                print()
                potencial = 0.00 - float(potencial_anions(anion))
                print("Potencial do ânodo:",potencial_anions(anion),"V.")
                print("Potencial do cátodo: 0.00 V.")
                if potencial > 0:
                    print("O valor do potencial resultou em",potencial,"V, indicando que neste sentido o processo é espontâneo e, consequentemente, representa uma pilha. Inverta as espécies do ânodo e do cátodo que foram selecionadas previamente e o resultado será negativo.")
                else:
                    print("Diferença de potencial:","%.2f" % potencial,"V")
            if 0 < cation < 7 and anion >= 3:
                print()
                print("Com base nas espécies selecionadas apenas o cátion que você indicou irá descarregar, enquanto o ânion que participará da reação será o OH-(neste caso haverá a autoionização da água), seguem os dados do processo eletroquímico:")
                print()
                potencial = float(potencial_cations(cation)) - 0.4
                print("Potencial do ânodo: 0.40 V.")
                print("Potencial do cátodo:",potencial_cations(cation),"V.")
                if potencial > 0:
                    print("O valor do potencial resultou em",potencial,"V, indicando que neste sentido o processo é espontâneo e, consequentemente, representa uma pilha. Inverta as espécies do ânodo e do cátodo que foram selecionadas previamente e o resultado será negativo.")
                else:
                    print("Diferença de potencial:","%.2f" % potencial,"V")
            if cation >=7 and anion >=3:
                print()
                print("Nenhuma das espécies selecionadas irá descarregar durante a eletrólise, havendo a participação apenas dos íons H+ (cátion) e OH- (ânion) (neste caso não necessita representar a dissociação do sal), seguem os dados do processo eletroquímico:")
                print()
                print("Potencial do ânodo: 0.4 V.")
                print("Potencial do cátodo: 0.00 V.")
                print("Diferença de potencial: - 0.40 V")
    if mod1 == 3:
        #Inicia o módulo para testes de variação de massa.
        print()
        print("Escolha o tipo de teste:")
        print()
        print("  [1] Simples")
        print("  [2] Comparativo")
        print()
        corrosao = 0
        while corrosao < 1 or corrosao > 2:
            corrosao = int(input("Digite um número: "))
        if corrosao == 1:
            print("O teste a seguir tem como objetivo avaliar a variação de massa de")
            print("um metal durante um processo eletrolítico")
            print()
            print("Escolha o metal a ser utilizado na simulação:")
            print()
            print("  [1] Alumínio")
            print("  [2] Ferro (II)")
            print("  [3] Ferro (III)")
            print("  [4] Zinco")
            print()
            metal = 0
            while metal < 1 or metal > 4:
                metal = int(input("Digite um número: "))
            print()
            print("Determine o tempo e a corrente elétrica aplicada ao sistema.")
            print()
            i = int(input("Corrente elétrica (A): "))
            t = int(input("Tempo (s): "))
            n = mols(i,t)
            if metal == 1:
                nox = 3
                MM = 27
                resposta_corrosao01(n,MM,nox)
            if metal == 2:
                nox = 2
                MM = 56
                resposta_corrosao01(n,MM,nox)
            if metal == 3:
                nox = 3
                MM = 56
                resposta_corrosao01(n,MM,nox)
            if metal == 4:
                nox = 2
                MM = 65
                resposta_corrosao01(n,MM,nox)
        if corrosao == 2:
            print("Defina a variável de comparação:")
            print()
            print("  [1] Metal") #Compara a variação de massa para diferentes metais.
            print("  [2] Corrente elétrica") #Compara a corrente elétrica relacionada a uma variação de massa em diferentes metais em um tempo determinado.
            print("  [3] Tempo") #Compara o tempo necessário para que haja uma variação de massa em diferentes metais para um dado valor de corrente elétrica.
            print()
            variavel = 0
            while variavel < 1 or variavel > 3:
                variavel = int(input("Digite um número: "))
            if variavel == 1:
                i = int(input("Corrente elétrica (A): "))
                t = int(input("Tempo (s): "))
                n = mols(i,t)
                print()
                print("Número de mols de elétrons envolvidos:","%.2f" % n,"mol(s)")
                print()
                print("Variação de massa:")
                print(" - Alumínio:","%.5f" % massa(n,3,27),"g")
                print(" - Ferro (II):","%.5f" % massa(n,2,56),"g")
                print(" - Ferro (III):","%.5f" % massa(n,3,56),"g")
                print(" - Zinco:","%.5f" % massa(n,2,65),"g")
            if variavel == 2:
                dm = float(input("Variação de massa (g): "))
                t = int(input("Tempo (s): "))
                resposta_nmols(dm)
                print("Corrente elétrica:")
                print(" - Alumínio:","%.5f" % corrente(massa_mol(dm,27),3,t),"A")
                print(" - Ferro (II):","%.5f" % corrente(massa_mol(dm,56),2,t),"A")
                print(" - Ferro (III):","%.5f" % corrente(massa_mol(dm,56),3,t),"A")
                print(" - Zinco:","%.5f" % corrente(massa_mol(dm,65),2,t),"A")
            if variavel == 3:
                dm = float(input("Variação de massa: "))
                i = int(input("Corrente elétrica (A): "))
                resposta_nmols(dm)
                print("Tempo:")
                print(" - Alumínio:","%.5f" % corrente(massa_mol(dm,27),3,i),"s")
                print(" - Ferro (II):","%.5f" % corrente(massa_mol(dm,56),2,i),"s")
                print(" - Ferro (III):","%.5f" % corrente(massa_mol(dm,56),3,i),"s")
                print(" - Zinco:","%.5f" % corrente(massa_mol(dm,65),2,i),"s")
                
if a == 2:
#Inicia o módulo avançado.
    print()
    print("Escolha a simulação que deseja iniciar:")
    print()
    print("  [1] Pilha")
    print()
    mod2 = 0
    while mod2 != 1:
        mod2 = int(input("Digite um número: "))
    print()
    if mod2 == 1:
        print()
        print("Escolha o ânodo:")
        lista_especies()
        anodo = 0
        while anodo < 1 or anodo > 9:
            anodo = int(input("Digite um número: "))
        print()
        print("Escolha o cátodo:")
        lista_especies()
        catodo = 0
        while catodo < 1 or catodo > 9:
            catodo = int(input("Digite um número: "))
        print()
        potencial_pad = potencial_padrao(catodo) - potencial_padrao(anodo)
        if potencial_pad < 0:
            print("O valor de potencial padrão resultou em um valor negativo, de modo que o processo não corresponde a uma pilha. Inverta as opções para que possa continuar.")
        else:
            temp = int(input("Temperatura (K): "))
            conc_anodo = float(input("Concentração molar do ânodo (mol/L): "))
            conc_catodo = float(input("Concentração molar do cátodo (mol/L): "))
            eano = eletro_espec(anodo)
            ecat = eletro_espec(catodo)
            if eano == 1 and ecat == 1:
                neletro = 1
                quociente = conc_anodo/conc_catodo
            if eano == 2 and ecat == 2:
                neletro = 2
                if anodo == 3:
                    quociente = (conc_anodo ** 2)/conc_catodo
                if catodo == 3:
                    quociente = conc_anodo/(conc_catodo ** 2)
                else:
                    quociente = conc_anodo/conc_catodo
            if eano == 1 and ecat == 2:
                neletro = 2
                if catodo == 3:
                    quociente = (conc_anodo ** 2)/(conc_catodo ** 2)
                else:
                    quociente = (conc_anodo ** 2)/conc_catodo
            if eano == 2 and ecat == 1:
                neletro = 2
                if anodo == 3:
                    quociente = (conc_anodo ** 2)/(conc_catodo ** 2)
                else:
                    quociente = conc_anodo/(conc_catodo ** 2)
            potencial = potencial_pad - ((8.31447 * temp)/(neletro * 96485.3))*math.log(quociente)
            print("Potencial padrão:",potencial_pad,"V")
            print("Número de mols de elétrons:",neletro,"mol(s)")
            print("Quociente:", "%.2f" % quociente)
            print()
            print("Potencial da pilha:", "%.2f" % potencial,"V")
