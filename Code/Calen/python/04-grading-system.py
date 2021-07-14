#----------------------------------------------------#
# *'-.-'*'-.-'(👍≖‿‿≖)👍 👍(≖‿‿≖👍)*'-.-'*'--'*#
# 
#          Project: Python grading system
#          Version: 1.0
#          Author: Calen Ray
#          Email: Calen.w.ray@gmail.com
#          Date: 04/30/21
#----------------------------------------------------#

#requirements: 
import random

# constraints: 

# 90-100 = A
# 80-89 = B
# 70-79 = C
# 60-69 = D
# 00-50 = F

# 00-03 = -
# 04-06 = (blank)
# 07-09 = +


#---------------------#1-------------------------------#

# Lets start with getting our two scores

score = input("Enter your score percentage from 0-100%:    ") # user input a string (by default)
score = float(score) # convert the string to a float 

score_2 = random.randint(0, 100) 
score_2 = float(score_2) # this was going to bother me if score 1 & 2 were not both floats....


#----------------------#2------------------------------#


# Users score

if score >= 90:
    grade = 'A' 

elif score >= 80:
    grade = 'B'

elif score >= 70:
    grade = 'C'

elif score >= 60:
    grade = 'D'

elif score >= 0:
    grade = 'F'

else: 
    print("There seems to be an error. Please restart with valid numbers.")

# other user score (player 2, etc)

if score_2 >= 90:
    grade_2 = 'A' 

elif score_2 >= 80:
    grade_2 = 'B'

elif score_2 >= 70:
    grade_2 = 'C'

elif score_2 >= 60:
    grade_2 = 'D'

elif score_2 >= 0:
    grade_2 = 'F'

#---------------------#3-------------------------------#

#  Lets try to modulus our way into a A+ in this class..

# set new variables.
score_id = score % 10
score_2_id = score_2 % 10


# Users score ID.

if score <= 59:
  print("")  #this will keep us from assigning a F+ for something like a 49 which score_ID would assume is a 9 which would be a +

elif score_id >= 7:
    grade = grade + '+' 

elif score_id >= 4:
    grade = grade + ''

elif score_id >= 0:
    grade = grade + '-'


# Player 2's score identifier 

if score_2_id <= 59:
  print("")   #this will keep us from assigning a F+ for something like a 49 which score_ID would assume is a 9 which would be a +

elif score_2_id >= 7:
    grade_2 = grade_2 + '+' 

elif score_2_id >= 4:
    grade_2 = grade_2 + ''

elif score_2_id >= 0:
    grade_2 = grade_2 + '-'



#---------------------FINAL----------------------------#

# Now lets move onto relaying this info to the user.

if score == 100:
    print(f"Wowza. you got a {grade} ({score})?? Nice work, your bff got a {grade_2}({score_2})")

elif score >= 90:
    print(f"Looks like your score was {score}, or {grade}, nice work. Your Bff got a {grade_2}({score_2}) ")

elif score >= 80:
    print(f"Looks like your score was {score}, or {grade}, decent for sure. Your Bff got a {grade_2}({score_2})")

elif score >= 70:
    print(f"Looks like your score was {score}, or {grade}, C's get degrees baby! Your Bff got a {grade_2}({score_2})")

elif score == 69:
    print(f"Nice. your score was {score}, or {grade}. Your BFF got {score_2} or {grade_2}({score_2})")

elif score >= 60:
    print(f"Looks like your score was {score}, or {grade}, Please take study time more serious. Your Bff got a {grade_2}({score_2})")

elif score >= 0:
    print(f"Looks like your score was {score}, or {grade}. Your Bff got a {grade_2}({score_2})..")

else:
    print("there appears to have been an error, please retry with a proper number.")


#---------------------DONE----------------------------#