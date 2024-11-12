
ans = ""

i = 0
j = 0
count = 0

chars = ["a"]



while j < len(chars): 
    if chars[i] == chars[j]:
        j+=1
        count +=1
    else: 
        ans+= chars[i]
        if(count > 1):
            ans += str(count)
        i = j
        count = 0


        
ansArr = [char for char in ans]

print(ansArr)