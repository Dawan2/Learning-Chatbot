import json
from difflib import get_close_matches
from colorama import Style, Fore

data = json.load(open("data.json"))

def get_closest_match(word, options):
  matches = get_close_matches(word,options, n = 1, cutoff = 0.8)
  if matches:
    return matches [0]
  else:
    return None

def get_response(word):
  word = word.lower()
  if word in data:
    return data[word]
  else:
    closest_match = get_closest_match(word, data.keys())
    if closest_match:
      return data[closest_match]
    else:
      return None

def update_data(question, response):
  data[question] = response
  with open("data.json", "w") as json_file:
    json.dump(data, json_file)

def main():
  while True:
    user_input = input(Fore.GREEN + Style.BRIGHT + "You: " + Style.RESET_ALL)
    if user_input.lower() == 'quit':
      break
      
    response = get_response(user_input)

    if response:
      print (Fore.YELLOW + Style.BRIGHT + "ChatBot:" + Style.RESET_ALL, response)
    else:
      print (Fore.RED + Style.BRIGHT + "ChatBot: " + Style.RESET_ALL + "Sorry I am not sure how to respond to that. Can you help me understand?")
      correct_response = input(Fore.GREEN + Style.BRIGHT + "You: " + Style.RESET_ALL)
      update_data(user_input.lower(), correct_response)
      print (Fore.YELLOW + Style.BRIGHT + "ChatBot: " + Style.RESET_ALL + "Thank you I will remember that next time." + Style.RESET_ALL)

if __name__ == "__main__":
  main()
