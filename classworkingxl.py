import openpyxl
wb=openpyxl.Workbook()
ws1=wb.active
ws1.append([x for x in range(10)])
ws1['F5']=3.14
wb.save(filename='test1.xlsx')
