#===================================================Header Files==========================================================
from random import sample
import random
import sys
#===================================================Function Area========================================================
def validate_faces(faces):
    #INPUT:Value of faces in digit only.
    #RETURN:Value of faces only when the amount is greater than one and lesser than 21.
    not_good = True
    while not_good:
        faces = input("Enter # of faces [2,20]: ")
        while not faces.isdigit():
            print("I'm sorry, that isn't a valid postive integer, please try again.")
            faces = input("Enter # of faces [2,20]: ")
        faces = int(faces)
        if faces > 1 and faces < 21:
            not_good = False
        else:
            print("Faces have to atleast 2 and maximam 20")
    return faces

def validate_dice(dice):
    #INPUT:Value of dice in digit only.
    #RETURN:Value of dices only when the amount is lies between 3 and 6.
    not_good2 = True
    while not_good2:
        dice = input("Enter # of dice [3,6]: ")
        while not dice.isdigit():
            print("I'm sorry, that isn't a valid postive integer, please try again.")
            dice = input("Enter # of dice [3,6]: ")
        dice = int(dice)
        if dice > 2  and dice < 7:
            not_good2 = False
        else:
            print("Dices have to atleast 3 and maximam 6")
    return dice

def roll_dice(faces,dice):  
    #INPUT:Both values of faces and dices.
    #RETURN:Random numbers in list.
    sequence = list(range(1,faces+1))
    empty_list = []
    i = 0
    while i<dice:
        subset = list(sample(sequence,1))
        empty_list.extend(subset)
        i=i+1    
    subset = empty_list
    return subset

def average(subset,dice):
    #INPUT:Random number list and dice value.
    #RETURN:sum and average of list elements.
    sum_of_list = sum(subset)
    average = round(sum_of_list/dice)
    return  sum_of_list ,average
    
def maximam_score(faces,dice):
    #INPUT:Value of faces and dice.
    #RETURN:Multiplication of faces and dices.
    maxi = faces*dice
    return maxi

def calculate_percentage( sum_of_list, maxi ):
    #INPUT:Sum of random list elements and maxi.
    #RETURN:Percentage
    percentage = sum_of_list/maxi
    return percentage

def pattern1(faces,subset,bonus_factor):
    #INPUT:Value of faces , list elements and bonus factor.
    #RETURN:Bounus factor and pattern1_valid which is either true or false.
    pattern1_valid = False
    result = False
    bonus_factor = 0
    if faces >=4:
        for i in subset:
            if subset.count(i) > 1:
                result = True
        if result:
            print("Pattern 1 matched in your rool, ",subset,"... some dice are same.")
            bonus_factor = bonus_factor + 10
            pattern1_valid = True
        else:
            print("Pattern 1 not matched in your rool, ",subset,"... some dice are different.")
            pattern1_valid = False
    return bonus_factor , pattern1_valid

def pattern2( maxi, sum_of_list,bonus_factor):
    #INPUT:Maximam , sum of lists , bonus factor
    #RETURN:Bounus factor and pattern2_valid which is either true or false.
    pattern2_valid = False
    if maxi >=20:
        num = sum_of_list
      
        if num > 1:  
           for i in range(2,num):  
               if (num % i) == 0:  
                   print("Pattern 2 did not matched, ",num," is not a prime number!")  
                   #print(i,"times",num//i,"is",num)
                   pattern2_valid = False
                   break  
           else:  
               print("Pattern 2 matched! ",num," is a prime number")
               bonus_factor = bonus_factor + 15
               pattern2_valid = True
    else:
        print("Pattern 2 did not matched ",maxi," is not equal or greater than to 20")
        pattern2_valid = False
    return bonus_factor , pattern2_valid
    

def pattern3( dice,subset,average,bonus_factor):
    #INPUT: Value of dice, list of elements, average of list elements , bonus factor.
    #RETURN: Bonus factor and pattern3_valid.
    pattern3_valid = False
    if dice >= 5:
        count = 0
        
        for i in subset:
            if i >=average:
                count = count + 1
        elements_in_list = len(subset)
        half_of = elements_in_list / 2
        if count >= half_of:
            print("Pattern 3 Matched! More than half of ",subset," are greater than or equal to the average of 5.")
            bonus_factor = bonus_factor + 5
            pattern3_valid = True
        else:
            print("Pattern 3 does not apply since More than half of ",subset," are not greater than or equal to the average of 5.")
            pattern3_valid = False
    else:
        print("Pattern 3 does not apply since there are less than 5 Dice")
        pattern3_valid = False
    return bonus_factor , pattern3_valid


def pattern4( faces, dice, subset, bonus_factor ):
    #INPUT:Face and dice values , list elements , bonus factor
    #RETURN:Bonus factor and pattern4_valid.
    pattern4_valid = False
    result = False
    if dice > 4 and faces > dice:
        for i in subset:
            if subset.count(i) > 1:
                result = True
        if result:
            print("Pattern 4 does not match! Some of the values in ",subset," match!")
            pattern4_valid = False

        else:
            print("Pattern 4  matched!,All dices have different values.")
            bonus_factor = bonus_factor + 8
            pattern4_valid = True
    else:
        print("Pattern 4 does not apply, either sides <=4 or # sides <= # dice.")
        pattern4_valid = False
    return bonus_factor , pattern4_valid       

