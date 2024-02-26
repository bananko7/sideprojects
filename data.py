# version 1: 9.57
# with average steps needed for convergence: 459
# web2 word set
import re
file = open("data.txt", "r")
numberslist = []
#print(file.read())
for line in file:
    numbers = []
    match = re.search(r'score: (\d+\.\d+) convergence instances: (\d+) total number of scores: (\d+)', line)
    score = float(match.group(1))
    instances = int(match.group(2))
    total_scores = int(match.group(3))
    numbers = [score, instances, total_scores]
    numberslist.append(numbers)
file.close()
scores = 0
operations = 0
last = 0
weightedscores = []
for a,b,c in numberslist:
    scores += a
    numberofcurrentscores = c - last
    last = c
    weightedscores.append(a*numberofcurrentscores)
answer = []
for i in weightedscores:
    answer.append(i/last)
print(round(sum(answer),2))
print("average steps needed for convergence:",round(last/len(numberslist)))
from english_words import get_english_words_set
print(len(list(get_english_words_set(['gcide'], lower=True))))