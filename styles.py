import streamlit as st

_LIQUID_GLASS_CSS = """
<style>
.stApp {
    background:
        radial-gradient(circle at 15% 20%, rgba(255, 138, 156, 0.55) 0%, transparent 45%),
        radial-gradient(circle at 85% 15%, rgba(255, 99, 132, 0.45) 0%, transparent 50%),
        radial-gradient(circle at 70% 85%, rgba(230, 57, 70, 0.40) 0%, transparent 55%),
        linear-gradient(135deg, #fff5f5 0%, #ffe0e6 50%, #ffd6e0 100%);
    background-attachment: fixed;
}

[data-testid="stHeader"] {
    background: rgba(255, 255, 255, 0.25);
    backdrop-filter: blur(24px) saturate(180%);
    -webkit-backdrop-filter: blur(24px) saturate(180%);
    border-bottom: 1px solid rgba(255, 255, 255, 0.35);
}

[data-testid="stSidebar"] > div:first-child {
    background: rgba(255, 255, 255, 0.45);
    backdrop-filter: blur(28px) saturate(200%);
    -webkit-backdrop-filter: blur(28px) saturate(200%);
    border-right: 1px solid rgba(255, 255, 255, 0.45);
    box-shadow: 0 8px 32px rgba(230, 57, 70, 0.08);
}

[data-testid="stChatMessage"] {
    background: rgba(255, 255, 255, 0.55) !important;
    backdrop-filter: blur(20px) saturate(180%);
    -webkit-backdrop-filter: blur(20px) saturate(180%);
    border: 1px solid rgba(255, 255, 255, 0.5);
    border-radius: 20px;
    box-shadow: 0 8px 32px rgba(230, 57, 70, 0.10);
    padding: 16px 20px;
    margin-bottom: 12px;
}

[data-testid="stChatInput"] {
    background: rgba(255, 255, 255, 0.55);
    backdrop-filter: blur(24px) saturate(180%);
    -webkit-backdrop-filter: blur(24px) saturate(180%);
    border-radius: 18px;
    border: 1px solid rgba(255, 255, 255, 0.5);
    box-shadow: 0 4px 24px rgba(230, 57, 70, 0.10);
}

[data-testid="stChatInput"] textarea {
    background: transparent !important;
}

[data-testid="stTextInput"] input,
[data-testid="stTextArea"] textarea,
[data-testid="stFileUploaderDropzone"] {
    background: rgba(255, 255, 255, 0.55) !important;
    backdrop-filter: blur(16px) saturate(180%);
    -webkit-backdrop-filter: blur(16px) saturate(180%);
    border: 1px solid rgba(255, 255, 255, 0.5) !important;
    border-radius: 14px !important;
}

[data-testid="stFileUploaderDropzone"] {
    box-shadow: 0 4px 18px rgba(230, 57, 70, 0.08);
}

.stButton > button,
.stDownloadButton > button,
.stFormSubmitButton > button {
    background: rgba(230, 57, 70, 0.85) !important;
    color: white !important;
    border: 1px solid rgba(255, 255, 255, 0.4) !important;
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    border-radius: 12px !important;
    box-shadow: 0 4px 16px rgba(230, 57, 70, 0.25);
    transition: all 0.2s ease;
}

.stButton > button:hover,
.stDownloadButton > button:hover,
.stFormSubmitButton > button:hover {
    transform: translateY(-1px);
    box-shadow: 0 6px 22px rgba(230, 57, 70, 0.35);
}

[data-testid="stAlert"] {
    background: rgba(255, 255, 255, 0.55) !important;
    backdrop-filter: blur(16px) saturate(180%);
    -webkit-backdrop-filter: blur(16px) saturate(180%);
    border: 1px solid rgba(255, 255, 255, 0.5) !important;
    border-radius: 16px !important;
    box-shadow: 0 4px 20px rgba(230, 57, 70, 0.08);
}

h1, h2, h3 {
    letter-spacing: -0.02em;
}

@keyframes bird-float {
    0%, 100% { transform: translateY(0); }
    50% { transform: translateY(-6px); }
}

@keyframes bird-flap {
    0%, 100% { transform: scaleY(1) translateY(0); }
    50% { transform: scaleY(0.45) translateY(-2px); }
}

@keyframes dots-pulse {
    0%, 80%, 100% { opacity: 0.25; }
    40% { opacity: 1; }
}

.loading-bird-wrap {
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 4px 0;
}

.loading-bird-svg {
    width: 56px;
    height: 56px;
    animation: bird-float 1.1s ease-in-out infinite;
    filter: drop-shadow(0 4px 10px rgba(255, 105, 180, 0.35));
}

.loading-bird-svg .wing {
    transform-origin: 38px 48px;
    animation: bird-flap 0.42s ease-in-out infinite;
}

.loading-bird-text {
    color: #C2185B;
    font-weight: 500;
    letter-spacing: 0.01em;
}

.loading-bird-dots span {
    display: inline-block;
    animation: dots-pulse 1.2s infinite ease-in-out;
}
.loading-bird-dots span:nth-child(2) { animation-delay: 0.2s; }
.loading-bird-dots span:nth-child(3) { animation-delay: 0.4s; }
</style>
"""


_LOADING_BIRD_HTML = """
<div class="loading-bird-wrap">
  <svg class="loading-bird-svg" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
    <ellipse cx="50" cy="60" rx="26" ry="20" fill="#FF8FAB"/>
    <circle cx="70" cy="42" r="15" fill="#FFB3C6"/>
    <path class="wing" d="M28 52 Q42 36 54 52 Q42 62 28 60 Z" fill="#FF6B9D"/>
    <polygon points="83,42 92,44 83,47" fill="#FFB347"/>
    <circle cx="73" cy="40" r="2.4" fill="#1a1a1a"/>
    <circle cx="73.6" cy="39.4" r="0.8" fill="#fff"/>
    <path d="M40 78 Q46 84 52 78" stroke="#FF6B9D" stroke-width="2.5" fill="none" stroke-linecap="round"/>
    <path d="M58 78 Q64 84 70 78" stroke="#FF6B9D" stroke-width="2.5" fill="none" stroke-linecap="round"/>
  </svg>
  <span class="loading-bird-text">Pensando<span class="loading-bird-dots"><span>.</span><span>.</span><span>.</span></span></span>
</div>
"""


CONVERSATION_STARTERS = [
    ("✍️ Resumir", "Resumime en 5 viñetas las ideas principales del libro 'Atomic Habits' de James Clear."),
    ("🌐 Traducir", "Traducí al inglés: 'Espero que tengas un excelente día y mucha suerte con tu proyecto.'"),
    ("💡 Ideas", "Dame 3 ideas de proyectos pequeños para aprender Python usando APIs públicas."),
]


CAPABILITIES = [
    "📝 Resumir textos largos",
    "🌐 Traducir entre idiomas",
    "💻 Explicar y depurar código",
    "💡 Generar ideas y brainstorm",
    "❓ Responder preguntas generales",
]


TONE_OPTIONS = ["Formal", "Neutral", "Casual"]


def apply_liquid_glass() -> None:
    st.markdown(_LIQUID_GLASS_CSS, unsafe_allow_html=True)


def loading_bird_html() -> str:
    return _LOADING_BIRD_HTML


def system_prompt(tone: str, refine_mode: str | None = None) -> str:
    base = f"Use a {tone.lower()} tone. Match the user's language."
    if refine_mode == "shorter":
        base += " Provide a noticeably more concise version of your previous response — same substance, fewer words."
    return base
