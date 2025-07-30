import requests

def chat_with_ollama(model="llama3"):
    print(f"🤖 Chatbot (model: {model}) – Type 'exit' to quit\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() in ["exit", "quit"]:
            print("Exiting chat. Goodbye!")
            break

        response = requests.post(
            "http://localhost:11434/api/generate",
            json={"model": model, "prompt": user_input}
        )

        if response.status_code == 200:
            content = response.json()
            print(f"{model}: {content.get('response', '').strip()}\n")
        else:
            print(f"Error: {response.status_code} – {response.text}\n")

if __name__ == "__main__":
    chat_with_ollama()
