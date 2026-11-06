import streamlit as st


st.set_page_config(
    page_title="나의 이야기",
    page_icon=":rainbow:",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# 이 사전의 내용만 바꾸면 자기소개 페이지를 빠르게 수정할 수 있습니다.
PROFILE = {
    "name": "곽주은",
    "role": "배우고 만들며 성장하는 사람",
    "organization": "청주교육대학교",
    "dream": "아이들이 자신의 꿈을 마음껏 펼칠 수 있도록 격려해주는 초등교사가 되고 싶습니다.",
    "intro": (
        "안녕하세요! 새로운 것을 배우고, 직접 시도하고, 경험을 나누는 일을 좋아합니다. "
        "이 페이지는 저를 소개하는 작은 온라인 공간입니다."
    ),
    "email": "hello@example.com",
    "github": "github.com/your-id",
    "instagram": "@your_id",
}





st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&family=Space+Grotesk:wght@500;600;700&display=swap');
    :root { --ink:#17202a; --paper:#fffaf2; --pink:#ff4f81; --yellow:#ffd166; --blue:#4cc9f0; --green:#80ed99; --purple:#8338ec; }
    .stApp { background: var(--paper); color: var(--ink); font-family: 'DM Sans', sans-serif; }
    [data-testid='stHeader'] { background: rgba(255,250,242,.85); }
    .block-container { max-width: 1180px; padding-top: 2rem; padding-bottom: 4rem; }
    h1, h2, h3 { font-family: 'Space Grotesk', sans-serif !important; color: var(--ink); }
    h1 { font-size: clamp(3.2rem, 8vw, 7.5rem) !important; line-height: .9 !important; letter-spacing: 0 !important; }
    h2 { font-size: 2.4rem !important; margin-top: 2rem !important; }
    .hero { padding: 3rem 3.2rem 3.5rem; border: 3px solid var(--ink); border-radius: 26px; background: linear-gradient(120deg, #ff4f81 0 25%, #ffd166 25% 48%, #4cc9f0 48% 72%, #80ed99 72%); box-shadow: 12px 12px 0 var(--ink); position: relative; overflow: hidden; }
    .hero:after { content:'✦'; position:absolute; right:6%; top:8%; font-size:7rem; color:#fff; transform:rotate(15deg); }
    .hero-kicker { font-family:'Space Grotesk'; font-weight:700; font-size:1.05rem; letter-spacing:.12em; text-transform:uppercase; background:#fff; display:inline-block; padding:.45rem .8rem; border:2px solid var(--ink); border-radius:999px; }
    .hero-name { max-width: 760px; margin: 1.4rem 0 1rem; }
    .hero-role { font-size:1.25rem; font-weight:700; max-width:650px; }
    .pill { display:inline-block; padding:.42rem .8rem; margin:.25rem .25rem 0 0; border:2px solid var(--ink); border-radius:999px; font-weight:700; background:#fff; }
    .section-label { font-family:'Space Grotesk'; font-size:.9rem; font-weight:700; color:var(--purple); letter-spacing:.12em; text-transform:uppercase; }
    .story { padding:2rem; border:3px solid var(--ink); border-radius:20px; background:#fff; box-shadow:7px 7px 0 var(--blue); min-height:215px; }
    .dream { padding:2.2rem; border:3px solid var(--ink); border-radius:20px; background:var(--purple); color:#fff; box-shadow:7px 7px 0 var(--yellow); }
    .dream h3 { color:#fff !important; font-size:1.7rem !important; }
    .lesson { padding:1.5rem; border:3px solid var(--ink); border-radius:18px; background:#fff; min-height:210px; }
    .lesson-icon { font-size:2.5rem; }
    .travel { padding:1.4rem; border:3px solid var(--ink); border-radius:18px; min-height:180px; background:var(--yellow); }
    .travel:nth-child(2) { background:var(--blue); } .travel:nth-child(3) { background:var(--green); } .travel:nth-child(4) { background:#ff8fab; }
    .travel-place { font-family:'Space Grotesk'; font-size:1.6rem; font-weight:700; }
    .travel-emoji { font-size:2.5rem; float:right; }
    .contact { padding:1.5rem; border:3px solid var(--ink); border-radius:18px; background:#fff; }
    .footer { margin-top:3rem; padding:1rem 0; border-top:3px solid var(--ink); font-weight:700; }
    </style>
    """,
    unsafe_allow_html=True,
)


with st.sidebar:
    st.markdown("## 페이지 메뉴")
    st.caption("프로필 내용은 streamlit_app.py 위쪽의 PROFILE에서 수정하세요.")
    st.markdown("[내 이메일](mailto:%s)" % PROFILE["email"])


st.markdown('<div class="hero">', unsafe_allow_html=True)
st.markdown('<span class="hero-kicker">PERSONAL PORTFOLIO / 2026</span>', unsafe_allow_html=True)
st.markdown(f'<h1 class="hero-name">{PROFILE["name"]}</h1>', unsafe_allow_html=True)
st.markdown(f'<p class="hero-role">{PROFILE["role"]} · {PROFILE["organization"]}</p>', unsafe_allow_html=True)
st.markdown(
    '<span class="pill">CURIOUS</span><span class="pill">CREATIVE</span><span class="pill">ALWAYS LEARNING</span>',
    unsafe_allow_html=True,
)
st.markdown('</div>', unsafe_allow_html=True)


st.write("")
about, dream = st.columns([1.2, 1], gap="large")
with about:
    st.markdown('<p class="section-label">01 / ABOUT ME</p>', unsafe_allow_html=True)
    st.markdown('<div class="story">', unsafe_allow_html=True)
    st.subheader("저를 소개합니다")
    st.write(PROFILE["intro"])
    st.markdown('</div>', unsafe_allow_html=True)
with dream:
    st.markdown('<p class="section-label">02 / MY DREAM</p>', unsafe_allow_html=True)
    st.markdown('<div class="dream">', unsafe_allow_html=True)
    st.markdown("### ✨ 내가 그리고 있는 미래")
    st.write(PROFILE["dream"])
    st.markdown('</div>', unsafe_allow_html=True)


st.markdown('<p class="section-label">03 / WHAT I LEARNED</p>', unsafe_allow_html=True)
st.header("배운 수업들")
lesson_columns = st.columns(4, gap="medium")
for column, lesson in zip(lesson_columns, LESSONS):
    with column:
        st.markdown('<div class="lesson">', unsafe_allow_html=True)
        st.markdown(f'<div class="lesson-icon">{lesson["icon"]}</div>', unsafe_allow_html=True)
        st.markdown(f'### {lesson["title"]}')
        st.write(lesson["text"])
        st.markdown('</div>', unsafe_allow_html=True)


st.markdown('<p class="section-label">04 / PLACES I HAVE BEEN</p>', unsafe_allow_html=True)
st.header("여행의 장면들")
travel_columns = st.columns(4, gap="medium")
for column, travel in zip(travel_columns, TRAVELS):
    with column:
        st.markdown('<div class="travel">', unsafe_allow_html=True)
        st.markdown(f'<span class="travel-emoji">{travel["emoji"]}</span>', unsafe_allow_html=True)
        st.markdown(f'<div class="travel-place">{travel["place"]}</div>', unsafe_allow_html=True)
        st.caption(travel["country"])
        st.write(travel["note"])
        st.markdown('</div>', unsafe_allow_html=True)


st.markdown('<p class="section-label">05 / KEEP IN TOUCH</p>', unsafe_allow_html=True)
st.header("이야기를 나누고 싶다면")
contact_left, contact_right = st.columns([1, 1], gap="large")
with contact_left:
    st.markdown('<div class="contact">', unsafe_allow_html=True)
    st.write(f"📮 {PROFILE['email']}")
    st.write(f"💻 {PROFILE['github']}")
    st.write(f"📸 {PROFILE['instagram']}")
    st.markdown('</div>', unsafe_allow_html=True)
with contact_right:
    message = st.text_input("방문자 메시지", placeholder="응원의 한마디를 남겨 주세요")
    if st.button("메시지 보내기", type="primary", use_container_width=True):
        if message.strip():
            st.success("메시지를 확인했어요. 고맙습니다!")
        else:
            st.warning("먼저 메시지를 입력해 주세요.")


st.markdown('<div class="footer">Made with curiosity, color, and Streamlit ✦</div>', unsafe_allow_html=True)
