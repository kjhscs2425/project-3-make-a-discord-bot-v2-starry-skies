"""

**Do NOT change the name of this function.**

This function will be called every time anyone says anything on a channel where the bot lives.

* It returns `True` if the bot notices something it wants to repond to.
* You can have certain words or patterns in the messages trigger the bot.
* You can have the bot respond differently to different users
"""
import random
def should_i_respond(user_message, user_name):
  if "up" in user_message:
   return True
  if "down" in user_message:
    return True
  if "animal" or "pet" in user_message:
    return True
  if "mixed" in user_message:
    return True
  if "cheesy" or "corny" in user_message:
    return True
  if "hungry" in user_message:
     return True
  if "cold" in user_message:
    return True
  if "random" in user_message:
    return True
  if "time" in user_message:
    return True
  if "backward" in user_message:
    return True
  else:
    should_i_respond(user_message, user_name)


  
""" 
**Do NOT change the name of this function.**

This function will be called every time the `should_i_respond` function returns `True`.

* This function returns a string.
* The bot will post the returned string on the channel where the original message was sent.
* You can have the bot respond differently to different messages and users
"""
def respond(user_message, user_name):
  if "up" == True:
    user_message.upper()
  if "down" == True:
    user_message.lower()
  if "animal" == True or "pet" == True:
    animal_jokes = [
      "A polar bear’s hair is not white – it’s colourless!",
      "There are no male or female earthworms. All earthworms have both male and female parts – but it still takes two of them to reproduce."
      "Huskies can run at speeds of around 31km per hour (20mph)!",
      "An eagle’s eyes are at least four times sharper than a human’s!",
      "Giant tortoise from the Galápagos Islands near Ecuador can weigh up to 250kg (550lbs) – the same as a brown bear!",
      "The lion has the loudest roar of all the big cats. It can be heard as far as 5km (3 miles) away.",
      "Humans share 98.8 percent of chimpanzee DNA. But even with DNA so similar, humans and chimps have around 35 million differences between them."
    ]
    random.choice(animal_jokes)
    print("Here's a fun fact about animals! {animal_jokes}")

  if "corny" == True or "cheesy" == True:
    corny_jokes = [ 
    "Why do crabs never give to charity? Because they’re shellfish.",
    "For a fungi to grow, you must give it as mushroom as possible.",
    "I was going to grow some herbs, but I couldn’t find the thyme.",
    "What do you call a sheep who can sing and dance? Lady Ba Ba.",
    "What do you call a French man wearing sandals? Philipe Fallop.",
    "Who won the neck decorating contest? It was a tie.",
    "What do you call the security guards for Samsung? Guardians of the galaxy.",
    ]
    random.choice(corny_jokes)
    print(corny_jokes)
  if "mixed" == True:
    def mixed():
      text = user_message
      text = text.replace("a", "A")
      text = text.replace("e", "E")
      text = text.replace("i", "I")
      text = text.replace("o", "O")
      text = text.replace("u", "U")
      print(text)
      return
    mixed()
  if "hungry" == True:
    cuisine_list = input("Do you like Italian, Mexican, Japanese, or Indian food?")
    if "Italian" in cuisine_list:
      italian = ["lasagna", "risotto", "cacio e pepe", "tiramisu", "arancini", "focaccia", "gelato"]
      italian_food = random.choice(italian)
      print("I suggest you try {italian_food}!")
    if "Mexican" in cuisine_list:
      mexican = ["tamales", "enchiladas", "pozole", "churros", "birria", "fajitas", "tortas"]
      mexican_food = random.choice(mexican)
      print("I suggest you try {mexican_food}!")
    if "Japanese" in cuisine_list:
      japanese = ["ramen", "takoyaki", "gyudon", "sushi", "tempura", "udon", "shabu-shabu"]
      japanese_food = random.choice(japanese)
      print("I suggest you try {japanese}!")
    if "Indian" in cuisine_list:
      indian = ["biryani", "samosas", "tikka masala", "pani puri", "aloo gobi", "masala dosa", "chana masala"]
      indian_food = random.choice(indian)
      print("I suggest you try {indian_food}!")
    if "cold" == True:
      print ("Make sure to wear a jacket!")
    if "random" == True:
      2
  



  # {user_message.replace("robot", user_message + "What would you like me to do?")}"""

#  * [ ] `.lower()`, `.upper()`, and/or `.capitalize()`
#     * [ ] `.replace()`
# * [ ] You should iterate through at least one string using a `for` loop
# * [ ] You should use string string indexing (e.g. `my_string[3]`) and/or string slicing (e.g. `my_string[3:6]`)
# * [ ] Your code should use at least one function from the `random` library
# * [ ] Your bot should respond to at least 10 different messages that a user in your discord channel might send
# if "up" == True:

]\

# When a user says: hungry
# My bot will respond by: give a suggestion of what they should eat
# When a user says: hungry
# My bot will respond by: give a suggestion of what they should eat

# When a user says: cold
# My bot will respond by: telling them to wear a jacket

# When a user says: random
# My bot will respond by: mix up the letters in the sentence

# When a user says: time
# My bot will respond by: count down to blast off

# When a user says: backwards
# My bot will respond by: repeat the message backwards