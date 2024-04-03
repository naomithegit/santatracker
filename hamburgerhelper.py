import emoji
from emoji import emojize

import datetime

hamburger = emojize(":hamburger:")
print()
print()
print()
print(hamburger)

pizza = emojize(':pizza:')
print(pizza)

thinkingface = emojize(":thinking_face:")
print(thinkingface)

today = datetime.datetime.now()
#print(today)

lastdayofkeyin = "2024-12-20"
lastdayofkeyin = datetime.datetime.strptime(lastdayofkeyin, "%Y-%m-%d")
##print(lastdayofkeyin)

xmasday = "2024-12-25"
xmasday = datetime.datetime.strptime(xmasday, "%Y-%m-%d")
#print(xmasday)

sleepstilsanta = xmasday - today
#print(sleepstilsanta)

sleepstilGraduation = lastdayofkeyin - today
#print(sleepstilGraduation)

sleepstisantaDSP = sleepstilsanta.days

sadface = emojize(":neutral_face:")

print(f"Don't be sad guys.{sadface} ")
print (f"Only {sleepstisantaDSP} sleeps til SANTA!!!")

telephone = emojize(":grapes:")
clown = emojize(":clown_face:")
print(telephone, clown,telephone, clown, telephone, clown, telephone)
sleepstilGraduationDSP = sleepstilGraduation.days
print(f"AND>>>>>only {sleepstilGraduationDSP} sleeps til we are done school!!!!!")
print('seems kinda a long way off!!!')
turtle = emojize(":turtle:")
warning = emojize(":fire:")
print(turtle, warning, turtle, warning, turtle, warning, turtle, warning, turtle, warning, turtle, warning, turtle, warning, turtle)
print()
print()
print()
print()
print()
