def longest_substring_k_unique(s: str, k: int) -> int:
    if k == 0:
        return 0

    left = 0
    maxLength = 0 
    chars = {}

    for i in range(len(s)):
        char = s[i] 
        if i in chars:
            chars[char] += 1
        else:
            chars[char] = 1 

        while len(chars) > k:
            left_char = s[left]
            chars[left] -= 1 
            if chars[left] == 0:
                del chars[left] 
            left += 1 
        if k ==  len(chars):
            maxLength = max(maxLength, i - left + 1) 
    return maxLength
    # Write your code here
    pass
