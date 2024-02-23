#from PyDictionary import PyDictionary
#dictionary=PyDictionary()
def levenshtein_distance(s1, s2):
    if len(s1) < len(s2):
        return levenshtein_distance(s2, s1)

    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row
    
    return previous_row[-1]

def similarity_score(s1, s2):
    max_len = max(len(s1), len(s2))
    if max_len == 0:
        return 10
    distance = levenshtein_distance(s1, s2)
    normalized_distance = distance / max_len
    similarity = 1 - normalized_distance
    score = similarity * 10
    return score
while(input("do you want to continue?")=="yes" or input("do you want to continue?")=="y" or input("do you want to continue?")=="Yes"):
    print("similarity score from 1 to 10",similarity_score(input("string 1:"),input("string 2:")))