length_text = int(input())
words = list(map(str, input().split()))

result = ''
for word in words:
    if len(word) != len(result):
        if len(word) > len(result):
            result = word


print(result)
print(len(result))
