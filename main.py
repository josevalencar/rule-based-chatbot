import re
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
import nltk
from difflib import get_close_matches

nltk.download('stopwords')

class Chatbot:
    def __init__(self):
        self.intentions = {
            "big_house": "Pegasus is flying to the Big House.",
            "arena": "Pegasus is soaring towards the Arena.",
            "stables": "Pegasus is returning to the Pegasus Stables.",
            "strawberry_fields": "Pegasus is gliding over the Strawberry Fields."
        }

        self.actions = {
            "big_house": self.fly_to_big_house,
            "arena": self.fly_to_arena,
            "stables": self.fly_to_pegasus_stables,
            "strawberry_fields": self.fly_to_strawberry_fields
        }

        self.stop_words = set(stopwords.words('english'))
        self.tokenizer = RegexpTokenizer(r'\w+')

    def preprocess_input(self, user_input):
        words = self.tokenizer.tokenize(user_input.lower())
        return [word for word in words if word not in self.stop_words]

    def get_response(self, processed_input):
        for word in processed_input:
            match = get_close_matches(word, self.intentions.keys(), n=1, cutoff=0.6)
            if match:
                intention = match[0]
                action_result = self.actions[intention]()
                return f"{self.intentions[intention]} {action_result}"
        return "Sorry, I didn't understand the command."

    def fly_to_big_house(self):
        return "Action: Flying to the Big House."

    def fly_to_arena(self):
        return "Action: Soaring towards the Arena."

    def fly_to_pegasus_stables(self):
        return "Action: Returning to the Pegasus Stables."

    def fly_to_strawberry_fields(self):
        return "Action: Gliding over the Strawberry Fields."

    def run(self):
        print("Camp Half-Blood Pegasus Chatbot started. Awaiting commands...")

        while True:
            try:
                user_input = input("Give a command: ")
                processed_input = self.preprocess_input(user_input)
                response = self.get_response(processed_input)
                print(f"Response: {response}")
            except KeyboardInterrupt:
                print("\nShutting down the Pegasus chatbot.")
                break

if __name__ == "__main__":
    bot = Chatbot()
    bot.run()
