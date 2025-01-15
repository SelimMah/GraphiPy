from classes_graphes import * #On importe classes_graphes
from tkinter import * #Les imporations tkinter
from tkinter import filedialog
from tkinter import tix
from PIL import ImageTk, Image
import tkinter as tk #On importe tkinter dont on change le nom (A telecharger)
import csv #On importe la bibliothéque csv 
import codecs #On importe la bibliothéque csv (A telecharger)
import networkx as nx #On importe la bibliothéque networkx (A telecharger)
import matplotlib.pyplot as plt #On importe la bibliothéque matplotlib (A telecharger)
import pathlib #On importe la bibliothéque pathlib (A telecharger)
import os #On importe os 

#Initialisation 
fenetre = tk.Tk() #On cree la fenetre tkinter
fenetre.title("Graphe") #On nome la fenétre tkinter
fenetre.geometry("1600x1000") # Définie la taille de la fenétre tkinter
fenetre.configure(bg="#0C1739") # couleur

#Réinitialisation
files_T1 = os.listdir('img/Hist/') #On récupere les documents qui se trouve dans le fichier hist pour les supprimer  
for file in files_T1: #Parcour le fichier
    os.remove('img/Hist/'+file) #Supprime les docs
    
# Données "permanente", commune a plusieur fonctions
Données=[0,0] # Une liste de 2 élements qui va prendre les spécifications de l'affichage
Données_Temp=[] # Une liste de 2 élements qui va permetre l'affichage d'un refresh
files = [] # Une liste contenent le nom de plusieur documents, et qui servira pour l'historique 
files_1 = [] # Une liste contenent le nom de plusieur documents
LT_Hist = [0] # Une liste qui permet le bon fonctionnement des fonctions hist
LT_Hist2 = [] # Une liste qui permet le bon fonctionnement des fonctions hist
L_Hist = 0 #Un variable qui permet le bon fonctionnement des fonctions hist 

#Fonctions Tkinter      
def GetFiles(): #Permet la selection du fichier csv
    filename = filedialog.askopenfilename(initialdir="CSV/",filetypes=[("Image Files", ".csv")]) #Permet de selectinner uniquement les docs .csv et de comencer dans le fichier "CVS"
    Données[0]=filename # La premier valeur contenue dans Données 'spécifé precedament' prend comme valeur le chemin du fichier csv
    return Données #Données est modifié


def GetAff(Aff): #Permet la selection de L'affichage du graph selon la valeur envoyé par le menu selection
    if Aff == 0: #l'élement d'indice 1 dans Données devient le type d'affichage; a savoir Dictionaire, Graph,ou les deux
        Données[1]="Dictionaire"
        return Données #Données est modifié
    elif Aff == 1:
        Données[1]="Graph"
        return Données #Données est modifié
    elif Aff == 2:
        Données[1]="Dictionaire + Graph"
        return Données #Données est modifié

def Creat(): #Cette fontion fait l'intermédiaire entre le bouton creat et les différentes fontion qui permettent l'aff du graph 
    for i in Données:
        assert i != 0 ,"Fichier ou affichage non mensionné" #On vérifie que Données est bien remplie
    
    while Données_Temp!=[]: #On Suprime les élément de Données_Temp 
        Données_Temp.pop(0)

    for i in Données: #On copie Données dans Données_Temp   
        Données_Temp.append(i)
    
    if Données[1] == "Dictionaire": #Si l'aff selectionné est Dictionaire On fait appel a Graph_D dont la valeur est mise dans la zone text
        text.delete('1.0', END)#On suprime le text contenue dans la zone de text
        text.insert(INSERT, Graph_D(Données[0]))
        
        Img_T("Img/NoSing.jpg",840,60,650) #On fait appel a la fontion Img_T
        
    elif Données[1] == "Graph": #Si l'aff selectionné est Graph On fait appel a Graph_G qui remplacera l'image prédéfinie ou deja mise en place
        text.delete('1.0', END)#On suprime le text contenue dans la zone de text
        text.insert(INSERT, "No Data")
        
        Graph_G(Données[0]) #On fait appel a la fontion Graph_G avec le fichier csv spécifié par l'utilisateur
        
        Img_T("Img/Temp/Graphe.png",840,60,650) #On fait appel a la fontion Img_T  
        
        LT_Hist2.append(Graph_D(Données[0])) #On ajoute le dictionaire du graph dans la liste hist 
        
    else: #Si l'aff selectionné est Graph+Dictionaire On fait appel a Graph_D et Graph_G 
        text.delete('1.0', END) #On suprime le text contenue dans la zone de text
        text.insert(INSERT, Graph_D(Données[0])) #la valeur est mise dans la zone text
        
        Graph_G(Données[0]) #On fait appel a la fontion Graph_G avec le fichier csv spécifié par l'utilisateur
        
        Img_T("Img/Temp/Graphe.png",840,60,650) #On fait appel a la fontion Img_T
        
        LT_Hist2.append(Graph_D(Données[0]))#On ajoute le dictionaire du graph dans la liste hist 
        
    Img_T("Img/NoSing.jpg",60,500,400) #On fait appel a la fontion Img_T
    
    text2.delete('1.0', END) #On suprime le nom du fichier affiché dans l'historique 
    text2.insert(INSERT, "No Data")
    
    return Données_Temp , Données,LT_Hist2 #Données,Données_Temp et LT_Hist2 sont modifiées


