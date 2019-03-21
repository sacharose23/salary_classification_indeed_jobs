# Feature Extraction
import pickle
import re

# ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
print("______________________________________________________")
print("\nFeature Extraction - Initializing f1,f2,f3")
print("\tCreating f1, f2, f3 flags")
print("\tCreating f1, f2, f3 values")
print("\tDefault values = 100")
# ----- ----- ----- ----- ----- ----- ----- ----- ----- -----

f = open('2_data.pkl', 'rb')
data = pickle.load(f)
f.close()

for i in range(len(data)):
    data[i]['f1_flag'] = 0
    data[i]['f1_value'] = 100

    data[i]['f2_flag'] = 0
    data[i]['f2_value'] = 100

    data[i]['f3_flag'] = 0
    data[i]['f3_value'] = 100

    pass

size = len(data)
dictionary = {"one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9", "ten":"10", "twelve":"12", "fifteen":"15", "twenty":"20", "years’": "years", "yrs":"years", "year":"years"}
patterns = ['experience', 'experence', 'years', 'experience:', 'yrs', 'year']

# ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
print("______________________________________________________")
print("\nExtracting Feature 1 - Experience")
print("\tStep 1: Matching pattern --> (num) (num) (years)")
# ----- ----- ----- ----- ----- ----- ----- ----- ----- -----

outside_list = []

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

    for itr in range(len(words)):
        for key in dictionary.keys():
            if len(key) == len(words[itr]):
                #print(words[itr])
                words[itr] = words[itr].replace(key, dictionary[key])

    inside_list = []

    for j in range(len(words) - 2):
        if words[j].isdigit():
            if words[j + 1].isdigit():
                if words[j + 2] == "years":
                    inside_list.append([words[j], words[j+1]])
                    data[i]['f1_flag'] = 1

    outside_list.append(inside_list)

    if len(outside_list[i]) > 0:
        outside_list[i].sort()
        avg = (int(outside_list[i][0][0]) + int(outside_list[i][0][0])) / 2.0
        data[i]['f1_value'] = min(avg, 100)
        #print(data[i]['f1_value'])
pass

count = 0
for i in range(size):
    if data[i]['f1_flag'] == 1:
        count += 1
print("\n\tStats:")
print("\t\tCount (Total):", size)
print("\t\tCount (Tagged):", count)
print("\t\tPercent (Tagged):", int(count/size*100))

# ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
print("______________________________________________________")
print("\tStep 2: Matching pattern --> (num) (years) (big_list)")
# ----- ----- ----- ----- ----- ----- ----- ----- ----- -----

outside_list = []

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

    for itr in range(len(words)):
        for key in dictionary.keys():
            if len(key) == len(words[itr]):
                #print(words[itr])
                words[itr] = words[itr].replace(key, dictionary[key])

    inside_list = []
    big_list = ["of", "experience", "required", "relevant", "related", "as", "preferred", "with", "combined", "working", "minimum", "building",  "managing", "process", "it", "system", "systems", "demonstrated", "infrastructure", "supporting", "or", "linux", "mac", "windows", "microsoft", "vmware",  "work", "pc", "recent", ";", "professional", "prior", "web", "agency", "plus", "building", "production", "administration", "in"]


    for j in range(len(words) - 2):
        if words[j].isdigit():
            if words[j + 1] == "years":
                if words[j+2] in big_list:
                #if (words[j + 2] == "of") or (words[j + 2] == "experience") or (words[j + 2] == "required") or (words[j + 2] == "relevant") or (words[j + 2] == "related") or (words[j + 2] == "as") or (words[j + 2] == "preferred") or (words[j + 2] == "with") or (words[j + 2] == "combined") or (words[j + 2] == "working") or (words[j + 2] == "minimum"):
                    inside_list.append(words[j])
                    data[i]['f1_flag'] = 1

    outside_list.append(inside_list)

    if len(outside_list[i]) > 0:
        outside_list[i].sort()
        avg = int(outside_list[i][0])
        data[i]['f1_value'] = min(avg, data[i]['f1_value'])
        #print(data[i]['f1_value'])
pass

count = 0
for i in range(size):
    if data[i]['f1_flag'] == 1:
        count += 1
print("\n\tStats:")
print("\t\tCount (Total):", size)
print("\t\tCount (Tagged):", count)
print("\t\tPercent (Tagged):", int(count/size*100))

# ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
print("______________________________________________________")
print("\tStep 3: Matching pattern --> (num) (to) (num)")
# ----- ----- ----- ----- ----- ----- ----- ----- ----- -----

outside_list = []

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

    for itr in range(len(words)):
        for key in dictionary.keys():
            if len(key) == len(words[itr]):
                #print(words[itr])
                words[itr] = words[itr].replace(key, dictionary[key])

    inside_list = []

    for j in range(len(words) - 2):
        if words[j].isdigit():
            if words[j + 1] == "to":
                if words[j+2].isdigit():
                    inside_list.append([words[j], words[j+1]])
                    data[i]['f1_flag'] = 1

    outside_list.append(inside_list)

    if len(outside_list[i]) > 0:
        outside_list[i].sort()
        avg = (int(outside_list[i][0][0]) + int(outside_list[i][0][0])) / 2.0
        data[i]['f1_value'] = min(avg, data[i]['f1_value'])
        #print(data[i]['f1_value'])
pass

count = 0
for i in range(size):
    if data[i]['f1_flag'] == 1:
        count += 1
print("\n\tStats:")
print("\t\tCount (Total):", size)
print("\t\tCount (Tagged):", count)
print("\t\tPercent (Tagged):", int(count/size*100))

# ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
print("______________________________________________________")
print("\tStep 4: Matching pattern --> (minimum) (num) (years)")
# ----- ----- ----- ----- ----- ----- ----- ----- ----- -----

outside_list = []

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

    for itr in range(len(words)):
        for key in dictionary.keys():
            if len(key) == len(words[itr]):
                #print(words[itr])
                words[itr] = words[itr].replace(key, dictionary[key])

    inside_list = []

    for j in range(len(words) - 2):
        if words[j] == "minimum":
            if words[j+1].isdigit():
                if words[j+2] == "years":
                    inside_list.append(words[j+1])
                    data[i]['f1_flag'] = 1

    outside_list.append(inside_list)

    if len(outside_list[i]) > 0:
        outside_list[i].sort()
        avg = int(outside_list[i][0])
        data[i]['f1_value'] = min(avg, data[i]['f1_value'])
        #print(data[i]['f1_value'])
pass

count = 0
for i in range(size):
    if data[i]['f1_flag'] == 1:
        count += 1
print("\n\tStats:")
print("\t\tCount (Total):", size)
print("\t\tCount (Tagged):", count)
print("\t\tPercent (Tagged):", int(count/size*100))

# ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
print("______________________________________________________")
print("\tStep 5: Matching pattern --> (minimum) (of) (num) (years)")
# ----- ----- ----- ----- ----- ----- ----- ----- ----- -----

outside_list = []

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

    for itr in range(len(words)):
        for key in dictionary.keys():
            if len(key) == len(words[itr]):
                #print(words[itr])
                words[itr] = words[itr].replace(key, dictionary[key])

    inside_list = []

    for j in range(len(words) - 2):
        if words[j] == "minimum":
            if words[j+1] == "of":
                if words[j+2].isdigit():
                    #if words[j+3] == "years":
                    inside_list.append(words[j+2])
                    data[i]['f1_flag'] = 1

    outside_list.append(inside_list)

    if len(outside_list[i]) > 0:
        outside_list[i].sort()
        avg = int(outside_list[i][0])
        data[i]['f1_value'] = min(avg, data[i]['f1_value'])
        #print(data[i]['f1_value'])
pass

count = 0
for i in range(size):
    if data[i]['f1_flag'] == 1:
        count += 1
print("\n\tStats:")
print("\t\tCount (Total):", size)
print("\t\tCount (Tagged):", count)
print("\t\tPercent (Tagged):", int(count/size*100))

# ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
print("______________________________________________________")
print("\tStep 6: Matching pattern --> (num) (or) (more) (years)")
# ----- ----- ----- ----- ----- ----- ----- ----- ----- -----

outside_list = []

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

    for itr in range(len(words)):
        for key in dictionary.keys():
            if len(key) == len(words[itr]):
                #print(words[itr])
                words[itr] = words[itr].replace(key, dictionary[key])

    inside_list = []

    for j in range(len(words) - 3):
        if words[j].isdigit():
            if words[j + 1] == "or":
                if words[j + 2] == "more":
                    if words[j+3] == "years":
                        inside_list.append(words[j])
                        data[i]['f1_flag'] = 1

    outside_list.append(inside_list)

    if len(outside_list[i]) > 0:
        outside_list[i].sort()
        avg = int(outside_list[i][0])
        data[i]['f1_value'] = min(avg, data[i]['f1_value'])
        #print(data[i]['f1_value'])
