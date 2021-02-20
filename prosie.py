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
    print("-----------------------------------------------------------")
    print("Número de mols de elétrons envolvidos:","%.5f" % n,"mol(s)")
    print("Massa molar:",MM,"g/mol")
    print("Número de oxidação:",nox)
    print()
    print("Variação de massa:","%.5f" % massa(n,nox,MM),"g")
    print("-----------------------------------------------------------")

def resposta_nmols(dm):
    print()
    print("Número de mols:")
    print(" - Alumínio:","%.5f" % massa_mol(dm,27),"mol(s)")
    print(" - Ferro:","%.5f" % massa_mol(dm,56),"mol(s)")
    print(" - Zinco:","%.5f" % massa_mol(dm,65),"mol(s)")
    print()

def lista_especies():
    lista_ion = ("  [1] Li+/Li","  [2] Zn2+/Zn","  [3] H+/H","  [4] Ag+/Ag","  [5] F/F-","  [6] K+/K","  [7] Pb2+/Pb","  [8] Cu2+/Cu","  [9] Cl/Cl-")
    print()
    for x in lista_ion:
        print(x)
    print()
    
def potencial_padrao(x):
    plist = (-3.04, -0.76, 0.00, 0.8, 2.87, -2.92, -0.13, 0.34, 1.36)
    return float(plist[x-1])

def eletro_espec(x):
    elist = (1, 2, 2, 1, 2, 1, 2, 2, 2)
    return int(elist[x-1])

def eletro_cations():
    cat = ("  [1] Hg2+","  [2] Ag+","  [3] Cd2+","  [4] Pb2+","  [5] Fe2+","  [6] Zn2+","  [7] Al3+","  [8] Na+","  [9] Ca2+")
    print()
    print("Escolha o cátion:")
    print()
    for x in cat:
        print(x)
    print()

def potencial_cations(x):
    clist = (0.85, 0.80, -0.40, -0.13, -0.44, -0.76, -1.66, -2.71, -2.87)
    return float(clist[x-1])

def eletro_anions():
    anion = ("  [1] Cl-","  [2] I-","  [3] NO3 -","  [4] SO4 2-","  [5] F-")
    print()
    print("Escolha o ânion:")
    print()
    for y in anion:
        print(y)
    print()

def potencial_anions(x):
    anlist = (1.36, 0.53, 0.96, 0.2, 2.87)
    return float(anlist[x-1])

def resposta_tabelacom2(x,y):
    print("--------------------------------------------")
    print("Potencial do ânodo",'\t',"Potencial do cátodo")
    print("--------------------------------------------")
    print('{:>10,.2f}'.format(x),"V",'{:>22,.2f}'.format(y),"V")

def resposta_tabelacom3(x,y,z):
    print("-----------------------------------------------------------------------")
    print("Potencial do ânodo",'\t',"Potencial do cátodo",'\t',"Diferença de potencial")
    print("-----------------------------------------------------------------------")
    print('{:>10,.2f}'.format(x),"V",'{:>22,.2f}'.format(y),"V",'{:>20,.2f}'.format(z),"V")

