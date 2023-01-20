import matplotlib.pyplot as plt

def generateBar(labels, values):
  try:
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.show()
  except KeyboardInterrupt:
    print(" GRAFICO FINALIZADO POR CORTE\n Hasta la proxima...")
    return


def generatePie(labels, values):
  try:
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    ax.axis('equal')
    plt.show()
  except KeyboardInterrupt:
    print(" GRAFICO FINALIZADO POR CORTE\n Hasta la proxima...")
    return
