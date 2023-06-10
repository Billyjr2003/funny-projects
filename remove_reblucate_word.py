def remove(word):
    word_list = word.split(" ")
    output = []
    for i in word_list :
        if i not in output :
            output.append(i)
    return " ".join(output)

print(remove("ahmed nabil mohamed ahmed mohamed"))