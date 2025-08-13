from funciones import *
from clientes import cliente 
from apartamentos import apartamento
from conexionBD import *
from fpdf import FPDF
import xlsxwriter

def menu_exportar():
    borrarPantalla()
    print("\n\t..::: Exportar tablas :::..."
                    "\n\t 1.- pdf"
                    "\n\t 2.- xlsx"
                    "\n\t 3.- Salir al menu principal")
    formato = input("\n\t Selecciona el formato en el que deseas exportar: ")
    return formato

def exportarPDF():
    borrarPantalla()
    print("\t..::EXPORTAR A PDF::..")
    print("\t\nTabla de clientes (1)")
    cliente.mostrarTodo()
    print("\t\n Tabla de apartamentos(2)")
    apartamento.mostrarTodo()
    opcion = True
    while opcion:
        tabla = input("\t\t Selecciona la tabla que desees exportar a pdf(introduce '3' para salir): ")
        match tabla:
            case "1":
                cursor1,conexion1 = conectarBD()
                cursor1 = conexion1.cursor(dictionary=True)
                query = "SELECT * FROM clientes LIMIT 50"  # Limitar para no sobrecargar el PDF
                cursor1.execute(query)
                resultados = cursor1.fetchall()
                # 3. Crear PDF
                pdf = FPDF()
                pdf.add_page()
                pdf.set_font("Arial", size=8)
                # 4. Agregar título
                pdf.cell(200, 10, txt="Tabla Clientes", ln=1, align='C')
                # 5. Agregar encabezados (usamos las claves del primer registro)
                if resultados:
                    # Ancho de celda basado en el número de columnas
                    ancho_celda = 190 / len(resultados[0])
                    for columna in resultados[0].keys():
                        pdf.cell(ancho_celda, 10, txt=columna, border=1)
                    pdf.ln()
                    # 6. Agregar filas de datos
                    for fila in resultados:
                        for valor in fila.values():
                            pdf.cell(ancho_celda, 10, txt=str(valor), border=1)
                        pdf.ln()
                # 7. Guardar PDF
                pdf.output("tabla_clientes.pdf")
                # 8. Cerrar conexión
                cursor1.close()
                conexion1.close()
                print("PDF generado con éxito")
            case "2":
                cursor1,conexion1 = conectarBD()
                cursor1 = conexion1.cursor(dictionary=True)
                query = "SELECT * FROM apartamentos LIMIT 50"  # Limitar para no sobrecargar el PDF
                cursor1.execute(query)
                resultados = cursor1.fetchall()

                # 3. Crear PDF
                pdf = FPDF()
                pdf.add_page()
                pdf.set_font("Arial", size=8)

                # 4. Agregar título
                pdf.cell(200, 10, txt="Tabla Apartamentos", ln=1, align='C')

                # 5. Agregar encabezados (usamos las claves del primer registro)
                if resultados:
                    # Ancho de celda basado en el número de columnas
                    ancho_celda = 190 / len(resultados[0])
                    
                    for columna in resultados[0].keys():
                        pdf.cell(ancho_celda, 10, txt=columna, border=1)
                    pdf.ln()

                    # 6. Agregar filas de datos
                    for fila in resultados:
                        for valor in fila.values():
                            pdf.cell(ancho_celda, 10, txt=str(valor), border=1)
                        pdf.ln()

                # 7. Guardar PDF
                pdf.output("tabla_apartamentos.pdf")

                # 8. Cerrar conexión
                cursor1.close()
                conexion1.close()

                print("PDF generado con éxito")
            case "3":
                opcion=False
            case _:
                borrarPantalla() 
                input("\n\t 📛 Opción invalida vuelva a intentarlo ... por favor 📛")

def exportarXlsx():
    borrarPantalla()
    print("\t..::EXPORTAR A XLSX::..")
    print("\t\nTabla de clientes (1)")
    cliente.mostrarTodo()
    print("\t\n Tabla de apartamentos(2)")
    apartamento.mostrarTodo()
    opcion = True
    while opcion:
        tabla = input("\t\t Selecciona la tabla que desees exportar a xlsx(introduce '3' para salir): ")
        match tabla:
            case "1":
                cursor1, conexion1 = conectarBD()
                # 2. Ejecutar consulta
                query = "SELECT * FROM clientes"
                cursor1.execute(query)

                # 3. Obtener datos y nombres de columnas
                datos = cursor1.fetchall()
                nombres_columnas = [i[0] for i in cursor1.description]

                # 4. Crear archivo Excel
                nombre_archivo = "tabla_clientes.xlsx"
                workbook = xlsxwriter.Workbook(nombre_archivo)
                worksheet = workbook.add_worksheet("Datos")

                # 5. Formato para encabezados
                header_format = workbook.add_format({
                    'bold': True,
                    'bg_color': "#295A20",
                    'font_color': 'white',
                    'align': 'center',
                    'valign': 'vcenter',
                    'border': 1
                })

                # 6. Formato para celdas de datos
                data_format = workbook.add_format({
                    'align': 'left',
                    'valign': 'vcenter',
                    'border': 1
                })

                # 7. Escribir encabezados
                for col_num, col_name in enumerate(nombres_columnas):
                    worksheet.write(0, col_num, col_name, header_format)
                    # Ajustar ancho de columna basado en la longitud del nombre
                    worksheet.set_column(col_num, col_num, len(col_name) + 4)

                # 8. Escribir datos
                for row_num, row_data in enumerate(datos, start=1):
                    for col_num, cell_data in enumerate(row_data):
                        worksheet.write(row_num, col_num, str(cell_data), data_format)

                # 9. Cerrar archivo y conexión
                workbook.close()
                cursor1.close()
                conexion1.close()

                print(f"\n\t Tabla exportada exitosamente a {nombre_archivo}")
            case "2":
                cursor1, conexion1 = conectarBD()
                # 2. Ejecutar consulta
                query = "SELECT * FROM apartamentos"
                cursor1.execute(query)
                # 3. Obtener datos y nombres de columnas
                datos = cursor1.fetchall()
                nombres_columnas = [i[0] for i in cursor1.description]
                # 4. Crear archivo Excel
                nombre_archivo = "tabla_apartamentos.xlsx"
                workbook = xlsxwriter.Workbook(nombre_archivo)
                worksheet = workbook.add_worksheet("Datos")
                # 5. Formato para encabezados
                header_format = workbook.add_format({
                    'bold': True,
                    'bg_color': "#960E0E",
                    'font_color': 'white',
                    'align': 'center',
                    'valign': 'vcenter',
                    'border': 1
                })
                # 6. Formato para celdas de datos
                data_format = workbook.add_format({
                    'align': 'left',
                    'valign': 'vcenter',
                    'border': 1
                })
                # 7. Escribir encabezados
                for col_num, col_name in enumerate(nombres_columnas):
                    worksheet.write(0, col_num, col_name, header_format)
                    # Ajustar ancho de columna basado en la longitud del nombre
                    worksheet.set_column(col_num, col_num, len(col_name) + 4)
                # 8. Escribir datos
                for row_num, row_data in enumerate(datos, start=1):
                    for col_num, cell_data in enumerate(row_data):
                        worksheet.write(row_num, col_num, str(cell_data), data_format)
                # 9. Cerrar archivo y conexión
                workbook.close()
                cursor1.close()
                conexion1.close()

                print(f"\n\t Tabla exportada exitosamente a {nombre_archivo}")
            case "3":
                opcion=False
            case _:
                borrarPantalla() 
                input("\n\t 📛 Opción invalida vuelva a intentarlo ... por favor 📛")

