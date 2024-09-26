import random   # Needed for Pt 4
vidNames =[]

# You are running an online video channel. Your subscribers
# pay to watch videos on your channel of different lengths.
# You also have a competing channel - will your subscribers
# spend more time watching your videos than your competitor's?
# Who will be more successful?!

# Part 1 - Part 1 - What are the titles of the videos in your channel?
#I created a forever loop so that can the user can upload as many titles as they want
#In order to break the loop, the user must type 'finished' after the input the last
#Video name. I got the idea for writing a program like this from the lesson
#8.8 ZyLabs. I also want the names of the videos to be saved as a string.

print("Part 1 - What are the titles of the videos in your channel? ")
while True:
    userNames = str(input('What are the titles of the videos in your channel? After you have inputted all the names for the videos, please type out \'Finished\' to save your list!: \n'))
    if userNames.lower() in ('finished', 'f'):
        break
    vidNames.append(userNames)
    
print('\nHere are the names of all your YouTube videos!\n',f'{vidNames}\n')


# Part 2 - How long is each video in your channel?
#First, we need to know how long our list is. To do this we must utilize the len()
#function. After we have our count, we can create a list that houses all the time
#lengths of the videos. Since we want video times for every single video in our list
#from part 1, we must create a loop that iterates for the same length as vidNames.
#After we have all of our video lengths, we use basic python features such as
#max(), min(), sum(), and len() to get the longest video, shortest video, and average
#length of a video. We must also save our variables as floats as they can be decimals.
#I also create a dictionary so that the video name and its respective run time can be
#stored together so that we can call upon this dictionary later in our program

print("Part 2 - How long is each video in your channel?")
viewDict = {}
vidTimes = []

for i in vidNames:
    userTime = float(input('How long is each video in your channel? Keep in mind, the videos are measured in minutes:'))
    viewDict[i] = userTime
    vidTimes.append(userTime)

print('\nThe shortest video on the channel is ',f'{min(vidTimes)} minutes')
print('The longest video on the channel is ',f'{max(vidTimes)} minutes')
averageTime = sum(vidTimes) / len(vidTimes)
print('The average length of a video on the channel is ',f'{averageTime:.3f} minutes')


# Part 3 - Let's talk about subscribers!
#In this part, we need to make sure the user can input their desired number of
#subscribers. Since this number will always be an integer, I made sure the
#input was always saved as an integer. I saved the number of subscribers as a variable
#This variable will be used in the loop. Since every subscriber needs to have their own
#video, I made sure that the number of loop interations matches the number of
#subscribers. Every time the loop interates, each subscriber would get assigned a
#random number. In addition, this loop also calls upon the dictionary created in part 2
#This part of the loop takes the video name and the associated time of the video
#it adds up the times of each video found in list of videos assigned to the subscriber.
#The final part of this code creates a set out of the subscriber video list so that the
#user can see which videos were viewed without having any repeats. It also shows the user
#the total time spent watching the videos across all subscribers. Code for calling the dictionary
#comes from https://www.geeksforgeeks.org/python-accessing-key-value-in-dictionary/

print("Part 3 - Let's talk about subscribers.")
viewers = int(input('\nHow many subscribers do you want you the channel have?: '))
viewList = []
totalMinutes = 0

for i in range (viewers):
    randVid = random.choice(vidNames)
    viewList.append(randVid)
    print('\nWe recommend Subscriber #',i+1,'watch the',randVid,'video\n')
    totalMinutes += viewDict[randVid]


vidListSet = set(viewList)

print('These viewers have spent', totalMinutes,'minutes watching videos')
print('The subscribers watched these videos:',vidListSet,'\n')



# Part 4 - Let's compare our channel to our competitor!
#This part starts off with me assigning the competitor channel with a random number of subscribers
#Later, I want to give each of these subscribers a watch time for the videos, so I assign them a random
#time between 1 and 5 minutes. I use a random.uniform to generate a random float value. I then make a loop
#to store all the watch times in a list. After the loop is done iterating, I print the sum of all the watch
#times. After printing the competitor watch time, I run a conditional to compare my watch times to the competition's watch time
#There are unique outputs depending on if their channel has more view minutes than us, if we have more view minutes than them, or
#if we have an equal amount of view minutes.

print("Part 4 - Let's compare our channel to our competitor!")
compTime = []
compSubs = random.randint(1,100)
print('The competitor has',compSubs,'subscribers')

for i in range(compSubs):
    compTime.append(random.uniform(1,5))

print('Competitor watch time is ',f'{sum(compTime):.3f} minutes\n')
lostDifference = sum(compTime) - totalMinutes
winDifference = totalMinutes - sum(compTime)

if totalMinutes > sum(compTime):
    print('We win! We have ',f'{winDifference:.3f} more minutes watched than our competitor!')
elif sum(compTime) > totalMinutes:
    print('We lost. Our competitor had',f'{lostDifference:.3f} more minutes watched than us.')
else:
    print('It\'s a tie! We have the same watch time!\n')

print('For reference, the competitor\'s watch time was ',f'{sum(compTime):.3f} minutes.\nWhile our watch time was ',f'{totalMinutes} minutes.')




