import readcsv as readCSV

def run():
    #Envio del path para la lectura
    orders = readCSV.readCsv('./app/superstore.csv')
    print(orders[4])
    #Aqui debe ir un menu de opcion
    

if __name__ == '__main__':
  run()
