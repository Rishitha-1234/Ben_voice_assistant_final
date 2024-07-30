def get_joke():
    url = "https://v2.jokeapi.dev/joke/Any"
    response = requests.get(url).json()
    speak(f"Here's a joke: {response['setup']} - {response['punchline']}")
    print(f"Here's a joke: {response['setup']} - {response['punchline']}")
    