pass

count = 0
for i in range(size):
    if data[i]['f1_flag'] == 1:
        count += 1
print("\n\tStats:")
print("\t\tCount (Total):", size)
print("\t\tCount (Tagged):", count)
print("\t\tPercent (Tagged):", int(count/size*100))

# ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
print("______________________________________________________")
print("\tStep 7: Matching pattern --> (minimum) (num) (num) (years)")
# ----- ----- ----- ----- ----- ----- ----- ----- ----- -----

outside_list = []

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

    for itr in range(len(words)):
        for key in dictionary.keys():
            if len(key) == len(words[itr]):
                #print(words[itr])
                words[itr] = words[itr].replace(key, dictionary[key])

    inside_list = []

    for j in range(len(words) - 3):
        if words[j] == "minimum":
            if words[j+1].isdigit():
                if words[j + 1].isdigit():
                    if words[j+3] == "years":
                        inside_list.append(words[j+1])
                        data[i]['f1_flag'] = 1

    outside_list.append(inside_list)

    if len(outside_list[i]) > 0:
        outside_list[i].sort()
        avg = int(outside_list[i][0])
        data[i]['f1_value'] = min(avg, data[i]['f1_value'])
        #print(data[i]['f1_value'])
pass

count = 0
for i in range(size):
    if data[i]['f1_flag'] == 1:
        count += 1
print("\n\tStats:")
print("\t\tCount (Total):", size)
print("\t\tCount (Tagged):", count)
print("\t\tPercent (Tagged):", int(count/size*100))

# ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
print("______________________________________________________")
print("\tStep 8: Matching pattern --> (least) (num) (years)")
# ----- ----- ----- ----- ----- ----- ----- ----- ----- -----

outside_list = []

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

    for itr in range(len(words)):
        for key in dictionary.keys():
            if len(key) == len(words[itr]):
                #print(words[itr])
                words[itr] = words[itr].replace(key, dictionary[key])

    inside_list = []

    for j in range(len(words) - 2):
        if words[j] == "least":
            if words[j+1].isdigit():
                if words[j + 2] == "years":
                    inside_list.append(words[j+1])
                    data[i]['f1_flag'] = 1

    outside_list.append(inside_list)

    if len(outside_list[i]) > 0:
        outside_list[i].sort()
        avg = int(outside_list[i][0])
        data[i]['f1_value'] = min(avg, data[i]['f1_value'])
        #print(data[i]['f1_value'])
pass

count = 0
for i in range(size):
    if data[i]['f1_flag'] == 1:
        count += 1
print("\n\tStats:")
print("\t\tCount (Total):", size)
print("\t\tCount (Tagged):", count)
print("\t\tPercent (Tagged):", int(count/size*100))

# ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
print("______________________________________________________")
print("\tStep 9: Matching pattern --> (than) (num) (years)")
# ----- ----- ----- ----- ----- ----- ----- ----- ----- -----

outside_list = []

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

    for itr in range(len(words)):
        for key in dictionary.keys():
            if len(key) == len(words[itr]):
                #print(words[itr])
                words[itr] = words[itr].replace(key, dictionary[key])

    inside_list = []

    for j in range(len(words) - 2):
        if words[j] == "than":
            if words[j+1].isdigit():
                if words[j + 2] == "years":
                    inside_list.append(words[j+1])
                    data[i]['f1_flag'] = 1

    outside_list.append(inside_list)

    if len(outside_list[i]) > 0:
        outside_list[i].sort()
        avg = int(outside_list[i][0])
        data[i]['f1_value'] = min(avg, data[i]['f1_value'])
        #print(data[i]['f1_value'])
pass

count = 0
for i in range(size):
    if data[i]['f1_flag'] == 1:
        count += 1
print("\n\tStats:")
print("\t\tCount (Total):", size)
print("\t\tCount (Tagged):", count)
print("\t\tPercent (Tagged):", int(count/size*100))

# ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
print("______________________________________________________")
print("\tStep 10: Matching pattern --> (num) (plus) (years)")
# ----- ----- ----- ----- ----- ----- ----- ----- ----- -----

