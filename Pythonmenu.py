print (chr(27)+"[0;36m"+"Desarrollado por MBD")
print (30 * '-')
print ("   M A I N - M E N U")
print (30 * '-')
print ("1. Numeros a ingresar para el LOTO")
print ("2. QUINI 6")
print ("3. Area de triangulo")
print ("4. Jugando con numpy")
print ("5. Recursividad")
print ("6. Medicion de distancias desde Buenos Aires")
print ("7. Barra de progreso")
print ("8. Log")
print ("9. Generador de password")
print (30 * '-')

import random
import numpy as np
from datetime import datetime
import string

###########################
## Error handling  ##
## Only accepts integers       ##
###########################
## Wait for valid input in while...not ###
is_valid = 0

while not is_valid :
        try :
                choice = int ( input('Enter your choice [1-9] : ') )
                is_valid = 1 ## set it to 1 to validate input and to terminate the while..not loop
        except ValueError as e :
            print ("'%s' is not a valid integer." % e.args[0].split(": ")[1])

### Take action as per selected menu-option ###
if choice == 1: #Loto -- 6 Numeros para elegir para el Loto
        print ("Numeros para el Loto------")
        def getNums(size):
            nums = []
            for x in range(size):
                num = int(input("Ingresa un numero entero: "))
                nums.append(num)
            return nums
        mynums = getNums(6)
        print("Tus numeros de la Quiniela son los siguientes:", mynums)
        print("Buena suerte!!!")
elif choice == 2:
        print ("QUINI 6 - Numeros random")
        #Quini random numbers
        nums = [] #creamos lista vacia

        balls = [i for i in range(1,46)]
        random.shuffle(balls)
        nums = balls[:6]

        print("Numeros de la suerte:")
        print(nums)
        print("No te olvides de compartir la guita conmigo!")
elif choice == 3:
        print ("Calcula el area de un triangulo")
        #Calculate area of a triangle by Mich
        def calculate_area(base,height):
            area = float(height*base/2)
            return area

        #Demand inputs
        height = float(input("Ingrese la altura: "))
        base = float(input("Ingrese la base: "))
        msg = "El area de su triangulo es: "

        #Print the results
        print(msg + str(calculate_area(height,base)))
elif choice == 4:
        print ("Jugando con numpy -- In progress")
        r = np.arange(36)
        r.resize((6, 6))
        print (r)

        print ('''''')
        r2 = r[:3,:3]
        print (r2)

        print ('''''')
        test = np.random.randint(0, 10, (4,3))
        for i, row in enumerate(test):
            print('row', i, 'is', row)

        #Generando arrays / Nota: las dimensiones se tienen que corresponder con el tamanio
        e = input("Tamano del array: ")
        r = np.arange(int(e))
        f = input("Dimensiones del array x: ")
        g = input("Dimensiones del array y: ")
        r.resize(int(g), int(f))
        print (r)
        print ("Array en diagonal:", np.diag(r))

elif choice == 5:
        print ("Recursividad")
        #Recursividad // Se llega al final de la recursividad cuando n es igual o menor a 0.
        def contador(n):
            if n>0:
                print (n)
                return contador(n-1)
            print ("Booom!!!")

        contador(10)
elif choice == 6:
        print ("---------------Mediciones de distancias")
        import Geoloc #importamos el programita que hicimos
elif choice == 7:
        # Progress bar
        class ProgressBar():
            def __init__(self, width=50):
                self.pointer = 0
                self.width = width

            def __call__(self,x):
                 # x in percent
                 self.pointer = int(self.width*(x/100.0))
                 return "|" + "#"*self.pointer + "-"*(self.width-self.pointer)+\
                        "|\n %d percent done" % int(x)

        if __name__ == '__main__':
            import time, os
            pb = ProgressBar()
            print ("Descarga en proceso")
            for i in range(101):
                os.system('CLS')
                print (pb(i))
                time.sleep(0.01)
            if i == 100:
              print("Finalizado Satisfactoriamente!!!")
elif choice == 8:
        print ("---------------Log")
        i = datetime.now()

        with open('log.txt', 'a+') as f:   #con el metodo with, el archivo se cierra automaticamente
            f.write(("\n------------------Edicion nueva de archivo \nFecha y hora: " + (i.strftime('%Y/%m/%d %H:%M:%S ')) + input("Usuario: ")))
            f.write("\n" + (i.strftime('%Y/%m/%d %H:%M:%S.%f ')[:-5])) #con la \n se cambia de linea el -5 acortamos los milisegundos
            f.write(" " + input("Linea a agregar: "))

        with open('hello.txt', 'r') as f:
            data = f.readlines()


        #Imprimimos palabra por palabra
        print ("Palabra por palabra:")
        for line in data:
            words = line.split()
        print (words)

        #Imprimimos linea por linea
        print ("\nLinea por linea:")
        for line in data:
            print (line)
elif choice == 9:
    #Password Generator
    all_char = string.ascii_letters + string.punctuation + string.digits # Todos los caracteres
    # leters_n_nums = [chr(i) for i in range(97, 123)] + [str(x) for x in range(10)]

    def pass_generator(length):
      leng = length
      password = [] #creamos una lista vacia
      for i in range(leng):
        password.append(random.choice(all_char))
      return "".join(password) #retornamos todos los caracteres a la lista

    length = int(input("Pasword length: "))
    print("Password generada:", pass_generator(length))

else:
        print ("Invalid number. Try again...")




''' To add later
lista1 = ['Rodolfo', 'Maria','Jose']
a = input("Ingresa el nombre: ")
b = [] #Lista vacia para guardar la opcion incorrecta
if a in lista1:
    print ("El nombre " + a + " esta en la lista")
else:
    print ("El nombre " + a + " NO esta en la lista!!!")
    b.append(a) #guardamos la opcion incorrecta a nuestra lista

print ("La lista de valores invalidos es ", b)
'''

