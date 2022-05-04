def is_unique(string:str) -> bool:
    """Time O(n), Space O(n)"""
    known_chars = set()
    for ch in string:
        if ch in known_chars:
            return False
        known_chars.add(ch)
    return True


def is_unique_brute(string:str) -> bool:
    """O(n**2), Space O(1)"""
    for i in range(len(string)):
        for j in range(i+1, len(string)):
            if string[i] == string[j]:
                return False
    return True
