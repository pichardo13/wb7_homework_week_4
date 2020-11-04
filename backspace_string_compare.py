"""
https://leetcode.com/problems/backspace-string-compare

Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.
Note that after backspacing an empty text, the text will continue empty.

Example 1:
Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".

Example 2:
Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".

Example 3:
Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".

Example 4:
Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".
"""
def backspaceCompare(S, T):
    stack1 = []
    for ss in S:
        if ss == '#':
            if stack1 != []:
                stack1.pop()
        else:
            stack1.append(ss)
    
    stack2 = []
    for tt in T:
        if tt == '#':
            if stack2 != []:
                stack2.pop()
        else:
            stack2.append(tt)
    
    return stack2 == stack1

print(backspaceCompare('ab#c', 'ad#c'))
print(backspaceCompare('ab##', 'c#d#'))
print(backspaceCompare('a##c', '#a#c'))
print(backspaceCompare('a#c', 'b'))