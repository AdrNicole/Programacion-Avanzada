# Practica -*-
"""
for x in range(1,11):
    print("{3}{0:<10.2f}{3}{3}{1:.^10d}{3}{3}{2:>10}{3}".format(x,x**2,x**3,"|"))

# agregar relleno
x.ljust(campo, carácter de relleno)
x.rjust(campo, carácter de relleno)
x.center(campo,carácter de relleno) # ambos lados

# eliminacion
x.lstrip(caracteres) # principio
x.rstrip(caracteres) # final
x.strip(caracteres) # ambos lados

# reemplazo
x.replace(subcadena1, subcadena2, ocurrencias)
x.replace(ahora,despues,x3 veces siguientes al texto reemplazado)

# encontrar
x.find(subcadena,inicio,fin)
x.find(parte del texto, posicion de inicio, posicion final)
"""
a= "efv  _Hola mundo mundo_  efv"
print(a.lstrip("efv  _"))
print(a.rstrip("efv  _"))

b= a.strip("efv  _")
print("|"+b.center(12,"=")+"|")


print(b.replace("mundo","Adriana",1))

cadena = "Este es el testimonio de un terrestre"
print (cadena.find("monio", 16, 30))
print (cadena.find("rrestre", 32, 37))
#---------------------------------------------------------------
"""
1. (Ejercicio original 19)
Formatea el número 3.14159265 para mostrarlo con 3 decimales usando format().
"""
print("{0:<10.3f}".format(3.14159265))

"""
2. (Ejercicio original 20)
Escribe un programa que lea un DNI y lo muestre con ceros a la izquierda 
en un campo de 8 dígitos usando zfill().
"""
DNI = "71234447"
print(DNI.zfill(16))

"""
3. (Ejercicio original 17)
Dada una dirección de correo electrónico, extrae el nombre de usuario y 
el dominio usando split("@").
"""
correo = "an.macedoe@alum.up.edu.pe"
print(correo.split("@"))

"""
4. (Ejercicio original 16)
Escribe un programa que cuente las palabras en una frase ingresada por 
el usuario.
"""
frase = "Es un maravilloso dia realmente"
espacios=0
for i in frase:
    if i==" ":
        espacios+=1

print(f"Hay {espacios+1} palabras")

"""
5. (Ejercicio original 18)
Verifica si una cadena es un palíndromo (se lee igual al derecho y al revés).
"""
texto= "reconocer"
#texto= "Hola"
if texto==texto[::-1]:
    print("La cadena es un palíndromo")
else:
    print("La cadena no lo es")

"""
6. (Ejercicio original 26)
Crea un programa que lea una frase y cuente la frecuencia de cada letra, 
ignorando mayúsculas/minúsculas.
"""

frase2  = "Carambola es rica"

frase2 = frase2.lower()
lista= []
for i in frase2:
    frecuencia = frase2.count(i)
    lista.append(frecuencia)

print(lista)

"""
7. (Ejercicio original 29)
Crea una función que reciba una cadena y devuelva un diccionario con la 
frecuencia de cada palabra.
"""
cadena  = "carambola"
num_letras = {letra: cadena.count(letra) for letra in cadena}
print(num_letras)

"""
8. (Ejercicio original 23)
Crea una función que extraiga todas las vocales de una cadena y las 
devuelva en orden descendente sin repetir.
"""
vocales = "aeiou"
cadena3 = "muurcielagooo"

voc = []
for i in cadena3:
    if i in vocales:
        voc.append(i)
# con set no repite
a = set(voc)
# ordenar de forma de descendente
print(sorted(a,reverse=True))

"""
9. (Ejercicio original 21)
Implementa un cifrado César que reciba un texto y un número de 
desplazamiento y devuelva el texto cifrado. El espacio debe 
mantenerse como tal.
"""
def cifrado_cesar(texto, desplazamiento):
    resultado = ""
    
    for caracter in texto:
        if caracter == " ":
            # El espacio se mantiene igual
            resultado += " "
        elif caracter.isupper():
            # Letras mayúsculas: 'A' = 65 en Unicode
            posicion = ord(caracter) - ord('A')
            nueva_posicion = (posicion + desplazamiento) % 26
            resultado += chr(nueva_posicion + ord('A'))
        elif caracter.islower():
            # Letras minúsculas: 'a' = 97 en Unicode
            posicion = ord(caracter) - ord('a')
            nueva_posicion = (posicion + desplazamiento) % 26
            resultado += chr(nueva_posicion + ord('a'))
        else:
            # Cualquier otro carácter (números, signos) se mantiene igual
            resultado += caracter
    
    return resultado


# Ejemplo de uso
texto_original = "Te amo"
desplazamiento = 3
texto_cifrado = cifrado_cesar(texto_original, desplazamiento)

print(f"Texto original: {texto_original}")
print(f"Texto cifrado: {texto_cifrado}")

