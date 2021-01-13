import xlwings as xw
import os

cur_path=os.getcwd() #当前目录路径
file_path=cur_path + '\\'+ 'test.xlsx'
print(file_path)

app=xw.App(visible=False)
wb=app.books.add() # 新增excel工作簿
wb.save(file_path)
wb.close()
app.quit()