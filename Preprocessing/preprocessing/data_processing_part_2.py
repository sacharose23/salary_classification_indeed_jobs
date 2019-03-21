# Tokenizing Data sentence by sentence
import pickle

# ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
print("______________________________________________________")
print("\nRemoving \\n --> Char and Delimiter...")
# ----- ----- ----- ----- ----- ----- ----- ----- ----- -----

f = open('1_data.pkl', 'rb')
data = pickle.load(f)
f.close()

for itr in range(len(data)):
    print(itr)
    old_words = (data[itr]['text'])
    #print("Raw:\n", old_words)

    new_words = []
    for word in old_words:
        if word != "\n":
            new_words.append(word)

    superwords = ""
    for i in range(len(new_words)):
        for j in range(len(new_words[i])):
            if ord(new_words[i][j]) == 10:
                if new_words[i][j-1] != '.':
                    superwords = superwords + '.'
            else:
                superwords = superwords + new_words[i][j]

    superwords_split = superwords.split('.')
    data[itr]['text'] = superwords_split
    #print("Split --> without \\n as char, delimiter:\n",superwords_split, "\n")

# ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
print("______________________________________________________")
print("\nPickling Data")
# ----- ----- ----- ----- ----- ----- ----- ----- ----- -----

f = open('2_data.pkl','wb')
pickle.dump(data,f,-1)
f.close()

# ----- ----- ----- ----- ----- ----- ----- ----- ----- -----