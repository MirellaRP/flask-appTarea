import pymysql

class DAOUsuario:
    def connect(self):
        return pymysql.connect("localhost","root","","db_poo" )

    def read(self, id):
        con = DAOUsuario.connect(self)
        cursor = con.cursor()

        try:
            if id == None:
                cursor.execute("SELECT * FROM usuario order by nombres asc")
            else:
                cursor.execute("SELECT * FROM usuario where id = %s order by nombres asc", (id,))
            return cursor.fetchall()
        except:
            return ()
        finally:
            con.close()

    def insert(self,data):
        con = DAOUsuario.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("INSERT INTO usuario(codigo,nombres,login, clave , tipo) VALUES(%s, %s, %s,%s,%s)", (data['codigo'],data['nombres'],data['login'],data['clave'],data['tipo']))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()

    def update(self, id, data):
        con = DAOUsuario.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("UPDATE usuario set codigo = %s, nombres = %s, login = %s, clave = %s, tipo = %s,  where id = %s", (data['codigo'],data['nombres'],data['login'],data['clave'],data['tipo'],id,))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()

    def delete(self, id):
        con = DAOUsuario.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("DELETE FROM usuario where id = %s", (id,))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()

    
    def CompararDatos(self,data,login,clave):
        con = DAOUsuario.connect(self)
        cursor = con.cursor()
        yes=10000

        try:
            #Obtenemos los nombres de usuario del los integrantes de la base de datos
            cursor.execute("SELECT login FROM usuario")
            names = cursor.fetchall()
            #Obtenemos las contrasenas de los usuario de los integrantes de la base de datos
            cursor.execute("SELECT clave FROM usuario")
            contrasena = cursor.fetchall()
            #Chequeamos si coincide
            for i in range(len(names)): #for i in range(2): []
                nombre="('"+str(login)+"',)"
                contra="('"+str(clave)+"',)"
                if nombre==str(names[i]) and contra==str(contrasena[i]):
                    yes=i
                    print(yes)
            con.commit()
            return yes
        except:
            con.rollback()
            return False
        finally:
            con.close()


    def BuscarTipo(self,data,numero):
        con = DAOUsuario.connect(self)
        cursor = con.cursor()
        try:
            cursor.execute("SELECT tipo FROM usuario")
            tipo = cursor.fetchall()
            TipoU=str(tipo[numero])
            print(numero)    
            con.commit()
            return TipoU
        except:
            con.rollback()
            return False
        finally:
            con.close()

  