"""
10. (Ejercicio original 22)
Escribe un programa que decodifique un texto cifrado con el cifrado César, dado el texto cifrado y el desplazamiento.
"""

def decifrado_Cesar(textual, desplazado):
    decodificado = ""
    for i in textual:
        if i==" ":
            decodificado+=" "
        elif i.isupper():
            ansi = ord(i) - ord("A")
            posicion= (ansi - desplazado) % 26
            decodificado += chr(posicion + ord("A"))
            
        elif i.islower():
            ansi = ord(i) - ord("a")
            posicion= (ansi - desplazado) % 26
            decodificado += chr(posicion + ord("a"))
        else:
            # cualquier  otro caracter i se mantiene igual
            decodificado += i
        
    return decodificado

texto_cifrado_Cesar = "Wh dpr"
desplazado = 3
decifrado = decifrado_Cesar(texto_cifrado_Cesar,desplazado)
            
print(f"Texto cifrado: {texto_cifrado_Cesar}")      
print(f"Texto decifrado: {decifrado}")

"""
11. (Ejercicio original 25)
Escribe una función que valide si una cadena es una dirección 
de correo electrónico válida.
"""
def validacion_correo(correo):
    if correo.find("@")!=-1 and correo.find(".pe")==len(direccion_correo)-3 or correo.find(".com")==len(direccion_correo)-4:
        print("Dirección de correo electrónico válida")
    else:
        print("No es una dirección de correo electrónico válida")
        
#direccion_correo = "an.macedoe@alum.up.edu.pe" 
direccion_correo = "xbah1@jbxajx"
#direccion_correo = "adriana@gmail.com"
validacion_correo(direccion_correo)

"""
12. (Ejercicio original 30)
Implementa una función que valide si una cadena cumple con el formato 
de contraseña segura: al menos 8 caracteres, una mayúscula, una 
minúscula, un número y un carácter especial.
        
"""

contrasena="MicOntra84@" # la contraseña es segura
#contrasena="Micontra84" # vuelva a intentar
#contrasena="Micon84"  # vuelva a intentar

lista = []
veces=0
numeros = [0,1,2,3,4,5,6,7,8,9]
cont_mayus=0
cont_minus=0
cont_especial=0
cont_num=0

if len(contrasena)>=8:
    for i in contrasena:
        veces+=1
        if i.isupper():
            cont_mayus+=1
            if cont_mayus==1:
                lista.append(i)
                
        elif i.islower():
            cont_minus+=1
            if cont_minus==1:
                lista.append(i)
        
        elif i.isalnum()==False:
            cont_especial+=1
            if cont_especial==1:
                lista.append(i)
        
        if veces==len(contrasena) and len(lista)==4:
            print("La contraseña es segura",lista)
        else:
            if veces==len(contrasena):
                print("Vuelva a intentar")
    
        for j in numeros:
            posicion_num = contrasena.find(str(j))
            if posicion_num!=-1:
                num_en_contrasena = int(contrasena[posicion_num])
                cont_num+=1
                if cont_num==1:
                    lista.append(num_en_contrasena)
else:
    #if veces==len(contrasena):
        print("Vuelva a intentar")

"""
13. (Ejercicio original 24)
Dada una base de datos de personas en formato "nombre-apellido-edad-dni", 
extrae: las 2 últimas letras del apellido, 
las 2 últimas letras del nombre, 
la suma de los dígitos de la edad en formato 00, 
y el tercer dígito del DNI.
"""

# "nombre-apellido-edad-dni"
persona = "Taehyung-kim-30-43578894"

posicion_nombre = persona.index("-")
eliminacion_primerGuion = persona[:posicion_nombre+1]
apellido_edad_dni = persona.lstrip(eliminacion_primerGuion)
posicion_segundoGuion = apellido_edad_dni.index("-")

Apellido_2letras = apellido_edad_dni[posicion_segundoGuion-2:posicion_segundoGuion]
Nombre_2letras = persona[posicion_nombre-2:posicion_nombre]

digito_edad1 = int(apellido_edad_dni[posicion_segundoGuion+1])
digito_edad2 = int(apellido_edad_dni[posicion_segundoGuion+2])

suma_digitos = digito_edad1 + digito_edad2
formato_00 = str(suma_digitos).zfill(3)

digito3_dni = apellido_edad_dni[-6]

print("las 2 últimas letras del apellido: ",Apellido_2letras)
print("las 2 últimas letras del nombre: ",Nombre_2letras)
print("la suma de los dígitos de la edad en formato 00: ",formato_00)
print("tercer dígito del DNI: ",digito3_dni)

print("codigo: ",Apellido_2letras+Nombre_2letras+formato_00+digito3_dni)

"""
14. (Ejercicio original 27)
Implementa una función que encuentre todas las subcadenas comunes entre 
dos cadenas.
"""

