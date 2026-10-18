"""
Corriges de entrainement.py - a ne regarder qu'apres avoir essaye !
Lancer les tests sur les corriges :  python3 tests.py solutions
"""

from algo_py import tree, treeasbin
from algo_py.queue import Queue


# ======================================================================
# 1. Taille (DFS)
# ======================================================================

def size_T(T):
    s = 1
    for C in T.children:
        s += size_T(C)
    return s


def size_B(B):
    s = 1
    C = B.child
    while C:
        s += size_B(C)
        C = C.sibling
    return s


# ======================================================================
# 2. Hauteur (DFS) - une feuille a une hauteur 0
# ======================================================================

def height_T(T):
    h = -1
    for C in T.children:
        h = max(h, height_T(C))
    return h + 1


def height_B(B):
    h = -1
    C = B.child
    while C:
        h = max(h, height_B(C))
        C = C.sibling
    return h + 1


# ======================================================================
# 3. Nombre de feuilles (DFS)
# ======================================================================

def leaves_T(T):
    if T.nbchildren == 0:
        return 1
    n = 0
    for C in T.children:
        n += leaves_T(C)
    return n


def leaves_B(B):
    if B.child is None:
        return 1
    n = 0
    C = B.child
    while C:
        n += leaves_B(C)
        C = C.sibling
    return n


# ======================================================================
# 4. Largeur (BFS) - nombre max de noeuds sur un meme niveau
# ======================================================================

def width_T(T):
    q = Queue()
    q.enqueue(T)
    q.enqueue(None)
    w, cur = 0, 0
    while not q.isempty():
        T = q.dequeue()
        if T is None:
            w = max(w, cur)
            cur = 0
            if not q.isempty():
                q.enqueue(None)
        else:
            cur += 1
            for C in T.children:
                q.enqueue(C)
    return w


def width_B(B):
    # version 2 files
    q = Queue()
    q.enqueue(B)
    w = 0
    while not q.isempty():
        q_next = Queue()
        cur = 0
        while not q.isempty():
            B = q.dequeue()
            cur += 1
            C = B.child
            while C:
                q_next.enqueue(C)
                C = C.sibling
        w = max(w, cur)
        q = q_next
    return w


# ======================================================================
# 5. Level up (exam B5 2025) - BFS
# ======================================================================

def level_up(T):
    q = Queue()
    q.enqueue(T)
    q.enqueue(None)
    prev, cur = 0, 0
    while not q.isempty():
        T = q.dequeue()
        if T is None:
            if cur <= prev:
                return False
            prev, cur = cur, 0
            if not q.isempty():
                q.enqueue(None)
        else:
            cur += 1
            for C in T.children:
                q.enqueue(C)
    return True


# ======================================================================
# 6. Check sum (exam B5 2025) - DFS
# ======================================================================

def check_sum(B):
    if B.child is None:
        return True
    s = 0
    C = B.child
    while C and check_sum(C):
        s += C.key
        C = C.sibling
    return C is None and s == B.key


# ======================================================================
# 7. Cles du niveau k (au choix BFS ou DFS)
# ======================================================================

def __level_keys(B, k, L):
    """ajoute a L les cles de niveau k du sous-arbre B (B au niveau 0)"""
    if k == 0:
        L.append(B.key)
    else:
        C = B.child
        while C:
            __level_keys(C, k - 1, L)
            C = C.sibling


def level_keys_B(B, k):
    L = []
    __level_keys(B, k, L)
    return L


# ======================================================================
# 8. Max de chaque niveau (BFS)
# ======================================================================

def max_per_level(T):
    q = Queue()
    q.enqueue(T)
    L = []
    while not q.isempty():
        q_next = Queue()
        m = None
        while not q.isempty():
            T = q.dequeue()
            if m is None or T.key > m:
                m = T.key
            for C in T.children:
                q_next.enqueue(C)
        L.append(m)
        q = q_next
    return L


# ======================================================================
# 9. Niveau de x (BFS) - premier x rencontre, -1 si absent
# ======================================================================

def level_of(T, x):
    q = Queue()
    q.enqueue(T)
    q.enqueue(None)
    lvl = 0
    while not q.isempty():
        T = q.dequeue()
        if T is None:
            lvl += 1
            if not q.isempty():
                q.enqueue(None)
        elif T.key == x:
            return lvl
        else:
            for C in T.children:
                q.enqueue(C)
    return -1


# ======================================================================
# 10. Arite max (DFS, TreeAsBin)
# ======================================================================

def max_arity_B(B):
    k, m = 0, 0
    C = B.child
    while C:
        k += 1
        m = max(m, max_arity_B(C))
        C = C.sibling
    return max(k, m)


# ======================================================================
# 11. Chemin de somme s (DFS, TreeAsBin) - racine -> feuille
# ======================================================================

def path_sum(B, s):
    s -= B.key
    if B.child is None:
        return s == 0
    C = B.child
    while C and not path_sum(C, s):
        C = C.sibling
    return C is not None


# ======================================================================
# 12. Longueur de cheminement externe (DFS) - somme des profondeurs des feuilles
# ======================================================================

def __lce(T, d):
    if T.nbchildren == 0:
        return d
    s = 0
    for C in T.children:
        s += __lce(C, d + 1)
    return s


def external_path_length(T):
    return __lce(T, 0)


# ======================================================================
# 13. Niveaux croissants (BFS) - sur chaque niveau, cles strictement
#     croissantes de gauche a droite
# ======================================================================

def increasing_levels(B):
    q = Queue()
    q.enqueue(B)
    q.enqueue(None)
    last = None
    while not q.isempty():
        B = q.dequeue()
        if B is None:
            last = None
            if not q.isempty():
                q.enqueue(None)
        else:
            if last is not None and B.key <= last:
                return False
            last = B.key
            C = B.child
            while C:
                q.enqueue(C)
                C = C.sibling
    return True


# ======================================================================
# 14. Pere de x (DFS, Tree) - cle du pere du premier x en prefixe,
#     None si x absent ou x est la racine
# ======================================================================

def __parent(T, x):
    """retourne (trouve, cle du pere ou None)"""
    for C in T.children:
        if C.key == x:
            return (True, T.key)
        (found, p) = __parent(C, x)
        if found:
            return (True, p)
    return (False, None)


def parent_of(T, x):
    if T.key == x:
        return None
    return __parent(T, x)[1]
