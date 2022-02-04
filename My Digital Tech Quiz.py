from Question import Question #imports question function from other file
import time #sets time variable


question_prompts = [ #questions for easy quiz set in a list - identified as question prompts so that can use the variable for question answers
    "What is the worlds most populated species of fish? - \na) Trout \nb) Snapper \nc) Carp \nd) Salmon ",
    "What is the most common fish in NZ? - \na) Stargazer \nb) Snapper \nc) Kahawai \nd) Kingfish ",
    "What is the most popular type of fishing that occurs? - \na) Fly Fishing \nb) Salt/Fresh Water Fishing \nc) Ice Fishing \nd) Catch And Release ",
    "Fish breathe by pulling air through their lungs - \nTrue \nFalse ",
    "Most fish give birth by laying eggs - \nTrue \nFalse ",
    "Fish are an important resource for humans worldwide, especially as what? - \na) Pets \nb) Fishing bait \nc) Clothing \nd) Food ",
    "How many fish are estimated to be in the ocean? - \na) 3.5 trillion \nb) 5.2 million \nc) 78.4 million \nd) 9.7 trillion ",
    "What is the largest fresh water fish? - \na) CatFish \nb) Trout \nc) Sturgeon \nd) Salmon ",
    "What is the legal size for a snapper? (Snappers are common fish in NZ) - \na) 50cm \nb) 10cm \nc) 25cm \nd) 30cm ",
    "A group of fish is called a shoal - \nTrue \nFalse  ",
]


questions = [ #questions for easy quiz answers with correct/incorrect responses in a list - takes question prompts from above 
    Question(question_prompts[0], "c", "carp", "Incorrect! It is actually Carp.", "Correct! Carp are smaller fish that are very common in america, so common that they have carp tournaments where whoever catches the biggest carp wins."),
    Question(question_prompts[1], "a", "stargazer", "Incorrect! Good Try, the answer is Stargazer, you didn't think i'd make it too easy for you?", "Correct! A stargazer is a fish that acts as a sea vacuum, it lays at the bottom of the sea bed camouflaged by sand eating smaller fish."),
    Question(question_prompts[2], "b", "salt/fresh water fishing", "Incorrect! The answer was Salt/Fresh water fishing, so far but so close", "Correct! Fresh/saltwater fishing is the easiest way to fish for beginners and can always snag a beauty."),
    Question(question_prompts[3], "false", "f", "Incorrect! The answer was False,  maybe I am making this too hard..?", "Correct! Fish breathe through their gills"),
    Question(question_prompts[4], "true", "t", "Incorrect! The answer was True, I am sorry that was pretty tricky", "Correct! Most fish give birth by laying eggs"),  
    Question(question_prompts[5], "d", "food", "Incorrect! The answer was food, I guess you don't eat fish..", "Correct! Fish can make up an amazing meal and on top of that it is very nutritional"),  
    Question(question_prompts[6], "a", "3.5 trillion", "Incorrect! The answer was 3.5 trillion and yes there is that many fish in the sea", "Correct! There is in fact 3.5 trillion fish estimated to be swimming in the ocean"),  
    Question(question_prompts[7], "c", "sturgeon", "Incorrect! The answer was Sturgeon a fish which has been around for about 250 million years", "Correct! A sturgeon is a long eel like fish that compared to some catfish which is another popular freshwater fish are a lot bigger."),  
    Question(question_prompts[8], "d", "30cm", "Incorrect! The answer was 30cm, legal sizes for fish all vary on what sort of fish you are catching or have caught", "Correct! In order to catch and keep a snapper it must be 30cm or above"),    
    Question(question_prompts[9], "true", "t", "Incorrect! The answer was Shoal, school is more commonly used but shaol can also describe a group of fish", "Correct! The most common collective nouns for a group of fish in general are either a school or shoal"),          
]


