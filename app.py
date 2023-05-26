import streamlit as st
import openai

openai.api_key = st.secrets["api_key"]
st.title("ChatGPT Plus DALL-E")
user_input = st.text_input("Prompt")

with(st.form("form")):
    st.write(user_input)
    submit = st.form_submit_button("Submit")

if submit and user_input:
    prompt = [{
        "role": "system",
        "content": "Imagine the detail appearance of the input. Response in shortly"
    }, {
        "role": "user",
        "content": user_input
    }]

    with(st.spinner("waiting...")):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=prompt
        )

    gpt_response = response["choices"][0]["message"]["content"]
    st.write(gpt_response)

    with(st.spinner("waiting...")):
        dalle_response = openai.Image.create(
            prompt=gpt_response,
            size="1024x1024"
        )

    st.image(dalle_response["data"][0]["url"])
