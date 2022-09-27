text1 = input("String: ")
text2 = input("Substring: ")

count = 0
for i in range(len(text1)):
    
    match_letters = 0
    for j in range(len(text2)): 
        
        if i+len(text2) > len(text1) or text1[j+i] != text2[j]:
            break
        else: 
            match_letters = match_letters + 1
            
    if match_letters == len(text2):
        count = count + 1
        
print(count)