print("A Rod And Reel Quiz") #introduces quiz name 
print("-------------------------------------------------------------------------")
#Asks user for their name
name = input("Welcome to the Rod And Reel quiz, in this quiz you'll be answering questions based on fishing and fish in general. This quiz is to determine if you are a fishing master. What is your name? ")
print("-------------------------------------------------------------------------")
print("Hello {}, all the best for completing the quiz. Dooo youuu have what it takes to be a fishing master?" .format(name)) #greets the user by name 
print("-------------------------------------------------------------------------")
#while true is loop variable for the quiz
while True:
    quiz_difficulty = input("What sort of fishing quiz would you like to attempt? *Please answer with their allocated letters - a or b - \n\na)Easy  \nb)Hard") #allows user to choose what difficulty they would like to attempt
    quiz_difficulty = quiz_difficulty.lower() #makes input lowercase
    #if easy quiz was selected
    if quiz_difficulty == "a":
        start_time = time.time() #records current time
        print("-------------------------------------------------------------------------")
#breif introduction to quiz and score variable set
        print("You have decided to attempt the Easy fishing quiz. This quiz is combined with multi-question and True/False questions. When answering the questions please answer each by either their allocated letter or with True/False. The objective of this quiz is to get 5 or more questions correct so do your best. *note that not all questions may be what you think ")
        score = 0 #score variable set
        print("-------------------------------------------------------------------------")

        def run_test(questions): #function used for easy quiz
            global score #makes the score variable avaiable outside of the function
            score = 0 #score variable set
            for question in questions: #asks the question even though there is still questions to be asked 
                answer = input(question.prompt) #asks the question prompt
                answer = answer.lower() #makes the answer all in lowercase even if user types it in with caps
                if answer == question.answer: 
                    score += 1 #adds plus 1 score if user gets correct 
                    print(question.correct) #prints the correct response
                    print("YOUR SCORE IS NOW " + str(score)) #prints the score and lets the user know
                    print("-------------------------------------------------------------------------")
                elif answer == question.answer1:
                    score += 1 #adds plus 1 score if user gets correct
                    print(question.correct) #prints correct response
                    print("YOUR SCORE IS NOW " + str(score)) #prints the score  and lets the user know
                    print("-------------------------------------------------------------------------")
                else:
                    print(question.incorrect) #prints incorrect response
                    print("YOUR SCORE IS STILL " + str(score)) #prints the score and lets the user know
                    print("-------------------------------------------------------------------------")
        run_test(questions) #runs the questions
        
#End of easy quiz score/review/tally/time calculation
        end_time = time.time() #prints the time
        total_time = end_time - start_time #prints the time by subtracting end time by start time
        total_time = int(total_time) #prints the time as a whole number

        print("Congratulations, you've made it through the easy Rod and Reel quiz. Your final score is {} points.".format(score))
        print("-------------------------------------------------------------------------")
        print("Your total time taken to answer this quiz was {} seconds".format(total_time)) #lets user know their time taken to answer the quiz
        print("-------------------------------------------------------------------------")

        if score >= 10: #if user got 10/10
            print("Wow you really are a fishing master, probably even better than me!")

        elif score <=9 and score >=5: #if user got a score between 9 and 5
            print("Although it is not a 10/10 you are still a master in my books!")
 
        elif score == 5 and score >=2: #if user got score between 5 and 2
            print("Don't worry everyone still has room to improve and you can always try the quiz again!")

        else: #if user got score below 2
            print("Maybe next time use google for assistance when completing the quiz, that means next time you won't feel bad about not knowing anything.")

        print("-------------------------------------------------------------------------")
#looping code for person to try quiz again/attempt different difficulty quiz
        again = input("Would you like to attempt this quiz again or try a different difficulty? *please answer with either - yes or no -*")

        if again == 'Yes':
            next #repeats the whole code at choosing quiz difficulty

        elif again == 'yes':
            next

        elif again == 'Y':
            next

        elif again == 'y':
            next

