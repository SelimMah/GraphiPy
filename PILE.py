#Classe Pile

class Pile:
    def __init__(self):
        self.valeur=[]
    def est_vide(self):
        return len(self.valeur)==0
    def empiler(self,v):
        self.valeur.append(v)
    def depiler(self):
        if self.est_vide():
            raise IndexError("la liste est vide")
        return self.valeur.pop()
    
#Classe File avec deux piles
class File:
    def __init__(self):
        self.tete=Pile()
        self.queue=Pile()
    def est_vide(self):
        return self.tete.est_vide() and self.queue.est_vide()
    def enfiler(self,v):
        self.tete.empiler(v)
    def defiler(self):
        if self.queue.est_vide():
            while not self.tete.est_vide():
                self.queue.empiler(self.tete.depiler())
        if self.queue.est_vide():
            raise IndexError("la file est vide")
        return self.queue.depiler()