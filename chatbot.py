import openai
import gradio

openai.api_key = "******PUT API KEY HERE*******"

messages = [{"role": "system", "content": "You're a music recommender that also returns a song suggestion with every response. All suggestions are based on the prompts you recieve."}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "Music Mate")

demo.launch(share=True)