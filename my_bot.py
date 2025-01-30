
import random
import string
alphabet = string.ascii_lowercase
def should_i_respond(user_message, user_name):
     if "robot" in user_message:
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
       return False
     
def respond(user_message, user_name):
 if "robot" == user_message:
   return user_message.upper()
 if "down" == user_message:
   return user_message.lower()
 if "animal" == user_message or "pet" == user_message:
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
   return("Here's a fun fact about animals! {animal_jokes}")

 if "corny" == user_message or "cheesy" == user_message:
   corny_jokes = [ 
     "Why do crabs never give to charity? Because they’re shellfish.",
     "For a fungi to grow, you must give it as mushroom as possible.",
     "I was going to grow some herbs, but I couldn’t find the thyme.",
     "What do you call a sheep who can sing and dance? Lady Ba Ba.",
     "What do you call a French man wearing sandals? Philipe Fallop.",
     "Who won the neck decorating contest? It was a tie.",
     "What do you call the security guards for Samsung? Guardians of the galaxy.",
   ]
   random_jokes = random.choice(corny_jokes)
   return(random_jokes)
 if "mixed" == user_message:
   def mixed():
     text = user_message
     text = text.replace("a", "A")
     text = text.replace("e", "E")
     text = text.replace("i", "I")
     text = text.replace("o", "O")
     text = text.replace("u", "U")
     return text
   mixed()
 if "hungry" == user_message:
   cuisine_list = input("Do you like Italian, Mexican, Japanese, or Indian food?")
   if "Italian" in cuisine_list:
     italian = ["lasagna", "risotto", "cacio e pepe", "tiramisu", "arancini", "focaccia", "gelato"]
     italian_food = random.choice(italian)
     return("I suggest you try {italian_food}!")
   if "Mexican" in cuisine_list:
     mexican = ["tamales", "enchiladas", "pozole", "churros", "birria", "fajitas", "tortas"]
     mexican_food = random.choice(mexican)
     return("I suggest you try {mexican_food}!")
   if "Japanese" in cuisine_list:
     japanese = ["ramen", "takoyaki", "gyudon", "sushi", "tempura", "udon", "shabu-shabu"]
     japanese_food = random.choice(japanese)
     return("I suggest you try {japanese}!")
   if "Indian" in cuisine_list:
     indian = ["biryani", "samosas", "tikka masala", "pani puri", "aloo gobi", "masala dosa", "chana masala"]
     indian_food = random.choice(indian)
     return("I suggest you try {indian_food}!")
   if "cold" == user_message:
     return ("Make sure to wear a jacket!")
   if "random" == user_message:
     key = float(input("Pick a number!"))
     def randomize(user_message):
       new_text = ""
       for letter in user_message:
          old_position = alphabet.find(letter)
          if old_position == -1:
            new_text += " "
          else:
            new_position = old_position + key
            new_position = new_position % len(alphabet)
            new_letter = alphabet[new_position]
            new_text += new_letter
       return new_text
     return(randomize(user_message))
   if "time" == user_message:
      def countdown():
        time = float(input("Pick a number!"))
        for i in range(time):
          countdown -= 1
          return countdown
        if countdown == 0:
            return "Blast off!!!"
      countdown()

     
     
    
       
     


