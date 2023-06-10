def longest_word(word):
  words_list = word.split(" ")
  count = []
  for i in words_list:
     count.append(len(i))
  max_word = count.index(max(count))
  print(words_list[max_word])



longest_word('ahmed love football tooooooooooooooooooo much ')