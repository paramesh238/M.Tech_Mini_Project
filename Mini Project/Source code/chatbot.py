import tkinter as tk
import json
import random

class CovidChatbotApp:
    def __init__(self, root):
        self.root = root
        self.root.title("COVID-19 Medical Chatbot")

        self.chat_log = tk.Text(root, wrap=tk.WORD, width=40, height=10)
        self.chat_log.pack(padx=10, pady=10)

        self.input_entry = tk.Entry(root, width=40)
        self.input_entry.pack(padx=10, pady=10)

        self.send_button = tk.Button(root, text="Send", command=self.send_message)
        self.send_button.pack()

        self.intents = self.load_intents("C:\\Users\\knvbo\\OneDrive\\Desktop\\data\\covid-19.json")

    def load_intents(self, file_path):
        with open(file_path, "r") as json_file:
            intents = json.load(json_file)
        return intents["intents"]

    def send_message(self):
        user_input = self.input_entry.get()
        self.update_chat_log("You: " + user_input)

        response = self.get_response(user_input)
        self.update_chat_log("Bot: " + response)

    def get_response(self, user_input):
        for intent in self.intents:
            for pattern in intent["patterns"]:
                if pattern.lower() in user_input.lower():
                    return random.choice(intent["responses"])
        return "I'm sorry, I don't have an answer for that."

    def update_chat_log(self, message):
        self.chat_log.insert(tk.END, message + "\n")
        self.chat_log.see(tk.END)
        self.input_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = CovidChatbotApp(root)
    root.mainloop()
