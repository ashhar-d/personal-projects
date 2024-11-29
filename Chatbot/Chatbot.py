import google.generativeai as genai

GOOGLE_API_KEY = 'Your_API_Key'
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')

def chat_with_bot():

    chat = model.start_chat(history=[])
    print("Chatbot: Hello")

    while True:

        user_input = input("You: ").strip()

        if user_input.lower() == 'quit':
            print("Chatbot: Goodbye!")
            break
        try:
            reponse = chat.send_message(user_input)
            print("Chatbot:", reponse.text)

        except Exception as e:
            print(f"An error occured: {str(e)}")

if __name__ == "__main__":
    chat_with_bot()