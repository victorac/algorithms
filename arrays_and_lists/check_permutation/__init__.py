def check_permutation(string_1: str, string_2: str) -> bool:
    """Time O(n) Space O(n)"""
    counts = {}
    for w in string_1:
        counts[w] = counts.get(w, 0) + 1

    for w in string_2:
        if w in counts:
            counts[w] = counts[w] - 1
        else:
            return False
        if counts[w] == 0:
            del counts[w]
    
    if len(counts) == 0:
        return True
    return False

def check_permutation_brute(string_1: str, string_2: str) -> bool:
    """Time O(n^2) Space O(1)"""
    if len(string_1) != len(string_2): 
        return False
    for ch in string_1:
        if ch not in string_2:
            return False
    return True