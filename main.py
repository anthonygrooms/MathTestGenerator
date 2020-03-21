'''
Generate a math test that includes randomly generated questions with
answer key as a .txt file:

User enters...
1) name of file
2) how many math questions
3) types of math questions they want generated

Generate the test
'''

#Gives us random functionality
import random

#Recieve required data from the user to create the test
fileName = ''
questionCount = 0
questionTypes = ''

fileName = input('Enter the name for the text without .txt extension: ')+'.txt'

while True:
    try:
        questionCount = int(input('How many questions? '))
        if questionCount >= 1:
            break
        print('Number of questions must be greater than 0.\n')
    except:
        print('Enter an integer.\n')

while True:
    print('Enter every question type desired on one line (+ addition,- subtraction,* multiplication,/ division)')
    questionTypes = input('Example Input: +* : ')
    if '+' in questionTypes or '-' in questionTypes or '*' in questionTypes or '/' in questionTypes:
        break
    print('Input must contain one of the operation symbols.\n')

outF = open(fileName,'w')

answers = [] #Create a list to store the correct answers

#Create a list to store all the desired types of operations
types = []
for operation in '+-*/':
    if operation in questionTypes:
        types.append(operation)

outF.write('questions:\n')

#Write all the questions
for question in range(1,questionCount+1):
    
    typeQ = types[random.randint(0,len(types)-1)] #Randomize the type of question
    #Randomize a and b
    a = random.randint(0,12)
    b = random.randint(0,12)

    #Compute the answer
    if typeQ == '+':
        c = a + b
    elif typeQ == '-':
        c = a - b
    elif typeQ == '*':
        c = a * b
    else:
        #If the type of question is division, force b to evenly fit into a
        while b != 0 and a % b != 0:
            b = random.randint(0,12)
        
        #If b is 0, do not divide a by b, rather set the answer c equal to 'undefined'
        if b == 0:
            c = 'undefined'
        else:
            c = a / b
    
    #Add the answer to our list of answers
    if c == 'undefined':
        answers.append(c)
    else:
        answers.append(int(c))

    #Write the question to the output file
    outF.write('{}. {} {} {} = ?\n'.format(question,a,typeQ,b))

#Write the answer key
outF.write('\nanswer key:\n')
for question in range(1,questionCount+1):
    outF.write('{}. {}\n'.format(question,answers[question-1]))
outF.close()

print('\ndone.')