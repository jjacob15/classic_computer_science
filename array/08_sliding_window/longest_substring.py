# the dictionary holds the position of the character
# if the char doesn't exist set the char and postion to dict
# compute max size and max of max size and right - left + 1
# else change left as max of left or char pos +1

def longest_unique_substring(s):
    char_map = {} # use the map to keep the postion of char
    left = 0
    max_size = 0
    for right in range(len(s)):
        if s[right] in char_map:
            # if char exists, move left to the max position of the char + 1
            left = max(left,char_map[s[right]] + 1) 
        char_map[s[right]] = right
        max_size = max(max_size, right - left + 1)

    return max_size
