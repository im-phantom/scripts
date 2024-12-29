import random
string=input("Enter a string: ")
opt=input("Encode or Decode ?\n(E or D)\n==> ")
results=''
list=string.split()
#Encoder
if opt.upper()=="E":
  for word in list:
    char='abcdefghijklmnopqrstuvwxyz'
    rand1=random.choices(char,k=3)
    rand2=random.choices(char,k=3)
    randx=''
    randy=''
    for i in rand1:
      randx+=i
    for j in rand2:
      randy+=j
    if len(word)<3:
      try:
        word=word[1]+word[0]
      except:
        word=word[0]
    else:
      g=word[0]
      word=randx+word[1:]+g+randy
    results+=word+" "
  print(results)
#Decoder
elif opt.upper()=="D":
  
  for word in list:
    if len(word)<3:
        try:
            word=word[1]+word[0]
        except:
            word=word[0]
    elif len(word)>3:
      try:    
        word=word[3:-3]
        word=word[-1]+word[:-1]
      except:
        word=word
    results+=word+" "
  print(results)

else:
  print("Option Error")
