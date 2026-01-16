# session_state -> cookies do navegador -> (armazena) lista de mensagens
# chat_input -> usuário escreve
# chat_message -> mensagem no chat
# write -> mostra no front
from streamlit import chat_input, chat_message, write, session_state, set_page_config, title, subheader
from dotenv import load_dotenv

set_page_config(page_title='ChatBot Callebe', page_icon='😄')
title('Chatbot Callebe')

if not 'message_list' in session_state:
    session_state['message_list'] = []

message = chat_input('Type your ask:')
if message:
    message_dict = {
        'avatar': 'user',
        'name': 'user',
        'message': message
    }
    session_state['message_list'].append(message_dict)

    ai_message = ...
    ai_dict = {
        'avatar': 'ai',
        'name': 'ai',
        'message': ai_message
    }
    session_state['message_list'].append(ai_dict)

    for mss in session_state['message_list']:
        chat_message(avatar=mss['avatar'], name=mss['name'], width='content').write(mss['message'])