#import os
file1="dictionary.txt"
f= open(file1,"r")
ln=0
longestWord=""
for word in f:
    if ln<len(word):
        ln=len(word)
        longestWord=word
f.seek(0)
print(longestWord)

file2="temp.txt"
f2=open(file2,"w")
for word in f:
    wl=len(word)
    if word[wl-1]=='\n':   
        word=word[:wl-1]
        wl=wl-1
    for i in range(0,ln-wl):
        word=word+'#'
    word=word+'\n'
    f2.write(word)

f.close()
f2.close()
#delete(file1)
#os.rename(file2,file1)
