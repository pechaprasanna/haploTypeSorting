#!/usr/bin/python -tt

import xlsxwriter

def writeoutputcsv(tupdata):
	workbook = xlsxwriter.Workbook('OutputData.xlsx')
	for key in tupdata.keys():
		worksheet = workbook.add_worksheet(name=key)
		row = 0
		col = 0
		for field in tupdata[key][0]:
			worksheet.write(row, col, field)
			col+=1
		for data in tupdata[key][1]:
			col = 0
			row+=1
			for rowdata in data:
				worksheet.write(row, col, rowdata)
				col+=1
	workbook.close()

