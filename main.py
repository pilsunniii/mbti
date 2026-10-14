
import streamlit as st

st.set_page_config(
    page_title="MBTI로 포켓몬 찾기",
    page_icon="🌼",
    layout="centered",
)

POKEMON = {
    "ISTJ": {
        "name": "꼬부기", "english": "Squirtle", "id": 7,
        "types": "물 타입",
        "traits": "성실함 · 침착함 · 믿음직함",
        "tagline": "차근차근 자기 길을 가는 든든한 친구",
        "reason": [
            "꼼꼼하고 책임감이 강해 맡은 일을 끝까지 해내는 모습이 닮았어요.",
            "차분하게 상황을 살피고 꾸준히 실력을 쌓는 믿음직한 단짝이에요."
        ],
        "match": "ESFP",
        "match_reason": "밝고 활기찬 ESFP가 즐거움을 더해 주고, ISTJ는 든든한 안정감을 나눠 줄 수 있어요."
    },
    "ISFJ": {
        "name": "해피너스", "english": "Blissey", "id": 242,
        "types": "노말 타입",
        "traits": "배려심 · 다정함 · 헌신",
        "tagline": "곁에 있는 것만으로 마음이 편안해지는 친구",
        "reason": [
            "주변 사람의 기분을 세심하게 살피고 조용히 도움을 건네요.",
            "소중한 사람을 지키려는 따뜻하고 성실한 마음이 닮았어요."
        ],
        "match": "ESFP",
        "match_reason": "ESFP의 밝은 에너지가 활기를 더하고, ISFJ는 편안히 쉴 수 있는 자리를 만들어 줘요."
    },
    "INFJ": {
        "name": "가디안", "english": "Gardevoir", "id": 282,
        "types": "에스퍼 · 페어리 타입",
        "traits": "공감력 · 직관 · 신념",
        "tagline": "소중한 사람을 진심으로 지켜 주는 수호자",
        "reason": [
            "조용하지만 깊은 생각과 자신만의 신념을 소중히 여겨요.",
            "상대의 마음을 이해하고 의미 있는 일을 하고 싶어 하는 점이 닮았어요."
        ],
        "match": "ENFP",
        "match_reason": "ENFP가 새로운 가능성과 활기를 더해 주고, INFJ는 깊이와 방향을 더해 줄 수 있어요."
    },
    "INTJ": {
        "name": "뮤츠", "english": "Mewtwo", "id": 150,
        "types": "에스퍼 타입",
        "traits": "전략적 · 독립적 · 분석적",
        "tagline": "큰 그림을 그리고 전략을 세우는 지략가",
        "reason": [
            "혼자 생각을 정리하고 목표를 향해 전략적으로 움직여요.",
            "복잡한 문제를 분석하고 더 나은 방법을 찾는 모습이 잘 어울려요."
        ],
        "match": "ENFP",
        "match_reason": "ENFP는 새로운 관점과 에너지를 더하고, INTJ는 아이디어를 계획으로 발전시켜요."
    },
    "ISTP": {
        "name": "메타몽", "english": "Ditto", "id": 132,
        "types": "노말 타입",
        "traits": "유연함 · 실용적 · 침착함",
        "tagline": "어떤 상황에서도 방법을 찾아내는 해결사",
        "reason": [
            "필요한 순간에 침착하게 문제를 살피고 직접 해결해요.",
            "틀에 얽매이기보다 상황에 맞춰 유연하게 움직이는 점이 닮았어요."
        ],
        "match": "ESTJ",
        "match_reason": "ESTJ의 계획성과 추진력이 ISTP의 실전 감각과 만나면 아이디어를 빠르게 실행할 수 있어요."
    },
    "ISFP": {
        "name": "이브이", "english": "Eevee", "id": 133,
        "types": "노말 타입",
        "traits": "감수성 · 자유로움 · 다정함",
        "tagline": "자기만의 색깔로 성장하는 감성파",
        "reason": [
            "자유롭고 섬세하며 자신이 좋아하는 것을 진심으로 아껴요.",
            "자기만의 방식으로 성장하는 모습과 부드러운 감성이 닮았어요."
        ],
        "match": "ESFJ",
        "match_reason": "ESFJ의 따뜻한 배려가 편안함을 주고, ISFP는 관계에 감성과 여유를 더해요."
    },
    "INFP": {
        "name": "이상해씨", "english": "Bulbasaur", "id": 1,
        "types": "풀 · 독 타입",
        "traits": "상상력 · 진정성 · 다정함",
        "tagline": "다정한 마음으로 천천히 성장하는 친구",
        "reason": [
            "상상력이 풍부하고 자신만의 가치와 감정을 소중히 여겨요.",
            "작은 가능성을 믿고 조용히 자신만의 꽃을 피우는 모습이 닮았어요."
        ],
        "match": "ENFJ",
        "match_reason": "ENFJ는 INFP의 꿈을 응원하고, INFP는 ENFJ에게 진솔한 마음과 새로운 시선을 전해 줘요."
    },
    "INTP": {
        "name": "폴리곤", "english": "Porygon", "id": 137,
        "types": "노말 타입",
        "traits": "호기심 · 논리적 · 독창적",
        "tagline": "호기심으로 세상을 탐구하는 생각 천재",
        "reason": [
            "궁금한 것이 생기면 원리를 파고들고 여러 가능성을 상상해요.",
            "독창적인 아이디어와 논리적인 탐구를 즐기는 점이 닮았어요."
        ],
        "match": "ENTJ",
        "match_reason": "ENTJ의 결단력은 INTP의 아이디어를 실행으로 옮기는 데 도움을 주고 서로의 사고를 자극해요."
    },
    "ESTP": {
        "name": "루카리오", "english": "Lucario", "id": 448,
        "types": "격투 · 강철 타입",
        "traits": "대담함 · 순발력 · 행동력",
        "tagline": "기회를 포착하고 바로 움직이는 행동파",
        "reason": [
            "생각만 하기보다 직접 부딪치며 경험에서 답을 찾아요.",
            "순발력과 대담함으로 예상치 못한 상황을 즐기는 모습이 닮았어요."
        ],
        "match": "ISFJ",
        "match_reason": "ISFJ의 세심함이 안정감을 더하고, ESTP는 새로운 경험에 도전하도록 북돋울 수 있어요."
    },
    "ESFP": {
        "name": "피카츄", "english": "Pikachu", "id": 25,
        "types": "전기 타입",
        "traits": "활발함 · 표현력 · 친화력",
        "tagline": "주변을 환하게 만드는 에너지 충전기",
        "reason": [
            "밝고 표현력이 풍부해 함께 있으면 분위기가 살아나요.",
            "지금 이 순간을 즐기고 사람들과 기쁨을 나누는 모습이 닮았어요."
        ],
        "match": "ISTJ",
        "match_reason": "ISTJ의 차분함이 든든한 중심이 되고, ESFP는 일상에 즐거운 변화를 더해요."
    },
    "ENFP": {
        "name": "파치리스", "english": "Pachirisu", "id": 417,
        "types": "전기 타입",
        "traits": "호기심 · 열정 · 상상력",
        "tagline": "반짝이는 아이디어가 넘치는 분위기 메이커",
        "reason": [
            "새로운 가능성을 발견하면 사람들과 나누고 싶어 해요.",
            "호기심과 따뜻한 열정으로 주변에 활기를 전하는 점이 닮았어요."
        ],
        "match": "INFJ",
        "match_reason": "INFJ의 깊은 통찰이 아이디어를 다듬어 주고, ENFP는 INFJ에게 신선한 영감을 전해요."
    },
    "ENTP": {
        "name": "팬텀", "english": "Gengar", "id": 94,
        "types": "고스트 · 독 타입",
        "traits": "재치 · 기발함 · 도전 정신",
        "tagline": "기발한 발상으로 판을 흔드는 친구",
        "reason": [
            "남들이 당연하게 여기는 것도 새롭게 바라보며 아이디어를 떠올려요.",
            "재치 있는 대화와 색다른 시도를 즐기는 점이 닮았어요."
        ],
        "match": "INTJ",
        "match_reason": "ENTP의 발상과 INTJ의 전략이 만나면 아이디어를 탄탄한 계획으로 키울 수 있어요."
    },
    "ESTJ": {
        "name": "잠만보", "english": "Snorlax", "id": 143,
        "types": "노말 타입",
        "traits": "책임감 · 현실적 · 든든함",
        "tagline": "든든하게 책임지고 일을 마무리하는 리더",
        "reason": [
            "목표를 정하고 필요한 일을 체계적으로 처리하는 편이에요.",
            "현실적인 판단과 책임감으로 주변에 믿음을 주는 점이 닮았어요."
        ],
        "match": "ISTP",
        "match_reason": "ISTP의 유연한 문제 해결 방식이 새로운 길을 더하고, ESTJ는 실행의 방향을 잡아 줘요."
    },
    "ESFJ": {
        "name": "푸린", "english": "Jigglypuff", "id": 39,
        "types": "노말 · 페어리 타입",
        "traits": "친절함 · 사교성 · 배려심",
        "tagline": "모두가 편안하게 어울리도록 돕는 친구",
        "reason": [
            "사람들이 편안하고 행복하게 지내는 것을 중요하게 생각해요.",
            "먼저 챙겨 주고 함께 어울리는 따뜻한 마음이 닮았어요."
        ],
        "match": "ISFP",
        "match_reason": "ISFP의 섬세한 감성과 ESFJ의 다정한 배려가 만나면 따뜻한 관계를 만들 수 있어요."
    },
    "ENFJ": {
        "name": "가디안", "english": "Gardevoir", "id": 282,
        "types": "에스퍼 · 페어리 타입",
        "traits": "공감력 · 응원 · 리더십",
        "tagline": "소중한 사람을 지켜 주는 따뜻한 응원단장",
        "reason": [
            "사람들의 장점을 발견하고 함께 성장하도록 응원해요.",
            "공감 능력과 긍정적인 영향력으로 주변을 이끄는 점이 닮았어요."
        ],
        "match": "INFP",
        "match_reason": "INFP의 진솔함과 상상력이 새로운 시선을 주고, ENFJ는 INFP가 꿈을 펼치도록 응원해요."
    },
    "ENTJ": {
        "name": "리자몽", "english": "Charizard", "id": 6,
        "types": "불꽃 · 비행 타입",
        "traits": "추진력 · 자신감 · 목표 지향",
        "tagline": "목표를 향해 거침없이 날아오르는 리더",
        "reason": [
            "큰 목표를 세우고 자신 있게 방향을 정하는 편이에요.",
            "도전을 두려워하지 않고 일을 추진하는 점이 잘 어울려요."
        ],
        "match": "INTP",
        "match_reason": "INTP의 독창적인 분석이 전략을 풍성하게 하고, ENTJ의 추진력이 아이디어를 현실로 이끌어요."
    }
}

