import string,os
# def arrange(array):
#     array=list(array)
#     output = []
#     if len(array) == 1:
#         return [array]#当数组只有一个元素时直接返回该数组
#     else:
#         for i in array:
#             subArr = array.copy()
#             subArr.remove(i)
#             for j in arrange(subArr):
#                 newArr = [i]+j
#                 output.append(newArr)
#     return output
# a=input()
# b=input()
# c=arrange(a)
# d=[]
# for i in c:
#     i=''.join(i)
#     if i not in d:
#      d.append(i)
# num=0
# for i in d:
#     if i in b:
#         num+=1
# print(num)
#
# from itertools import permutations
# a=input()
# b=input()
# a= permutations(a)
# print(list(a))
# d=[]
# num=0
# for i in a:
#     i=''.join(i)
#     if i not in d:
#       d.append(i)
# for i in d:
#     if i in b:
#         num+=1
# print(num)
# def perm(s=''):
#     if len(s) <= 1:
#         return [s]
#     sl = []
#     for i in range(len(s)):
#         for j in perm(s[0:i] + s[i + 1:]):
#             sl.append(s[i] + j)
#     return sl


# def main():
#     # 可能包含重复的串
#     a=input()
#     b=input()
#     num=0
#     perm_nums = perm(a)
#     no_repeat_nums = list(set(perm_nums))
#     for i in no_repeat_nums:
#         if i in b:
#             num+=1
#     print(num)
# if __name__ == '__main__':
#     main()
