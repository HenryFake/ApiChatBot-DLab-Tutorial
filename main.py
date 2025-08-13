import requests

url = "https://dlabot.azurewebsites.net/chat"
payload = {
    "sysApi": "Actúa como Goku",
    "assisApi": "Hola, soy Goku",
    "user_text": "¿Me enseñas algunas técnicas?"
}

while True:
    r = requests.post(url, json=payload)
    data = r.json()
    print("Bot:", data.get("content", ""))

    user_input = input("Tú: ")
    if user_input.lower() in ["salir", "exit"]:
        break
    payload["user_text"] = user_input
    payload["assisApi"] = data.get("content", "")