st.markdown("""
<style>
.stApp {
    background: #fff9e9;
    color: #403626;
}
.block-container {
    max-width: 900px;
    padding-top: 2rem;
}
h1, h2, h3 {
    color: #403626;
}
.hero {
    text-align: center;
    padding: 1.5rem 0;
}
.hero h1 {
    font-size: clamp(2.3rem, 6vw, 3.8rem);
    line-height: 1.2;
}
.hero p {
    font-size: 1.15rem;
    color: #776b57;
    line-height: 1.8;
}
div.stButton > button {
    min-height: 3.2rem;
    border-radius: 15px;
    border: 1px solid #ecdcae;
    background: #fff1bd;
    color: #403626;
    font-size: 1.05rem;
    font-weight: 800;
}
div.stButton > button:hover {
    background: #ffd968;
    color: #403626;
    border-color: #d5a526;
}
.info-box {
    padding: 1.1rem;
    border-radius: 18px;
    background: #fff4d5;
    margin-bottom: .7rem;
    line-height: 1.8;
}
.green-box {
    background: #e7efd9;
}
.congrats {
    text-align: center;
    background: #ffe89a;
    padding: 1rem;
    border-radius: 18px;
    font-size: 1.25rem;
    font-weight: bold;
    margin: 1rem 0;
}
.pokemon-title {
    text-align: center;
    font-size: 2.5rem;
    font-weight: bold;
}
.pokemon-subtitle {
    text-align: center;
    font-size: 1.15rem;
    color: #79663a;
}
.note {
    text-align: center;
    color: #8a7c63;
    font-size: .9rem;
    margin-top: 2rem;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <h1>🌼 MBTI로 포켓몬 찾기</h1>
    <p>
        나와 가장 잘 어울리는 단짝 포켓몬은 누구일까요?<br>
        MBTI를 선택하고 나만의 포켓몬을 만나 보세요!
    </p>
</div>
""", unsafe_allow_html=True)

