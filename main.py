from translate import Translator
first = input("Do you want to do conjugator or translator: ")
if first == "translator":
  language = input("What language is the word in: ")
  language2 = input("What language is the word into: ")
  word = input("What is the word: ")
  translator= Translator(from_lang=language,to_lang=language2)
  translation = translator.translate(word)
  print("In",language2,word,"is",translation)
  quit()
elif first == "conjugator":
  pass
else:
  print("Invalid")
  quit()
word = input("What is the regular verb to conjugate in Spanish: ")
tense= input("is it present or past tense: ")
translator= Translator(from_lang="spanish",to_lang="english")
translation = translator.translate(word)
new_word = word[:-2]
a=(word.endswith("er"))
b=(word.endswith("ir"))
c=(word.endswith("ar"))
if a==True and tense=="present":
  print("to "+translation,",yo",new_word+"o,",
"tu",new_word+"es,","el/ella/usted",new_word+"e,","ellos/ellas/ustedes",new_word+"en,","nosotros",new_word+"emos")
elif b==True and tense=="present":
    print("to "+translation,",yo",new_word+"o,",
"tu",new_word+"es,","el/ella/usted"+"e,","ellos/ellas/ustedes",new_word+"en,","nosotros",new_word+"imos")
elif c==True and tense=="present":
  print("to "+translation,",yo",new_word+"o,",
"tu",new_word+"as,","el/ella/usted",new_word+"a,","ellos/ellas/ustedes",new_word+"an,","nosotros",new_word+"amos")
elif a==True and tense=="past":
  print("to "+translation,",yo",new_word+"í,",
"tu",new_word+"iste,","el/ella/usted",new_word+"ió,","ellos/ellas/ustedes",new_word+"ieron,","nosotros",new_word+"imos")
elif b==True and tense=="past":
  print("to "+translation,",yo",new_word+"í,",
"tu",new_word+"iste,","el/ella/usted",new_word+"ió,","ellos/ellas/ustedes",new_word+"ieron,","nosotros",new_word+"imos")
elif c==True and tense=="past":
  print("to "+translation,",yo",new_word+"é,",
"tu",new_word+"aste,","el/ella/usted",new_word+"ó,","ellos/ellas/ustedes",new_word+"aron,","nosotros",new_word+"amos")
else:
  print("invalid, please do a regular verb ending with ir,er or ar")
  quit()