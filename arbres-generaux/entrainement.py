"""
Entrainement arbres generaux - DFS / BFS
=========================================
Remplace chaque `raise NotImplementedError` par ton code, puis lance :

    python3 entrainement.py        -> teste tout
    python3 entrainement.py 5      -> teste seulement l'exo 5

Regles comme a l'exam : uniquement len, range, min, max, abs et Queue.
L'optimisation est notee -> arrete-toi des que la reponse est connue.

Rappels :
  Tree      : T.key, T.children (liste), T.nbchildren
  TreeAsBin : B.key, B.child (premier fils), B.sibling (frere droit)
  Queue     : Queue(), q.enqueue(e), q.dequeue(), q.isempty()

Convention de hauteur : une feuille a une hauteur 0.
Arbres de test : voir LIN dans tests.py (representation lineaire).
"""

from algo_py import tree, treeasbin
from algo_py.queue import Queue


# ======================================================================
# 1. Taille - DFS                                                (echauffement)
# ======================================================================

def size_T(T):
    """nombre de noeuds de T (Tree)"""
    raise NotImplementedError


def size_B(B):
    """nombre de noeuds de B (TreeAsBin)"""
    raise NotImplementedError


# ======================================================================
# 2. Hauteur - DFS
# ======================================================================

def height_T(T):
    """hauteur de T (feuille -> 0)"""
    raise NotImplementedError


def height_B(B):
    """hauteur de B (feuille -> 0)"""
    raise NotImplementedError


# ======================================================================
# 3. Nombre de feuilles - DFS
# ======================================================================

def leaves_T(T):
    raise NotImplementedError


def leaves_B(B):
    raise NotImplementedError


# ======================================================================
# 4. Largeur - BFS (TD1 ex 2.2)
#    nombre maximum de noeuds sur un meme niveau.
#    Fais une version avec marqueur None et l'autre avec 2 files.
# ======================================================================

def width_T(T):
    raise NotImplementedError


def width_B(B):
    raise NotImplementedError


# ======================================================================
# 5. Level up - BFS (exam B5 2025, 5 pts)
#    chaque niveau contient strictement plus de noeuds que le precedent.
#    level_up(Tree(42)) -> True
# ======================================================================

def level_up(T):
    raise NotImplementedError


# ======================================================================
# 6. Check sum - DFS OBLIGATOIRE (exam B5 2025, 6 pts)
#    la cle de chaque noeud interne = somme des cles de ses fils.
#    Une feuille seule -> True.
# ======================================================================

def check_sum(B):
    raise NotImplementedError


# ======================================================================
# 7. Cles du niveau k - DFS (TreeAsBin)
#    liste des cles a la profondeur k, de gauche a droite (racine = 0).
#    [] si le niveau n'existe pas.  Indice : fonction auxiliaire (B, k, L).
# ======================================================================

def level_keys_B(B, k):
    raise NotImplementedError


# ======================================================================
# 8. Max de chaque niveau - BFS (Tree)
#    max_per_level(T1) -> [15, 9, 11, 4]
# ======================================================================

def max_per_level(T):
    raise NotImplementedError


# ======================================================================
# 9. Niveau de x - BFS (Tree)
#    profondeur du premier x rencontre en largeur, -1 si absent.
# ======================================================================

def level_of(T, x):
    raise NotImplementedError


# ======================================================================
# 10. Arite max - DFS (TreeAsBin)
#     plus grand nombre de fils d'un noeud (feuille seule -> 0).
# ======================================================================

def max_arity_B(B):
    raise NotImplementedError


# ======================================================================
# 11. Chemin de somme s - DFS (TreeAsBin)
#     existe-t-il un chemin racine -> FEUILLE dont la somme des cles vaut s ?
#     Arrete-toi des que tu en trouves un.
# ======================================================================

def path_sum(B, s):
    raise NotImplementedError


# ======================================================================
# 12. Longueur de cheminement externe - DFS (Tree)
#     somme des profondeurs de toutes les feuilles (racine = profondeur 0).
#     LCE(T1) = 2+2+3+3+2+2+1 = 15
# ======================================================================

def external_path_length(T):
    raise NotImplementedError


# ======================================================================
# 13. Niveaux croissants - BFS (TreeAsBin)
#     sur chaque niveau, les cles sont strictement croissantes de gauche
#     a droite (T_levels -> True).
# ======================================================================

def increasing_levels(B):
    raise NotImplementedError


# ======================================================================
# 14. Pere de x - DFS (Tree)
#     cle du pere du premier x rencontre en ordre prefixe.
#     None si x est absent ou si x est la racine.
# ======================================================================

def parent_of(T, x):
    raise NotImplementedError


# ======================================================================
if __name__ == "__main__":
    import sys
    import tests
    tests.run(globals(), int(sys.argv[1]) if len(sys.argv) > 1 else None)
