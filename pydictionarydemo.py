# Importing PyDictionary module
#from PyDictionary import PyDictionary
# Creating an instance of PyDictionary
#dictionary=PyDictionary()

# Function to calculate Levenshtein distance between two strings
def levenshtein_distance(s1, s2):
    # If the first string is shorter than the second one, swap them
    if len(s1) < len(s2):
        return levenshtein_distance(s2, s1)

    # If the second string is empty, the distance is the length of the first string
    if len(s2) == 0:
        return len(s1)

    # Initialize the previous row of distances
    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        # Initialize the current row of distances
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            # Calculate insertions, deletions and substitutions
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            # Append the minimum value to the current row
            current_row.append(min(insertions, deletions, substitutions))
        # Set the current row as the previous row for the next iteration
        previous_row = current_row
    
    # Return the last element of the previous row which is the Levenshtein distance
    return previous_row[-1]

# Function to calculate similarity score between two strings
def similarity_score(s1, s2):
    # Calculate the maximum length between the two strings
    max_len = max(len(s1), len(s2))
    # If the maximum length is 0, return 10
    if max_len == 0:
        return 10
    # Calculate the Levenshtein distance
    distance = levenshtein_distance(s1, s2)
    # Normalize the distance
    normalized_distance = distance / max_len
    # Calculate the similarity
    similarity = 1 - normalized_distance
    # Calculate the score
    score = similarity * 10
    # Return the score
    return score

# Test the similarity_score function
#while(input("do you want to continue?")=="yes" or input("do you want to continue?")=="y" or input("do you want to continue?")=="Yes"):
#    print("similarity score from 1 to 10",similarity_score(input("string 1:"),input("string 2:")))