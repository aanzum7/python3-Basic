words = ["water", "chair", "pen", "basket", "hi", "car"]
num_words =0
charatersInWord =[]
for item in words:
    charatersInWord.append(len(item))
print(charatersInWord)
for num in charatersInWord:
    if num >3:
        num_words = num_words +1
print(num_words)