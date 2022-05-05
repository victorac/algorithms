def check_permutation(string_1: str, string_2: str) -> bool:
    return set(string_1) == set(string_2) and len(string_1) == len(string_2)


def check_permutation_brute(string_1: str, string_2: str) -> bool:
    if len(string_1) != len(string_2): 
        return False
    for ch in string_1:
        if ch not in string_2:
            return False
    return True