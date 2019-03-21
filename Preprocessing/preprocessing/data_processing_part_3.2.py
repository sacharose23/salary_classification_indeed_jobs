# Feature Extraction
import pickle
import re

f = open('2.1_data.pkl', 'rb')
data = pickle.load(f)
f.close()

print(data[0])

size = 50#len(data)
dictionary = {"degree":"d"}
patterns = ['bsc', 'msc', 'bs', 'ms', 'phd', 'bachelor', 'master', 'degree', 'diploma']

# ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
print("______________________________________________________")
print("\nFeature Extraction - Degree")
print("\tStep 1: Matching pattern --> (num) (num) (years)")
# ----- ----- ----- ----- ----- ----- ----- ----- ----- -----

#outside_list = []

for i in range(size):
    sentences = data[i]['text']

    matches_set = set()
    for j in range(len(sentences)):
        for pattern in patterns:
            if re.search(pattern, sentences[j]):
                matches_set.add(sentences[j])

    sent_list = list(matches_set)
    sent_str = " ".join(sent_list)
    words = sent_str.split()

    print(words)

    #inside_list = []

    #for j in range(len(words) - 2):
    #    if words[j].isdigit():
    #        if words[j + 1].isdigit():
    #            if words[j + 2] == "years":
    #                inside_list.append([words[j], words[j+1]])
    #                data[i]['f1_flag'] = 1

    #outside_list.append(inside_list)

    #if len(outside_list[i]) > 0:
    #    outside_list[i].sort()
    #    avg = (int(outside_list[i][0][0]) + int(outside_list[i][0][0])) / 2.0
    #    data[i]['f1_value'] = min(avg, 100)
    #    #print(data[i]['f1_value'])
pass


"""
count = 0
for i in range(size):
    if data[i]['f1_flag'] == 1:
        count += 1
print("\n\tStats:")
print("\t\tCount (Total):", size)
print("\t\tCount (Tagged):", count)
print("\t\tPercent (Tagged):", int(count/size*100)) 
"""