def Refresh(): #Cette fonction est un miroire de la fonction Creat cependant elle n'utilise pas "Données" mais "Données_Temp" 
    assert len(Données_Temp) != 0,"Aucun Graph crée" #On vérifie que Données_Temp est bien remplie
    
    if Données_Temp[1] == "Graph": #Si l'aff selectionné est Graph On fait appel a Graph_G qui remplacera l'image prédéfinie ou deja mise en place
        
        text.delete('1.0', END)#On suprime le text contenue dans la zone de text
        text.insert(INSERT, "No Data")
        
        Graph_G(Données_Temp[0]) #On fait appel a la fontion Graph_G avec le fichier csv spécifié par l'utilisateur
        
        Img_T("Img/Temp/Graphe.png",840,60,650) #On fait appel a la fontion Img_T  
        
        LT_Hist2.append(Graph_D(Données_Temp[0])) #On ajoute le dictionaire du graph dans la liste hist 
        
    elif Données_Temp[1] == "Dictionaire": #Si l'aff selectionné est Dictionaire On fait appel a Graph_D dont la valeur est mise dans la zone text
        text.delete('1.0', END) #On suprime le text contenue dans la zone de text
        text.insert(INSERT, Graph_D(Données_Temp[0]))
        
        Img_T("Img/NoSing.jpg",840,60,650) #On fait appel a la fontion Img_T
        
        
    else:
        text.delete('1.0', END) #On suprime le text contenue dans la zone de text
        text.insert(INSERT, Graph_D(Données_Temp[0])) #la valeur est mise dans la zone text
        Graph_G(Données_Temp[0]) #On fait appel a la fontion Graph_G avec le fichier csv spécifié par l'utilisateur
        
        Img_T("Img/Temp/Graphe.png",840,60,650) #On fait appel a la fontion Img_T
        
        LT_Hist2.append(Graph_D(Données_Temp[0])) #On ajoute le dictionaire du graph dans la liste hist 
    
    Img_T("Img/NoSing.jpg",60,500,400) #On fait appel a la fontion Img_T
    
    text2.delete('1.0', END) #On suprime le nom du fichier affiché dans l'historique 
    text2.insert(INSERT, "No Data")
        
    return Données_Temp

def Hist():
    while files!=[]: #On suprime les éléments contenue dans "files"
        files.pop(0)
    
    initial_count = 0  # On vérifie le nombre de docs contenue dans le fichier historique
    for path in pathlib.Path("Img/Hist").iterdir():
        if path.is_file():
            initial_count += 1
            
    assert initial_count != 0,"Historique vide" #On verifie que l'Historique n'est pas vide
    
    L_Hist = LT_Hist[0] 
    files_T = os.listdir('img/Hist/') 
    for file in files_T: #On met les noms des docs contenue dans le fichier Historique dans la liste file
        files.append(file)
        
    files.sort(key = len) #Permet de trier la liste des fichier selon leurs longeur, pour palier au problem de windows
    
    Img_T("Img/NoSing.jpg",840,60,650) #On fait appel a la fontion Img_T
    
    Img_T('img/Hist/'+files[L_Hist],60,500,400) #On affiche le graph du dernier fichier visité dans l'historique 
    
    if L_Hist != 0: #On fait correspondre au graph son dictionnaire contenue dans L_Hist
        text.delete('1.0', END)
        text.insert(INSERT, Graph_D(LT_Hist2[0]))
    
    text2.delete('1.0', END) #On aff le nom du dernier fichier visité dans l'historique 
    text2.insert(INSERT, files[L_Hist])
        
    return files,LT_Hist,L_Hist #files,LT_Hist et L_Hist sont modifié 

