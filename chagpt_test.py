import requests
import json

# ChatGPT APIキー
chatgpt_api_key = "YOUR_CHAGPT_API_KEY"

# Voicevox APIキー
voicevox_api_key = "YOUR_VOICEVOX_API_KEY"

# ChatGPT APIエンドポイント
chatgpt_url = "https://api.openai.com/v1/chat/completions"

# Voicevox APIエンドポイント
voicevox_url = "https://api.ceco.asia/v1/tts"

def generate_voice(text):
    # ChatGPT APIを呼び出す
    response = requests.post(chatgpt_url,
                             headers={"Content-Type": "application/json",
                                      "Authorization": f"Bearer {chatgpt_api_key}"},
                             json={"model": "gpt-3.5-turbo",
                                   "messages":[{"role": "user",  "content": text}]})


    output_text = response.json()["choices"][0]["message"]["content"]
#    output_text = response.json()

    return output_text

test = generate_voice("what is your name?")

print(test)