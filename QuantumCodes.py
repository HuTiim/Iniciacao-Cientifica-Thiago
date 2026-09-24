
import numpy as np
# import qutip as qt
import matplotlib.pyplot as plt
from qutip import *



#Definindo as idéias
# Qobj() = Ket
# x=np.array() , Qobj(x) = Bra
#Basis() , .dag()



#Entendendo{
#Conceito Bra
#Bra0=np.array([[1,0]])
#Bra1=np.array([[0,1]])
#print("Bra |0> \n", Qobj(Bra0), "\n Bra|1> \n", Qobj(Bra1), "\n")

#Conceito Matriz
#m=np.random.rand(4,4) (aleatória)
#print(Qobj(m))
#qeye() , identidade


#}




#                                      ------ Exercícios Iniciação Científica ------


#---------------------------------------------------------------------------

print("Questão 1  Gerar os Kets |0> e |1>")


Ket0=(Qobj([[1],[0]]))

Ket1=(Qobj([[0],[1]]))

print("Ket |0> \n" , Ket0, "\n Ket |1> \n", Ket1)

ket0 = basis(2,0)

print("Ket |0>",ket0)

ket1 = basis(2,1)

print("Ket |1>",ket1)

print("---------------------------------------------")

#---------------------------------------------------------------------------

print("Questão 2 Fazer os produtos internos <0|0>, <0|1>, <1|0> e <1,1>")

pi0e0 = ket0.dag() * ket0
pi0e1 = ket0.dag() * ket1
pi1e0 = ket1.dag() * ket0
pi1e1 = ket1.dag() * ket1

print("Produto Interno <0|0>\n", pi0e0)
print("Produto Interno <0|1>\n", pi0e1)
print("Produto Interno <1|0>\n", pi1e0)
print("Produto Interno <1|1>\n", pi1e1)

# print(ket0 * ket0).unit()

print("---------------------------------------------")
#---------------------------------------------------------------------------

print("Questão 3 Fazer os produtos externos  |0x0| , |0x1|, |1x0| e |1x1|")

pe0x0=ket2dm(ket0)
pe01x01=ket0 * ket1.dag()
pe10x10=ket1 * ket0.dag()
pe11x11=ket2dm(ket1)

print("Produto Externo |0x0|\n", pe0x0)
print("Produto Externo |0x1|\n", pe01x01)
print("Produto Externo |1x0|\n", pe10x10)
print("Produto Externo |1x1|\n", pe11x11)

print("---------------------------------------------")
#---------------------------------------------------------------------------

print("Questão 4 Construir matriz densidade para os diferentes casos")

md0e01=pe0x0 + pe01x01
md0e10=pe0x0 + pe10x10
md0e11=pe0x0 + pe11x11

md01e10=pe01x01 + pe10x10
md01e11=pe01x01 + pe11x11

md10e11=pe10x10 + pe11x11


print("Matriz densidade |0x0| + |0x1|\n", md0e01)
print("Matriz densidade |0x0| + |1x0|\n", md0e10)
print("Matriz densidade |0x0| + |1x1|\n", md0e11)
print("Matriz densidade |0x1| + |1x0|\n", md01e10)
print("Matriz densidade |0x1| + |1x1|\n", md01e11)
print("Matriz densidade |1x0| + |1x1|\n", md10e11)




print("---------------------------------------------")
#---------------------------------------------------------------------------

print("Questão 5 Criar os Kets |00>, |01>, |10> e |11> no qutip")

zerozero=tensor(ket0,ket0)
zeroum=tensor(ket0,ket1)
umzero=tensor(ket1,ket0)
umum=tensor(ket1,ket1)

print("|00>\n", zerozero)
print("|01>\n", zeroum)
print("|10>\n", umzero)
print("|11>\n", umum)



print("---------------------------------------------")
#---------------------------------------------------------------------------

print("Questão 6 Calcular os produtos internos")

pi00=zerozero.dag() * zerozero
pi01=zeroum.dag() * zeroum
pi10=umzero.dag() * umzero
pi11=umum.dag() * umum

print("Produto Interno |00>\n", pi00)
print("Produto Interno |01>\n", pi01)
print("Produto Interno |10>\n", pi10)
print("Produto Interno |11>\n", pi11)

print("---------------------------------------------")
#---------------------------------------------------------------------------

print("Questão 7 Calcular os produtos externo")

pe00e00=ket2dm(zerozero)
pe01e01=ket2dm(zeroum)
pe10e10=ket2dm(umzero)
pe11e11=ket2dm(umum)

print("Produto Externo |00>\n",pe00e00)
print("Produto Externo |01>\n",pe01e01)
print("Produto Externo |10>\n",pe10e10)
print("Produto Externo |11>\n",pe11e11)

print("---------------------------------------------")
#---------------------------------------------------------------------------

print("Questão 8 Construir matriz densidade de exemplo")