def retour(): #Fontion qui permet le parcour de l'historique en revenant en arriere
    
    L_Hist = LT_Hist[0]
    assert L_Hist != 0,"vous etes deja au premier fichier" #On verifie qu'on n'est pas au premier fichier
    
    if L_Hist != 0: #On vérifie qu'on est pas au debut de l'historique
        L_Hist += -1
    LT_Hist[0] = L_Hist 
    
    Img_T('img/Hist/'+files[L_Hist],60,500,400)#On affiche le graph précedent  

    if len(LT_Hist2) != 1: #On affiche le dictionnaire qui correspond au graph précedent  
        text.delete('1.0', END)
        text.insert(INSERT, LT_Hist2[L_Hist])
    
    text2.delete('1.0', END)#On aff le nom du doc précedent
    text2.insert(INSERT, files[L_Hist])
    
    return L_Hist,LT_Hist

def suivant():#Fontion inverse de retour qui permet le parcour de l'historique vers l'avant
    
    L_Hist = LT_Hist[0]
    assert L_Hist != len(files),"vous etes au dernier fichier" #On verifie qu'on n'est pas au dernier fichier 
    
    if L_Hist != len(files): #On vérifie qu'on est pas a la fin de l'historique
        L_Hist += 1
    LT_Hist[0] = L_Hist
    
    Img_T('img/Hist/'+files[L_Hist],60,500,400) #On affiche le graph suivant
    
    if len(LT_Hist2) != 1: #On affiche le dictionnaire qui correspond au graph suivant
        text.delete('1.0', END)
        text.insert(INSERT, LT_Hist2[L_Hist])
    
    text2.delete('1.0', END) #On aff le nom du doc suivant
    text2.insert(INSERT, files[L_Hist])
    
    return L_Hist,LT_Hist #LT_Hist et L_Hist sont modifiés

def Img_T(Img,x,y,d): #Permet d'afficher une image selon le chemin de l'image , les coordonées et la taille souhaité 
    image = Image.open(Img)
    resize_image = image.resize((d, d)) #On redimensionne l'image
    photo = ImageTk.PhotoImage(resize_image)
    img_label = tk.Label(image=photo)
    img_label.image = photo
    
    img_label.place(x=x, y=y) #place l'image selon les coor x et y

#Fonctions Autre
def Dic_GNN(enr2):#Transforme le fichier csv en un dictionnaire de GNN 
    GL = Graphe()
    for o in enr2:
        GL.ajoutArete(o[0],o[1])
    return GL #On renvoi de dictionnaire
        
def Dic_GON(enr2): #Transforme le fichier csv en un dictionnaire de GON 
    GL = GrapheOr()
    for o in enr2:
        GL.ajoutArc(o[0],o[1])
    return GL #On renvoi de dictionnaire 
        
def Dic_GOP(enr2): #Transforme le fichier csv en un dictionnaire de GOP 
    GL = GraphePondereOr()
    for o in enr2:
        GL.ajoutArc(o[0],o[1],float(o[2]))
    return GL #On renvoi de dictionnaire

def Graph_D(fichier): #On vérichie le type du graph selon le fichier csv pour obtenir son aff en dictionnaire
    le=list(csv.reader(codecs.open(fichier)))
    enr2=le[1:]
    if le[0] == ['G', 'N', 'N']: #Graph non orienté non pondéré
        return Dic_GNN(enr2) # On fait appel a Dic_GNN
        
    elif le[0] == ['G', 'O', 'P']: #Graph  orienté  pondéré
        return Dic_GOP(enr2) # On fait appel a Dic_GOP
        
    elif le[0] == ['G', 'O', 'N']:#Graph  orienté  non pondéré
        return Dic_GON(enr2) # On fait appel a Dic_GON
    