def start():
    print("Escolha o módulo que será iniciado:")
    print()
    print("  [1] Básico")
    print("  [2] Avançado")
    print()
    a = 0
    while a < 1 or a > 2:
        a = int(input("Digite um número: "))

    #Inicia o módulo básico.
    if a == 1:
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

    #Inicia o módulo básico para cálculo do potencial de uma pilha.
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
            if potencial < 0:
                print("O valor do potencial resultou em",'{.2f}'.format(potencial),"V, indicando que neste sentido o processo não é espontâneo e, consequentemente, representa uma eletrólise. Inverta as espécies do ânodo e do cátodo que foram selecionadas previamente e o resultado será positivo.")
            else:
                resposta_tabelacom3(potencial_padrao(anodo),potencial_padrao(catodo),potencial)

    #Inicia o módulo básico de eletrólise.
        if mod1 == 2:
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

    #Realiza os cálculos para eletrólise ígnea.
            if eletro01 == 1:
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
                if potencial > 0:
                    resposta_tabelacom2(potencial_padrao(anodo),potencial_padrao(catodo))
                    print(" ")
                    print("O valor do potencial resultou em",potencial,"V, indicando que neste sentido o processo é espontâneo e, consequentemente, representa uma pilha.")
                else:
                    resposta_tabelacom3(potencial_padrao(anodo),potencial_padrao(catodo),potencial)

    #Realiza os cálculos para eletrólise aquosa.
            if eletro01 == 2:
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
                    print(" ")
                    potencial = float(potencial_cations(cation)) - float(potencial_anions(anion))                
                    if potencial > 0:
                        resposta_tabelacom2(potencial_anions(anion),potencial_cations(cation))
                        print(" ")
                        print("O valor do potencial resultou em",'{.2f}'.format(potencial),"V, indicando que neste sentido o processo é espontâneo e, consequentemente, representa uma pilha.")
                    else:
                        resposta_tabelacom3(potencial_anions(anion),potencial_cations(cation),potencial)
                if cation >= 7 and 0 < anion < 3:
                    print()
                    print("Com base nas espécies selecionadas apenas o ânion que você indicou irá descarregar, enquanto o cátion que participará da reação será o H+ (neste caso haverá a autoionização da água), seguem os dados do processo eletroquímico:")
                    print()
                    pot_cation = 0.00
                    potencial = pot_cation - float(potencial_anions(anion))
                    if potencial > 0:
                        resposta_tabelacom2(potencial_anions(anion),pot_cation)
                        print(" ")
                        print("O valor do potencial resultou em",'{.2f}'.format(potencial),"V, indicando que neste sentido o processo é espontâneo e, consequentemente, representa uma pilha.")
                    else:
                        resposta_tabelacom3(potencial_anions(anion),pot_cation,potencial)
                if 0 < cation < 7 and anion >= 3:
                    print()
                    print("Com base nas espécies selecionadas apenas o cátion que você indicou irá descarregar, enquanto o ânion que participará da reação será o OH-(neste caso haverá a autoionização da água), seguem os dados do processo eletroquímico:")
                    print()
                    pot_anion = 0.40
                    potencial = float(potencial_cations(cation)) - pot_anion
                    if potencial > 0:
                        resposta_tabelacom2(pot_anion,potencial_cations(cation))
                        print(" ")
                        print("O valor do potencial resultou em",'{.2f}'.format(potencial),"V, indicando que neste sentido o processo é espontâneo e, consequentemente, representa uma pilha.")
                    else:
                        resposta_tabelacom3(pot_anion,potencial_cations(cation),potencial)
                if cation >=7 and anion >=3:
                    pot_cation = 0.00
                    pot_anion = 0.40
                    potencial = pot_cation - pot_anion
                    print(" ")
                    print("Nenhuma das espécies selecionadas irá descarregar durante a eletrólise, havendo a participação apenas dos íons H+ (cátion) e OH- (ânion) (neste caso não necessita representar a dissociação do sal), seguem os dados do processo eletroquímico:")
                    print(" ")
                    resposta_tabelacom3(pot_anion,pot_cation,potencial)

    #Inicia o módulo para testes de variação de massa.
        if mod1 == 3:
            print()
            print("Escolha o tipo de teste:")
            print()
            print("  [1] Simples")
            print("  [2] Comparativo")
            print()
            corrosao = 0
            metais = ("  [1] Al","  [2] Fe(II)","  [3] Fe(III)","  [4] Zn")
            nox = (3,2,3,2)
            MM = (27,56,56,65)
            while corrosao < 1 or corrosao > 2:
                corrosao = int(input("Digite um número: "))
            
    #Inicia o cálculo da variação de massa em um determinado metal sob as condições de corrente elétrica (A) e tempo (s) estipulados.
            if corrosao == 1:
                print("O teste a seguir tem como objetivo avaliar a variação de massa de")
                print("um metal durante um processo eletrolítico")
                print()
                print("Escolha o metal a ser utilizado na simulação:")
                print()
                for w in metais:
                    print(w)
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
                resposta_corrosao01(n,MM[metal-1],nox[metal-1])

    #Permite realizar comparações de variação de massa, corrente elétrica e tempo em um processo de corrosão.
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
                    print()
                    for x in range(4):
                        print(metais[x],"\t","==>","\t","%.5f" % massa(n,nox[x],MM[x]),"g")

                if variavel == 2:
                    dm = float(input("Variação de massa (g): "))
                    t = int(input("Tempo (s): "))
                    resposta_nmols(dm)
                    print("Corrente elétrica:")
                    for x in range(4):
                        print(metais[x],'\t',"==>",'\t',"%.5f" % corrente(massa_mol(dm,MM[x]),nox[x],t),"A")

                if variavel == 3:
                    dm = float(input("Variação de massa: "))
                    i = int(input("Corrente elétrica (A): "))
                    resposta_nmols(dm)
                    print("Tempo:")
                    for x in range(4):
                        print(metais[x],'\t',"==>",'\t',"%.5f" % corrente(massa_mol(dm,MM[x]),nox[x],i),"s")

    #Inicia o módulo avançado.   
    if a == 2:
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
                print("O valor de potencial padrão resultou em um valor negativo (",'{.2f}'.format(potencial_pad),"V ) de modo que o processo não corresponde a uma pilha. Inverta as opções de cátodo e ânodo para que possa continuar.")
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
                print(" ")
                print("-----------------------------------------------------------------------------------")
                print("Potencial padrão",'\t',"Número de elétrons",'\t',"Quociente",'\t',"Potencial da pilha")
                print("-----------------------------------------------------------------------------------")
                print('{:>8,.2f}'.format(potencial_pad),"V",'{:>20}'.format(neletro),"mol(s)",'{:>16,.2f}'.format(quociente),'{:>20,.2f}'.format(potencial),"V")
    restart()

def restart():
    print()
    print("Deseja continuar usando o programa?")
    print()
    print(" [1] Sim;",'\n',"[2] Não.")
    reinicio = 0
    while reinicio < 1 or reinicio > 2:
        reinicio = int(input("Digite sua opção: "))
    if reinicio == 1:
        print()
        print("=====================================================================")
        print("/////////////////////////////////////////////////////////////////////")
        print("=====================================================================")
        start()
    else:
        print()
        print("=================================FIM=================================")

print()
print("     ________  ________    ________   _______    ___   ______")
print("    /  __   / /  __   /   /  __   /  /   ___/   /  /  /  ___/")
print("   /  /_/  / /  /_/  /   /  / /  /  /  /____   /  /  /  /_")
print("  /  _____/ /      _/   /  / /  /  /___    /  /  /  /  __/")
print(" /  /      /  /\  \    /  /_/  /   ___/   /  /  /  /  /___")
print("/__/      /__/  \__\  /_______/  /_______/  /__/  /______/")
print("==============================================================")
print("PROGRAMA PARA SIMULAÇÃO DE PROCESSOS ELETROQUÍMICOS")
#Versão 0.5.1
print("Produzido por: Jenivaldo Lisboa")
print()
print("Olá Mundo!!!")
print()

start()
