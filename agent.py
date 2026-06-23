from groq import Groq
import math
import os 

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def calculate(expression):
    try:
        result = eval(expression, {"__builtins__": {}}, {"math": math})
        return str(result)
    except Exception as e:
        return f"Error: {e}"


def get_weather(city):
    # Mock weather data for demo purposes
    data = {
        "almaty": "Almaty: +28C, sunny",
        "moscow": "Moscow: +15C, cloudy",
        "london": "London: +12C, rainy",
    }
    return data.get(city.lower(), f"No weather data for '{city}'")


def search_info(query):
    # Placeholder - replace with SerpAPI for real search
    return f"Search result for '{query}': connect a real search API like SerpAPI"


def run_agent(user_input):
    system_prompt = """You are a helpful AI assistant with tools.
    Answer in the user's language. Be concise and helpful."""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input}
        ],
        max_tokens=500
    )

    return response.choices[0].message.content


def main():
    print("AI Agent is running! Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() in ["exit", "quit"]:
            print("Agent stopped.")
            break

        if not user_input:
            continue

        response = run_agent(user_input)
        print(f"\nAgent: {response}\n")


if __name__ == "__main__":
    main()