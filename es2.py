
class Atleta:
    def __init__(self, name, age, height, weight, visitaMedica, squadra):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.visitaMedica = visitaMedica
        self.squadra = squadra
    def info(self):
        print("Nome:",self.name,"Età:",self.age,"Altezza:",self.height,"Peso:",self.weight,"Squadra:",self.squadra)
        if self.visitaMedica == True:
            print("L'atleta",self.name,"ha ricevuto la visita medica.")
        if self.visitaMedica == False:
            print("L'atleta",self.name,"non ha ricevuto la visita medica.")

a1 = Atleta("Matteo Zaccarelli", 15, "1.75 m", "70 kg", True, "Reggiana")
a1.info()
a2 = Atleta("Mario Rossi", 22, "1.80 m", "80 kg", False, "Parma")
a2.info()