def elegir_medio(km, kg):
    if kg > 20:
        return "camioneta", "paquete pesado"
    if km <= 6 and kg <= 5:
        return "bicicleta", "distancia corta y paquete ligero"
    if kg <= 1 and km > 10:
        return "dron", "paquete muy ligero y distancia larga"
    if kg <= 10 and km <= 15:
        return "moto", "distancia media y paquete ligero"
    return "camioneta", "distancia larga o paquete pesado"