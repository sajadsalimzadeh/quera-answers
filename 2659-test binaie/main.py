n = int(input())
str1 = input()
str2 = input()

wrong = 0
i = 0
while i < n:
    if(str1[i] != str2[i]):
        wrong += 1
    i += 1
    
print(wrong)