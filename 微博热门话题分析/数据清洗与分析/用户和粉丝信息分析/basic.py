import json as js
import datetime
import csv
filename = 'lyzzr_u_m.json'
with open(filename,'r',encoding="utf8") as f:
	data=js.load(f)
count=0
gendertable={}
placetable={}
agetable={}
fansNumtable=[]
followNumtable=[]
a=0
b=0
for x in data:
	if count==0:
		print('number:')
		print(data[x],'\n')
		count=count+1
	else:
		info=data[x][6]
		if 'gender' in info.keys():
			if info['gender'] in gendertable:
				gendertable[info['gender']]=gendertable[info['gender']]+1
			else:
				gendertable[info['gender']]=1
		else:
			pass
		if 'place' in info.keys():
			place=info['place']
			p=place.split(' ')
			if p[0] in placetable:
				placetable[p[0]]=placetable[p[0]]+1
			else:
				placetable[p[0]]=1
		else:
			pass
		if 'birthday' in info.keys():
			bir=info['birthday']
			if bir=='01-01' or bir=='unknown' or bir=='0001-00-00' or '-' not in bir:
				pass
			else:
				t=bir.split('-')
				age=2018-int(t[0])
				if age<5 or age >80:
					pass
				else:
					if str(age) in agetable:
						agetable[str(age)]=agetable[str(age)]+1
					else:
						agetable[str(age)]=1
		else:
			pass
		if 'fansNum' in info.keys():
			fansNum=info['fansNum']
			if fansNum==-1:
				pass
			else:
				fansNumtable.append(fansNum)
		else:
			pass
		if 'followNum' in info.keys():
			followNum=info['followNum']
			if followNum==-1:
				pass
			else:
				followNumtable.append(followNum)
		else:
			pass
		count=count+1
print(gendertable)
print(placetable)
print(agetable)
print(fansNumtable)
print(followNumtable)
agetable_new={'未成年':0,'18-25岁':0,'26-30岁':0,'31-40岁':0,'41-50岁':0,'50岁以上':0}
for x in agetable.keys():
	if int(x)<18:
		agetable_new['未成年']=agetable_new['未成年']+agetable[x]
	elif int(x)<26:
		agetable_new['18-25岁']=agetable_new['18-25岁']+agetable[x]
	elif int(x)<30:
		agetable_new['26-30岁']=agetable_new['26-30岁']+agetable[x]
	elif int(x)<40:
		agetable_new['31-40岁']=agetable_new['31-40岁']+agetable[x]
	elif int(x)<50:
		agetable_new['41-50岁']=agetable_new['41-50岁']+agetable[x]
	else:
		agetable_new['50岁以上']=agetable_new['50岁以上']+agetable[x]
print(agetable_new)
print(count)
placetable_excel='placetable_user.csv'
with open(placetable_excel, "w") as csvFile:
		csvWriter = csv.writer(csvFile)
		for k in placetable.keys():
			csvWriter.writerow([k,placetable[k]])
		csvFile.close()
agetable_excel='agetable_user.csv'
with open(agetable_excel, "w") as csvFile:
		csvWriter = csv.writer(csvFile)
		for k in agetable_new.keys():
			csvWriter.writerow([k,agetable_new[k]])
		csvFile.close()
fansnumtable_excel='fansnum_user.csv'
with open(fansnumtable_excel, "w") as csvFile:
		csvWriter = csv.writer(csvFile)
		for k in fansNumtable:
			a=int(a)+1
			a=str(a)
			csvWriter.writerow([a,k])
		csvFile.close()
follownumtable_excel='follownum_user.csv'
with open(follownumtable_excel, "w") as csvFile:
		csvWriter = csv.writer(csvFile)
		for k in followNumtable:
			b=int(b)+1
			b=str(b)
			csvWriter.writerow([b,k])
		csvFile.close()