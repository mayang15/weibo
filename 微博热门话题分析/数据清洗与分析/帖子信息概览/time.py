import json as js
import datetime
import csv
filename = 'lyzzr_u_t.json'
with open(filename,'r',encoding="utf8") as f:
	data=js.load(f)
count=0
latest_update_table={}
repost_table={}
comments_table={}
user_id_table={}
a=0
b=0
count2=0
count3=0
for x in data:
	if count==0:
		print('number:')
		print(data[x],'\n')
		count=count+1
	else:
		info=data[x][6]
		temp = str(info['user_id'])+str(info['comments'])+str(info['reposts'])
		if temp in user_id_table:
			count2=count2+1
			continue
		else:
			count3=count3+1
			user_id_table[temp]=1
		if 'latest_update' in info.keys():
			uptime=info['latest_update']
			p=uptime.split(' ')
			if p[0] in latest_update_table:
				latest_update_table[p[0]]=latest_update_table[p[0]]+1
			else:
				latest_update_table[p[0]]=1
		else:
			pass
		if 'reposts' in info.keys():
			if info['reposts'] in repost_table:
				repost_table[info['reposts']]=repost_table[info['reposts']]+1
			else:
				repost_table[info['reposts']]=1
		else:
			pass
		if 'comments' in info.keys():
			if info['comments'] in comments_table:
				comments_table[info['comments']]=comments_table[info['comments']]+1
			else:
				comments_table[info['comments']]=1
		else:
			pass
		count=count+1
print(count)
print(count2)
print(count3)
latest_update_table_excel='latest_update_user.csv'
with open(latest_update_table_excel, "w") as csvFile:
		csvWriter = csv.writer(csvFile)
		for k in latest_update_table.keys():
			csvWriter.writerow([k,latest_update_table[k]])
		csvFile.close()
repost_table_excel='repost_table_user.csv'
with open(repost_table_excel, "w") as csvFile:
		csvWriter = csv.writer(csvFile)
		for k in repost_table.keys():
			csvWriter.writerow([k,repost_table[k]])
		csvFile.close()
comments_table_excel='comments_table_user.csv'
with open(comments_table_excel, "w") as csvFile:
		csvWriter = csv.writer(csvFile)
		for k in comments_table.keys():
			csvWriter.writerow([k,comments_table[k]])
		csvFile.close()
