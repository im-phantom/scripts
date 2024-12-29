#!/usr/bin/python

import random
string=input("Enter string: \n===> ") # Takes user input

results = ''  # An empty string initialized so that words can be appended later on in this variable

list=string.split() # Splits the given string and stores into a list. Eg: "Hello world" changes to a list of ["Hello","world"]
list= list[::-1]  # Reverses the list order. Eg: ["Hello","world"] changes to ["world","Hello"]


## Decoder

if list[0]=="0X0" and list[-1]=="0x0":  # Only enters the decoding block if first item of list = "0X0" and last item = "0x0"
  
  # Removes "0x0" and "0X0" from the list.
  list.remove("0x0")
  list.remove("0X0")
  
  # Word decoding happens...
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

    results+=word+" " # Appends the decoded words one by one to results string we initialized at the top

  print(results)  # Prints the decoded message


## Encoder

elif 1:
  results+="0x0 " # Appends "0x0" to results variable so that it can be identified as an encoded message by our program's decoder block for later

  # Encoding bits happens here...
  for word in list:
    char='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
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
    results+=word+" " # Appends the encoded words one by one to results string we initialized at the top
  
  results+="0X0"  

  print(results)  # Prints the encoded message

else:
  print("Error 609! Touch some grass.")
