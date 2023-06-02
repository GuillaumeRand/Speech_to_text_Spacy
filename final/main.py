import pandas as pd
import spacy
import sys
import os
sys.path.append(os.path.abspath("D:\\Users\\Documents\\Dev\\Python\\T-AIA-901-MPL_7\\audio"))
sys.path.append(os.path.abspath("D:\\Users\\Documents\\Dev\\Python\\T-AIA-901-MPL_7\\dijkstra"))
import speechToText
import dijkstra

nlp = spacy.load("D:\\Users\\Documents\\Dev\\Python\\T-AIA-901-MPL_7\\spacy\\output\\model-best")


print("""
 ________                                       __                         
|        \                                     |  \                        
 \$$$$$$$$______   ______  __     __   ______  | $$                        
   | $$  /      \ |      \|  \   /  \ /      \ | $$                        
   | $$ |  $$$$$$\ \$$$$$$\\$$\ /  $$|  $$$$$$\| $$                        
   | $$ | $$   \$$/      $$ \$$\  $$ | $$    $$| $$                        
   | $$ | $$     |  $$$$$$$  \$$ $$  | $$$$$$$$| $$                        
   | $$ | $$      \$$    $$   \$$$    \$$     \| $$                        
    \$$  \$$       \$$$$$$$    \$      \$$$$$$$ \$$                        
  ______                   __                                              
 /      \                 |  \                                             
|  $$$$$$\  ______    ____| $$  ______    ______                           
| $$  | $$ /      \  /      $$ /      \  /      \                          
| $$  | $$|  $$$$$$\|  $$$$$$$|  $$$$$$\|  $$$$$$\                         
| $$  | $$| $$   \$$| $$  | $$| $$    $$| $$   \$$                         
| $$__/ $$| $$      | $$__| $$| $$$$$$$$| $$                               
 \$$    $$| $$       \$$    $$ \$$     \| $$                               
  \$$$$$$  \$$        \$$$$$$$  \$$$$$$$ \$$                               
 _______                                 __                                
|       \                               |  \                               
| $$$$$$$\  ______    _______   ______  | $$ __     __   ______    ______  
| $$__| $$ /      \  /       \ /      \ | $$|  \   /  \ /      \  /      \ 
| $$    $$|  $$$$$$\|  $$$$$$$|  $$$$$$\| $$ \$$\ /  $$|  $$$$$$\|  $$$$$$
| $$$$$$$\| $$    $$ \$$    \ | $$  | $$| $$  \$$\  $$ | $$    $$| $$   \$$
| $$  | $$| $$$$$$$$ _\$$$$$$\| $$__/ $$| $$   \$$ $$  | $$$$$$$$| $$      
| $$  | $$ \$$     \|       $$ \$$    $$| $$    \$$$    \$$     \| $$      
 \$$   \$$  \$$$$$$$ \$$$$$$$   \$$$$$$  \$$     \$      \$$$$$$$ \$$      
                                                                           
                                                                           
                                                                           
""")



value = speechToText.recording()

doc = nlp(value)
print(doc)
# spacy.displacy.render(doc, style="ent", jupyter=True)

# Récupération du départ et de l'arrivée
destination = ''
depart = ''
for ent in doc.ents:
    if (ent.label_ == 'DESTINATION'):
        destination = str(ent.text).upper()
        continue
    if (ent.label_ == 'DEPART'):
        depart = str(ent.text).upper()

print(destination, depart)

#region dijkstra
# Création du graphique Dijkstra
init_graph = {}
nodes = dijkstra.get_all_locations()
for node in nodes:
    init_graph[node] = {}

df = pd.read_csv('D:\\Users\\Documents\\Dev\\Python\\T-AIA-901-MPL_7\\dijkstra\\clearData.csv')
for index, row in df.iterrows():
    init_graph[str(row['depart']).upper()][str(row['destination']).upper()] = row['duree']

graph = dijkstra.Graph(nodes, init_graph)



# Recherche du chemin le plus rapide
print('Départ : ', depart , ' Destination : ', destination)
previous_nodes, shortest_path = dijkstra.dijkstra_algorithm(graph, depart)
dijkstra.print_result(previous_nodes, shortest_path, depart, destination)
#endregion