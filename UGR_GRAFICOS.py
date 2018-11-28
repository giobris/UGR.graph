import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

N = int(input("Qual gráfico quer gerar? 1 - Setor, 2 - Boxplot, 3 - Barra:"))

form = pd.read_excel('C:\\Users\\User\\Desktop\\Test form (Responses).xlsx')

#Gráficos:

#Setor
if N == 1:
    form.PH.groupby(form.Departamento).sum().plot(kind='pie')
    plt.axis('equal')
    plt.savefig("C:\\Users\\User\\Desktop\\grafico_pizza.png")
    plt.show()


#Boxplot
elif N == 2:
    sns.boxplot(x = form['PH'], y = form['Laboratório'])
    plt.savefig("C:\\Users\\User\\Desktop\\grafico_boxplot.png")
    plt.show()

#Barras
elif N == 3:
    sns.barplot(x = form["PH"], y = form["Laboratório"])
    plt.savefig("C:\\Users\\User\\Desktop\\grafico_barra.png")
    plt.show()

else:
    print("Erro, digite o número corretamente!")