from streamlit import chat_input, chat_message, session_state, set_page_config, title
from dotenv import load_dotenv
from huggingface_hub import InferenceClient
from os import getenv

set_page_config(page_title='ChatBot Callebe', page_icon='😁')
title('Chatbot Callebe 😁')

load_dotenv()
hf_token = getenv('HF_TOKEN')
client = InferenceClient(
    model='meta-llama/Llama-3.2-3B-Instruct',
    token=hf_token
)

if not 'message_list' in session_state:
    session_state['message_list'] = []

for mss in session_state['message_list']:
    chat_message(avatar=mss['avatar'], name=mss['name'], width='content').write(mss['content'])

message = chat_input('Type your ask:')
if message:
    chat_message(name='user', avatar='user', width='content').write(message)
    user_message_dict = {
        'avatar': 'user',
        'name': 'user',
        'content': message
    }

    session_state['message_list'].append(user_message_dict)
    
    api_messages = [
        {
            'role': 'user' if m['avatar'] == 'user' else 'assistant', 'content': m['content']
        }
        for m in session_state['message_list']
    ]

    stream = client.chat_completion(
        messages=session_state['message_list'],
        max_tokens=500,
        stream=True
    )

    ai_response = ''

    for chunk in stream:
        token = chunk.choices[0].delta.content
        if token:
            ai_response += token

    ai_dict = {
        'avatar': 'ai',
        'name': 'ai',
        'content': ai_response
    }

    chat_message(name='ai', avatar='ai', width='content').write(ai_response)
    session_state['message_list'].append(ai_dict)