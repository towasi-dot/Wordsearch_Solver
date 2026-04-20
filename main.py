x, y = map(int, input().split())
words = list(input().lower().split())
wordSearch = [list(input()) for _ in range(y)]
found = []

for word in words:
    length = len(word)

    for j in range(y):  # Horizontal (left -> right)
        for i in range(x - length + 1):
            row = "".join(wordSearch[j][i:i+length])
            if row == word or row == word[::-1]:
                if word not in found:
                    found.append(word)
                for k in range(length):
                    wordSearch[j][i+k] = wordSearch[j][i+k].upper()

    for i in range(x): # Vertical (top -> bottom)
        for j in range(y - length + 1):
            col = "".join(wordSearch[j+k][i] for k in range(length))
            if col == word or col == word[::-1]:
                if word not in found:
                    found.append(word)
                for k in range(length):
                    wordSearch[j+k][i] = wordSearch[j+k][i].upper()

    for j in range(y - length + 1): # Diagonal left-to-right checking
        for i in range(x - length + 1):
            dia = "".join(wordSearch[j+k][i+k] for k in range(length))
            if dia == word or dia == word[::-1]:
                if word not in found:
                    found.append(word)
                for k in range(length):
                    wordSearch[j+k][i+k] = wordSearch[j+k][i+k].upper()

    for j in range(y - length + 1): # Diagonal right-to-left
        for i in range(length - 1, x):
            dia = "".join(wordSearch[j + k][i - k] for k in range(length))
            if dia == word or dia == word[::-1]:
                if word not in found:
                    found.append(word)
                for k in range(length):
                    wordSearch[j + k][i - k] = wordSearch[j + k][i - k].upper()

suffix = "these are all" if len(found) == len(words) else "rest are not there"
print(f"Found words: {' '.join(found)}, {suffix}")
for row in wordSearch:
    print("".join(row))
