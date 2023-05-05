# UCS (Uniform Cost Search)  :
signifie Recherche du coût uniforme. C'est un algorithme de recherche informée utilisé pour parcourir un graphe ou un arbre de manière à trouver le chemin avec le coût le plus faible. UCS étend la frontière de l'espace de recherche en fonction du coût total du chemin du nœud de départ au nœud actuel, plutôt que de la profondeur du nœud dans l'arbre de recherche comme dans BFS.

# Voici les étapes impliquées dans l'algorithme UCS :

*   Initialisez une file de priorité et insérez le nœud de départ avec un coût de zéro.

*   Créez un ensemble pour suivre les nœuds visités.

*   Tant que la file de priorité n'est pas vide, effectuez ce qui suit :

    *   a. Retirez le nœud avec le coût le plus bas de la file.

    *   b. Si le nœud retiré est le but recherché, retournez le chemin menant au nœud.

    *   c. Sinon, ajoutez le nœud aux nœuds visités et explorez ses voisins.

    *   d. Pour chaque voisin du nœud, calculez le coût du chemin pour y accéder à partir du nœud actuel.

    *   e. Si le voisin n'a pas encore été visité, ajoutez-le à la file de priorité avec le coût total mis à jour.

    *   f. Si le voisin est déjà dans la file de priorité, mais avec un coût plus élevé, mettez à jour son coût dans la file.

    Si la file de priorité est vide et que le nœud but n'a pas été trouvé, alors il n'y a pas de chemin possible.