# 20. Write a Python class to find the three elements that sum to zero
# from a list of n real numbers. Input array : [-25, -10, -7, -3, 2, 4, 8, 10] Output : [[-10, 2, 8], [-7, -3, 10]]

class SumToZero:

    def check(self,num, n):
        result = []
        for i in range(0,n-2):
            for j in range(i+1,n-1):
                for k in range(j+1, n):
                    if (num[i] + num[j] + num[k] == 0):
                        result.append([num[i], num[j], num[k]])
        return result


lst = [-25, -10, -7, -3, 2, 4, 8, 10]
example = SumToZero()
n = len(lst)
print(example.check(lst, n))