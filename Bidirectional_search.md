# L'algorithme de recherche bidirectionnelle  :
est une technique de recherche qui cherche simultanément à partir du nœud de départ et du nœud de destination pour trouver un chemin commun qui relie les deux nœuds.

# Voici les étapes algorithmiques de l'algorithme de recherche bidirectionnelle :

L'algorithme de recherche bidirectionnelle est une technique de recherche qui cherche simultanément à partir du nœud de départ et du nœud de destination pour trouver un chemin commun qui relie les deux nœuds.

Voici les étapes algorithmiques de l'algorithme de recherche bidirectionnelle :

*   Créer deux files d'attente vides : forward_queue et backward_queue.
Ajouter le nœud de départ à forward_queue et le nœud de destination à backward_queue sous forme de listes contenant uniquement le nœud de départ et le nœud de destination, respectivement.
*   Créer deux ensembles vides : forward_visited et backward_visited pour stocker les nœuds visités dans chaque direction.
*   Tant que les deux files d'attente ne sont pas vides, faire :
    *   a. Retirer le premier chemin de forward_queue et stocker le dernier nœud dans forward_node.
    *   b. Si forward_node est égal au nœud de destination ou est présent dans backward_visited, renvoyer la concaténation des chemins forward_path et backward_path renversé.
    *   c. Si forward_node n'a pas encore été visité, ajouter forward_node à forward_visited et ajouter à forward_queue toutes les adjacences de forward_node sous forme de nouveaux chemins.
    *   d. Retirer le premier chemin de backward_queue et stocker le dernier nœud dans backward_node.
    *   e. Si backward_node est égal au nœud de départ ou est présent dans forward_visited, renvoyer la concaténation des chemins forward_path et backward_path.
    *   f. Si backward_node n'a pas encore été visité, ajouter backward_node à backward_visited et ajouter à backward_queue toutes les adjacences de backward_node sous forme de nouveaux chemins.
    
Si les deux files d'attente sont vides et qu'aucun chemin commun n'a été trouvé, renvoyer None ou une valeur indiquant que le chemin n'a pas été trouvé.