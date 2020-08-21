sentence = "students flock to the arb for a variety of outdoor activities such as jogging and picnicking"
same_letter_count = 0

words = sentence.split(' ')
# wordslen = len(words)
# print(words)
for word in words:
    if word[0] == word[-1]:   ## star and ens same word
        same_letter_count += 1  ## count
print(same_letter_count)