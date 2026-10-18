"""
Testeur pour entrainement.py

    python3 entrainement.py        -> teste tous les exos
    python3 entrainement.py 5      -> teste seulement l'exo 5
    python3 tests.py solutions     -> teste les corriges
"""

import sys
import importlib
from algo_py import tree, treeasbin

# ----------------------------------------------------------------------
# Arbres (representation lineaire). Chaque arbre existe en Tree (T_...)
# et en TreeAsBin (B_...).
# ----------------------------------------------------------------------
LIN = {
    'LEAF': '(42)',
    'T1':   '(15(3(-6)(10))(8(11(0)(4))(2)(5))(9))',            # TD1 fig. 1
    'T4':   '(12(2(25)(6)(-7))(0(18(1)(8))(9))(4(3)(11)))',     # TD1 fig. 4
    'TL':   '(1(2(6)(7(14(18))(15)))(3(8))(4(9)(10)(11(16)(17))(12))(5(13)))',  # T_levels
    'L1':   '(15(3(-6)(10))(8(2)(11)(5))(9))',                  # exam T_level1
    'L2':   '(15(3(-6)(10))(8(2)(11(0)(4))(5))(9))',            # exam T_level2
    'L3':   '(15(3(10))(14)(8(2)(11)(5))(9))',                  # exam T_level3
    'S1':   '(15(7(3)(2)(2))(5(3)(2))(3(1)(2)))',               # exam Bsum1
    'S2':   '(11(7(3)(2)(2))(5(3)(2))(3(1)(2)))',               # exam Bsum2
    'S3':   '(15(7(3)(2)(2))(5(3)(4))(3(1)(2)))',               # exam Bsum3
    'S4':   '(5(5(2(1)(1))(3(9))))',                            # erreur en profondeur
}
T = {n: tree.from_linear(s) for n, s in LIN.items()}
B = {n: treeasbin.from_linear(s) for n, s in LIN.items()}
NAMES = list(LIN)


def per_tree(values):
    """associe a chaque arbre (dans l'ordre de NAMES) sa valeur attendue"""
    return dict(zip(NAMES, values))


# ----------------------------------------------------------------------
# (numero, nom de la fonction, implementation, cas de test)
# Un cas = (description, arguments, resultat attendu)
# ----------------------------------------------------------------------
def build_cases():
    ex = []

    def on_all(num, fname, impl, values):
        src = T if impl == 'T' else B
        cases = [(n, (src[n],), v) for n, v in per_tree(values).items()]
        ex.append((num, fname, cases))

    on_all(1,  'size_T',   'T', [1, 11, 13, 18, 9, 11, 9, 11, 11, 11, 7])
    on_all(1,  'size_B',   'B', [1, 11, 13, 18, 9, 11, 9, 11, 11, 11, 7])
    on_all(2,  'height_T', 'T', [0, 3, 3, 4, 2, 3, 2, 2, 2, 2, 3])
    on_all(2,  'height_B', 'B', [0, 3, 3, 4, 2, 3, 2, 2, 2, 2, 3])
    on_all(3,  'leaves_T', 'T', [1, 7, 8, 10, 6, 7, 6, 7, 7, 7, 3])
    on_all(3,  'leaves_B', 'B', [1, 7, 8, 10, 6, 7, 6, 7, 7, 7, 3])
    on_all(4,  'width_T',  'T', [1, 5, 7, 8, 5, 5, 4, 7, 7, 7, 3])
    on_all(4,  'width_B',  'B', [1, 5, 7, 8, 5, 5, 4, 7, 7, 7, 3])
    on_all(5,  'level_up', 'T', [True, False, False, False, True, False, False,
                                 True, True, True, False])
    on_all(6,  'check_sum', 'B', [True, False, False, False, False, False, False,
                                  True, False, False, False])

    ex.append((7, 'level_keys_B', [
        ('B_T4, k=%d' % k, (B['T4'], k), v) for k, v in enumerate(
            [[12], [2, 0, 4], [25, 6, -7, 18, 9, 3, 11], [1, 8], []])
    ] + [('B_LEAF, k=0', (B['LEAF'], 0), [42])]))

    on_all(8,  'max_per_level', 'T', [[42], [15, 9, 11, 4], [12, 4, 25, 8],
                                      [1, 5, 13, 17, 18], [15, 9, 11],
                                      [15, 9, 11, 4], [15, 14, 11], [15, 7, 3],
                                      [11, 7, 3], [15, 7, 4], [5, 5, 3, 9]])

    ex.append((9, 'level_of', [
        ('T4, x=%d' % x, (T['T4'], x), v)
        for x, v in [(12, 0), (0, 1), (9, 2), (8, 3), (42, -1)]
    ] + [('S1, x=2', (T['S1'], 2), 2), ('LEAF, x=42', (T['LEAF'], 42), 0)]))

    on_all(10, 'max_arity_B', 'B', [0, 3, 3, 4, 3, 3, 4, 3, 3, 3, 2])

    ex.append((11, 'path_sum', [
        ('B_T1, s=%d' % s, (B['T1'], s), v)
        for s, v in [(12, True), (30, False), (34, True), (33, False),
                     (24, True), (0, False), (38, True)]
    ] + [('B_LEAF, s=42', (B['LEAF'], 42), True),
         ('B_LEAF, s=0', (B['LEAF'], 0), False)]))

    on_all(12, 'external_path_length', 'T', [0, 15, 18, 25, 11, 15, 10,
                                             14, 14, 14, 9])
    on_all(13, 'increasing_levels', 'B', [True, False, False, True, False,
                                          False, False, False, False, False,
                                          False])

    ex.append((14, 'parent_of', [
        ('T4, x=%d' % x, (T['T4'], x), v)
        for x, v in [(12, None), (2, 12), (18, 0), (8, 18), (11, 4), (42, None)]
    ] + [('S1, x=2 (1er en prefixe)', (T['S1'], 2), 7)]))
    return ex


# ----------------------------------------------------------------------
def run(ns, only=None):
    total_ok = total = 0
    todo = []
    for num, fname, cases in build_cases():
        if only is not None and num != only:
            continue
        f = ns.get(fname)
        if f is None:
            print("  ?  exo %2d %-22s introuvable" % (num, fname))
            continue
        fails = []
        not_done = False
        for desc, args, expected in cases:
            try:
                got = f(*args)
            except NotImplementedError:
                not_done = True
                break
            except Exception as e:
                got = "%s: %s" % (type(e).__name__, e)
            if got != expected:
                fails.append((desc, expected, got))
        if not_done:
            todo.append("%d %s" % (num, fname))
            continue
        total += 1
        if fails:
            print("  FAIL exo %2d %-22s %d/%d" % (num, fname,
                  len(cases) - len(fails), len(cases)))
            for desc, exp, got in fails[:3]:
                print("        %-24s attendu %-14r obtenu %r" % (desc, exp, got))
        else:
            total_ok += 1
            print("  OK   exo %2d %s" % (num, fname))
    print("\n  %d/%d fonctions OK" % (total_ok, total))
    if todo:
        print("  A faire : " + ", ".join(todo))


if __name__ == "__main__":
    mod = importlib.import_module(sys.argv[1] if len(sys.argv) > 1 else "entrainement")
    run(vars(mod), int(sys.argv[2]) if len(sys.argv) > 2 else None)