outside_list = []

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

    for itr in range(len(words)):
        for key in dictionary.keys():
            if len(key) == len(words[itr]):
                #print(words[itr])
                words[itr] = words[itr].replace(key, dictionary[key])

    inside_list = []

    for j in range(len(words) - 2):
        if words[j].isdigit():
            if words[j + 1] == "plus":
                if words[j + 2] == "years":
                    inside_list.append(words[j])
                    data[i]['f1_flag'] = 1

    outside_list.append(inside_list)

    if len(outside_list[i]) > 0:
        outside_list[i].sort()
        avg = int(outside_list[i][0])
        data[i]['f1_value'] = min(avg, data[i]['f1_value'])
        #print(data[i]['f1_value'])
pass

count = 0
for i in range(size):
    if data[i]['f1_flag'] == 1:
        count += 1
print("\n\tStats:")
print("\t\tCount (Total):", size)
print("\t\tCount (Tagged):", count)
print("\t\tPercent (Tagged):", int(count/size*100))

# ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
print("______________________________________________________")
print("\tStep 11: Matching pattern --> (experience) (num)")
# ----- ----- ----- ----- ----- ----- ----- ----- ----- -----

outside_list = []

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

    for itr in range(len(words)):
        for key in dictionary.keys():
            if len(key) == len(words[itr]):
                #print(words[itr])
                words[itr] = words[itr].replace(key, dictionary[key])

    inside_list = []

    for j in range(len(words) - 1):
        if (words[j] == "experience") or (words[j] == "experience:"):
            if words[j+1].isdigit():
                inside_list.append(words[j+1])
                data[i]['f1_flag'] = 1

    outside_list.append(inside_list)

    if len(outside_list[i]) > 0:
        outside_list[i].sort()
        avg = int(outside_list[i][0])
        data[i]['f1_value'] = min(avg, data[i]['f1_value'])
        #print(data[i]['f1_value'])
pass

count = 0
for i in range(size):
    if data[i]['f1_flag'] == 1:
        count += 1
print("\n\tStats:")
print("\t\tCount (Total):", size)
print("\t\tCount (Tagged):", count)
print("\t\tPercent (Tagged):", int(count/size*100))

# ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
print("______________________________________________________")
print("\tStep 12: Matching pattern --> (small_list) (num) (years)")
# ----- ----- ----- ----- ----- ----- ----- ----- ----- -----

outside_list = []

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

    for itr in range(len(words)):
        for key in dictionary.keys():
            if len(key) == len(words[itr]):
                #print(words[itr])
                words[itr] = words[itr].replace(key, dictionary[key])

    inside_list = []
    small_list = ["plus", "degree", "phd"]

    for j in range(len(words) - 2):
        if words[j] in small_list:
            if words[j+1].isdigit():
                if words[j + 2] == "years":
                    inside_list.append(words[j+1])
                    data[i]['f1_flag'] = 1

    outside_list.append(inside_list)

    if len(outside_list[i]) > 0:
        outside_list[i].sort()
        avg = int(outside_list[i][0])
        data[i]['f1_value'] = min(avg, data[i]['f1_value'])
        #print(data[i]['f1_value'])
pass

count = 0
for i in range(size):
    if data[i]['f1_flag'] == 1:
        count += 1
print("\n\tStats:")
print("\t\tCount (Total):", size)
print("\t\tCount (Tagged):", count)
print("\t\tPercent (Tagged):", int(count/size*100))

# ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
print("______________________________________________________")
print("\nPickling Data")
# ----- ----- ----- ----- ----- ----- ----- ----- ----- -----

f = open('2.1_data.pkl','wb')
pickle.dump(data,f,-1)
f.close()

# ----- ----- ----- ----- ----- ----- ----- ----- ----- -----

# ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
# ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
# ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
"""
for i in range(len(data)):
    if data[i]['f1_value'] == 100:
        print(data[i]['text'])
print("\n\tStats:")
print("\t\tCount (Total):", size)
print("\t\tCount (Tagged):", count)
print("\t\tPercent (Tagged):", int(count/size*100))
"""

# done:

#1 num num years
#2 num years (of / experience / required / relevant / related / as / preferred / with / combined / working / minimum) + building managing process it system systems demonstrated infrastructure supporting or linux mac windows microsoft vmware  work pc recent ; professional prior web agency plus building
#3 num to num
#4 minimum num years
#5 minimum of num
#6 num or more years
#7 minimum num num years
#8 least num years
#9 than num years
#10 num plus years
#11 experience num
#12 plus num years

# to do:

#1 ...
#2 ...

# latest result:
#   Count(Total): 14867
#   Count(Tagged): 11822
#   Percent(Tagged): 79



