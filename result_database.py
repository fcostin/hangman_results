import collections
Result = collections.namedtuple('Result', ['word_length', 'lives', 'outcome', 'method'])

def RES(w, l, o, m=None):
    return Result(w, l, o, m)

"""
these results from wed apr 04
"""

DATA = []

# (1) these results are obvious
for w in range(1, 31 + 1):
    if w in (26, 30): # no words of this length
        continue
    DATA.append(RES(w, 0, 'loss', 'thought'))
    DATA.append(RES(w, 26, 'win', 'thought'))

# (2) these results are from hangman_exclude_cpp's a.out
# specifically, version
#   8b6cba00a531fdc75576c15b9377e18f929350d9
# on friday 6th april
DATA += [
    RES(1, 25, 'loss', 'exclude_bound'),
    RES(2, 21, 'loss', 'exclude_bound'),
    RES(3, 16, 'loss', 'exclude_bound'), # may be improved?
    RES(4, 11, 'loss', 'exclude_bound'), # may be improved?
    RES(5, 8, 'loss', 'exclude_bound'),
    RES(6, 7, 'loss', 'exclude_bound'),
    RES(7, 7, 'loss', 'exclude_bound'),
    RES(8, 5, 'loss', 'exclude_bound'),
    RES(9, 5, 'loss', 'exclude_bound'),
    RES(10, 5, 'loss', 'exclude_bound'),
    RES(11, 5, 'loss', 'exclude_bound'),
    RES(12, 5, 'loss', 'exclude_bound'),
    RES(13, 4, 'loss', 'exclude_bound'),
    RES(14, 4, 'loss', 'exclude_bound'),
    RES(15, 4, 'loss', 'exclude_bound'),
    RES(16, 3, 'loss', 'exclude_bound'),
    RES(17, 3, 'loss', 'exclude_bound'),
    RES(18, 3, 'loss', 'exclude_bound'),
    RES(19, 3, 'loss', 'exclude_bound'),
    RES(20, 2, 'loss', 'exclude_bound'),
    RES(21, 2, 'loss', 'exclude_bound'),
    RES(22, 1, 'loss', 'exclude_bound'),
    RES(23, 2, 'loss', 'exclude_bound'),
    RES(24, 1, 'loss', 'exclude_bound'),
    RES(25, 1, 'loss', 'exclude_bound'),
    RES(27, 1, 'loss', 'exclude_bound'),
    RES(28, 1, 'loss', 'exclude_bound'),
    RES(29, 1, 'loss', 'exclude_bound'),
    RES(31, 0, 'loss', 'exclude_bound'),
]

# these results are from the minimax search code,
# on friday 6th april, using version
# 68c62debc61b9cefd131bc81ab4e49f5c889896f
# from hangmap_cpp's a.out

DATA += [
    RES(2, 24, 'win', 'minimax'),

    RES(3, 22, 'win', 'minimax'),

    RES(4, 20, 'win', 'minimax'),

    RES(5, 19, 'win', 'minimax'),

    RES(6, 15, 'win', 'minimax'),

    RES(7, 13, 'win', 'minimax'),

    RES(8, 6, 'loss', 'minimax'), # <5min, 10th April using ea03359afc09c212bf9fade4e2e33483fa824799
    RES(8, 7, 'loss', 'minimax'), # 11min, 10th April using ea03359afc09c212bf9fade4e2e33483fa824799
    # XXX BAD ALLOC for 8 9 after 42 minutes using 68c62debc61b9cefd131bc81ab4e49f5c889896f
    RES(8, 10, 'win', 'minimax'),

    RES(9, 7, 'loss', 'minimax'), # requires roughly 2 hrs of search
    RES(9, 8, 'win', 'minimax'),

    RES(10, 6, 'win', 'minimax'),

    RES(11, 6, 'loss', 'minimax'), # took 23 minutes 20 seconds of search
    RES(11, 7, 'win', 'minimax'),

    RES(12, 6, 'win', 'minimax'),

    RES(13, 4, 'loss', 'minimax'),
    RES(13, 5, 'win', 'minimax'),

    RES(14, 4, 'loss', 'minimax'),
    RES(14, 5, 'win', 'minimax'),

    RES(15, 4, 'loss', 'minimax'),
    RES(15, 5, 'win', 'minimax'),

    RES(16, 3, 'loss', 'minimax'),
    RES(16, 4, 'win', 'minimax'),

    RES(17, 3, 'loss', 'minimax'),
    RES(17, 4, 'win', 'minimax'),

    RES(18, 3, 'loss', 'minimax'),
    RES(18, 4, 'win', 'minimax'),

    RES(19, 3, 'loss', 'minimax'),
    RES(19, 4, 'win', 'minimax'),

    RES(20, 2, 'loss', 'minimax'),
    RES(20, 3, 'win', 'minimax'),

    RES(21, 2, 'loss', 'minimax'),
    RES(21, 3, 'win', 'minimax'),

    RES(22, 1, 'loss', 'minimax'),
    RES(22, 2, 'win', 'minimax'),

    RES(23, 2, 'loss', 'minimax'),
    RES(23, 3, 'win', 'minimax'),

    RES(24, 1, 'loss', 'minimax'),
    RES(24, 2, 'win', 'minimax'),

    RES(25, 1, 'loss', 'minimax'),
    RES(25, 2, 'win', 'minimax'),

    RES(27, 1, 'loss', 'minimax'),
    RES(27, 2, 'win', 'minimax'),

    RES(28, 1, 'loss', 'minimax'),
    RES(28, 2, 'win', 'minimax'),

    RES(29, 1, 'loss', 'minimax'),
    RES(29, 2, 'win', 'minimax'),

    RES(31, 0, 'loss', 'minimax'),
    RES(31, 1, 'win', 'minimax'),
]

# these results are from the minimax search code,
# on thurs 12th april, using version
# fc9808a7fc63da2d29c01c87f36fb26458b5f33b
# from hangmap_cpp's a.out
DATA += [
    RES(8, 8, 'loss', 'minimax'), # 52 minutes search

    RES(7, 8, 'loss', 'minimax'), # 30 minutes search
    RES(7, 9, 'loss', 'minimax'), # 84 minutes search

    RES(6, 8, 'loss', 'minimax'), # 24 minutes search
    RES(6, 9, 'loss', 'minimax'), # 69 minutes search

    RES(5, 9, 'loss', 'minimax'), # 31 minutes search
    RES(5, 10, 'loss', 'minimax'), # 84 minutes search
]

