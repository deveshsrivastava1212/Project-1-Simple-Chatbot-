class CustomChatbot:
    def __init__(self):
        self.context = {}

    def greet(self):
        return "Hello! I'm your custom chatbot. What would you like to talk about today?"

    def respond_to_question(self, question):
        responses = {
            "How are you today?": "I'm functioning well, thank you for asking!",
            "What's your name?": "I'm known as the Simple Chatbot.",
            "What is the meaning of life?": "The meaning of life is subjective and varies from person to person.",
            "Tell me about Universe": "Sure, The Universe is the vast cosmic expanse containing galaxies, stars, planets, and all matter and energy.",
            "What is Turing Test?": " Evaluates machine's ability to exhibit intelligent behavior indistinguishable from human.",
        }

        return responses.get(question, "I'm not sure how to respond to that at the moment.")

    def farewell(self):
        return "Goodbye! Feel free to return anytime for more conversations."

    def ask_user_questions(self):
        questions = [
            "How's your day going so far?",
            "What's on your mind?",
        ]

        for question in questions:
            user_response = input(question + " ")
            self.context[question] = user_response
            print("Chatbot: Interesting!")

    def handle_user_input(self, user_input):
        if "bye" in user_input.lower():
            return self.farewell()

        response = self.respond_to_question(user_input)

        if response == "I'm not sure how to respond to that at the moment.":
            print("Chatbot: Apologies, I didn't quite catch that. Could you please rephrase?")
        else:
            print(f"Chatbot: {response}")

    def chat(self):
        print(self.greet())
        self.ask_user_questions()

        while True:
            user_input = input("User: ")
            if not user_input:
                continue

            if "exit" in user_input.lower():
                print(self.farewell())
                break

            self.handle_user_input(user_input)


if __name__ == "__main__":
    chatbot = CustomChatbot()
    chatbot.chat()
