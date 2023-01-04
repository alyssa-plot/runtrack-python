def fonction(type, saison):
    if type == "fruits" and saison == "hiver":
        print("orange mandarine kiwi")
    elif type == "fruits" and saison == "ete":
        print("Poire, fraise, cassis")
    elif type == "legumes" and saison == "hiver":
        print("carotte, topinambour, endive")
    elif type == "legumes" and saison == "ete":
        print("artichaut, aubergine,navet")

fonction("fruits","hiver")
fonction("fruits","ete")
fonction("legumes","hiver")
fonction("legumes","ete")