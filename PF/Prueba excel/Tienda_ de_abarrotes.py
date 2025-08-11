
import xlsxwriter

workbook=xlsxwriter.Workbook("INVENTARIO.xlsx")
worksheet=workbook.add_worksheet()

row=0
col=0

campo=["codigo","producto","precio","existencias"]
r1=["254","crema","40","5"]
r2=["968","azucar","60","3"]
r3=["151","jugo de naranja","18","10"]
r4=["260","leche","36","2"]
r5=["300","Galletas","25","6"]
r6=["700","Huevo","60","8"]

conjunto=(campo,r1,r2,r3,r4,r5,r6)

for codigo,producto,precio,existencias in (conjunto):
    worksheet.write(row,col,codigo)
    worksheet.write(row,col+1,producto)
    worksheet.write(row,col+2,precio)
    worksheet.write(row,col+3,existencias)
    row+=1
workbook.close()
