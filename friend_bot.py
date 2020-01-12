                            #friend bot using NLP
# importing libraries for machine learning chatbot 
from nltk import PorterStemmer
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
import datetime
import time
import random
import re


ps = PorterStemmer
stopwords = set(stopwords.words('english'))

#Definition
gender_male = ["male","m","men","MALE","mALE","M"]
gender_female = ["female","f","women","FEMALE","fEMALE","F"]
random_m = ("arav","Vihaan","Aryan","Shaurya","Dhruv","Ishaan","Kabir","Manoj","Rohit","Rohan","Siddharth","Pratyush","Samarth")
random_f = ("Aahna","Aesha","Chahna","Damini","Fulki","Ishita","Keerthi","Maalai","Neysa","Pari","Rina","Saloni","Taara","Vahini","Vilina","Zaina")

#chatbot code
#personal details
name = input("Kindly type your Full name ")
new_name = word_tokenize(name)
print("Hello "+ new_name[0])
time.sleep(0.8)
print("Nice to meet you")
email = input("Kindly also share your email id\n")
time.sleep(1)
gender = input("Are you male(m)/female(f)")

#self introduction
if gender in gender_male:
    print("Hey! My name is " +random.choice(random_f))
time.sleep(0.8)
if gender in gender_female:
    print("Hey! My name is " +random.choice(random_m))
time.sleep(0.8)
    
print("Nice to meet you")