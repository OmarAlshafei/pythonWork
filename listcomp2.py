word = input()

nonVowel = [word[i] for i in range(len(word)) if word[i] not in ['a', 'e', 'i', 'o', 'u']]

print(nonVowel)
