# BFS (Breadth-First Search) : 
 signifie Recherche en largeur. C'est un algorithme de recherche non informée utilisé pour parcourir un graphe ou un arbre de manière systématique et à largeur d'abord, c'est-à-dire qu'il explore tous les nœuds d'un niveau avant de passer au niveau suivant.

# Voici les étapes impliquées dans l'algorithme BFS :

* Initialisez une file et insérez le nœud de départ.

* Créez un ensemble pour suivre les nœuds visités.

* Tant que la file n'est pas vide, effectuez ce qui suit :

    *   a. Retirez le premier nœud de la file.

    *   b. Si le nœud retiré est le but recherché, retournez le chemin menant au nœud.

    *   c. Sinon, ajoutez le nœud aux nœuds visités et explorez ses voisins.

    *   d. Pour chaque voisin du nœud, vérifiez s'il a déjà été visité. S'il n'a pas encore été visité, ajoutez-le à la file et marquez-le comme visité.

Si la file est vide et que le nœud but n'a pas été trouvé, alors il n'y a pas de chemin possible.

# DFS (Depth-First Search):  
est un algorithme de recherche de chemin dans un graphe qui explore autant en profondeur que possible avant de revenir en arrière pour explorer d'autres branches. Il commence par un nœud de départ, visite tous les nœuds voisins, puis visite les nœuds voisins de ces nœuds, et ainsi de suite, jusqu'à ce qu'il atteigne le nœud cible ou qu'il n'y ait plus de nœuds à visiter.

L'algorithme utilise une pile pour stocker les nœuds à visiter, en poussant chaque nouveau nœud adjacent sur la pile et en continuant à explorer la branche la plus profonde. Lorsque le nœud cible est atteint, le chemin est retourné. Si le nœud cible n'est pas atteint et qu'il n'y a plus de nœuds à explorer, alors l'algorithme remonte la pile jusqu'à ce qu'un nœud avec des voisins non visités soit trouvé, puis reprend l'exploration à partir de ce nœud.

# diff entre DFS et BFS :
*   DFS explore autant en profondeur que possible avant de revenir en arrière pour explorer d'autres branches. Il commence par un nœud de départ, visite tous les nœuds voisins, puis visite les nœuds voisins de ces nœuds, et ainsi de suite, jusqu'à ce qu'il atteigne le nœud cible ou qu'il n'y ait plus de nœuds à visiter. L'algorithme utilise une pile pour stocker les nœuds à visiter.

*   En revanche, BFS explore en largeur, en visitant tous les voisins d'un nœud avant de passer aux voisins de ces voisins. Il commence par un nœud de départ, visite tous les nœuds voisins, puis visite les voisins de ces nœuds, et ainsi de suite, en utilisant une file d'attente pour stocker les nœuds à visiter.