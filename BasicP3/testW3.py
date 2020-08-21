sentence = "python is a high level general purpose programming language that can be applied to many different classes of problems."
words= sentence.split()
num_a_or_e = 0
for word in words:
    if ('a' in word) or ('e' in word):
        num_a_or_e += 1
print(num_a_or_e)