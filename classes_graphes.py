from math import inf
from PILE import *
import random


#classe de graphe non orienté
class Graphe:
    #Constructeur
    def __init__(self):
        self.dic=dict()
    
    #Mutateurs
    def ajoutSommet(self,a):
        if a not in self.dic:
            self.dic[a]=[]
        
    def ajoutArete(self,a,b):
        if b not in self.dic:
            self.dic[b]=[]
        if a not in self.dic:
            self.dic[a]=[]
        self.dic[a].append(b)
        self.dic[b].append(a)
        
    #Selecteurs
    def voisin(self,a):
        if a in self.dic:
            return self.dic[a]
        else:
            return None
        
    def sommets(self):
        return self.keys()
    
    def ordre(self):
        return len(self.sommets())
    
    def __repr__(self):
        return str(self.dic)
    
    def Matrice(self):
        l = []
        for i in range((len(self.dic))):
            l.append(len(self.dic)*[0])
    
        for t in self.dic:
            for u in self.dic[t]:
                l[t-1][u-1] = 1
    
        for y in l:
            print(y)
            
    def parcours_largeur(self,SM):
        f = File()
        f.enfiler(SM)
        sommets_visités = []
        while not f.est_vide():
            s = f.defiler()
            if s not in sommets_visités:
                sommets_visités.append(s)
                
            VS = self.dic[s]
            for i in VS:
                if i not in sommets_visités and i not in [f]:
                    f.enfiler(i)
        return sommets_visités
    
    def parcours_Profondeur(self,SM):
        sommets_visités = [SM]
        sommets_retenue = []
        p = Pile()
        p.empiler(SM)
        while not p.est_vide():
            voisins = []
            s = p.depiler()
            p.empiler(s)
            for i in self.dic[s]:
                if i not in sommets_visités:
                    voisins.append(i)
            if voisins != []:
                v = random.choice(voisins)
                sommets_visités.append(v)
                p.empiler(v)
            else:
                sommets_retenue.append(s)
                p.depiler()
        return sommets_visités
        
#Graphe orienté
class GrapheOr:
    
    #Constructeur
    def __init__(self):
        self.dic=dict()
    
    #Mutateurs
    def ajoutSommet(self,a):
        if a not in self.dic:
            self.dic[a]=[]
            
    def ajoutArc(self,a,b): #arc de a vers b
        if b not in self.dic:
            self.dic[b]=[]
        if a not in self.dic:
            self.dic[a]=[b]
        else:
            self.dic[a].append(b)
            
    #Selecteurs
    def sommets(self):
        return self.keys()
    
    def ordre(self):
        return len(self.sommets())
    
    def successeurs(self,a):
        if a in self.dic:
            return self.dic[a]
        else:
            return None
        
    def predecesseurs(self,a):
        return [c for c in self.dic.keys() if a in self.dic[c]]
    
    
    def __repr__(self):
        return str(self.dic)
    
    def Matrice2(self):
        l = []
        for i in range((len(self.dic))):
            l.append(len(self.dic)*[0])
    
        for t in self.dic:
            for u in self.dic[t]:
                l[u-1][t-1] = 1
    
        for y in l:
            print(y)
            
    def parcours_largeur2(self,SM):
        f = File()
        f.enfiler(SM)
        sommets_visités = []
        while not f.est_vide():
            s = f.defiler()
            if s not in sommets_visités:
                sommets_visités.append(s)
                
            VS = self.dic[s]
            for i in VS:
                if i not in sommets_visités and i not in [f]:
                    f.enfiler(i)
        return sommets_visités
    
    def parcours_Profondeur2(self,SM):
        sommets_visités = [SM]
        sommets_retenue = []
        p = Pile()
        p.empiler(SM)
        while not p.est_vide():
            voisins = []
            s = p.depiler()
            p.empiler(s)
            for i in self.dic[s]:
                if i not in sommets_visités:
                    voisins.append(i)
            if voisins != []:
                v = random.choice(voisins)
                sommets_visités.append(v)
                p.empiler(v)
            else:
                sommets_retenue.append(s)
                p.depiler()
        return sommets_visités
    
    
#Graphe pondéré
class GraphePondereOr:
    
    #Constructeur
    def __init__(self):
        self.dic=dict()
        
    #Selecteurs
    def sommets(self):
        return self.keys()
    
    def ordre(self):
        return len(self.sommets())
    
    def successeurs(self,a):
        if a in self.dic:
            return self.dic[a]
        else:
            return None
        
    def predecesseurs(self,a):
        return [c for c in self.dic.keys() if a in self.dic[c]]
    
        
    #Mutateurs
    def ajoutSommet(self,a):
        if a not in self.dic:
            self.dic[a]={}
    def ajoutArc(self,a,b,p):
        if a not in self.dic:
            self.dic[a]={}
        if b not in self.dic:
            self.dic[b]={} 
        self.dic[a][b]=p
            
    def __repr__(self):
        return str(self.dic)
    
    def Matrice3(self):
        l = []
        for i in range((len(self.dic))):
            l.append(len(self.dic)*['∞']) #inf

        for t in self.dic:
            for u in self.dic[t]:
                l[u-1][t-1] = self.dic[t][u]
    
        for y in l:
            print(y)
    
    def parcours_largeur3(self,SM):
        f = File()
        f.enfiler(SM)
        sommets_visités = []
        while not f.est_vide():
            s = f.defiler()
            if s not in sommets_visités:
                sommets_visités.append(s)
                
            VS = self.dic[s]
            for i in VS:
                if i not in sommets_visités and i not in [f]:
                    f.enfiler(i)
        return sommets_visités
    
    def parcours_Profondeur3(self,SM):
        sommets_visités = [SM]
        sommets_retenue = []
        p = Pile()
        p.empiler(SM)
        while not p.est_vide():
            voisins = []
            s = p.depiler()
            p.empiler(s)
            for i in self.dic[s]:
                if i not in sommets_visités:
                    voisins.append(i)
            if voisins != []:
                v = random.choice(voisins)
                sommets_visités.append(v)
                p.empiler(v)
            else:
                sommets_retenue.append(s)
                p.depiler()
        return sommets_visités
    
    

    
        