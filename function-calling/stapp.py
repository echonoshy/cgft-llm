import os
from dotenv import load_dotenv

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import json
import openai

import streamlit as st

GPT_MODEL = "gpt-4o-mini"

load_dotenv()
# 获取环境变量
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
AUTHORIZATION_CODE = os.getenv("AUTHORIZATION_CODE")

client = openai.OpenAI(api_key=OPENAI_API_KEY)

tools = [
    {
        "type": "function",
        "function": {
            "name": "send_email",
            "description": "Send an email to the specified email with the subject and content",
            "parameters": {
                "type": "object",
                "properties": {
                    "FromEmail": {
                        "type": "string",
                        "description": "The email address, eg., remember0101@126.com",
                    },
                    "Subject": {
                        "type": "string",
                        "description": "Subject of the email",
                    },
                    "Body": {
                        "type": "string",
                        "description": "The content of the email",
                    },
                    "Recipients": {
                        "type": "string",
                        "description": "The recipients' email addresses",
                    }
                },
                "required": ["FromEmail", "Subject", "Body", "Recipients"],
            },
        }
    }
]

st.sidebar.header("📃 Dialgue Session:")

def chat_completion_request(messages, tools=None, tool_choice=None, model=GPT_MODEL):
    try:
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            tools=tools,
            tool_choice=tool_choice,
        )
        return response
    except Exception as e:
        print("Unable to generate ChatCompletion response")
        print(f"Exception: {e}")
        return e

def send_email(sender_email, sender_authorization_code, recipient_email, subject, body):
    # 创建 MIMEMultipart 对象
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = recipient_email
    message["Subject"] = subject

    message.attach(MIMEText(body, "plain"))

    # 创建 SMTP_SSL 会话
    with smtplib.SMTP_SSL("smtp.126.com", 465) as server:
        server.login(sender_email, sender_authorization_code)
        text = message.as_string()
        server.sendmail(sender_email, recipient_email, text)

def main():
    st.title("📥 Mail Assistant")

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # React to user input
    if prompt := st.chat_input("What is your message?"):
        # Display user message in chat message container
        st.chat_message("user").markdown(prompt)
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})

        response = chat_completion_request(
            messages=st.session_state.messages,
            tools=tools
        )
        st.sidebar.json(st.session_state)
        st.sidebar.write(response)
        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            if content := response.choices[0].message.content:
                st.markdown(content)
                st.session_state.messages.append({"role": "assistant", "content": content})
            else:
                fn_name = response.choices[0].message.tool_calls[0].function.name
                fn_args = response.choices[0].message.tool_calls[0].function.arguments

                def confirm_send_fn():
                    send_email(
                                sender_email=args["FromEmail"],
                                sender_authorization_code=AUTHORIZATION_CODE,
                                recipient_email=args["Recipients"],
                                subject=args["Subject"],
                                body=args["Body"],
                            )
                    st.success("邮件已发送")
                    st.session_state.messages.append({"role": "assistant", "content": "邮件已发送，还需要什么帮助吗？"})
                    # reflash sidebar
                    st.sidebar.json(st.session_state)
                    st.sidebar.write(response)
                    
                
                def cancel_send_fn():    
                    st.warning("邮件发送已取消")
                    st.session_state.messages.append({"role": "assistant", "content": "邮件已取消，还需要什么帮助吗？"})
                    # reflash sidebar
                    st.sidebar.json(st.session_state)
                    st.sidebar.write(response)
                    
                if fn_name == "send_email":
                    args = json.loads(fn_args)
                    st.markdown("邮件内容如下：")
                    st.markdown(f"发件人: {args['FromEmail']}")
                    st.markdown(f"收件人: {args['Recipients']}")
                    st.markdown(f"主题: {args['Subject']}")
                    st.markdown(f"内容: {args['Body']}")

                    col1, col2 = st.columns(2)
                    with col1:
                        st.button(
                            label="✅确认发送邮件", 
                            on_click=confirm_send_fn)
                    with col2:
                        st.button(
                            label="❌取消发送邮件",
                            on_click=cancel_send_fn
                        )

if __name__ == "__main__":
    main()
