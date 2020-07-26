#!/usr/bin/python -tt

def createdatacsv(dict, fields, ignorelist, subpoplist):
	firstrow = []
	for field in fields:
		if not field in ignorelist:
			firstrow.append(field)
	for subpop in subpoplist:
		firstrow.append(subpop)
	firstrow.append('Total')

	data = []
	for key in dict.keys():
		tempdata = []
		for i in range(len(fields)):
			if not fields[i] in ignorelist:
				tempdata.append(key.split(',')[i])
		for subpop in subpoplist:
			if not subpop in dict[key].keys():
				tempdata.append('')
			else:
				tempdata.append(dict[key][subpop])
		tempdata.append(sumofsubpop(dict[key]))
		data.append(tempdata)
	return (firstrow,data)

def sumofsubpop(dict):
	sum = 0
	for key in dict.keys():
		sum+=dict[key]
	return sum




