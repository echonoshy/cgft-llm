import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from openai import OpenAI
import json

# Streamlit 页面配置
st.set_page_config(page_title="GPT Mail", page_icon="✉️")

# 侧边栏设置
st.sidebar.header('Required API Keys')
OPENAI_API_KEY = st.sidebar.text_input("Enter OpenAI's API key", '', type='password')
Authorization_Code = st.sidebar.text_input("Enter 126 Mail's Authorization code", type="password")


# OPENAI_API_KEY = st.secrets['OPENAI_API_KEY']
# Authorization_Code = st.secrets["Authorization_Code"]

client = OpenAI(api_key=OPENAI_API_KEY)

# 主页面标题
st.title("GPT Mail")
st.markdown("Chat with AI to send emails!")

# GPT模型和工具设置
GPT_MODEL = "gpt-4o-mini"

tools = [
    {
        "type": "function",
        "function": {
            "name": "send_email",
            "description": "Send an email to the specified email with the subject and content",
            "parameters":{
                "type": "object",
                "properties": {
                    "FromEmail": {
                        "type": "string",
                        "description": "The email address, eg., rememeber0101@126.com",
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
        st.error(f"Unable to generate ChatCompletion response: {e}")
        return None

def send_email(sender_email, sender_authorization_code, recipient_email, subject, body):
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = recipient_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))
    
    try:
        with smtplib.SMTP_SSL("smtp.126.com", 465) as server:
            server.login(sender_email, sender_authorization_code)
            text = message.as_string()
            server.sendmail(sender_email, recipient_email, text)
        return True
    except Exception as e:
        st.error(f"Error sending email: {e}")
        return False

# 初始化会话状态
if "messages" not in st.session_state:
    st.session_state.messages = []

# 显示聊天历史
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 聊天输入
if prompt := st.chat_input("What's your message?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # 获取AI响应
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        response = chat_completion_request(
            messages=st.session_state.messages,
            tools=tools
        )
        
        if response:
            if content := response.choices[0].message.content:
                full_response = content
            else:
                fn_call = response.choices[0].message.tool_calls[0].function
                fn_name = fn_call.name
                fn_args = json.loads(fn_call.arguments)
                
                if fn_name == "send_email":
                    if send_email(
                        sender_email=fn_args["FromEmail"],
                        sender_authorization_code=Authorization_Code, 
                        recipient_email=fn_args["Recipients"], 
                        subject=fn_args["Subject"], 
                        body=fn_args["Body"],
                    ):
                        full_response = "Email sent successfully!"
                    else:
                        full_response = "Failed to send email. Please check your settings and try again."
                else:
                    full_response = f"Unknown function call: {fn_name}"
            
            message_placeholder.markdown(full_response)
            st.session_state.messages.append({"role": "assistant", "content": full_response})

# 添加清除聊天历史的按钮
if st.button("Clear Chat History"):
    st.session_state.messages = []
    st.experimental_rerun()