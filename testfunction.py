def dashy(word):
    if len(word) > 2:
        return '-'*2 + word[2:]

print(dashy("Madam"))
print(dashy("am"))
