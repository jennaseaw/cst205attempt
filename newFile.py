import matplotlib.pyplot as plt

scrabble_words = {
    'jazzy' : 34, 'zombify' : 27, 'zap' : 15, 'zilch' : 20
}

print(list(scrabble_words.keys()))
print(list(scrabble_words.values()))

plt.bar(list(scrabble_words.keys()), list(scrabble_words.values()))
plt.title("Four Interesting Scrabble Words")
plt.ylabel("Points")
plt.xlabel("Word")
plt.show()

