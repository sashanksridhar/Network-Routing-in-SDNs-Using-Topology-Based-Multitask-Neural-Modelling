import csv
def remove_values_from_list(the_list, val):
   return [value for value in the_list if value != val]
filename = input("filename")
with open('D:\\fyp\\fyp_codes\\'+filename+'.csv','r') as r,open('D:\\fyp\\fyp_codes\\'+filename+'_norm.csv','w') as w:
    reader = csv.reader(r)
    writer = csv.writer(w,lineterminator='\n')
    writer.writerow(["ID","Interval","Transfer","Bandwidth","Write","Error","Retry","CongestionWindow","RTT","NetPower","Server","Client","ServerPort","ClientPort","Window Buffer Size","TCP Window Size","CT","ServerHost","ClientHost","Host1","Host2","Host3","Host4","Host5","Host6","Host7","Host8","Hop","Switch1","Switch2","Switch3","Switch4","Switch5","Switch6","Switch7"])
    count = 0
    server = '10.0.0.1'
    client = '10.0.0.2'
    shost = '1'
    chost = '2'
    serverport = '5001'
    clientport = '35062'
    wbuf = '128'
    tcp = '85.3'
    ct = '30.35'
    interval = '0.1'
    h1 = '1'
    h2 = '1'
    h3 = '0'
    h4 = '0'
    h5 = '0'
    h6 = '0'
    h7 = '0'
    h8 = '0'
    hop = '2'
    sw1 = '1'
    sw2 = '0'
    sw3 = '0'
    sw4 = '0'
    sw5 = '0'
    sw6 = '0'
    sw7 = '0'
    for row in reader:
        if count<=6:
            count+=1
            continue
        # if count == 1:
        #     r2 = row[0].split(" ")
        #     global client
        #     client = r2[3]
        #     continue
        count+=1
        splstr = row[0].split(" ")
        splstr = remove_values_from_list(splstr, '')
        c = 0
        entry = []
        for var in splstr:
            if c==0 or c==3 or c==5 or c == 7 or c == 11:
                c+=1
                continue
            if c== 1:
                l = var.split(']')
                entry.append(l[0])
            if c == 2:
                entry.append(interval)
            if c == 4:
                entry.append(var)
            if c==6:
                entry.append(var)
            if c == 8:
                l = var.split('/')
                entry.append(l[0])
                entry.append(l[1])
            if c==9:
                entry.append(var)
            if c==10:
                l = var.split('/')
                i = l[0].split('K')
                entry.append(i[0])
                entry.append(l[1])
            if c == 12:
                entry.append(var)
            c+=1
        entry.append(server)
        entry.append(client)
        entry.append(serverport)
        entry.append(clientport)
        entry.append(wbuf)
        entry.append(tcp)
        entry.append(ct)
        entry.append(shost)
        entry.append(chost)
        entry.append(h1)
        entry.append(h2)
        entry.append(h3)
        entry.append(h4)
        entry.append(h5)
        entry.append(h6)
        entry.append(h7)
        entry.append(h8)
        entry.append(hop)
        entry.append(sw1)
        entry.append(sw2)
        entry.append(sw3)
        entry.append(sw4)
        entry.append(sw5)
        entry.append(sw6)
        entry.append(sw7)
        writer.writerow(entry)
        print(count)