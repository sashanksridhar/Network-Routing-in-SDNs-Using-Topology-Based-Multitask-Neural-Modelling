from sklearn import preprocessing
import pandas as pd
import csv

with open("D:\\fyp\\fyp_codes\\1.csv",'r') as r:
    X = []
    Y = []
    header = []
    c = 0
    reader = csv.reader(r)
    for row in reader:
        if c==0:
            header.extend(row)
            c+=1
            continue
        x = []
        for i in [x for x in range(1,len(row)-7) if x!=10 and x!=11 and x!=17 and x!=18]:
            x.append(float(row[i]))
        X.append(x)
        Y.append(row[len(row)-7:])
    print(len(X))
    print(len(Y))
    print(X)
    print(header)
    header.remove('Switch1')
    header.remove('Switch2')
    header.remove('Switch3')
    header.remove('Switch4')
    header.remove('Switch5')
    header.remove('Switch6')
    header.remove('Switch7')
    header.remove("Client")
    header.remove("Server")
    header.remove("ClientHost")
    header.remove("ServerHost")
    del(header[0])
    # del(header[18])
    # del(header[19])
    print(len(header))
    df = pd.DataFrame(X,columns =header )

    maxObj = df.max()
    for label,content in df.items():
        if float(maxObj[label])!=float(0):
            df[label] = df[label].div(float(maxObj[label]))
    l = df.values.tolist()
    for i in range(0,len(Y)):
        for j in range(0,len(Y[i])):
            l[i].append(Y[i][j])
#store each column's max object in an array
    with open("D:\\fyp\\fyp_codes\\1.csv",'w') as w:
        writer = csv.writer(w,lineterminator='\n')
        writer.writerow(header)
        for i in range(0,len(l)):
            writer.writerow(l[i])
