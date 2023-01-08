#les commentaires sont là pour me réperer

def distance(x, y):
  #on calcule la distance parcourue sur un seul jour en descendant aux toilettes, x étant le nombre de marches, 
  #y la hauteur en cm, x 2 car un aller puis un retour = 2
  marche_hauteur = x * y * 2

  #on calcule la distance parcourue par semaine, dans une semaine il y a 7jours
  semaine = marche_hauteur * 7

  #on affiche le résultat
  print(f"Pour {x} marches de {y} cm, le gardien parcours {semaine / 100} m par semaine.") 
  #on divise par 100 pour obtenir le résultat en mètre

#Si on définit qu'il y a 150marches qui font 15cm chacunes, alors:
distance(150, 15)