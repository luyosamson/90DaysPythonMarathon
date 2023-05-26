def getSmallestString(s: str, k: int) -> str:
    n = len(s)
    t = ['a'] * n  # Initialize t as a string of 'a' with the same length as s
    
    for i in range(n):
        if s[i] != 'a':
            # Calculate the minimum distance needed to make s[i] lexicographically smallest
            distance = (ord('a') + k - ord(s[i])) % 26
            t[i] = chr(ord('a') + distance)  # Apply the minimum distance to t[i]
            k -= distance  # Decrease the remaining allowed distance
            
    return ''.join(t)