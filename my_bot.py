"""
**Do NOT change the name of this function.**

This function will be called every time anyone says anything on a channel where the bot lives.

* It returns `True` if the bot notices something it wants to repond to.
* You can have certain words or patterns in the messages trigger the bot.
* You can have the bot respond differently to different users
"""
def should_i_respond(user_message, user_name):
  if "favourite color" in user_message:
    return True
  elif "what is your name" in user_message:
    return True
  elif "what is your favourite food" in user_message:
    return True
  elif "how old are you" in user_message:
    return True
  elif "what is your favourite class" in user_message:
    return True
  elif "what is your favourite snack" in user_message:
    return True
  elif "do you have any relatives" in user_message:
    return True
  elif "Do you like apples or oranges more" in user_message:
    return True
  elif "Do you like Halloween or Christmas more" in user_message:
   return True
  elif "Do you have any siblings" in user_message:
    return True
  else:
    return False

"""
**Do NOT change the name of this function.**

This function will be called every time the `should_i_respond` function returns `True`.

* This function returns a string.
* The bot will post the returned string on the channel where the original message was sent.
* You can have the bot respond differently to different messages and users
"""
def respond(user_message, user_name):
  if "what is your name" in user_message:
    return "my name is chat-bot"
  elif "favourite color" in user_message:
    return "my favourite color is green"
  elif "what is your favourite food" in user_message:
    return "my favourite food is pizza"
  elif "how old are you" in user_message:
    return "I am 156 years old"
  elif "what is your favourite class" in user_message:
    return "my favourite class is Computer Science" 
  elif "what is your favourite snack" in user_message:
    return "my favourite snack is Oreos"
  elif "do you have any relatives" in user_message:
   return "no"
  elif "Do you like apples or oranges more" in user_message:
   return "I like oranges more"
  elif "Do you like Halloween or Christmas more" in user_message:
    return "I like Halloween more"
  elif "Do you have any siblings" in user_message:
    return "no"