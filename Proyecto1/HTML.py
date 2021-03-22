import subprocess
import time

def MHTML(rest, limite):
    try:
        a = open('Menu.html', 'w')
        a.write("""<html>
            <head>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous">
                <nav class="navbar navbar-dark bg-dark">
                  <a class="navbar-brand">
                  <h2><b> Proyecto 1 - Lenguajes formales y de programación </b></h2>
                  <h3><b> Allan Josué Rafael Morales - 201709196 </b></h3>
                  </a>
                </nav>
            </head>
            <body>""")
        a.write("<br><br>\n")
        a.write("""
            <div class="container" style="text-align: center;"><h2> <b> """ + rest.nombre +
                """</b> </h2></div>
            <br>
            <div class="container" style="text-align: center;" > <ul class="list-group">""")

        for sec in rest.secciones:
            a.write("<h3>" + sec.nombre + ":" + "</h3>")
            if limite is None:
                for op in sec.opciones:
                    a.write("""<li class="list-group-item">""")
                    a.write("<h4>" + op.nombre + "</h4>" + " <h5> Precio: </h5> Q.{:,.2f}".format(float(op.precio)))
                    a.write("<br>")
                    a.write("Descripción: " + op.descripcion + "\n")
                    a.write("</li>")

        a.write('\n</ul> </div> \n')
        fin = """</body>
                </html>"""
        a.write(fin)
        a.close()
        subprocess.Popen(['menu.html'], shell=True)
    except:
        print("Algo ha ocurrido")

def FHTML(fact, rest):
    try:
        a = open('Factura.html', 'w')
        a.write("""<html>
            <head>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous">
                <nav class="navbar navbar-dark bg-dark">
                  <a class="navbar-brand">
                  <h2><b> Proyecto 1 - Lenguajes formales y de programación </b></h2>
                  <h3><b> Allan Josué Rafael Morales - 201709196 </b></h3>
                  </a>
                </nav>
            <style>
            table, th {
              border: 1px solid black;
              border-collapse: collapse;
            }
            </style>
            </head>
            <body>""")
        a.write("<br><br>\n")
        a.write("""
            <div class="container" style="text-align: center;"><h4 > <b> """ + rest.nombre +
                """</b> </h4></div>""")
        a.write("""<div class="container" style="text-align: center;"><h4 > <b>  Factura No. 1""" +
                """</b> </h4></div>""")
        a.write("""<div class="container" style="text-align: center;"><h4 > <b> Fecha:  """ + time.strftime("%d/%m/%y") +
                """</b> </h4></div><br>""")
        a.write(""" <div class="container" style="text-align: left;"> <h4><b> Datos del Cliente: </b> </h4></div>
            <br>""")
        a.write(""" <div class="container" style="text-align: left;"> <b>Nombre:  """ + fact.nombre +
                """</b> </div>""")
        a.write(""" <div class="container" style="text-align: left;"> <b>NIT: """ + fact.nit +
                """</b> </div>""")
        a.write(""" <div class="container" style="text-align: left;"> <b>Dirección: """ + fact.direccion +
                """</b> </div><br>""")
        a.write(""" <div class="container" style="text-align: left;"> <b>Descripción:</b> </div>""")
        a.write("""<div class="container" style="text-align: center;" > \n""")
        a.write("""<li class="list-group-item">""")
        a.write("<table style=\"width:100%\">\n")
        a.write("<tr>\n")
        a.write("<th><b> Cantidad: </b></th>\n")
        a.write("<th><b> Nombre: </b></th>\n")
        a.write("<th><b> Precio: </b></th>\n")
        a.write("<th><b> Total: </b></th>\n")
        a.write("</tr>\n")
        for ped in fact.pedidos:
            a.write("<tr>")
            a.write("<td> " + ped.cantidad + "</td>\n")
            a.write("<td> " + ped.nombre + "</td>\n")
            a.write("<td> Q{:,.2f}".format(float(ped.precio)) + "</td>\n")
            a.write("<td> Q{:,.2f}".format(float(ped.total)) + "</td>\n")
            a.write("</tr>\n")
        a.write("<tr>\n")
        a.write("<td> Subtotal: </td>\n")
        a.write("<td> </td>\n")
        a.write("<td> </td>\n")
        a.write("<td> Q{:,.2f}".format(float(fact.subTotal)) + "</td>\n")
        a.write("</tr>\n")

        a.write("<tr>\n")
        a.write("<td> Propina: ({:,.2f}".format(float(fact.propina)) + "%)</td>\n")
        a.write("<td> </td>\n")
        a.write("<td> </td>\n")
        a.write("<td> Q{:,.2f}".format(float(fact.totalPropina)) + "</td>\n")
        a.write("</tr>\n")

        a.write("<tr>\n")
        a.write("<th><b> Total </b></th>\n")
        a.write("<th> </th>\n")
        a.write("<th> </th>\n")
        a.write("<th> Q{:,.2f}".format(float(fact.total)) + "</th>\n")
        a.write("</tr>\n")

        a.write("</table>\n")
        a.write('\n</li> \n')
        a.write('\n</div> \n')
        fin = """</body>
                </html>"""
        a.write(fin)
        a.close()
        subprocess.Popen(['factura.html'], shell=True)
    except:
        print("Algo ha ocurrido")