st.subheader("🌷 나의 MBTI를 골라 주세요")

types = [
    "ISTJ", "ISFJ", "INFJ", "INTJ",
    "ISTP", "ISFP", "INFP", "INTP",
    "ESTP", "ESFP", "ENFP", "ENTP",
    "ESTJ", "ESFJ", "ENFJ", "ENTJ",
]

if "selected_type" not in st.session_state:
    st.session_state.selected_type = None

for row in range(4):
    cols = st.columns(4)
    for col, mbti in zip(cols, types[row * 4:(row + 1) * 4]):
        with col:
            if st.button(mbti, key=mbti, use_container_width=True):
                st.session_state.selected_type = mbti
                st.session_state.celebrate = True

selected = st.session_state.selected_type

if selected:
    data = POKEMON[selected]

    if st.session_state.get("celebrate", False):
        st.balloons()
        st.snow()
        st.session_state.celebrate = False

    st.markdown(
        f'<div class="congrats">🎉 축하해요! '
        f'{selected}의 단짝 포켓몬을 찾았어요! 🎉</div>',
        unsafe_allow_html=True,
    )

    image_url = (
        "https://raw.githubusercontent.com/PokeAPI/sprites/master/"
        f"sprites/pokemon/other/official-artwork/{data['id']}.png"
    )

    st.image(
        image_url,
        width=280,
        caption=f"{data['name']} ({data['english']})",
    )

    st.markdown(
        f'<div class="pokemon-title">{data["name"]}</div>'
        f'<div class="pokemon-subtitle">{data["english"]}</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        f'<div class="pokemon-subtitle">{data["tagline"]}</div>',
        unsafe_allow_html=True,
    )

    left, right = st.columns(2)

    with left:
        st.markdown(
            '<div class="info-box">'
            '<h3>💛 나와 닮은 이유</h3>'
            f'<p>{data["reason"][0]}<br>{data["reason"][1]}</p>'
            '</div>',
            unsafe_allow_html=True,
        )

    with right:
        st.markdown(
            '<div class="info-box green-box">'
            '<h3>✨ 포켓몬 특징</h3>'
            f'<p><b>타입</b>: {data["types"]}<br>'
            f'<b>특징</b>: {data["traits"]}</p>'
            '</div>',
            unsafe_allow_html=True,
        )

    st.markdown(
        '<div class="info-box green-box">'
        f'<h3>🤝 잘 맞는 MBTI: {data["match"]}</h3>'
        f'<p>{data["match_reason"]}</p>'
        '</div>',
        unsafe_allow_html=True,
    )

    if st.button("↩️ 다시 고르기", use_container_width=True):
        st.session_state.selected_type = None
        st.session_state.celebrate = False
        st.rerun()

else:
    st.info("💛 위에서 MBTI를 선택하면 단짝 포켓몬이 나타나요!")

st.markdown(
    '<div class="note">'
    '재미로 즐기는 성격 유형 콘텐츠예요. '
    '포켓몬 이미지를 표시하려면 인터넷 연결이 필요합니다.'
    '</div>',
    unsafe_allow_html=True,
)
