#work with graphs and pandas

import matplotlib.pyplot as plt
import numpy as np


plt.figure(figsize = (5,3), dpi = 100)#redimencionando a escala
x = [1,2,3,4,5]
y = [2,4,6,8,10]


x2 = np.arange(0,4,0.5)
plt.plot(x2[:5],x2[:5]**2,'r',label = 'X^2')
plt.plot(x2[4:],x2[4:]**2,'r--',label = 'X^2')

plt.plot(x,y,label = '2x',color = 'red', linewidth = 2, marker = '*',linestyle = '--', markersize = 8, markeredgecolor = 'blue')
#plota grafico com propriedades se necessrio 
# de legenda, cor, largura da linha , tipo macador, tipo linha, tamanho e cor do marcador
plt.title('Our first Graph ',fontdict={'fontname':'Comic Sans MS','fontsize':20})

plt.xlabel('X Axis')
plt.ylabel('Y Axis')

#escala
plt.xticks(([0,1,2,3]))
plt.yticks(([0,2,4,6,8,10]))

plt.legend()#faz aparecer a legenda
plt.savefig('mygraph.png',dpi = 100)
plt.show()#elimina tirulo ruido
