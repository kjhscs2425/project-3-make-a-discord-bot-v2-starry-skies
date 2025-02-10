
import random
import string
alphabet = string.ascii_lowercase
global state
state = ""

def should_i_respond(user_message, user_name):
     if "up" in user_message:
      return True
     if "down" in user_message:
      return True
     if "animal" or "pet" in user_message:
      return True
     if "capitilize" in user_message:
      return True
     if "joke" in user_message:
      return True
     if "hungry" in user_message:
      return True
     if "cold" in user_message:
       return True
     if "encrypt" in user_message:
      return True
     if "time" in user_message:
      return True
     if "backward" in user_message:
       return True
     if "Italian" in user_message or "italian" in user_message:
       return True
     if "Mexican" in user_message or "mexican" in user_message:
       return True
     if "Japanese" in user_message or "japanese" in user_message:
       return True
     if "Indian" in user_message or "indian" in user_message:
       return True
     else:
       return False
     
def my_respond(user_message, user_name):
  global state
  state = ""
  if "up" in user_message:
    state = "up"
    return "What word should I capitilize?"
  if state == "up":
    message = user_message.upper()
    state = "start"
    return message
  if "down" in user_message:
    state = "down"
    return "What word should I lowercase?"
  if state == "down":
    return user_message.lower()
  if "animal" in user_message or "pet" == user_message:
   animal_jokes = ["A polar bear’s hair is not white – it’s colourless!", "There are no male or female earthworms. All earthworms have both male and female parts – but it still takes two of them to reproduce.", "Huskies can run at speeds of around 31km per hour (20mph)!", "An eagle’s eyes are at least four times sharper than a human’s!", "Giant tortoise from the Galápagos Islands near Ecuador can weigh up to 250kg (550lbs) – the same as a brown bear!", "The lion has the loudest roar of all the big cats. It can be heard as far as 5km (3 miles) away.","Humans share 98.8 percent of chimpanzee DNA. But even with DNA so similar, humans and chimps have around 35 million differences between them."]
   random_animal_jokes = random.choice(animal_jokes)
   return(f"Here's a fun fact about animals! " + random_animal_jokes)
  if "joke" in user_message:
   corny_jokes = [ "Why do crabs never give to charity? Because they’re shellfish.", "For a fungi to grow, you must give it as mushroom as possible.", "I was going to grow some herbs, but I couldn’t find the thyme.", "What do you call a sheep who can sing and dance? Lady Ba Ba.", "What do you call a French man wearing sandals? Philipe Fallop.", "Who won the neck decorating contest? It was a tie.", "What do you call the security guards for Samsung? Guardians of the galaxy."]
   random_jokes = random.choice(corny_jokes)
   return(random_jokes)
  if  "capitilize" in user_message:
   user_message = user_message.replace("a", "A")
   user_message = user_message.replace("e", "E")
   user_message = user_message.replace("i", "I")
   user_message = user_message.replace("o", "O")
   user_message = user_message.replace("u", "U")
   return user_message
  if "cold" in user_message:
    return "Make sure to wear a jacket!"
  if "encrypt" in user_message:
    state = "encrypt"
    return "What word should I encrypt?"
  if state == "encrypt":
    key_choices = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
    random_key = random.choice(key_choices)
    new_text = ""
    for letter in user_message:
          old_position = alphabet.find(letter)
          if old_position == -1:
            new_text += " "
          else:
            new_position = (old_position + random_key) % len(alphabet)
            new_letter = alphabet[new_position]
            new_text += new_letter
    return new_text
  if "time" in user_message:
    random_time = random.randint(1, 100)
    message = ""
    for i in range(random_time, 0, -1):
       message += str(i) + " "
    return message
  if "backward" in user_message:
    state = "backwards"
    return "What word should I spell backwards?"
  if state == "backwards":
    reverse = user_message[::-1]
    return reverse
  if "hungry" in user_message:
    state = "hungry"
    return f"""Do you want to have Italian, Mexican, Japanese, or Indian food?"""
  if state == "hungry":
    if "Italian" or "italian" in user_message:
      state == "Italian"
      italian = ["lasagna", "risotto", "cacio e pepe", "tiramisu", "arancini", "focaccia", "gelato"]
      italian_food = random.choice(italian)
      return (f"I suggest you try " + italian_food + "!")
    if "Mexican" or "mexican" in user_message:
      state == "Mexican"
      mexican = ["tamales", "enchiladas", "pozole", "churros", "birria", "fajitas", "tortas"]
      mexican_food = random.choice(mexican)
      return (f"I suggest you try " + mexican_food + "!")
    if "Japanese" or "japanese" in user_message:
      state = "Japanese"
      japanese = ["ramen", "takoyaki", "gyudon", "sushi", "tempura", "udon", "shabu-shabu"]
      japanese_food = random.choice(japanese)
      return(f"I suggest you try " + japanese_food + "!")
    if "Indian" or "indian" in user_message:
      state = "Indian"
      indian = ["biryani", "samosas", "tikka masala", "pani puri", "aloo gobi", "masala dosa", "chana masala"]
      indian_food = random.choice(indian)
      return f"I suggest you try " + indian_food + "!"
  