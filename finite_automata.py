def generate_transition_table(pattern):
    m = len(pattern)
    unique_char = set(pattern)
    transition_table = [{} for i in range(0, m+1)]

    for i in range(0, m):
        for char in unique_char:
            next_state = 0
            curr = pattern[0:i] + char
            for j in range(0, len(curr)):
                if curr[len(curr)-1-j:len(curr)] == pattern[0:j+1]:
                    next_state = j+1

            transition_table[i][char] = next_state

    print(transition_table)

    return transition_table


def finite_automata(pattern, string):
    transition_table = generate_transition_table(pattern)

    j = 0

    for i in range(0, len(string)):
        char = pattern[j]
        if string[i] == char:
            j = transition_table[j][char]
        if j == len(pattern):
            print(f"Match found beginning from index {i-j+1}")
            break


string = "AABAACAADAABAAABAA"
pattern = "AABA"
finite_automata(pattern, string)
