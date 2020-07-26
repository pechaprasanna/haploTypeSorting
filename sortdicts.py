#!/usr/bin/python -tt


def getrawonlydata(dict, noofsnp):
	retdict = {}
	for key in dict.keys():
		if (len(key.split(',')) == int(noofsnp)) and not '' in key.split(',') and not ('/' in ''.join(key.split(','))):
			retdict[key] = dict[key]
	return retdict

def getrawincompletedata(dict, noofsnp):
	retdict = {}
	for key in dict.keys():
		if (len(key.split(',')) == int(noofsnp)) and '' in key.split(',') and not ('/' in ''.join(key.split(','))):
			retdict[key] = dict[key]
	return retdict

def getrawslashdata(dict, noofsnp):
	retdict = {}
	for key in dict.keys():
		if (len(key.split(',')) == int(noofsnp)) and not '' in key.split(',') and ('/' in ''.join(key.split(','))):
			retdict[key] = dict[key]
	return retdict

def getrawslashincompletedata(dict, noofsnp):
	retdict = {}
	for key in dict.keys():
		if (len(key.split(',')) == int(noofsnp)) and '' in key.split(',') and ('/' in ''.join(key.split(','))):
			retdict[key] = dict[key]
	return retdict

