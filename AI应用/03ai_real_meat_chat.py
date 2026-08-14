import streamlit as st
import os
import json
from datetime import datetime
from openai import OpenAI


# =========================
# 1. 页面配置
# =========================

st.set_page_config(
    page_title="AI智能伴侣",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={}
)

st.title("AI智能伴侣")


# =========================
# 2. DeepSeek 客户端
# =========================

client = OpenAI(
    api_key=os.environ.get("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)


# =========================
# 3. 会话文件
# =========================

SESSION_FILE = "chat_sessions.json"


# =========================
# 4. 读取历史会话
# =========================

def load_sessions():

    if not os.path.exists(SESSION_FILE):
        return {}

    try:
        with open(SESSION_FILE, "r", encoding="utf-8") as f:
            return json.load(f)

    except Exception:
        return {}


# =========================
# 5. 保存所有会话
# =========================

def save_sessions():

    with open(SESSION_FILE, "w", encoding="utf-8") as f:
        json.dump(
            st.session_state.sessions,
            f,
            ensure_ascii=False,
            indent=4
        )


# =========================
# 6. 创建新的会话 ID
# =========================

def create_session_id():

    return datetime.now().strftime("%Y%m%d_%H%M%S")


# =========================
# 7. 初始化 Session State
# =========================

if "sessions" not in st.session_state:
    st.session_state.sessions = load_sessions()


if "current_session" not in st.session_state:

    # 如果完全没有历史会话
    if not st.session_state.sessions:

        session_id = create_session_id()

        st.session_state.sessions[session_id] = {
            "messages": [],
            "name": "小甜甜",
            "personality": "温柔可爱",
        }

        st.session_state.current_session = session_id

        save_sessions()

    else:

        # 默认打开最近一个会话
        st.session_state.current_session = list(
            st.session_state.sessions.keys()
        )[-1]


# =========================
# 8. 获取当前会话
# =========================

current_session = st.session_state.current_session

session = st.session_state.sessions[current_session]


# =========================
# 9. 侧边栏
# =========================

with st.sidebar:

    st.header("AI控制面板")


    # -------------------------
    # 新建会话
    # -------------------------

    if st.button(
        "📝 新建会话",
        use_container_width=True
    ):

        session_id = create_session_id()

        # 防止同一秒创建两个相同 ID
        while session_id in st.session_state.sessions:
            session_id = create_session_id()

        st.session_state.sessions[session_id] = {
            "messages": [],
            "name": "小甜甜",
            "personality": "温柔可爱",
        }

        st.session_state.current_session = session_id

        save_sessions()

        st.rerun()


    st.subheader("历史会话")


    # -------------------------
    # 显示历史会话
    # -------------------------

    session_ids = list(
        st.session_state.sessions.keys()
    )


    for session_id in session_ids:

        col1, col2 = st.columns([4, 1])


        with col1:

            # 当前会话
            if session_id == st.session_state.current_session:

                if st.button(
                    f"📄 {session_id}",
                    key=f"open_{session_id}",
                    use_container_width=True
                ):
                    pass

            else:

                if st.button(
                    f"📄 {session_id}",
                    key=f"open_{session_id}",
                    use_container_width=True
                ):

                    st.session_state.current_session = session_id

                    save_sessions()

                    st.rerun()


        with col2:

            if st.button(
                "❌",
                key=f"delete_{session_id}"
            ):

                del st.session_state.sessions[session_id]


                # 如果删除的是当前会话
                if session_id == st.session_state.current_session:

                    # 还有其他会话
                    if st.session_state.sessions:

                        st.session_state.current_session = list(
                            st.session_state.sessions.keys()
                        )[-1]

                    # 一个会话都没有了
                    else:

                        new_id = create_session_id()

                        st.session_state.sessions[new_id] = {
                            "messages": [],
                            "name": "小甜甜",
                            "personality": "温柔可爱",
                        }

                        st.session_state.current_session = new_id


                save_sessions()

                st.rerun()


    st.divider()


    # =========================
    # AI 信息设置
    # =========================

    st.subheader("AI设置")


    ai_name = st.text_input(
        "名字",
        value=session.get("name", "小甜甜")
    )


    personality = st.text_area(
        "性格",
        value=session.get(
            "personality",
            "温柔可爱"
        )
    )


    # 更新 AI 设置
    session["name"] = ai_name
    session["personality"] = personality

    save_sessions()


# =========================
# 10. 当前会话标题
# =========================

st.caption(
    f"当前会话：{current_session}"
)


# =========================
# 11. 系统提示词
# =========================

system_prompt = f"""
你是一个AI智能伴侣。

你的名字是：{session["name"]}

你的性格是：
{session["personality"]}

请根据你的性格自然地与用户交流。
"""


# =========================
# 12. 显示历史消息
# =========================

for message in session["messages"]:

    if message["role"] == "user":

        with st.chat_message("user"):
            st.write(message["content"])

    else:

        with st.chat_message(
            "assistant",
            avatar="🤖"
        ):
            st.write(message["content"])


# =========================
# 13. 用户输入
# =========================

prompt = st.chat_input(
    "请输入您的问题"
)


if prompt:

    # -------------------------
    # 显示用户消息
    # -------------------------

    with st.chat_message("user"):

        st.write(prompt)


    # -------------------------
    # 保存用户消息
    # -------------------------

    session["messages"].append({
        "role": "user",
        "content": prompt
    })


    save_sessions()


    # =========================
    # 14. 调用 DeepSeek
    # =========================

    response = client.chat.completions.create(

        model="deepseek-v4-pro",

        messages=[
            {
                "role": "system",
                "content": system_prompt
            }
        ] + session["messages"],

        stream=True
    )


    # =========================
    # 15. 流式输出
    # =========================

    def generate_response():

        for chunk in response:

            if not chunk.choices:
                continue

            content = chunk.choices[0].delta.content

            if content:
                yield content


    with st.chat_message(
        "assistant",
        avatar="🤖"
    ):

        answer = st.write_stream(
            generate_response()
        )


    # =========================
    # 16. 保存 AI 回复
    # =========================

    session["messages"].append({
        "role": "assistant",
        "content": answer
    })


    save_sessions()