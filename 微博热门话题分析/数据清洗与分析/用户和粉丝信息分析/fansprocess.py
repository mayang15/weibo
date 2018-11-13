import json as js
import datetime
import csv

filename = 'lyzzr_o_m6.json'
with open(filename, 'r', encoding="utf8") as f:
    data = js.load(f)
count = 0
ipo = 0
k = 0
fans_table = {}
for x in data:
    if count == 0:
        print('number:')
        print(data[x], '\n')
        count = count + 1
    else:
        info = data[x][6]
        if 'uid' in info.keys():
            uid = info['uid']
            fan = info['fans_id']
            if info['uid'] in fans_table.keys():
                ipo = ipo + 1
                for num in fan:
                    fans_table[uid].append(fan[num])

            else:
                k = k + 1
                fans_table[uid] = []
                for num in fan:
                    fans_table[uid].append(fan[num])

        # fans_table[uid].append(k)
        else:
            pass
        count = count + 1
print(fans_table)
print(count)
fans_file = 'm_lyzzr_o6.txt'
f2 = open(fans_file, 'w')
for u in fans_table:
    u_fan = fans_table[u]
    f2.write(str(u))
    f2.write(' ')
    for id in u_fan:
        f2.write(str(id))
        f2.write(' ')
    f2.write('\n')
f2.close()
print('ipo', ipo)
print('k', k)
chuang_fan_excel = 'm_fans_table.csv'
with open(chuang_fan_excel, "w") as csvFile:
    csvWriter = csv.writer(csvFile)
    for k in fans_table:
        for k_f in fans_table[k]:
            csvWriter.writerow([k, k_f])
    csvFile.close()