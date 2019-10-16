from operator import itemgetter
import os

def createtable(n):
    table = []
    for i in range(n):
        dic = dict()
        dic['name'] = input('Type the teams name: ')
        dic['wins'] = input('Type the wins number: ')
        dic['lost'] = input('Type the losses number: ')
        dic['touchdowns'] = input('Type the touchdowns number: ')
        table.append(dic)
    return table


def save(file,table):
    file = open(file,'w')
    for d in table:
        keys = list(d.keys())
    file.write(';'.join(keys))
    file.write('\n')
    for dic in table:
        values = list(dic.values())
        file.write(';'.join(values))
        file.write('\n')
    file.close()


def read(file):
    try:
        file = open(file)
        table = file.readlines()
        t = []
        for line in table:
            line = line.strip().split(';')
            t.append(line)
        read = []
        for i in range(1,len(t)):
            dic = {}
            for j in range(4):
                if j == 0:
                    dic['name'] = t[i][j]
                elif j == 1:
                    dic['wins'] = t[i][j]
                elif j == 2:
                    dic['lost'] = t[i][j]
                elif j == 3:
                    dic['touchdowns'] = t[i][j]
            read.append(dic)
        return read
    except:
        print('No file found')

def deletetable(file):
    os.remove(file)

def consult(table):
    name = input('Type the team name: ')
    for d in table:
        if d['name'] == name:
            reg = d
    return reg

def insert(file):
    file = open(file,'a')
    dic = dict()
    dic['name'] = input('Type the teams name: ')
    dic['wins'] = input('Type the wins number: ')
    dic['lost'] = input('Type the losses number: ')
    dic['touchdowns'] = input('Type the touchdowns number: ')
    values = list(dic.values())
    file.write(';'.join(values))
    file.write('\n')
    file.close()

def deletecell(tab):
    name = input('Type the teams name: ')
    for d in table:
        if d['name'] == name:
            reg = d
    for d in tab:
        if d == reg:
            tab.remove(d)
    return tab

def listit(tab):
    type = input('total or filtered? ')
    if type == 'total':
        for d in tab:
            print(d)
    elif type == 'filtered':
        filtered = []
        criteria = input('choose a criteria(winners or losers): ')
        if criteria == 'winners':
            for d in tab:
                if d['wins'] != '0':
                    print(d)
        elif criteria == 'losers':
            for d in tab:
                if d['lost'] != '0':
                    print(d)


while True:
    text = '''      1-  create a table.
      2-  Save the table in a file.
      3 – Read a table from a file.
      4 – Delete a table from file.
      5 – Order data from a table.
      6 – Consult a cell
      7 – Insert a cell in a table.
      8 – Delete cell
      9 – List data.
      0 – Exit'''

    print(text)
    print()
    x = int(input('What do you wish to do?(type a number) '))
    if x == 0:
        break
    elif x == 1:
        table = createtable(int(input('Number of cells: ')))
    elif x == 2:
        save(input('File name: '), table)
    elif x == 3:
        table = read(input('File name: '))
        print(table)

    elif x == 4:
        deletetable(input('File name: '))
    elif x == 5:
        ord = []
        i = input('Type the parameter: ')
        ord = sorted(table, key=itemgetter(i))
        table = ord

    elif x == 6:
         cell = consult(table)
         print(cell)
    elif x == 7:
        insert(input('File name: '))
    elif x == 8:
        table = deletecell(table)
    elif x == 9:
        listit(table)
