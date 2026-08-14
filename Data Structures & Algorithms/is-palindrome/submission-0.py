class Solution:
    def isPalindrome(self, s: str) -> bool:
        input_string = ''.join(char for char in s.lower() if char.isalnum())
        i = 0
        j = len(input_string) - 1
        while i <= j:
            if input_string[i] != input_string[j]:
                return False
            i += 1
            j -= 1

        return True