def rerool(re,b,value_rolled,n,turn,list_score):
    #INPUT:re = 0 ,A empty list , list of items that rolled , value of faces , turn , A empty list.
    #RETURN:Value rolled which gives new list of elements after giving yes to code, sure and reroll only has yes or no value , 
    b = []
    for i in value_rolled:
        
        b.append(i)
    
    
    not_good3 = True
    while not_good3:
        reroll = input("Do you want to rerool any dice? ['yes'],['no']")
        if reroll.casefold() == "yes" or reroll.casefold() == "no":
        
            not_good3 = False
        else:
            print("I'm sorry, the choices are ['yes','no'] .Please pick one of them.")
        
    if reroll.casefold() == "yes":
        for i in value_rolled:
            re = re + 1
            good = True
            while good:
                print("Reroll Die ",re,"( was ",i," ) ['y','n']",end="")
                c = input(" ")
               
                if c.casefold() == "y":    
                    value_rolled[re-1] = random.randint(1,n)
                    good = False
                elif c.casefold() == "n":
                    good = False
                else:
                    print("I'm sorry, the choices are['y','n'].Please pick one of them.")

    not_godd4 = True
    if  reroll.casefold() == "no":
        if turn > 1:
            turn_value,list_value = newturn(turn,list_score)
            turn_value,average_value = average_turn(turn,list_score)
            if list_value > average_value:
                print("Your score of ",list_value," on turn ",turn_value," was above average compared to another turns today.")
            elif list_value < average_value:
                print("Your score of ",list_value," on turn ",turn_value," was below average compared to another turns today.")
            elif list_value == average_value:
                print("Your score of ",list_value," on turn ",turn_value," was equal to average compared to another turns today.")
            
            another()
                
        not_godd4 = False

   
    sure = ""
    while not_godd4:
        good1 = True
        while good1:
            sure = input("Are you sure ?['yes','no']")
            print()
            if sure.casefold()== "yes":
                del(list_score[-1])
                print("you have rolled now:",value_rolled)
                all1(value_faces,value_dice)
                not_godd4 = False
                good1 = False
                
                if turn > 1:
                    
                    another()
                
            elif sure.casefold() == "no":
                another()
                not_godd4 = False
                good1 = False
            else:
                print("Sorry please re-enter the correct one: ['yes','no'] ")
                good1 = True
                 
    return value_rolled,sure,reroll
    
def newturn(turn,list_score):
    #INPUT:value of turn , list of wroth points.
    #RETURN:value of turn,last element of list.
    last_element = list_score[-1]
    return turn,last_element

def average_turn(turn,list_score):
    #INPUT:value of turn , list of wroth points.
    #RETURN:value of turn,average of list items.
    last_element_index = len(list_score)
    average_list = sum(list_score)/last_element_index
    return turn,average_list

def all1(value_faces,value_dice):
    #INPUT:Value of faces and dice.
    #RETURN:Nothing
    #Sum and average
    sum1,average_value = average(value_rolled,value_dice) 
    print("These die sum to ",sum1," and have an average rounded value of ",average_value)
    #Maximam Score
    maxi = maximam_score(value_faces,value_dice)
    #Percentage
    percentage = calculate_percentage(sum1,maxi)
    #Bonus Factor
    bonus_factor = 0
    #pattern1
    value_bonus , pattern1_valid = pattern1(value_faces,value_rolled,bonus_factor)
    #pattern 2
    value_bonus2 , pattern2_valid =pattern2( maxi, sum1, value_bonus)
    #pattern 3
    value_bonus3 , pattern3_valid = pattern3(value_dice,value_rolled,average_value,value_bonus2)
    #pattern 4
    value_bonus4 , pattern4_valid = pattern4(value_faces,value_dice,value_rolled,value_bonus3)
    #pattern 5
    if (pattern1_valid or pattern2_valid or pattern3_valid or pattern4_valid) == False:
        value_bonus4 = value_bonus4 + 1
        print("Some none of the other patterns were matched,pattern 5 is matched")
    else:
        print("You match some so pattern 5 is not matched.")
    #bonusfactor result
    print("Your bonus factor is: ",value_bonus4)
    #worth points
    a = value_bonus3*percentage
    b = 824885 % 500
    print("These dice are worth points ",round(a+b)," points.")

    list_score.append(round(a+b))
    
    print()

def another():
    #INPUT:NOTHING
    #RETURN:NOTHING
    good4 = True
    while good4:
        ask_user_after_no = input("Would you like to play another turn? ['y'] or ['n']")
        if ask_user_after_no.casefold() == "y" or ask_user_after_no.casefold() == "n":
            good4 = False
        else:
            print("Enter only ['y'] or ['n']")
            good4 = True
    if ask_user_after_no.casefold() == "n":
        good = False
        turn_value,average_value = average_turn(turn,list_score)
        
        print("You played ",turn_value," turns today with an average score of ",round(average_value)," points.")
        sys.exit()
#====================================================Starting of Program========================================================
print("Welcome to my game, good luck!")
print()
turn = 1
list_score = []
#faces
faces = ""
value_faces = validate_faces(faces)
print()
#dice
dice=""
value_dice = validate_dice(dice)
print()

good = True

while good:
    #Rolled
    value_rolled = roll_dice(value_faces,value_dice)
    print("You have rolled: ",value_rolled)
    print()
    all1(value_faces,value_dice)
    #rerool concept
    re = 0
    copy = []
    rerrol_values,sure,reroll = rerool(re,copy,value_rolled,value_faces,turn,list_score)
    #Are you sure
    if sure =="y":
        all1(value_faces,value_dice)
    if turn == 1:
        print("This is your first turn lets go again")
        good = True
        
    turn = turn + 1