def encontrar(cadena,cadena_left,cadena_right):
    posicion = []
    pos_cadena_left = cadena.index(cadena_left)
    pos_cadena_right = cadena.index(cadena_right)

    while cadena.find("voy",pos_cadena_left,pos_cadena_right)!=-1:
        # encontrar la subcadena
        cadena.find("voy",pos_cadena_left,pos_cadena_right)
    
        # posicion de la subcadena
        pos_subcadena = cadena.find("voy",pos_cadena_left,pos_cadena_right)
    
        # eliminar la subcadena
        cadena = cadena[pos_subcadena+len("voy"):]
        
        # posicion
        posicion.append(pos_subcadena)
    return print(posicion)
texto = "De noche voy a brillar, del día voy a escapar" # voy
#cadena = "La duda es la madre de la invención" # la
cadena_l = "noche"
cadena_r = "escapar"

encontrar(texto,cadena_l,cadena_r)

"""
15. (Ejercicio original 28)
Escribe un programa que convierta un número a su representación en 
palabras (ej: 123 → "ciento veintitrés").

"""
numero = 123
num_uni = [1,2,3,4,5,6,7,8,9,0]
texto_uni = ["uno","dos","tres","cuatro","cinco","seis","siete","ocho","nueve","cero"]
texto_un = ["once","doce","trece","catorce","quince"]
texto_dec = ["diez","veinte","treinta","cuarenta","cincuenta","sesenta","setenta","ochenta","noventa"]
texto_cent =["cien","doscientos","trescientos","cuatrocientos","quinientos","seiscientos","setecientos","ochocientos","novecientos"]

def lector_numeros_3cifras(numero):
    if len(str(numero))==1:
        # 1 cifra
        for i,j in zip(num_uni,texto_uni):
                if numero==i:
                    print(texto_uni[i-1])
    
    elif len(str(numero))==2:
        # 2 cifras
            
        lista_num = list(str(numero))
        cifra1 = int(lista_num[0])
        cifra2 = int(lista_num[1])
        
        # decena y unidad [ 11-15]
        if cifra1==1 and cifra2>=1 and cifra2<=5: 
            for i,j in zip(num_uni,texto_un):
                if cifra2==i:
                    unidad = texto_un[i-1]
        # decena y unidad [ 16-19]
        elif cifra1==1 and cifra2>5:
            for i,j in zip(num_uni,texto_dec):
                if cifra1==i:
                    decena = texto_dec[i-1]
                    
            for i,j in zip(num_uni,texto_uni):
                if cifra2==i:
                    unidad = texto_uni[i-1]
        # >20           
        elif cifra1>1: 
                    # decena
            for i,j in zip(num_uni,texto_dec):
                if cifra1==i:
                    decena = texto_dec[i-1]
                    # unidad
            for i,j in zip(num_uni,texto_uni):
                if cifra2==i:
                    unidad = texto_uni[i-1]
                    
        if cifra1==1 and cifra2>=1 and cifra2<=5:          
            print(unidad)
        else:
            if cifra2!=0:
                print(decena+" y "+unidad)
            
            elif cifra2==0:
                print(decena)
            
    elif len(str(numero))==3:
        # 3 cifras
            # centena
        lista_num = list(str(numero))
        cifra1 = int(lista_num[0])
        cifra2 = int(lista_num[1])
        cifra3 = int(lista_num[2])
        
        for i,j in zip(num_uni,texto_cent):
            if cifra1==i:
                centena=texto_cent[i-1]
            # decena
        # <10
        if cifra2==0 and cifra3<=9:
            for i,j in zip(num_uni,texto_uni):
                    if cifra3==i:
                        unidad = texto_uni[i-1]
        # decena y unidad [ 11-15]
        if cifra2==1 and cifra3>=1 and cifra3<=5: 
            for i,j in zip(num_uni,texto_un):
                if cifra3==i:
                    unidad = texto_un[i-1]
        # decena y unidad [ 16-19]
        elif cifra2==1 and cifra3>5:
            for i,j in zip(num_uni,texto_dec):
                if cifra2==i:
                    decena = texto_dec[i-1]
                
            for i,j in zip(num_uni,texto_uni):
                if cifra3==i:
                    unidad = texto_uni[i-1]
        # >20           
        elif cifra2>1: 
                    # decena
            for i,j in zip(num_uni,texto_dec):
                if cifra2==i:
                    decena = texto_dec[i-1]
                    # unidad
            for i,j in zip(num_uni,texto_uni):
                if cifra3==i:
                    unidad = texto_uni[i-1]
                    
        if cifra2==0 and cifra3<=9 and cifra3!=0:
            print(centena + " " +unidad)
            
        elif cifra2==1 and cifra3>=1 and cifra3<=5:          
            print(centena + " " +unidad)
            
        elif cifra2!=0 and cifra3!=0:   
            print(centena+" "+decena+" y "+unidad)
        else:
            
            if cifra2!=0 and cifra3==0:
                print(centena+" "+decena)

            elif cifra2==0 and cifra3==0:
                print(centena)

lector_numeros_3cifras(384)
                      
                      