def Graph_G(fichier): #On vérichie le type du graph selon le fichier csv pour obtenir son aff en img
    le=list(csv.reader(codecs.open(fichier)))
    enr2=le[1:]
    if le[0] == ['G', 'N', 'N']: #Graph non orienté non pondéré
        return networkx_GNN(Dic_GNN(enr2)) # On fait appel a networkx_GNN
        
    elif le[0] == ['G', 'O', 'P']: #Graph  orienté  pondéré
        return networkx_GOP(Dic_GOP(enr2)) # On fait appel a networkx_GOP
        
    elif le[0] == ['G', 'O', 'N']: #Graph  orienté  non pondéré
        return networkx_GON(Dic_GON(enr2)) # On fait appel a networkx_GON      

def networkx_GOP(G2): #Permet la création d'un graph GOP
    
    g= nx.DiGraph()
    plt.figure().clear()

    arcs= [] #On ajoute les arc du graph dans une liste
    for i in G2.dic:
        for t in G2.dic[i]:
            arcs.append([i,t,G2.dic[i][t]])

    g.add_weighted_edges_from(arcs) #On définie les parramétre d'aff de networkx
    pos=nx.spring_layout(g)
    nx.draw(g,pos,with_labels=True,node_color='lightgrey',
            node_size=600,font_weight='bold')

    edge_weight=nx.get_edge_attributes(g,'weight')  
    nx.draw_networkx_edge_labels(g, pos, edge_labels = edge_weight)

    initial_count = 0 #On compte le nombre de docs dans le fichier Historique pour pouvoir nommé l'image
    for path in pathlib.Path("Img/Hist").iterdir():
        if path.is_file():
            initial_count += 1
    
    filename = 'Graphe_'+str(initial_count)+'.png' #On définie le nom de l'img qui sera enregisté dans l'historique
    plt.savefig('img/Hist/'+ filename, format="PNG")#On enregistre l'image dans l'historique
    plt.savefig('img/Temp/Graphe.png', format="PNG")#On enregistre l'image temporairement dans le fichier temporaire 

    
def networkx_GNN(G2): #Permet la création d'un graph GNN 
    sommets=[] #On ajoute les sommets du graph dans une liste
    for i in G2.dic:
        sommets.append(i)
    
    aretes=[] #On ajoute les aretes du graph dans une liste
    for i in G2.dic:
        for t in G2.dic[i]:
            aretes.append([i,t])
           
    g2= nx.Graph()
    plt.figure().clear()
    g2.add_nodes_from(sommets) #On définie les sommets du graph
    g2.add_edges_from(aretes) #On définie les aretes du graph
    
    nx.draw(g2, with_labels=True, font_weight='bold', #On définie les parramétre d'aff de networkx
        node_size=800, node_color= 'lightgrey')
    plt.get_current_fig_manager().set_window_title('titre')
    
    initial_count = 0 #On compte le nombre de docs dans le fichier Historique pour pouvoir nommé l'image
    for path in pathlib.Path("Img/Hist").iterdir():
        if path.is_file():
            initial_count += 1
    
    filename = 'Graphe_'+str(initial_count)+'.png' #On définie le nom de l'img qui sera enregisté dans l'historique
    plt.savefig('img/Hist/'+ filename, format="PNG") #On enregistre l'image dans l'historique
    plt.savefig('img/Temp/Graphe.png', format="PNG") #On enregistre l'image temporairement dans le fichier temporaire 
    
def networkx_GON(G2): #Permet la création d'un graph GON 
    
    sommets=[] #On ajoute les sommets du graph dans une liste
    for i in G2.dic:
        sommets.append(i)
    
    aretes=[] #On ajoute les aretes du graph dans une liste
    for i in G2.dic:
        for t in G2.dic[i]:
            aretes.append([i,t])
    
    G = nx.MultiDiGraph()
    plt.figure().clear()
    G.add_nodes_from(sommets) #On définie les sommets du graph
    G.add_edges_from(aretes) #On définie les aretes du graph

    nx.draw(G, with_labels=True, font_weight='bold', node_size=800, node_color='lightgrey') #On définie les parramétre d'aff de networkx
    initial_count = 0
    for path in pathlib.Path("Img/Hist").iterdir():
        if path.is_file():
            initial_count += 1
    
    filename = 'Graphe_'+str(initial_count)+'.png' #On définie le nom de l'img qui sera enregisté dans l'historique
    plt.savefig('img/Hist/'+ filename, format="PNG") #On définie le nom de l'img qui sera enregisté dans l'historique
    plt.savefig('img/Temp/Graphe.png', format="PNG") #On enregistre l'image temporairement dans le fichier temporaire 


