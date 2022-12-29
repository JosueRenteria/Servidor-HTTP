# Declaracion de Librerias.
import socket 
import os
from os.path import exists
from concurrent.futures import ThreadPoolExecutor
import datetime
import time

e = datetime.datetime.now()

def task(serversocket):
    # Funcion para dar los diferentes tipos de Archivos.
    def Tipo_Header(myfile):
        if(myfile.endswith('.jpg')):
            mimetype = 'image/jpeg'
        elif(myfile.endswith('.png')):
            mimetype = 'image/png'
        elif(myfile.endswith('.pdf')):
            mimetype = 'application/pdf'
        elif(myfile.endswith('.docx')):
            mimetype = 'application/msword'
        elif(myfile.endswith('.c')):
            mimetype = 'text/plain'
        elif(myfile.endswith('.css')):
            mimetype = 'text/css'
        elif(myfile.endswith('.mp4')):
            mimetype = 'video/mp4'
        elif(myfile.endswith('.mp3')):
            mimetype = 'audio/mpeg'
        elif(myfile.endswith('.rar')):
            mimetype = 'application/x-rar-compressed'
        else:
            mimetype = 'text/html'
        header = 'HTTP/1.1 200 OK\n'
        return header, mimetype

    # Funcion para mostrar tablas.
    def Crear_Tabla(x, requesting_file):
        if x == 0:
            lista = []
            myfile2 = requesting_file.split('?')[1]
            myfile2 = myfile2.split('&')
                        
            for i in range(len(myfile2)):
                dato = myfile2[i].split('=')[1]
                lista.append(dato)
        else:
            lista = []
            myfile = string_list[(len(string_list)-1)]
            myfile2 = myfile.split('\r\n\r\n')[1]
            myfile2 = myfile2.split('&')
                
            for i in range(len(myfile2)):
                dato = myfile2[i].split('=')[1]
                lista.append(dato)
        return lista

    # Ciclo de todo el proceso.
    while True:
        # Inicializacion de los sockets.
        connection , address = serversocket.accept()
        request = connection.recv(1024).decode('utf-8')
        string_list = request.split(' ')

        # Ver que la peticion sea mayor a 1.
        if len(string_list) > 1:
            # Metodos y datos necesarios.
            method = string_list[0]
            requesting_file = string_list[1]
            print(request)
            
            # Si el Metodo es HEAD.
            if method.__contains__("HEAD"):
                
                # Definicion de nuestro File.
                myfile = requesting_file.split('?')[0]
                myfile = myfile.lstrip('/')

                # Para nuestro index.
                if(myfile == ''):
                    myfile = 'index.html'
                    requesting_file = '/index.html'

                try:
                    # Lectura del archivo.
                    file = open(myfile , 'rb')
                    response = file.read()
                    file.close()

                    # Llamada a la funcion Tipo_Header,
                    header, mimetype = Tipo_Header(myfile)

                    # Creacion de nuestro Header.
                    header += 'Content-Type: '+str(mimetype)+'\n' + "Date: " + time.strftime("%H:%M:%S") + '\n' + "Content-Length: " + str(os.path.getsize('./' + myfile)) + "\n\n"
                
                except Exception as e:
                    if myfile == 'head':
                        # Lista de Datos de los Usuarios.
                        lista = Crear_Tabla(0, requesting_file)
                        print(lista)
                        header = 'HTTP/1.1 200 OK\n\n'
                    else:
                        header = 'HTTP/1.1 404 Not Found\n\n'

            # Si el Metodo es GET.
            elif method == "GET":
                # Definicion de nuestro File.
                myfile = requesting_file.split('?')[0]
                myfile = myfile.lstrip('/')

                # Para nuestro index.
                if(myfile == ''):
                    myfile = 'index.html'
                    requesting_file = '/index.html'

                try:
                    # Lectura del archivo.
                    file = open(myfile , 'rb')
                    response = file.read()
                    file.close()

                    # Llamada a la funcion Tipo_Header,
                    header, mimetype = Tipo_Header(myfile)
                    # Creacion de nuestro Header.
                    header += 'Content-Type: '+str(mimetype)+'\n' + "Date: " + time.strftime("%H:%M:%S") + '\n' + "Content-Length: " + str(os.path.getsize('./' + myfile)) + "\n\n"

                except Exception as e:
                    if myfile == 'get':
                        # Lista de Datos de los Usuarios.
                        lista = Crear_Tabla(0, requesting_file)
                        header = 'HTTP/1.1 200 OK\n\n'
                        response = f'<head><title>Datos Ingresados</title></head><body><center><h1>Listado de Datos Ingresados</h1></center><br><table style="border: 1px solid black; margin: auto; text-align: center; font-size: xx-large;" border="1"><tr><td><strong> Datos requeridos </strong></td><td><strong> Datos Ingresados </strong></td></tr><tr><td> Nombre </td><td>{lista[0]}</td></tr><tr><td> Direccion </td><td>{lista[1]}</td></tr><tr><td> Telefono </td><td>{lista[2]}</td></tr><tr><td> Comentarios </td><td>{lista[3]}</td></tr></table></body></html>'.encode('utf-8')
                    else:
                        header = 'HTTP/1.1 404 Not Found\n\n'
                        response = '<html><head><meta charset="UTF-8"><title>Error 404 Not found</title><style>body{background-color: #D33F49;}</style></head><body><h1 style="margin-top:100px; text-align: center; color:#EFF0D1; font-family: monospace;">Error 404: Recurso no encontrado.</h1><p style = "margin-top:100px; text-align: center; color:#EFF0D1; font-family: monospace;">El sistema no puede encontrar el recurso especificado.</p>'.encode('utf-8') 
            # Si el Metodo es POST.
            elif method == "POST":
                # Lista de Datos de los Usuarios.
                lista = Crear_Tabla(1, requesting_file)
                header = 'HTTP/1.1 200 OK\n\n'
                response = f'<head><title>Datos Ingresados</title></head><body><center><h1>Listado de Datos Ingresados</h1></center><br><table style="border: 1px solid black; margin: auto; text-align: center; font-size: xx-large;" border="1"><tr><td><strong> Datos requeridos </strong></td><td><strong> Datos Ingresados </strong></td></tr><tr><td> Nombre </td><td>{lista[0]}</td></tr><tr><td> Direccion </td><td>{lista[1]}</td></tr><tr><td> Telefono </td><td>{lista[2]}</td></tr><tr><td> Comentarios </td><td>{lista[3]}</td></tr></table></body></html>'.encode('utf-8')
            
            # Si el Metodo es DELETE.
            elif method == "DELETE":
                try:
                    # Definicion de nuestro File.
                    myfile = requesting_file.split('?')[0]
                    
                    # Para nuestro index.
                    if(myfile == ''):
                        myfile = 'index.html'
                        requesting_file = '/index.html'

                    # Definicion de Ruta.
                    myFileNombre = myfile
                    myfile = myfile.lstrip('/')
                    
                    # Metodo para borrar Archivo
                    if(os.path.exists(myfile)):
                            tamano = str(os.path.getsize(myfile))
                            header, mimetype = Tipo_Header(myfile)
                            os.remove(myfile)
                            header = 'HTTP/1.1 202 Accepted\n\n'
                            header += 'Content-Type: '+str(mimetype)+'\n' + "Date: " + time.strftime("%H:%M:%S") + '\n' + "Content-Length: " + tamano + "\n\n"
                            response = '<html><head><meta charset="UTF-8"><title>202 OK Recurso eliminado</title><style>body{background-color: #D33F49;}</style></head><body><h1 style="margin-top:100px; text-align: center; color:#EFF0D1; font-family: monospace;">202 OK Recurso eliminado exitosamente.</h1><p style = "margin-top:100px; text-align: center; color:#EFF0D1; font-family: monospace;">El recurso ha sido eliminado permanentemente del servidor. Ya no se podra acceder más a él.</p>'.encode('utf-8') 
                    else:
                        header = 'HTTP/1.1 404 Not Found\n\n'
                        response = '<html><head><meta charset="UTF-8"><title>Error 404 Not found</title><style>body{background-color: #D33F49;}</style></head><body><h1 style="margin-top:100px; text-align: center; color:#EFF0D1; font-family: monospace;">Error 404: Recurso no encontrado.</h1><p style = "margin-top:100px; text-align: center; color:#EFF0D1; font-family: monospace;">Archivo no encontrado.</p>'.encode('utf-8') 
                except Exception as e:
                    header = 'HTTP/1.1 404 Not Found\n\n'
                    print(e)
            else:
                header = 'HTTP/1.1 501 Not Implemented\n'
                header += 'Content-Type: text/html' + '\n' + "Date: " + time.strftime("%H:%M:%S") + "\n\n"
                response = '<html><head><meta charset="UTF-8"><title>Error 501</title><style>body{background-color: #D33F49;}</style></head><body><h1 style="margin-top:100px; text-align: center; color:#EFF0D1; font-family: monospace;">Error 501: No implementado.</h1><p style = "margin-top:100px; text-align: center; color:#EFF0D1; font-family: monospace;">El método HTTP o funcionalidad solicitada no está implementada en el servidor.</p>'.encode('utf-8') 
            
            # Definicion del HEADER
            final_response = header.encode('utf-8')

            # Envio solo para el Metodo Head.
            if method.__contains__("HEAD"):
                connection.send(final_response)

            # Envio para todos los demas metodos.
            else:
                final_response += response
                connection.send(final_response)
            connection.close()

def main():
    # Datos del Host y del puerto.
    host , port = '127.0.0.1' , 8888

    # Inicializacion de los sockets.
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.setsockopt(socket.SOL_SOCKET , socket.SO_REUSEADDR , 1)
    serversocket.bind((host , port))
    serversocket.listen(1)
    print('servidor en el puerto: ' + str(port) + '\n')

    executor = ThreadPoolExecutor(5)
    future = executor.submit(task, serversocket)

if __name__ == '__main__':
    main()
