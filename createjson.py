#!/usr/bin/python -tt
import csv
import sys
import re

def createcolumnwisejson(filename, noofassayid):
	columndict = {}
	fields = []
	with open(filename, newline='',encoding="utf-8") as csvfile:
		reader = csv.reader(csvfile, delimiter=',', quotechar='|')
		fields = next(reader)[(-noofassayid):]
		for row in reader:
			for i in range(len(row[(-noofassayid):])):
				if not fields[i] in columndict.keys():
					columndict[fields[i]] = [row[i-noofassayid]]
				else:
					columndict[fields[i]].append(row[i-noofassayid])

	return columndict

def createrowwisejson(filename, noofassayid, subpopulationcolumn,type,fields,replacedict):
	rowdict={}
	with open(filename, newline='', encoding='utf-8') as csvfile:
		reader = csv.reader(csvfile, delimiter=',', quotechar='|')
		next(reader)
		for row in reader:
			if len(row)>22:
				sys.exit('Unwanted comma in this row --> '+ ','.join(row))
			dataset = row[-noofassayid:]
			if validdata(','.join(dataset)):
				if type:
					dataset = replacedata(dataset,fields,replacedict)
				key = ','.join(dataset)
				subpop = subpopulationcolumn-len(row)-1
				rowsubpop = row[subpop]
				if rowsubpop == '':
					rowsubpop = 'unknown'
				if not key in rowdict.keys():
					temphash ={}
					temphash[rowsubpop] = 1
					rowdict[key] = temphash
				else:
					if not row[subpop] in rowdict[key].keys():
						temphash = rowdict[key]
						temphash[rowsubpop] = 1
						rowdict[key] = temphash
					else:
						temphash = rowdict[key]
						temphash[rowsubpop]+=1
						rowdict[key] = temphash
	return rowdict


def createfieldslist(filename, noofassayid):
	with open(filename, newline='', encoding='utf-8') as csvfile:
		reader = csv.reader(csvfile, delimiter=',', quotechar='|')
		return next(reader)[-noofassayid:]

def createsubpoplist(filename,subpopulationcolumn):
	subpoplist = []
	with open(filename, newline='', encoding='utf-8') as csvfile:
		reader = csv.reader(csvfile, delimiter=',', quotechar='|')
		next(reader)
		for row in reader:
			subpop=subpopulationcolumn-len(row)-1
			rowsubpop = row[subpop]
			if rowsubpop == '':
				rowsubpop = 'unknown'
			if not rowsubpop in subpoplist:
				subpoplist.append(rowsubpop)
	return subpoplist

def replacedata(row,fields,replacedict):
	for i in range(len(fields)):
		if fields[i] in replacedict.keys():
			if row[i] in replacedict[fields[i]].keys():
				row[i] = replacedict[fields[i]][row[i]]	
	return row


def validdata(key):
	text = 'CGAT/,'
	return len(re.findall(r'(?!['+text+']).',key)) == 0