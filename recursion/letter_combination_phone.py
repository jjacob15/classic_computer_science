# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
# A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
# bas
def letterCombinations(digits):
    digit_to_letter = {2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}
    result = []

    def backtrack(index, combinations):
        if index == len(digits):
            if len(combinations) > 0:
                result.append("".join(combinations))
            return
        
        letters = digit_to_letter[int(digits[index])]
        print(index,letters,digits[index])

        for letter in letters:
            print(letter,index)
            combinations.append(letter)
            backtrack(index+1,combinations)
            combinations.pop()

    backtrack(0,[])
    print(result)
    return result


letterCombinations("24")