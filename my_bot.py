
def should_i_respond(user_message, user_name):
  if "robot" in user_message:
    return True
  else:
    return False
  
def respond(user_message, user_name):
  return f"""you said my name!!
  {user_message.replace("robot", user_name)}"""