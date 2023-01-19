import csv

def readCsv(path):
    with open (path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        header = next(reader)  #iterable
        orders = []
        for row in reader:
            iterable = zip(header, row)
            order = {key: value for key, value in iterable}
            orders.append(order)
    return orders

if __name__ == '__main__':
  orders = readCsv('./app/superstore.csv')
  print(orders[2])

