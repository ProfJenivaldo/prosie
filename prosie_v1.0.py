import math

def mols(i,t):
    #Converte valores de corrente em número de mols de elétrons.
    return (i * t) / 96500

def massa(n,nox,MM):
    return (n * MM) / nox
    
def resposta_corrosao01 (n,MM,nox):
    print()
    print("Número de mols de elétrons envolvidos:","%.2f" % n,"mol(s)")
    print("Massa molar:",MM,"g/mol")
    print("Número de oxidação:",nox)
    print()
    print("Variação de massa:","%.2f" % massa(n,nox,MM),"g")
    
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
    if x == 1:
        p = -3.04
    if x == 2:
        p = -0.76
    if x == 3:
        p = 0.00
    if x == 4:
        p = 0.8
    if x == 5:
        p = 2.87
    if x == 6:
        p = -2.92
    if x == 7:
        p = -0.13
    if x == 8:
        p = 0.34
    if x == 9:
        p = 1.36
    return float(p)

def eletro_espec(x):
    if x == 1:
        e = 1
    if x == 2:
        e = 2
    if x == 3:
        e = 2
    if x == 4:
        e = 1
    if x == 5:
        e = 2
    if x == 6:
        e = 1
    if x == 7:
        e = 2
    if x == 8:
        e = 2
    if x == 9:
        e = 2
    return e

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
    if x == 1:
        c = 0.85
    if x == 2:
        c = 0.80
    if x == 3:
        c = -0.40
    if x == 4:
        c = -0.13
    if x == 5:
        c = -0.44
    if x == 6:
        c = -0.76
    if x == 7:
        c = -1.66
    if x == 8:
        c = -2.71
    if x == 9:
        c = -2.87
    return c

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
    if x == 1:
        an = 1.36
    if x == 2:
        an = 0.53
    if x == 3:
        an = 0.96
    if x == 4:
        an = 0.2
    if x == 5:
        an = 2.87
    return an

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
#Versão 0.5
print("Produzido por: Jenivaldo Lisboa")
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
    print("  [3] Corrosão") #Realiza cálculos simples de perda de massa para um determinado material escolhido - inserir opção comparativa.
    print()
    mod1 = 0
    while mod1 < 1 or mod1 > 3:
        mod1 = int(input("Digite um número: "))
    if mod1 == 1:
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
        if potencial < 0:
            print("O valor do potencial resultou em",potencial,"V, indicando que neste sentido o processo não é espontâneo e, consequentemente, representa uma eletrólise. Inverta as espécies do ânodo e do cátodo que foram selecionadas previamente e o resultado será positivo.")
        else:
            print("Potencial padrão:",potencial,"V")
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
        #Inicia o módulo para testes de corrosão.
        print()
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
