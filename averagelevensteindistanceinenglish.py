import random
from english_words import get_english_words_set
# Function to calculate Levenshtein distance between two words in english
# uses get_english_words_set(['web2'], lower=True)
# or get_english_words_set(['gcide'], lower=True)
# 234450 words in the web2 set
# 114769 words in the gcide set

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
    #return score
    # return distance
    return round(distance,2)
def get_two_random_words():
    # Convert the set to a list to allow random selection
    words_list = list(get_english_words_set(['gcide'], lower=True)) 
    # return two random words
    return random.choice(words_list), random.choice(words_list)
average_score = 0
numberofscores = 1
convergence = 0
convergence_instances = 0
word1, word2 = get_two_random_words()
#print("Word 1:", word1)
#print("Word 2:", word2)
average_score = round(similarity_score(word1, word2),2)
overallscore = average_score
numberofscorestotal = 0
#print("Similarity Score:", average_score)
while(True):
    numberofscores = 1
    while(True):
        word1, word2 = get_two_random_words()
        #print("Word 1:", word1)
        #print("Word 2:", word2)

        new_average_score = round((average_score*numberofscores + similarity_score(word1, word2))/(numberofscores+1),2)
        if new_average_score == average_score:
            convergence += 1
        else:
            convergence = 0
        average_score = new_average_score
        if convergence == 10:
            break
        numberofscores += 1
        #print("Similarity Score:", similarity_score(word1, word2))
        #print("Average Score:", average_score)
        #print("Levenstein distance:", similarity_score(word1, word2))
        #print("Average Levenstein distance:", average_score)
        #print("Do you want to continue? (yes/no)")
        #if input() == "no":
        #s    break
    convergence_instances += 1
    numberofscorestotal += numberofscores
    overallscore = round((overallscore*numberofscorestotal + average_score)/(numberofscorestotal+1),6)
    print("score:",average_score,"convergence instances:",convergence_instances,"total number of scores:",numberofscorestotal)
# Test the similarity_score function
#while(input("do you want to continue?")=="yes" or input("do you want to continue?")=="y" or input("do you want to continue?")=="Yes"):
#    print("similarity score from 1 to 10",similarity_score(input("string 1:"),input("string 2:")))