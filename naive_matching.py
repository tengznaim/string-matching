def naive(string, pattern):
    for i in range(0, len(string)):
        j = 0
        while string[i] == pattern[j]:
            j += 1
            i += 1
            if i == len(string) or j == len(pattern):
                break

        if j == len(pattern):
            print("Match Found Starting from Index {i}".format(
                i=i-len(pattern)))


pattern = "abcdf"
string = "abcdfabcdfabcdf"
naive(string, pattern)