def THTML(toks):
    try:
        a = open('tokens.html', 'w')
        a.write("""<html>
            <head>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous">

                <nav class="navbar navbar-dark bg-dark">
                  <a class="navbar-brand">
                  <h2><b> Proyecto 1 - Lenguajes formales y de programación </b></h2>
                  <h3><b> Allan Josué Rafael Morales - 201709196 </b></h3>
                  </a>
                </nav>
                <style>
                table, th {
                  border: 1px solid black;
                  border-collapse: collapse;
                }
                </style>
            </head>
            <body>""")
        a.write("<br><br>\n")
        a.write("""
            <div class="container" style="text-align: center;"><h4 > <b> Tokens del Menú </b> </h4></div>
            <br>
            <div class="container" style="text-align: left;" > """)

        a.write("""<li class="list-group-item">""")
        a.write("<table style=\"width:100%\">\n")
        a.write("<tr>\n")
        a.write("<th><b> No.: </b></th>\n")
        a.write("<th><b> Lexema: </b></th>\n")
        a.write("<th><b> Fila: </b></th>\n")
        a.write("<th><b> Columna: </b></th>\n")
        a.write("<th><b> Token: </b></th>\n")
        a.write("</tr>\n")
        for tok in toks:
            a.write("<tr>")
            a.write("<td> " + str(tok.no) + "</td>\n")
            a.write("<td> " + tok.lexema + "</td>\n")
            a.write("<td>" + str(tok.fila) + "</td>\n")
            a.write("<td>" + str(tok.columna) + "</td>\n")
            a.write("<td>" + tok.tk + "</td>\n")
            a.write("</tr>\n")
        a.write("</table>\n")
        a.write('\n</li> \n')
        a.write('\n </div> \n')
        fin = """</body>
                </html>"""
        a.write(fin)
        a.close()
        subprocess.Popen(['tokens.html'], shell=True)
    except:
        print("Algo ha ocurrido")


def TEHTML(toks):
    try:
        a = open('tokensError.html', 'w')
        a.write("""<html>
            <head>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous">
                <nav class="navbar navbar-dark bg-dark">
                  <a class="navbar-brand">
                  <h2><b> Proyecto 1 - Lenguajes formales y de programación </b></h2>
                  <h3><b> Allan Josué Rafael Morales - 201709196 </b></h3>
                  </a>
                </nav>
                <style>
                table, th {
                  border: 1px solid black;
                  border-collapse: collapse;
                }
                </style>
            </head>
            <body>""")
        a.write("<br><br>\n")
        a.write("""<div class="container" style="text-align: center;"><h4 > <b> Tokens de Errores </b> </h4></div>
            <br><div class="container" style="text-align: left;" > """)
        a.write("""<li class="list-group-item">""")
        a.write("<table style=\"width:100%\">\n")
        a.write("<tr>\n")
        a.write("<th><b> No.: </b></th>\n")
        a.write("<th><b> Caracter: </b></th>\n")
        a.write("<th><b> Fila: </b></th>\n")
        a.write("<th><b> Columna: </b></th>\n")
        a.write("<th><b> Descripcion: </b></th>\n")
        a.write("</tr>\n")
        for tok in toks:
            a.write("<tr>")
            a.write("<td> " + str(tok.no) + "</td>\n")
            a.write("<td> " + tok.caracter + "</td>\n")
            a.write("<td>" + str(tok.fila) + "</td>\n")
            a.write("<td>" + str(tok.columna) + "</td>\n")
            a.write("<td>" + tok.descripcion + "</td>\n")
            a.write("</tr>\n")
        a.write("</table>\n")
        a.write('\n</li> \n')
        a.write('\n </div> \n')
        fin = """</body>
                </html>"""
        a.write(fin)
        a.close()
        subprocess.Popen(['tokensError.html'], shell=True)
    except:
        print("Algo ha ocurrido")