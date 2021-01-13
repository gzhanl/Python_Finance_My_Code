import xlwings as xw
import os

cur_path=os.getcwd() #当前目录路径
file_path=cur_path + '\\'+ 'AAA.xlsx'
print(file_path)

app=xw.App(visible=False)
wb=app.books.add() # 新增excel工作簿

sht=wb.sheets.add('new sheet')
sht.range('A1').value='AAA'

wb.save(file_path)
wb.close()
app.quit()