with open('C:\PycharmProjects\product1.csv', 'r') as t1, open('C:\PycharmProjects\product2.csv', 'r') as t2:
    fileone = t1.readlines()
    print(fileone)
    filetwo = t2.readlines()

with open('product3.csv', 'w') as outFile:
    for line in filetwo:
        if line not in fileone:
            outFile.write(line)


def compare(File1,File2):
    with open(File1,'r') as f:
        d=set(f.readlines())


    with open(File2,'r') as f:
        e=set(f.readlines())

    open('C:\PycharmProjects\product1.csv','w').close() #Create the file

    with open('file3.txt','a') as f:
        for line in list(d-e):
           f.write(line)
compare('C:\PycharmProjects\product1.csv','C:\PycharmProjects\product2.csv')