"""
**Do NOT change the name of this function.**

This function will be called every time anyone says anything on a channel where the bot lives.

* It returns `True` if the bot notices something it wants to repond to.
* You can have certain words or patterns in the messages trigger the bot.
* You can have the bot respond differently to different users
"""
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


  if "up" == True:

""" 
**Do NOT change the name of this function.**

This function will be called every time the `should_i_respond` function returns `True`.

* This function returns a string.
* The bot will post the returned string on the channel where the original message was sent.
* You can have the bot respond differently to different messages and users
"""
def respond(user_message, user_name):
  return f"""Hello, you called my name!
  {user_message.replace("robot", user_message + "What would you like me to do?")}"""

#  * [ ] `.lower()`, `.upper()`, and/or `.capitalize()`
#     * [ ] `.replace()`
# * [ ] You should iterate through at least one string using a `for` loop
# * [ ] You should use string string indexing (e.g. `my_string[3]`) and/or string slicing (e.g. `my_string[3:6]`)
# * [ ] Your code should use at least one function from the `random` library
# * [ ] Your bot should respond to at least 10 different messages that a user in your discord channel might send
if "up" == True:
  
When a user says: up
My bot will respond by: making all the letters uppercase

When a user says: down
My bot will respond by: making all the letters lowercase

When a user says: animal/pet
My bot will respond by: saying a random fun fact about animals

When a user says: cheesy/corny (both will work)
My bot will respond by: saying a dad joke

When a user says: mixed
My bot will respond by: change all the letters to mixed case

When a user says: hungry
My bot will respond by: give a suggestion of what they should eat
When a user says: hungry
My bot will respond by: give a suggestion of what they should eat

When a user says: cold
My bot will respond by: telling them to wear a jacket

When a user says: random
My bot will respond by: mix up the letters in the sentence

When a user says: time
My bot will respond by: count down to blast off

When a user says: backwards
My bot will respond by: repeat the message backwards