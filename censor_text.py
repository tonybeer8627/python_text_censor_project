# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()
###########
proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm",
                     "her", "herself"]

negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help",
                  "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed",
                  "distressed", "concerning", "horrible", "horribly", "questionable"]
###########
def censor_one(text,censor_text): ### Censor text with specific word
  censor = " "
  for i in censor_text:
    if i  ==" ":
      censor += " "
    else:
      censor += "X"
  return text.replace(censor_text, censor)
########## 

def censor_two(text, censor_text): ### Censor text with proprietary list of words
  list_censor = []
  for i in censor_text:
    censor = " "
    for k in i:
      if k  ==" ":
        censor += " "
      else:
        censor += "X"
    list_censor.append(censor) ### Create new proprietary words with "XXX"

  for i in range(len(list_censor)):
    text = text.replace(censor_text[i], list_censor[i]) ### Replace censor word that found in text with XXXX word
  return text
############################

def censor_three(text, censor_word, negative_words ):
  text_censor = censor_two(text, censor_word) ### create a list of text and replaace censor word with XXXX
  #print(text_censor)
  ###########
  negative_wordsX = [] ### create a list of negative words in XXX
  for i in negative_words:
    tempo_word=''
    for k in i:
        tempo_word += "X"
    negative_wordsX.append(tempo_word)
  
  text_list_with_censor = text_censor.split(" ")
  count = 0
  for i in range(0,len(text_list_with_censor)): ### Find wheater negative word are in text or not
    if text_list_with_censor[i].lower() in negative_words:
      count +=1
      if count > 2:
        index = negative_words.index(text_list_with_censor[i])
        text_list_with_censor[i] = negative_wordsX[index]
        count = 0
  final_text = " ".join(text_list_with_censor)
  return final_text
############################

word_censor_all = proprietary_terms + negative_words
punctuation = ['!', ',', '?', '.']

def censor_four(text):
    text_list = text.split() ### split text in to list
    for i in range(len(text_list)):
        word = text_list[i]
        for k in text_list[i]: ### Check text in list have a punctuation or not
            if k in punctuation :
                word = text_list[i].strip(k) ### if text in list have a punctuation then remove it
           
        if word.lower() in word_censor_all: ### Check text in list is in word censor list or not
            word_censor = ''
            for j in text_list[i]:
                if j in punctuation:
                    word_censor += j
                else:
                    word_censor += 'X'
            text_list[i] = word_censor ### Replace text in list with censor word XXXX
            
            if i-1 >= 0: ### If censor word is the fist text then do nothing
                tempo_word_before = ''
                for k in text_list[i-1]:
                    if k in punctuation:
                        tempo_word_before += k
                    else:
                        tempo_word_before += 'x'
            
                text_list[i-1] = tempo_word_before ## censor word before censor list
            
            if i+1 < len(text_list): ## If censor word is the last text then do nothing
                tempo_word_after = ''
                for k in text_list[i+1]:
                    if k in punctuation:
                        tempo_word_before += k
                    else:    
                        tempo_word_after += 'x'
                    
                text_list[i+1] = tempo_word_after ## censor word after censor list
                
    return " ".join(text_list)
                
  


    

 

    
#print(censor_two(email_two, proprietary_terms))  
#print(email_three.split(" "))
#print(email_three.split("\n"))
#print (censor_three(email_three, proprietary_terms, negative_words))
#print(email_three)
print(censor_four(email_four))
                
            
