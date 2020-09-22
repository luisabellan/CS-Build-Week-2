# Longest Palindromic Substring:  https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/780/


''' Start with window size = length of the input string
 and check if palindrome, if not, 
decrement the window size, and check all substrings 
of that length- If substring is palindrome, 
return the substring.. if no palindrome found for that window size, 
decrement window size again and repeat. Iterate until palindrome found, 
or window size is 1 (When window size reaches 1, just return
 the first character of the input string) '''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        str_len = len(s)
        p_table = [[0 for col in range(str_len)] for row in range(str_len)]
        # incrementally build up a lookup table, starting
        # with str len 1, up to 3 or more
        # Length 1
        max_len = 1
        idx = 0
        while idx < str_len:
            p_table[idx][idx] = True
            idx += 1
        # Length 2
        idx, start = 0, 0
        while idx < str_len - 1:
            if s[idx] == s[idx + 1]:
                p_table[idx][idx + 1] = True
                start = idx
                max_len = 2
            idx += 1
        # Length 3+
        pal_len = 3  # initialize palindrome len to 3, then work up to length str_len
        while pal_len <= str_len:
            idx = 0
            # Check substring of increasing size to see if they're a palindrome
            # Adjust the max_len if a larger palindromic substring is encountered
            while idx < (str_len - pal_len + 1):
                # Increment the length of the substring to test for pallandrome
                end = idx + pal_len - 1
                # Test if substr from index idx+1 to index-1 end is a pallandrome
                # and if the larger substring from idx to end is also a pallandrome
                if (p_table[idx + 1][end - 1] and s[idx] == s[end]):
                    p_table[idx][end] = True
                    if pal_len > max_len:
                        max_len = pal_len
                        start = idx
                idx += 1
            pal_len += 1
        print(s[start: start + max_len])
        return s[start: start + max_len]

Solution().longestPalindrome('babad')