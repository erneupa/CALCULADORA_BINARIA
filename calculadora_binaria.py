def obtener_valores():
    caracter1 = input("Introduce un primer valor de carácter binario de 8 bits:\n--->")
    caracter2 = input("Introduce un segundo valor de carácter binario de 8 bits:\n--->")
    return caracter1, caracter2

def verificar_validez(caracter1, caracter2):
    if len(caracter1) != 8 or len(caracter2) != 8:
        return False, "Uno o ambos números no tienen exactamente 8 bits."
    
    for char in caracter1 + caracter2:
        if char not in '01':
            return False, "Uno o ambos números contienen caracteres que no son '0' o '1'."
    
    return True, "Los dos números binarios son correctos."

def sumar_binarios(caracter1, caracter2):
    result = [0] * 8
    incremento = "0"
    
    for x in range(7, -1, -1):
        if caracter1[x] == "0" and caracter2[x] == "0":
            if incremento == "1":
                result[x] = "1"
                incremento = "0"
            else:
                result[x] = "0"
        elif caracter1[x] == "0" and caracter2[x] == "1" or caracter1[x] == "1" and caracter2[x] == "0":
            if incremento == "1":
                result[x] = "0"
                incremento = "1"
            else:
                result[x] = "1"
        else:  
            if incremento == "1":
                result[x] = "1"
                incremento = "1"
            else:
                result[x] = "0"
                incremento = "1"
    
    return result, incremento

def restar_binarios(caracter1, caracter2):
    result = [0] * 8
    incremento = "0"
    
    for x in range(7, -1, -1):
        if caracter1[x] == "0" and caracter2[x] == "0":
            if incremento == "1":
                result[x] = "1"
                incremento = "1"
            else:
                result[x] = "1"
        elif caracter1[x] == "0" and caracter2[x] == "1":
            if incremento == "1":
                result[x] = "0"
                incremento = "1"
            else:
                result[x] = "1"
                incremento = "1"
        elif caracter1[x] == "1" and caracter2[x] == "0":
            if incremento == "1":
                result[x] = "0"
                incremento = "1"
            else:
                result[x] = "1"
        else:
            if incremento == "1":
                result[x] = "1"
                incremento = "1"
            else:
                result[x] = "0"
    
    return result

def main():
    caracter1, caracter2 = obtener_valores()
    
    valido, mensaje = verificar_validez(caracter1, caracter2)
    print(mensaje)
    
    if valido:
        pregunta_suma_resta = input("Escribe 's' si quieres sumar o si quieres restar, escribe 'r':\n--->")
        
        if pregunta_suma_resta not in ['s', 'r']:
            print("Solo permite 's' o 'r'.")
        else:
            print("Parámetro correcto")
            
            if pregunta_suma_resta == 's':
                result, acarreo = sumar_binarios(caracter1, caracter2)
                print("La suma es", result, "y el acarreo es", acarreo)
            
            elif pregunta_suma_resta == 'r':
                if caracter2 > caracter1:
                    print("Esta resta no se puede hacer ya que es resultado negativo.")
                else:
                    result = restar_binarios(caracter1, caracter2)
                    print("La resta es", result)
    
if __name__ == "__main__":
    main()