#code below ends the whole quiz if player decides to type No that they don't want to attempt neither of the quizzes again       
        else:
            print("-------------------------------------------------------------------------")
            print("Ok, well I hoped you learned something new from this quiz {} and hopefully you are able to come back at some time to get an out of the water 10/10!" .format(name))
            break
        

        














#if hard quiz was selected
    if quiz_difficulty == "b":
        start_time = time.time() #records time
        print("-------------------------------------------------------------------------")
#breif introduction to quiz and score variable set
        print("You have decided to attempt the Hard fishing quiz. This quiz is combined with multi-question and True/False questions. When answering the questions please answer each by either their allocated letter or with True/False. The objective of this quiz is to get 5 or more questions correct so do your best. *note that not all questions may be what you think ")
        score = 0 #score variable for hard quiz set
        print("-------------------------------------------------------------------------")
#questions with correct/incorrect answers with responses
#scores aslo coninuously calculating
        hard_1 = input("Fish were the very first animal with a backbone to evolve - \nTrue \nFalse ")

        if hard_1 == 't':
            print("Correct! Fish were indeed the first animal to have a backbone and still evolve ")
            score += 1
            print("YOUR SCORE IS NOW: {} point".format(score))

        elif hard_1 == 'T':
            print("Correct! Fish were indeed the first animal to have a backbone and still evolve ")
            score += 1
            print("YOUR SCORE IS NOW: {} point".format(score))

        elif hard_1 == 'true':
            print("Correct! Fish were indeed the first animal to have a backbone and still evolve ")
            score += 1
            print("YOUR SCORE IS NOW: {} point".format(score))

        elif hard_1 == 'True':
            print("Correct! Fish were indeed the first animal to have a backbone and still evolve ")
            score += 1
            print("YOUR SCORE IS NOW: {} point".format(score))

        else:
            print("Incorrect! A jawless fish species were the first to evolve with a backbone.")
            print("YOUR SCORE IS STILL: {} points".format(score))
        

        print("-------------------------------------------------------------------------")


        hard_2 = input("Who Designed the first fishing rod? - \na) American Samuel Phillip \nb) John Badger \nc) Collin Phillips \nd) Mary Jones Badger ")

        if hard_2 == 'American Samuel Phillip':
            print("Correct! Until the mid-1800s rods were generally made in England. This changed in 1846 when American Samuel Phillip introduced an imported fishing rod the first six strips of Calcutta cane made in Bavaria where Phillippe was importing Violins that he passed off as his own handwork. ")
            score += 1
            print("YOUR SCORE IS NOW: {} points".format(score))

        elif hard_2 == 'american samuel phillip':
            print("Correct! Until the mid-1800s rods were generally made in England. This changed in 1846 when American Samuel Phillip introduced an imported fishing rod the first six strips of Calcutta cane made in Bavaria where Phillippe was importing Violins that he passed off as his own handwork. ")
            score += 1
            print("YOUR SCORE IS NOW: {} points".format(score))

        elif hard_2 == 'A':
            print("Correct! Until the mid-1800s rods were generally made in England. This changed in 1846 when American Samuel Phillip introduced an imported fishing rod the first six strips of Calcutta cane made in Bavaria where Phillippe was importing Violins that he passed off as his own handwork. ")
            score += 1
            print("YOUR SCORE IS NOW: {} points".format(score))

        elif hard_2 == 'a':
            print("Correct! Until the mid-1800s rods were generally made in England. This changed in 1846 when American Samuel Phillip introduced an imported fishing rod the first six strips of Calcutta cane made in Bavaria where Phillippe was importing Violins that he passed off as his own handwork. ")
            score += 1
            print("YOUR SCORE IS NOW: {} points".format(score))

        else:
            print("Incorrect! The answer was American Samuel Phillip, who used violin strings for the fishing line ")
            print("YOUR SCORE IS STILL: {} points".format(score))
        

        print("-------------------------------------------------------------------------")


        hard_3 = input("What was the first discovered fish?  - \na) hallucigenia \nb) anomalocaris \nc) opabinia \nd) pikaia ")

        if hard_3 == 'Pikaia':
            print("Correct! This extinct fish is said to be around 530 million years old ")
            score += 1
            print("YOUR SCORE IS NOW: {} points".format(score))

        elif hard_3 == 'pikaia':
            print("Correct! This extinct fish is said to be around 530 million years old ")
            score += 1
            print("YOUR SCORE IS NOW: {} points".format(score))

        elif hard_3 == 'D':
            print("Correct! This extinct fish is said to be around 530 million years old ")
            score += 1
            print("YOUR SCORE IS NOW: {} points".format(score))

        elif hard_3 == 'd':
            print("Correct! This extinct fish is said to be around 530 million years old ")
            score += 1
            print("YOUR SCORE IS NOW: {} points".format(score))

        else:
            print("Incorrect! The answer was Pikaia, this fish is a 500 year old extinct fish ")
            print("YOUR SCORE IS STILL: {} points".format(score))


        print("-------------------------------------------------------------------------")


        hard_4 = input("Do fish sleep? - \nTrue \nFalse ")

        if hard_4 == 't':
            print("Correct! While fish do not sleep in the same way that land mammals sleep, most fish do rest. ")
            score += 1
            print("YOUR SCORE IS NOW: {} points".format(score))

        elif hard_4 == 'T':
            print("Correct! While fish do not sleep in the same way that land mammals sleep, most fish do rest. ")
            score += 1
            print("YOUR SCORE IS NOW: {} points".format(score))

        elif hard_4 == 'true':
            print("Correct! While fish do not sleep in the same way that land mammals sleep, most fish do rest. ")
            score += 1
            print("YOUR SCORE IS NOW: {} points".format(score))

        elif hard_4 == 'True':
            print("Correct! While fish do not sleep in the same way that land mammals sleep, most fish do rest. ")
            score += 1
            print("YOUR SCORE IS NOW: {} points".format(score))
 
        else:
            print("Incorrect! The answer was True, fish DO sleep ")
            print("YOUR SCORE IS STILL: {} points".format(score))
        

        print("-------------------------------------------------------------------------")


        hard_5 = input("Which of these is not classified as a fish?  - \na) Moray Eel \nb) Lionfish \nc) jellyfish \nd) Sea horse ")

        if hard_5 == 'Jellyfish':
            print("Correct! Contrary to their name, the jellyfish is an invertebrate, not a fish. ")
            score += 1
            print("YOUR SCORE IS NOW: {} points".format(score))

        elif hard_5 == 'jellyfish':
            print("Correct! Contrary to their name, the jellyfish is an invertebrate, not a fish. ")
            score += 1
            print("YOUR SCORE IS NOW: {} points".format(score))

        elif hard_5 == 'C':
            print("Correct! Contrary to their name, the jellyfish is an invertebrate, not a fish. ")
            score += 1
            print("YOUR SCORE IS NOW: {} points".format(score))
   
        elif hard_5 == 'c':
            print("Correct! Contrary to their name, the jellyfish is an invertebrate, not a fish. ")
            score += 1
            print("YOUR SCORE IS NOW: {} points".format(score))

        else:
            print("Incorrect! The answer was Jellyfish, Jellyfish are invertebrates not fish. ")
            print("YOUR SCORE IS STILL: {} points".format(score))


        print("-------------------------------------------------------------------------")


        hard_6 = input("What determines a fish's body temperature?  - \na) How fast they swim \nb) What they eat  \nc) Water Temp \nd) Thermoregulation (like humans) ")

        if hard_6 == 'Water Temp':
            print("Correct! As cold-blooded animals, the body temperature of fish is determined by their environment, therefore it is determined by the temperature of the water they are in for nearly all fish. ")
            score += 1
            print("YOUR SCORE IS NOW: {} points".format(score))

        elif hard_6 == 'water temp':
            print("Correct! As cold-blooded animals, the body temperature of fish is determined by their environment, therefore it is determined by the temperature of the water they are in for nearly all fish. ")
            score += 1
            print("YOUR SCORE IS NOW: {} points".format(score))

        elif hard_6 == 'C':
            print("Correct! As cold-blooded animals, the body temperature of fish is determined by their environment, therefore it is determined by the temperature of the water they are in for nearly all fish. ")
            score += 1
            print("YOUR SCORE IS NOW: {} points".format(score))

        elif hard_6 == 'c':
            print("Correct! As cold-blooded animals, the body temperature of fish is determined by their environment, therefore it is determined by the temperature of the water they are in for nearly all fish. ")
            score += 1
            print("YOUR SCORE IS NOW: {} points".format(score))

        else:
            print("Incorrect! The answer was the water temperature, this also explains why fish are best to catch at certain times of the day. ")
            print("YOUR SCORE IS STILL: {} points".format(score))


        print("-------------------------------------------------------------------------")


        hard_7 = input("What is a unique characteristic that only fish behold?  - \na) Two-chambered heart \nb) Gills \nc) They Live In Water \nd) Scales ")

        if hard_7 == 'Two-chambered Heart':
            print("Correct! While fish display all these characteristics, some reptiles and mammals have scales, and some amphibians have gills and live in the water, the only thing true for fish alone is the two-chamber heart. ")
            score += 1
            print("YOUR SCORE IS NOW: {} points".format(score))

        elif hard_7 == 'two-chambered heart':
            print("Correct! While fish display all these characteristics, some reptiles and mammals have scales, and some amphibians have gills and live in the water, the only thing true for fish alone is the two-chamber heart. ")
            score += 1
            print("YOUR SCORE IS NOW: {} points".format(score))

        elif hard_7 == 'A':
            print("Correct! While fish display all these characteristics, some reptiles and mammals have scales, and some amphibians have gills and live in the water, the only thing true for fish alone is the two-chamber heart. ")
            score += 1
            print("YOUR SCORE IS NOW: {} points".format(score))

        elif hard_7 == 'a':
            print("Correct! While fish display all these characteristics, some reptiles and mammals have scales, and some amphibians have gills and live in the water, the only thing true for fish alone is the two-chamber heart. ")
            score += 1
            print("YOUR SCORE IS NOW: {} points".format(score))

        else:
            print("Incorrect! The answer was Two-chambered Heart")
            print("YOUR SCORE IS STILL: {} points".format(score))

 
        print("-------------------------------------------------------------------------")


        hard_8 = input("What is the fastest fish in the world?  - \na) Marlin \nb) Sailfish \nc) Tuna \nd) Nurse Shark ")

        if hard_8 == 'Sailfish':
            print("Correct! The Sailfish can swim up to 70mph ")
            score += 1
            print("YOUR SCORE IS NOW: {} points".format(score))

        elif hard_8 == 'sailfish':
            print("Correct! The Sailfish can swim up to 70mph ")
            score += 1
            print("YOUR SCORE IS NOW: {} points".format(score))
 
        elif hard_8 == 'B':
            print("Correct! The Sailfish can swim up to 70mph ")
            score += 1
            print("YOUR SCORE IS NOW: {} points".format(score))

        elif hard_8 == 'b':
            print("Correct! The Sailfish can swim up to 70mph ")
            score += 1
            print("YOUR SCORE IS NOW: {} points".format(score))

        else:
            print("Incorrect! The answer was Sailfish, the sailfish is the fastest fish in the world, followed by the marlin. ")
            print("YOUR SCORE IS STILL: {} points".format(score))


        print("-------------------------------------------------------------------------")


        hard_9 = input("What is the most consumed fish?  - \na) Tuna \nb) Cod \nc) Salmon \nd) Trout ")

        if hard_9 == 'Tuna':
            print("Correct! The most consumed fish is tuna, primarily in the form of canned tuna. ")
            score += 1
            print("YOUR SCORE IS NOW: {} points".format(score))

        elif hard_9 == 'tuna':
            print("Correct! The most consumed fish is tuna, primarily in the form of canned tuna. ")
            score += 1
            print("YOUR SCORE IS NOW: {} points".format(score))

        elif hard_9 == 'A':
            print("Correct! The most consumed fish is tuna, primarily in the form of canned tuna. ")
            score += 1
            print("YOUR SCORE IS NOW: {} points".format(score))

        elif hard_9 == 'a':
            print("Correct! The most consumed fish is tuna, primarily in the form of canned tuna. ")
            score += 1
            print("YOUR SCORE IS NOW: {} points".format(score))

        else:
            print("Incorrect! The answer was Tuna, this is found in supermarkets all over the world in the form of canned tuna ")
            print("YOUR SCORE IS STILL: {} points".format(score))


        print("-------------------------------------------------------------------------")


        hard_10 = input("What male species of fish are usually the ones who give birth?  - \na) Wolf Eel \nb) Sea Horse \nc) Swordfish \nd) Halibut ")

        if hard_10 == 'Sea Horse':
            print("Correct! Female seahorses transfer their eggs to the males making them the only creature where the males become pregnant. ")
            score += 1
            print("YOUR SCORE IS NOW: {} points".format(score))

        elif hard_10 == 'sea horse':
            print("Correct! Female seahorses transfer their eggs to the males making them the only creature where the males become pregnant. ")
            score += 1
            print("YOUR SCORE IS NOW: {} points".format(score))

        elif hard_10 == 'B':
            print("Correct! Female seahorses transfer their eggs to the males making them the only creature where the males become pregnant. ")
            score += 1
            print("YOUR SCORE IS NOW: {} points".format(score))

        elif hard_10 == 'b':
            print("Correct! Female seahorses transfer their eggs to the males making them the only creature where the males become pregnant. ")
            score += 1
            print("YOUR SCORE IS NOW: {} points".format(score))

        else:
            print("Incorrect! The answer was Sea Horse, these are the only animal species where the male gives birth. ")
            print("YOUR SCORE IS STILL: {} points".format(score))


        print("-------------------------------------------------------------------------")


 #End of hard quiz score/review/tally/time calculation

        end_time = time.time()
        total_time = end_time - start_time
        total_time = int(total_time)

        print("Congratulations, you've made it through the hard Rod and Reel quiz. Your final score is {} points.".format(score))
        print("-------------------------------------------------------------------------")
        print("Your total time taken to answer this quiz was {} seconds".format(total_time))
        print("-------------------------------------------------------------------------")

        
        if score >= 10:
            print("Wow 10/10 on the hard quiz, either you're a nerd at fishing or it was all luck, either way congrats")

        elif score <=9 and score >=5:
            print("Although it is not a 10/10 you are still a master in my books!")

        elif score == 5 and score >=2:
            print("Don't worry everyone still has room to improve and you can always try the quiz again!")

        else:
            print("Maybe next time use google for assistance when completing the quiz, that means next time you won't feel bad about not knowing anything.")


        print("-------------------------------------------------------------------------")

 #looping code for person to try quiz again/attempt different difficulty quiz
        again = input("Would you like to attempt this quiz again or try a different difficulty? *please answer with either yes or no*")

        if again == 'Yes':
            next

        elif again == 'yes':
            next

        elif again == 'Y':
            next

        elif again == 'y':
            next

#code below ends the whole quiz if player decides to type No that they don't want to attempt neither of the quizzes again       
        else:
            print("-------------------------------------------------------------------------")
            print("Ok, well I hoped you learned something new from this quiz {} and hopefully you are able to come back at some time to get an out of the water 10/10!" .format(name))
            break
        
    
    

                                                                            



    

   

        
    
        
    
        
    
    


    
        










        


 




