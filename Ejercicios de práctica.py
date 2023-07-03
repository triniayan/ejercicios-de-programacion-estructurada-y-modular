print("Ejercicios de práctica para la instancia evaLuativa de Programación I")
print("1. Realice un programa que contengan funciones de los tres tipos de triángulos. Los mismos deben estar acompañados de los mensajes respecto a la función decoradora. Para mejorarlo pueden agregar los nombres de cada función según los triángulos.")
print("2. Realizar un programa de funciones que contengan funciones con bucles y control de flujo fuera de la función decoradora. Al menos se deben tener dos condicionales o bucles.")
print("3. Escribir una función que calcule el total de una factura tras aplicarle el IVA. La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la factura. Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%.")
def calcular_total_factura(cantidad_sin_iva, porcentaje_iva=21):
    total = cantidad_sin_iva + (cantidad_sin_iva * porcentaje_iva / 100)
    return total
cantidad=1850 #Cantidad sin IVA
#Caso 1: Se abona la factura con carga impositiva
porcentaje_iva=21
total_factura=calcular_total_factura(cantidad, porcentaje_iva)
print("Total de la factura con {}% de IVA: {}".format(porcentaje_iva, total_factura.))
#Caso 2: Se abona la factura sin carga impositiva
porcentaje_iva=0
total_factura=calcular_total_factura(cantidad, porcentaje_iva)
print("Total de la factura con {}% de IVA: {}".format(porcentaje_iva, total_factura.))
print("4. Escribir una función que convierta un número decimal en los otros dos sistemas: Binario y Hexadecimal. Mostrar mensajes pertenecientes a cada función.")
def funcion_decoradora(funcion):
    def numero(numero_decimal):
        if funcion.__name__ == "decimal_a_binario":
            print("Convirtiendo número decimal a binario...")
        elif funcion.__name__ == "decimal_a_hexadecimal":
            print("Convirtiendo número decimal a hexadecimal...")
        resultado = funcion(numero_decimal)
        return resultado
    return numero
@funcion_decoradora
def decimal_a_binario(numero_decimal):
    return bin(numero_decimal)
@funcion_decoradora
def decimal_a_hexadecimal(numero_decimal):
    return hex(numero_decimal)
def convertir_numero(numero_decimal):
    resultado_binario = decimal_a_binario(numero_decimal)
    resultado_hexadecimal = decimal_a_hexadecimal(numero_decimal)
    print("Número decimal:", numero_decimal)
    print("Número binario:", resultado_binario)
    print("Número hexadecimal:", resultado_hexadecimal)
#Caso 1: Número 42
convertir_numero(42)
#Caso 2: Número 93
convertir_numero(93)