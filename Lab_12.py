class Ciudad:
    def __init__(self,ciudad):
        self.nombre = ciudad
        self.cph = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    def consumototal(self):
        total = 0
        for i in range(len(self.cph)):
            total += self.cph[i]
        return total
    
    def horapico(self):
        pico = 0
        for i in range(len(self.cph)):
            if self.cph[i] > self.cph[pico]:
                pico = self.cph.index(self.cph[i])
        return pico


class Subestacion:
    def __init__(self):
        self.ciudades = []

    def leerarchivo(self):
        f = open("ciudades.csv","r")
        for i in f:
            fila = i.split(';')
            ciudad = "Ciudad " + str(fila[1])
            c = True
            for x in range(len(self.ciudades)):
                if self.ciudades[x].nombre == ciudad:
                    ciudad = self.ciudades[x]
                    c = False
            if c == True:
                ciudad = Ciudad(ciudad)
                self.ciudades.append(ciudad)
            ciudad.cph[int(fila[0])] = float(fila[2][: -1])
        f.close()

    def mostrarDatos(self):
        for i in range(len(self.ciudades)):
            ciudad = self.ciudades[i]
            print('Nombre:', ciudad.nombre)
            print('Total de Consumo:', ciudad.consumototal())
            print('Hora pico:', ciudad.horapico())
            print('----------------------------------')

s = Subestacion()
s.leerarchivo()
s.mostrarDatos()