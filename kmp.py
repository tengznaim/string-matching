import random


def kmp(string, pattern):
    prefix_table = [0]*len(pattern)

    curr_longest = 0
    i = 1
    n = len(pattern)

    while i < n:
        if pattern[i] == pattern[curr_longest]:
            curr_longest += 1
            prefix_table[i] = curr_longest
            i += 1
        else:
            if curr_longest != 0:
                curr_longest = prefix_table[curr_longest - 1]
                # i not incremented because we still want to find the possible prefix with char
            else:
                prefix_table[i] = 0
                i += 1
                # no other option, it's a new prefix

    m = len(string)
    i = 0
    j = 0

    while i < m:
        if string[i] == pattern[j]:
            i += 1
            j += 1

        if j == n:
            print("Match found starting from index {i}".format(i=(i-j)))
            j = prefix_table[j-1]

        elif i < m and string[i] != pattern[j]:
            if j != 0:
                j = prefix_table[j-1]
            else:
                i += 1


string = "ffff"
pattern = "fff"
kmp(string, pattern)
# n = len(string)

# for i in range(1, 101):
#     ind_1 = random.randint(0, n)
#     ind_2 = random.randint(0, n)

#     while ind_1 == ind_2:
#         ind_2 = random.randint(0, n)

#     pattern = string[min(ind_1, ind_2):max(ind_1, ind_2)]
#     print("Test {i}: Pattern = {pattern}".format(i=i, pattern=pattern))
#     kmp(string, pattern)
