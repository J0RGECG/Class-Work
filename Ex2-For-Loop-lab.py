my_list = ['earth','exciting','day','laptop','electrochemical','blue','up']

x = 0

for words in my_list:
    num = len(words)
    print(words, num)
    x += num

longword = ""

for word in my_list:
    if len(word)> len(longword):
        longword = word

print("the longest word is:", longword)
     
print("\n------------------------------------------------------------------------")  

my_listR = ['indistinguishable', 'acorn', 'soap', 'ladder', 'cheese', 'disillusioned', 'pit', 'monday', 'placeholder', 'teleconference']

y = 0 

for Words in my_listR:
    num = len(Words)
    print(Words,num)
    x+= num
    
longwordd = ""

for Words in my_listR:
    if len(longword) <= len(Words):
        longwordd = Words

print("the longest word is:", longwordd)

print("\n------------------------------------------------------------------------")

my_listtt = ['fixture', 'dangerous', 'humanitarianism', 'trip', 'orange', 'cat', 'triskaidekaphobia', 'nominal', 'and', 'atomic']

b = 0

for wordss in my_listtt:
    num = len(wordss)
    print(wordss,num)
    b+= num   

longest = ""

for wordss in my_listtt:
    if len(wordss) > len(longest):
        longest = wordss   
print("the longest word is:", longest)        






  
















