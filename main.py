#Generate a math test (question and answers) in a .txt

import random

#Get the statistics for the test and assure correct input

fileName = ""
questionCount = 0
questionTypes = ""

fileName = input("Enter name for test without .txt extension: ")+".txt"

while True:
  try:
    questionCount = int(input("How many questions? "))
    if questionCount >= 1:
      break
    print("Number of questions must be greater than 0. \n")
  except:
    print("Enter an integer. \n")

while True:
  questionTypes = input("Enter every question type desired on one line (question types include + addition,- subtraction,* multiplication,/ division): ")
  if "+" in questionTypes or "-" in questionTypes or "*" in questionTypes or "/" in questionTypes:
    break
  print("Input must contain one of the operation symbols. \n")

outF = open(fileName,'w')

answers = [] #Create a list to store the correct answers

#Create a list to store all the desired types of questions
types = []
for operation in "+-*/":
  if operation in questionTypes:
          types.append(operation)

outF.write("questions:\n")

#Write all the questions
for question in range(1,questionCount+1):

  typeQ = types[random.randint(0,len(types)-1)]	#Randomize the type of question

  #Randomize a and b
  a = random.randint(0,12)
  b = random.randint(0,12)
  c = 0

  #Compute the correct answer
  if typeQ == "+":
    c = a + b
  elif typeQ == "-":
    c = a - b
  elif typeQ == "*":
    c = a * b
  else:
    #If the type of question is division, force b to evenly fit into a
    while b != 0 and a % b != 0:
      b = random.randint(0,12)
    #If b is 0, do not divide, rather set the correct answer equal to "error"
    if b == 0:
      c = "error"
    else:		
      c = a / b

  #Add the answer to our list of answers
  if c == "error":
    answers.append(c)
  else:
    answers.append(int(c))

  #Write the question to the output file
  outF.write("{}. {} {} {} = ?".format(question,a,typeQ,b)+"\n")
	
outF.write("\nanswer key:\n")

#Write the answer key
for question in range(1,questionCount+1):
        outF.write("{}: {}".format(question,answers[question-1])+"\n")
outF.close()

print("\ndone.")