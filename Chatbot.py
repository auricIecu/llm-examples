from openai import OpenAI
import streamlit as st
from styles import (
    apply_liquid_glass,
    loading_bird_html,
    CONVERSATION_STARTERS,
    CAPABILITIES,
    TONE_OPTIONS,
    system_prompt,
)

apply_liquid_glass()

with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
    "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
    "[View the source code](https://github.com/streamlit/llm-examples/blob/main/Chatbot.py)"

    st.divider()
    st.markdown("### ¿Qué puedo hacer?")
    for cap in CAPABILITIES:
        st.markdown(f"- {cap}")

    st.divider()
    tone = st.select_slider(
        "🎚️ Tono de respuesta",
        options=TONE_OPTIONS,
        value="Neutral",
    )

st.title("💬 Chatbot Bacán")
st.caption("🚀 A Streamlit chatbot powered by OpenAI")

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "¡Hola! ¿En qué te ayudo hoy?"}]


def _render_refinement_buttons(text: str, key_prefix: str) -> None:
    c1, c2, c3 = st.columns([1.4, 1.4, 1.2])
    if c1.button("↻ Regenerar", key=f"{key_prefix}_regen", use_container_width=True):
        st.session_state.pending_action = {"type": "regenerate"}
        st.rerun()
    if c2.button("✂️ Más corto", key=f"{key_prefix}_short", use_container_width=True):
        st.session_state.pending_action = {"type": "refine", "mode": "shorter"}
        st.rerun()
    with c3.popover("📋 Copiar", use_container_width=True):
        st.code(text, language=None)


def _call_openai(api_key: str, history: list, tone: str, refine: str | None) -> str:
    client = OpenAI(api_key=api_key)
    request_messages = [{"role": "system", "content": system_prompt(tone, refine)}] + history
    response = client.chat.completions.create(model="gpt-3.5-turbo", messages=request_messages)
    return response.choices[0].message.content


def _generate_assistant(api_key: str, tone: str, refine: str | None) -> None:
    if not api_key:
        with st.chat_message("assistant"):
            st.warning("Para chatear de verdad necesito una OpenAI API key — agregala en la barra lateral.")
            st.markdown("Mientras tanto, así se vería una respuesta de ejemplo:")
            st.info(
                "💡 **Ejemplo de respuesta:**\n\n"
                "¡Claro! Acá van 3 ideas:\n\n"
                "1. Un script que use la API de OpenWeather para mostrarte el clima de tus ciudades favoritas.\n"
                "2. Un bot de Telegram que te recuerde tomar agua cada 2 horas.\n"
                "3. Un dashboard en Streamlit que grafique los precios de criptomonedas en tiempo real."
            )
            st.markdown("👉 [Conseguí tu API key acá](https://platform.openai.com/account/api-keys)")
        return
    with st.chat_message("assistant"):
        placeholder = st.empty()
        placeholder.markdown(loading_bird_html(), unsafe_allow_html=True)
        response_text = _call_openai(api_key, st.session_state.messages, tone, refine)
        placeholder.write(response_text)
        _render_refinement_buttons(response_text, f"new_{len(st.session_state.messages)}")
    st.session_state.messages.append({"role": "assistant", "content": response_text})


action = st.session_state.pop("pending_action", None)
needs_assistant = False
refine_mode = None

if action:
    kind = action["type"]
    if kind == "user_prompt":
        st.session_state.messages.append({"role": "user", "content": action["prompt"]})
        needs_assistant = True
    elif kind == "regenerate":
        if st.session_state.messages and st.session_state.messages[-1]["role"] == "assistant":
            st.session_state.messages.pop()
        needs_assistant = True
    elif kind == "refine":
        if st.session_state.messages and st.session_state.messages[-1]["role"] == "assistant":
            st.session_state.messages.pop()
        needs_assistant = True
        refine_mode = action["mode"]

for i, msg in enumerate(st.session_state.messages):
    is_last = i == len(st.session_state.messages) - 1
    with st.chat_message(msg["role"]):
        st.write(msg["content"])
        if msg["role"] == "assistant" and is_last and i > 0 and not needs_assistant:
            _render_refinement_buttons(msg["content"], f"hist_{i}")

if len(st.session_state.messages) == 1 and not needs_assistant:
    st.markdown("**💫 Probá con uno de estos:**")
    cols = st.columns(len(CONVERSATION_STARTERS))
    for col, (label, prompt_text) in zip(cols, CONVERSATION_STARTERS):
        if col.button(label, key=f"starter_{label}", use_container_width=True):
            st.session_state.pending_action = {"type": "user_prompt", "prompt": prompt_text}
            st.rerun()

if needs_assistant:
    _generate_assistant(openai_api_key, tone, refine_mode)

if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)
    _generate_assistant(openai_api_key, tone, None)
