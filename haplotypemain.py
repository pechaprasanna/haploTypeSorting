#!/usr/bin/python -tt

import sys
import createjson
import os
from os import path
import sortdicts
import createoutputdata as op
import writecsv


def validatecol(columndict, percent):
	retlist = []
	for key in columndict.keys():	
		if (len(''.join(columndict[key]))/len(columndict[key]))*100 <5 :
			retlist.append(key)
	return retlist

def readinputs(inputfile):
	file = open(inputfile, 'r')
	dict ={}
	for line in file:
		data = line.rstrip('\n').split('=')
		if not data[1]:
			sys.exit('input data missing in input.txt \n'+line)
		else:
			dict[data[0]]=data[1]
	file.close()		
	return dict

def readreplacedata(inputfile):
	file = open(inputfile,'r')
	dict = {}
	for line in file:
		data = line.rstrip('\n').split(':')
		if not data[1]:
			sys.exit('incomplete data in replace.txt \n'+line)
		else:
			datalist = data[1].split(',')
			tmp = {}
			for replacedata in datalist:
				replacedatalist = replacedata.split('=')
				if not (replacedatalist[0] or replacedatalist[1]):
					sys.exit('incomplete data in replace.txt \n'+line)
				else:
					tmp[replacedatalist[0]] = replacedatalist[1]
			dict[data[0]]=tmp
	return dict		

def main():
	args=sys.argv[1:]
	if len(args)<2:
		sys.exit('Usage : haplotypemain.py input.txt replace.txt')
	if not path.exists(args[0]):
		sys.exit('input.txt missing')

	inputdict = readinputs(args[0])
	replacedict = readreplacedata(args[1])
	#print(createjson.createcolumnwisejson(args[0], int(args[1]))['15512627'])
	#print(createjson.createfieldslist(args[0],int(args[1])))
	ignoreList = ','.join(validatecol(createjson.createcolumnwisejson(inputdict['rawinputfile'],int(inputdict['noofSNP'])), inputdict['percentageofnegligence']))
	#print(ignoreList)
	rawdatafields = createjson.createfieldslist(inputdict['rawinputfile'],int(inputdict['noofSNP']))
	nonsynfields = createjson.createfieldslist(inputdict['nonSynonymousinputfile'],int(inputdict['noofNonsynSNP']))
	subpoplist = createjson.createsubpoplist(inputdict['rawinputfile'], int(inputdict['subpopulationcolumn']))
	noofSNP = int(inputdict['noofSNP'])
	subpopulationcolumn = int(inputdict['subpopulationcolumn'])
	rowwisejson = createjson.createrowwisejson(inputdict['rawinputfile'],noofSNP,subpopulationcolumn,False,rawdatafields,replacedict)
	replacerawwisedata = createjson.createrowwisejson(inputdict['rawinputfile'],noofSNP,subpopulationcolumn,True,rawdatafields,replacedict)
	outputtup = {}
	outputtup['RawData'] = op.createdatacsv(sortdicts.getrawonlydata(rowwisejson,noofSNP),rawdatafields,ignoreList,subpoplist)
	outputtup['IncompleteData'] = op.createdatacsv(sortdicts.getrawincompletedata(rowwisejson,noofSNP),rawdatafields,ignoreList,subpoplist)
	outputtup['RawDataSlash'] = op.createdatacsv(sortdicts.getrawslashdata(rowwisejson,noofSNP),rawdatafields,ignoreList,subpoplist)
	outputtup['IncompleteDataSlash'] = op.createdatacsv(sortdicts.getrawslashincompletedata(rowwisejson,noofSNP),rawdatafields,ignoreList,subpoplist)
	outputtup['ReRawData'] = op.createdatacsv(sortdicts.getrawonlydata(replacerawwisedata,noofSNP),rawdatafields,ignoreList,subpoplist)
	outputtup['ReIncompleteData'] = op.createdatacsv(sortdicts.getrawincompletedata(replacerawwisedata,noofSNP),rawdatafields,ignoreList,subpoplist)
	outputtup['ReRawDataSlash'] = op.createdatacsv(sortdicts.getrawslashdata(replacerawwisedata,noofSNP),rawdatafields,ignoreList,subpoplist)
	outputtup['ReIncompleteDataSlash'] = op.createdatacsv(sortdicts.getrawslashincompletedata(replacerawwisedata,noofSNP),rawdatafields,ignoreList,subpoplist)
	writecsv.writeoutputcsv(outputtup)
	#print()
	#print(sortdicts.getrawincompletedata(createjson.createrowwisejson(inputdict['rawinputfile'],int(inputdict['noofSNP']),int(inputdict['subpopulationcolumn'])),inputdict['noofSNP']))
	#print()
	#print(sortdicts.getrawslashdata(createjson.createrowwisejson(inputdict['rawinputfile'],int(inputdict['noofSNP']),int(inputdict['subpopulationcolumn'])),inputdict['noofSNP']))
	#print()	
	#print(sortdicts.getrawslashincompletedata(createjson.createrowwisejson(inputdict['rawinputfile'],int(inputdict['noofSNP']),int(inputdict['subpopulationcolumn'])),inputdict['noofSNP']))
	
	#print(createjson.createsubpoplist(args[0], int(args[3])))

if __name__ == '__main__':
  main()
