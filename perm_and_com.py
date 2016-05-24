# Challenge #265 [Easy] Permutations and combinations part 1

import itertools

def get_permutations(num_items) :
    """ Returns a list containing all possible arrangements of the integers from
        0 to (num_items - 1). """
    return list(itertools.permutations(range(num_items), num_items))

def get_indexed_permutation(num_items, perm_num) :
    return get_permutations(num_items)[perm_num - 1]

print "The 240th permutation of 6 is", get_indexed_permutation(6,240)
print "The 3,240th permutation of 7 is", get_indexed_permutation(7,3240)

def get_combinations(n, r) :
    """ Returns a list containing all possible combinations of r elements chosen
        from n total elements. """
    return list(itertools.combinations(range(n), r))

def get_indexed_combination(n, r, combo_num) :
    return get_combinations(n,r)[combo_num - 1]

print "24th combination of 3 out of 8:", get_indexed_combination(8,3,24)
print "112th combination of 4 out of 9:", get_indexed_combination(9,4,112)
