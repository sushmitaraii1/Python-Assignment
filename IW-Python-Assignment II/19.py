# 19. Write a Python class to find validity of a string of parentheses, '(', ')', '{', '}', '[' and ']. These
# brackets must be close in the correct order, for example "()" and "()[]{}" are valid but "[)", "({[)]" and "{{{"
# are invalid


class CheckerSolution:

    @staticmethod
    def is_valid(str1):
        lst, dict1 = [], {"(": ")", "{": "}", "[": "]"}
        for p in str1:
            if p in dict1:
                lst.append(p)
            elif len(lst) == 0 or dict1[lst.pop()] is not p:
                return False
        return len(lst) == 0


print(CheckerSolution().is_valid("()"))
print(CheckerSolution().is_valid("[)"))
print(CheckerSolution().is_valid("{{{"))
print(CheckerSolution().is_valid("{{{}}}[]()"))