# Menu
menubar = Menu(fenetre) #Création de la barre de menu "Fichier"
menufichier = Menu(menubar,tearoff=0)
menufichier.add_command(label="fichier CSV",command=lambda:GetFiles()) #L'onglet fichier CSV fait appel a la fontion GetFiles défini précédemment  
menubar.add_cascade(label="Fichier", menu=menufichier)

menuaide = Menu(menubar,tearoff=0) #Création de la barre de menu "Affichage"
menuaide.add_command(label="Dictionaire",command=lambda:GetAff(0)) #L'onglet "Dictionaire" fait appel a la fontion GetAff avec "0" comme attribue
menuaide.add_command(label="Graph",command=lambda:GetAff(1)) #L'onglet "Graph" fait appel a la fontion GetAff avec "1" comme attribue
menuaide.add_command(label="Dictionaire + Graph",command=lambda:GetAff(2)) #L'onglet "Dictionaire + Graph" fait appel a la fontion GetAff avec "2" comme attribue
menubar.add_cascade(label="Affichage", menu=menuaide)



fenetre.config(menu=menubar)

#Img
image = Image.open("Img/NoSing.jpg") #On définie une image de base au lancemant du programe
resize_image = image.resize((650, 650)) #On redimensionne l'image
photo = ImageTk.PhotoImage(resize_image)
img_label = tk.Label(image=photo)
img_label.image = photo 

img_label.place(x=840, y=60) #On place l'image selon x et y 

image2 = Image.open("Img/NoSing.jpg") #On définie une image de base au lancemant du programe
resize_image2 = image2.resize((400, 400)) #On redimensionne l'image
photo = ImageTk.PhotoImage(resize_image2)
img_label = tk.Label(image=photo)
img_label.image = photo 

img_label.place(x=60, y=500) #On place l'image selon x et y 

#F39C12
#button
bouton_refresh = Button(fenetre,text="Refresh",width=35,height=2,bg="#F39C12",command=lambda:Refresh()) #Le bouton "Refresh" fait appel a la fontion Refresh défini précédemment  
bouton_refresh.place(x=1240, y=750) #On place le bouton selon x et y 
bouton_Hist= Button(fenetre,text="Hist",width=35,height=2,bg="#F39C12",command=lambda:Hist()) #Le bouton "Hist"" fait appel a la fontion Hist défini précédemment 
bouton_Hist.place(x=840, y=750) #On place le bouton selon x et y 
bouton_comme_Creat= Button(fenetre,text="Creat",width=35,height=2,bg="#F39C12",command=lambda:Creat()) #Le bouton "Creat" fait appel a la fontion Creat défini précédemment 
bouton_comme_Creat.place(x=60, y=400) #On place le bouton selon x et y 
bouton_suivant= Button(fenetre,text="→",width=3,height=12,bg="#F39C12",command=lambda:suivant()) #Le bouton "→" fait appel a la fontion suivant défini précédemment 
bouton_suivant.place(x=480, y=500) #On place le bouton selon x et y 
bouton_retour= Button(fenetre,text="←",width=3,height=12,bg="#F39C12",command=lambda:retour()) #Le bouton "←" fait appel a la fontion retour défini précédemment 
bouton_retour.place(x=480, y=715) #On place le bouton selon x et y
bouton_Destroy= Button(fenetre,text="X",width=3,height=2,bg="#F39C12",command=fenetre.destroy) #Le bouton "Destroy" permet de fermer la fenêtre  
bouton_Destroy.place(x=1500, y=60) #On place le bouton selon x et y 

#afficheur
text=Text(fenetre,bg="#F39C12",width=90,height=20) #On crée une zone de texte
text.insert(INSERT, "No Data")
text.insert(END, ".")
text.place(x=60, y=60) #On place la zone de texte selon x et y 

text2=Text(fenetre,bg="#0C1739",fg='#fff',width=50,height=1) #On crée une zone de texte
text2.insert(INSERT, "No Data")
text2.insert(END, ".")
text2.place(x=60, y=910) #On place la zone de texte selon x et y 

fenetre.mainloop()

print("Nous vous remercions de nous avoir fait confiance ")