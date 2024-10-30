def special_str_again(n,s):
# A string is said to be a special string if either of two conditions is met:

# All of the characters are the same, e.g. aaa.
# All characters except the middle one are the same, e.g. aadaa.    

   # Step 1: Create an array to store the count of consecutive characters
   # so aabaa becomes [('a', 2), ('b', 1), ('a', 2)].
   # this DS allows you to count consecutive counts unlike a dictionary and using the formula (count * (count +1 ))//2 will 
   # give you all permutations you can make with that combination.

   # now to find characters with you just need to loop through the above list and find aba and return the min count of either of the 
   # a's. of aabaa give aba or aabaa. If it was  [('a', 2), ('b', 1), ('a', 3)], you take the min to make sure it matches

   # INSIGHT -> counting substrings of similar characters "aaaa" -> 10
   # first you take 4 a,a,a,a
   # count - 1 -> aa,aa,aa
   # count - 2 -> aaa,aaa
   # count -3  -> aaaa
   # this totals to 10. A mathamatially simplified form is (count * (count +1))//2 will give you 10 for 4.
    count = []
    i = 0
    
    while i < n:
        char_count = 1
        while i + 1 < n and s[i] == s[i + 1]:
            char_count += 1
            i += 1
        count.append((s[i], char_count))
        i += 1
    
    # Step 2: Count substrings with all same characters
    total_substrings = 0
    for char, char_count in count:
        total_substrings += (char_count * (char_count + 1)) // 2
    
    # Step 3: Count substrings with one different middle character
    for j in range(1, len(count) - 1): # start from 1
        if count[j][1] == 1 and count[j - 1][0] == count[j + 1][0]: # making sure the bounds don't hit
            total_substrings += min(count[j - 1][1], count[j + 1][1])
    
    return total_substrings