mdzzzu=ket2dm(zerozero) + ket2dm(zeroum)
mdzzuz=ket2dm(zerozero) + ket2dm(umzero)
mdzzuu=ket2dm(zerozero) + ket2dm(umum)

mdzuuz=ket2dm(zeroum) + ket2dm(umzero)
mdzuuu=ket2dm(zeroum) + ket2dm(umum)

mduzuu=ket2dm(umzero) + ket2dm(umum)

print("Matriz densidade |00> + |01>\n", mdzzzu)
print("Matriz densidade |00> + |10>\n", mdzzuz)
print("Matriz densidade |00> + |11>\n", mdzzuu)
print("Matriz densidade |01> + |10>\n", mdzuuz)
print("Matriz densidade |01> + |11>\n", mdzuuu)
print("Matriz densidade |10> + |11>\n", mduzuu)

print("---------------------------------------------")
#---------------------------------------------------------------------------


print("Questão 9 gerar as matrizes de pauli, matriz identidade sigma mais e sigma menos")

print("Matriz de pauli x\n",sigmax(), "\n Matriz de pauli y\n",sigmay(), "\n Matriz de pauli z\n",sigmaz(), "\n Matriz de pauli -\n",sigmam(), "Matriz de pauli +", sigmap())
print("\n Matriz Identidade", identity(2))

print("---------------------------------------------")
#---------------------------------------------------------------------------

print("Questão 10 Fazer o produto tensorial dessas varias matrizes SigmaX, SigmaY, SigmaZ, SigmaP, SigmaM e Sigma0")

dic = {'sx': sigmax(), 'sy': sigmay(), 'sz': sigmaz(), 'I': qeye(2), 'sp': sigmap(), 'sm': sigmam()}

for i in dic:
    for j in dic:
        print(i+'*'+j+'=', tensor(dic.get(i), dic.get(j)))
        print(50*"=")


print("---------------------------------------------")
#---------------------------------------------------------------------------

print("Questão 11 Calcular os Tr(SIGMAiSIGMAj)")


for i in dic:
    for j in dic:
        if i==j:
            print("Tr("+i+"*"+j+")=", (dic.get(i) @ dic.get(j)).ptrace(0))
            print(50*"=")
        else:
            print("Tr("+i+"*"+j+")=", (dic.get(i) @ dic.get(j)).ptrace(0))
            print(50*"=")
            
print("---------------------------------------------")
#---------------------------------------------------------------------------

print("Questão 12 Calcular Tr((SigmaI x SigmaJ)(SigmaL x SigmaN)) para todas as combinações possíveis de i=(x,y,z,0) onde 0 = matriz identidade.")

for i in dic:
    for j in dic:
        for L in dic:
            for N in dic:
                print("Tr("+"("+i+"X"+j+")"+"*"+"("+L+"X"+N+")"+")", (tensor(dic.get(i), dic.get(j)) @ tensor(dic.get(L), dic.get(N))).ptrace(0))
                print(50*"=")
                
print(50*"-")
#-----------------------------------------------------------------------------------
print("Extra (Sigmai X I) * |00>")

for i in dic:
    print(i,"X",qeye(2),")","*", "|00>", tensor(dic.get(i), qeye(2)) @ zerozero)
    print(50*"=")

print(50*"-")
#-----------------------------------------------------------------------------------

print("Extra (Sigmai X I) * |01>")

for i in dic:
    print(i,"X",qeye(2),")","*", "|01>", tensor(dic.get(i), qeye(2)) @ zeroum)
    print(50*"=")

print(50*"-")
#-----------------------------------------------------------------------------------

print("Extra (Sigmai X I) * |11>")

for i in dic:
    print(i,"X",qeye(2),")","*", "|11>", tensor(dic.get(i), qeye(2)) @ umum)
    print(50*"=")

print(50*"-")
#-----------------------------------------------------------------------------------

print("Extra (Sigmai X I) * |10>")

for i in dic:
    print(i,"X",qeye(2),")","*", "|10>", tensor(dic.get(i), qeye(2)) @ umzero)
    print(50*"=")

print(50*"-")
#-----------------------------------------------------------------------------------

print("Extra (Sigmai X |0>)")

for i in dic:
    print("("+i,"X","|0>"+")", tensor(dic.get(i), ket0))
    print(50*"=")

print(50*"-")
#-----------------------------------------------------------------------------------

print("Extra (Sigmai X |1>)")

for i in dic:
    print("("+i,"X","|1>"+")", tensor(dic.get(i), ket0))
    print(50*"=")

print(50*"-")
#-----------------------------------------------------------------------------------

print("Extra Tr(P0p)")

book = { "md0" : pe0x0, "md01" : pe01x01, "md10" : pe10x10, "md1" : pe11x11}

for a in book:
    print("Tr(",pe0x0,"*",a,")", (pe0x0 @ book.get(a)).ptrace(0))
    print(50*"=")

print(50*"-")
#-----------------------------------------------------------------------------------

