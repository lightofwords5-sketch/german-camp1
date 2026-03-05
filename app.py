import streamlit as st
import pandas as pd
import datetime
import random

# ─────────────────────────────────────────────
#  PAGE CONFIG
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="🇩🇪 German Mastery Camp",
    page_icon="🇩🇪",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─────────────────────────────────────────────
#  CUSTOM CSS — Black / Red / Gold palette
# ─────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=DM+Sans:wght@300;400;500;600&display=swap');

/* ---------- root variables ---------- */
:root {
    --black:  #0d0d0d;
    --red:    #cc0000;
    --gold:   #f5c518;
    --gold2:  #d4a017;
    --white:  #f8f5ef;
    --card:   #1a1a1a;
    --border: #2e2e2e;
    --muted:  #888;
}

/* ---------- global ---------- */
html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
    background-color: var(--black) !important;
    color: var(--white) !important;
}

/* ---------- sidebar ---------- */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0d0d0d 0%, #1a0000 100%) !important;
    border-right: 2px solid var(--red) !important;
}
[data-testid="stSidebar"] * { color: var(--white) !important; }

/* ---------- headings ---------- */
h1, h2, h3 { font-family: 'Playfair Display', serif !important; }
h1 { color: var(--gold) !important; font-size: 2.4rem !important; }
h2 { color: var(--red)  !important; }
h3 { color: var(--gold2)!important; }

/* ---------- metric cards ---------- */
[data-testid="stMetric"] {
    background: var(--card) !important;
    border: 1px solid var(--border) !important;
    border-radius: 12px !important;
    padding: 16px !important;
}
[data-testid="stMetricValue"] { color: var(--gold) !important; font-size: 2rem !important; }
[data-testid="stMetricLabel"] { color: var(--muted) !important; }

/* ---------- progress bar ---------- */
[data-testid="stProgressBar"] > div > div {
    background: linear-gradient(90deg, var(--red), var(--gold)) !important;
}

/* ---------- buttons ---------- */
.stButton > button {
    background: linear-gradient(135deg, var(--red), #8b0000) !important;
    color: var(--white) !important;
    border: none !important;
    border-radius: 8px !important;
    font-weight: 600 !important;
    transition: transform 0.15s ease, box-shadow 0.15s ease !important;
}
.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 6px 20px rgba(204,0,0,0.45) !important;
}

/* ---------- gold action button ---------- */
.gold-btn > button {
    background: linear-gradient(135deg, var(--gold), var(--gold2)) !important;
    color: var(--black) !important;
}

/* ---------- tabs ---------- */
[data-testid="stTabs"] button {
    color: var(--muted) !important;
    font-weight: 500 !important;
}
[data-testid="stTabs"] button[aria-selected="true"] {
    color: var(--gold) !important;
    border-bottom: 2px solid var(--gold) !important;
}

/* ---------- selectbox / text inputs ---------- */
[data-testid="stSelectbox"] > div, [data-testid="stTextInput"] > div > div {
    background: var(--card) !important;
    border: 1px solid var(--border) !important;
    color: var(--white) !important;
    border-radius: 8px !important;
}

/* ---------- checkboxes ---------- */
[data-testid="stCheckbox"] label { font-size: 0.95rem !important; }

/* ---------- custom cards ---------- */
.gmc-card {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 14px;
    padding: 20px 24px;
    margin-bottom: 16px;
}
.gmc-card.gold { border-left: 4px solid var(--gold); }
.gmc-card.red  { border-left: 4px solid var(--red);  }
.gmc-card.flag {
    background: linear-gradient(135deg, #1a1a1a 60%, #1a0000 100%);
    border: 1px solid var(--red);
}

.mantra-box {
    background: linear-gradient(135deg, #1a0a00, #1a1a00);
    border: 1px solid var(--gold);
    border-radius: 14px;
    padding: 22px 28px;
    text-align: center;
    font-size: 1.2rem;
    font-style: italic;
    color: var(--gold);
    font-family: 'Playfair Display', serif;
    margin-bottom: 24px;
}

.streak-badge {
    display: inline-block;
    background: var(--gold);
    color: var(--black);
    border-radius: 20px;
    padding: 4px 14px;
    font-weight: 700;
    font-size: 0.85rem;
}

.phase-badge {
    display: inline-block;
    background: var(--red);
    color: var(--white);
    border-radius: 6px;
    padding: 3px 10px;
    font-size: 0.8rem;
    font-weight: 600;
    letter-spacing: 0.05em;
    text-transform: uppercase;
}

.leader-row {
    display: flex;
    align-items: center;
    justify-content: space-between;
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 12px 18px;
    margin-bottom: 8px;
}
.leader-rank { font-size: 1.4rem; width: 36px; }
.leader-name { flex: 1; font-weight: 600; margin-left: 12px; }
.leader-stars { color: var(--gold); font-weight: 700; }

.phonetic-card {
    background: linear-gradient(135deg, #1a1a1a, #0d0d0d);
    border: 1px solid var(--gold);
    border-radius: 12px;
    padding: 18px;
    text-align: center;
    cursor: default;
}
.phonetic-symbol {
    font-size: 3rem;
    color: var(--gold);
    font-family: 'Playfair Display', serif;
    font-weight: 900;
}
.phonetic-desc { color: var(--muted); font-size: 0.85rem; margin-top: 6px; }

.resource-link {
    display: block;
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 14px 18px;
    margin-bottom: 10px;
    text-decoration: none !important;
    color: var(--white) !important;
    transition: border-color 0.2s;
}
.resource-link:hover { border-color: var(--gold); }

div[data-testid="column"] { padding: 6px !important; }
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
#  SESSION STATE INIT
# ─────────────────────────────────────────────
USERS = ["Ahmed", "Sara", "Mohamed", "Layla", "Omar", "Nour", "Youssef", "Hana"]

if "user_name"      not in st.session_state: st.session_state.user_name = USERS[0]
if "completed_days" not in st.session_state: st.session_state.completed_days = set()
if "daily_tasks"    not in st.session_state: st.session_state.daily_tasks = {}
if "total_stars"    not in st.session_state: st.session_state.total_stars = 0
if "leaderboard"    not in st.session_state:
    st.session_state.leaderboard = {
        "Sara":    {"stars": 185, "streak": 12},
        "Ahmed":   {"stars": 160, "streak": 9},
        "Layla":   {"stars": 140, "streak": 8},
        "Mohamed": {"stars": 115, "streak": 6},
        "Omar":    {"stars": 90,  "streak": 5},
        "Nour":    {"stars": 70,  "streak": 4},
        "Youssef": {"stars": 45,  "streak": 2},
        "Hana":    {"stars": 20,  "streak": 1},
    }

# ─────────────────────────────────────────────
#  DATA — 90-day plan (sample; load from GSheet in prod)
# ─────────────────────────────────────────────
MANTRAS = [
    "\"Sprache ist nicht nur Kommunikation — sie ist Identität.\" 🇩🇪",
    "\"Every German word you learn is a door to a new world.\"",
    "\"Fehler machen ist menschlich. Aufhören ist optional.\" (Making mistakes is human. Quitting is optional.)",
    "\"Du schaffst das! One day at a time, one word at a time.\"",
    "\"The alphabet is the key — grammar is the engine — you are the driver.\"",
    "\"Repetition is the mother of mastery. Wiederholen = Meistern.\"",
    "\"Ein Schritt nach dem anderen führt zum Ziel.\" (One step at a time leads to the goal.)",
]

PHASES = {
    "🏗️ Foundation (Days 1–30)":   list(range(1, 31)),
    "🧱 Construction (Days 31–60)": list(range(31, 61)),
    "⚡ Activation (Days 61–90)":   list(range(61, 91)),
}

PHASE_LABELS = {}
for phase, days in PHASES.items():
    for d in days:
        PHASE_LABELS[d] = phase

TOPICS = {
    **{d: f"Alphabet & Phonetics — Part {d}"       for d in range(1,  8)},
    **{d: f"Numbers, Colors & Greetings — Day {d}" for d in range(8,  15)},
    **{d: f"Basic Grammar: Artikel & Nouns — Day {d}" for d in range(15, 22)},
    **{d: f"Verbs & Present Tense — Day {d}"       for d in range(22, 31)},
    **{d: f"Sentence Building — Day {d}"           for d in range(31, 46)},
    **{d: f"Conversational Phrases — Day {d}"      for d in range(46, 61)},
    **{d: f"Reading & Listening — Day {d}"         for d in range(61, 76)},
    **{d: f"Writing & Expression — Day {d}"        for d in range(76, 91)},
}

NICOS_WEG_EPISODES = {
    **{d: f"https://www.dw.com/de/nicos-weg/s-52164?episode={d}" for d in range(1, 91)},
}

ARABIC_VIDEOS = {d: "https://www.youtube.com/results?search_query=تعلم+الألمانية+للمبتدئين" for d in range(1, 15)}

PHONETICS = [
    {"symbol": "r",  "name": "Das R",    "desc": "Guttural R — like gargling softly",     "yt": "https://www.youtube.com/watch?v=oRpSJXMJUDg"},
    {"symbol": "ch", "name": "Das CH",   "desc": "Two sounds: 'ich' vs 'ach' — position matters", "yt": "https://www.youtube.com/watch?v=pN3Aqs9BGLM"},
    {"symbol": "ä",  "name": "Das Ä",    "desc": "Like English 'air' but shorter",         "yt": "https://www.youtube.com/watch?v=XbiBS5YIQB0"},
    {"symbol": "ö",  "name": "Das Ö",    "desc": "Round lips, say 'e' — French 'eu'",      "yt": "https://www.youtube.com/watch?v=XbiBS5YIQB0"},
    {"symbol": "ü",  "name": "Das Ü",    "desc": "Round lips, say 'i' — French 'u'",       "yt": "https://www.youtube.com/watch?v=XbiBS5YIQB0"},
    {"symbol": "ß",  "name": "Das ß",    "desc": "Sharp S — like 'ss', never at word start","yt": "https://www.youtube.com/watch?v=oRpSJXMJUDg"},
]

CULTURAL_DROPS = [
    {"week": 1, "title": "Pünktlichkeit 🕐", "body": "Germans value punctuality above almost everything. Being 5 minutes late is rude — arriving 5 minutes early is respectful."},
    {"week": 2, "title": "Kaffee & Kuchen ☕", "body": "Sunday afternoon coffee and cake (Kaffee und Kuchen) is a sacred tradition — it's how families bond."},
    {"week": 3, "title": "Recycling Culture ♻️", "body": "Germany has one of the world's best recycling systems. Pfand (bottle deposits) make sustainability everyone's business."},
    {"week": 4, "title": "Brot & Wurst 🥖", "body": "Germany has 3,200+ bread varieties. Bread is emotional here — 'Heimweh' (homesickness) often starts with missing Brot."},
]

RESOURCES = [
    {"cat": "📺 Video", "name": "Nicos Weg — DW's A1 series", "url": "https://www.dw.com/de/nicos-weg/s-52164"},
    {"cat": "📺 Video", "name": "Easy German — Street interviews", "url": "https://www.youtube.com/@EasyGerman"},
    {"cat": "📺 Video", "name": "Deutsch für Euch — Grammar", "url": "https://www.youtube.com/@DeutschFuerEuch"},
    {"cat": "🃏 Anki",  "name": "Anki Web — Sync your decks", "url": "https://ankiweb.net"},
    {"cat": "🃏 Anki",  "name": "Shared Deck: German Core 2k", "url": "https://ankiweb.net/shared/info/1558798271"},
    {"cat": "🔊 Audio", "name": "YouGlish German — hear words in context", "url": "https://youglish.com/german"},
    {"cat": "🔊 Audio", "name": "Forvo — Native pronunciations", "url": "https://forvo.com/languages/de/"},
    {"cat": "📖 Read",  "name": "Slow German Podcast", "url": "https://slowgerman.com"},
    {"cat": "📖 Read",  "name": "DW Learn German Articles", "url": "https://www.dw.com/en/learn-german/s-2053"},
    {"cat": "🛠️ Tools", "name": "dict.cc — Best bilingual dictionary", "url": "https://www.dict.cc"},
    {"cat": "🛠️ Tools", "name": "Reverso Context — Word in sentences", "url": "https://context.reverso.net/translation/german-english/"},
    {"cat": "🛠️ Tools", "name": "LanguageTool — German grammar checker", "url": "https://languagetool.org"},
]

# ─────────────────────────────────────────────
#  HELPERS
# ─────────────────────────────────────────────
def get_current_day() -> int:
    return min(len(st.session_state.completed_days) + 1, 90)

def compute_streak(completed: set) -> int:
    if not completed: return 0
    streak, day = 0, max(completed)
    while day in completed:
        streak += 1
        day -= 1
    return streak

def stars_for_user() -> int:
    return len(st.session_state.completed_days) * 10 + st.session_state.total_stars

def phase_for_day(d: int) -> str:
    return PHASE_LABELS.get(d, "Foundation")

def google_sheet_url(sheet_url: str) -> str:
    """Convert a Google Sheets share URL to CSV export URL."""
    if "spreadsheets/d/" in sheet_url:
        sheet_id = sheet_url.split("spreadsheets/d/")[1].split("/")[0]
        return f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv"
    return sheet_url

# ─────────────────────────────────────────────
#  SIDEBAR
# ─────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style='text-align:center; padding: 10px 0 20px;'>
        <div style='font-size:2.5rem;'>🇩🇪</div>
        <div style='font-family:"Playfair Display",serif; font-size:1.3rem; color:#f5c518; font-weight:700;'>German Mastery Camp</div>
        <div style='color:#888; font-size:0.8rem; margin-top:4px;'>90-Day Intensive Program</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # User selector
    st.markdown("**👤 Your Profile**")
    user = st.selectbox("Select your name", USERS, index=USERS.index(st.session_state.user_name), label_visibility="collapsed")
    st.session_state.user_name = user

    st.markdown("---")

    # Phase navigation
    st.markdown("**📍 Phases**")
    page = st.radio(
        "Navigate",
        ["🏠 Home", "📅 Daily Dashboard", "📊 Progress", "🏆 Leaderboard", "🔬 Phonetics Lab", "📚 Resources", "🌍 Mentor Corner"],
        label_visibility="collapsed"
    )

    st.markdown("---")

    # Mini stats
    days_done = len(st.session_state.completed_days)
    streak    = compute_streak(st.session_state.completed_days)
    stars     = stars_for_user()

    st.markdown(f"""
    <div class='gmc-card gold' style='padding:14px;'>
        <div style='font-size:0.75rem; color:#888; margin-bottom:8px; text-transform:uppercase; letter-spacing:.06em;'>Your Stats</div>
        <div style='display:flex; justify-content:space-between; margin-bottom:6px;'>
            <span>✅ Days Done</span><strong style='color:#f5c518;'>{days_done}/90</strong>
        </div>
        <div style='display:flex; justify-content:space-between; margin-bottom:6px;'>
            <span>🔥 Streak</span><strong style='color:#cc0000;'>{streak} days</strong>
        </div>
        <div style='display:flex; justify-content:space-between;'>
            <span>⭐ Stars</span><strong style='color:#f5c518;'>{stars}</strong>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # GSheet connector
    st.markdown("---")
    st.markdown("**🔗 Google Sheet (optional)**")
    gsheet_url = st.text_input("Paste your Sheet URL", placeholder="https://docs.google.com/spreadsheets/d/...", label_visibility="collapsed")
    if gsheet_url and st.button("Load Data"):
        try:
            csv_url = google_sheet_url(gsheet_url)
            df = pd.read_csv(csv_url)
            st.session_state.gsheet_df = df
            st.success(f"✅ Loaded {len(df)} rows!")
        except Exception as e:
            st.error(f"❌ Error: {e}")

# ─────────────────────────────────────────────
#  PAGE: HOME
# ─────────────────────────────────────────────
if page == "🏠 Home":
    st.markdown(f"# 🇩🇪 Willkommen, {st.session_state.user_name}!")
    st.markdown("### *Learning is living — not just memorizing.*")

    # Mantra of the Day
    today_mantra = MANTRAS[datetime.date.today().timetuple().tm_yday % len(MANTRAS)]
    st.markdown(f'<div class="mantra-box">💬 Mantra of the Day<br><br>{today_mantra}</div>', unsafe_allow_html=True)

    # Overview metrics
    days_done = len(st.session_state.completed_days)
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("📅 Current Day",   f"Day {get_current_day()}/90")
    c2.metric("✅ Days Completed", days_done)
    c3.metric("🔥 Streak",        f"{compute_streak(st.session_state.completed_days)} days")
    c4.metric("⭐ Stars Earned",   stars_for_user())

    st.markdown("<br>", unsafe_allow_html=True)

    # Phase overview
    st.markdown("## 🗺️ Your 90-Day Journey")
    cols = st.columns(3)
    for i, (phase, days) in enumerate(PHASES.items()):
        done_in_phase = len([d for d in days if d in st.session_state.completed_days])
        pct = done_in_phase / len(days)
        with cols[i]:
            st.markdown(f"""
            <div class='gmc-card {"gold" if i==0 else "red" if i==1 else ""}'>
                <div style='font-size:1.5rem; margin-bottom:8px;'>{phase.split()[0]}</div>
                <div style='font-weight:700; font-size:1rem; margin-bottom:4px;'>{" ".join(phase.split()[1:])}</div>
                <div style='color:#888; font-size:0.82rem; margin-bottom:12px;'>Days {days[0]}–{days[-1]}</div>
                <div style='color:#f5c518; font-size:1.6rem; font-weight:700;'>{done_in_phase}/{len(days)}</div>
                <div style='color:#888; font-size:0.8rem;'>days completed</div>
            </div>
            """, unsafe_allow_html=True)
            st.progress(pct)

    # Philosophy
    st.markdown("---")
    st.markdown("## 🧠 The German Mastery Philosophy")
    st.markdown("""
    <div class='gmc-card flag'>
        <p style='line-height:1.8;'>
        This camp is built on one truth: <strong style='color:#f5c518;'>language is not memorized — it is lived.</strong>
        Every day, you don't just study German — you <em>become</em> a little more German in how you think, how you notice the world, 
        and how you connect with one of Europe's richest cultures.
        </p>
        <p style='line-height:1.8; margin-top:12px;'>
        The 120-minute daily routine is non-negotiable. It's not long — it's <strong style='color:#cc0000;'>focused</strong>. 
        Anki trains your brain. Nicos Weg trains your ear. YouGlish trains your mouth. Writing trains your soul.
        </p>
        <p style='line-height:1.8; margin-top:12px; color:#888; font-size:0.9rem;'>
        <em>"Ein Tag ohne Deutsch ist ein verlorener Tag."</em><br>
        A day without German is a lost day.
        </p>
    </div>
    """, unsafe_allow_html=True)

# ─────────────────────────────────────────────
#  PAGE: DAILY DASHBOARD
# ─────────────────────────────────────────────
elif page == "📅 Daily Dashboard":
    current_day = get_current_day()

    st.markdown(f"# 📅 Daily Dashboard")

    # Day selector
    col_a, col_b = st.columns([3,1])
    with col_a:
        selected_day = st.slider("Select Day", 1, 90, current_day, label_visibility="visible")
    with col_b:
        phase = phase_for_day(selected_day)
        short_phase = phase.split("(")[0].strip()
        st.markdown(f"<br><span class='phase-badge'>{short_phase}</span>", unsafe_allow_html=True)

    topic = TOPICS.get(selected_day, f"Day {selected_day} Content")
    st.markdown(f"### 📖 {topic}")
    st.markdown("---")

    # Foundation Bridge (Arabic videos, days 1-14)
    if selected_day <= 14:
        st.markdown("### 🌉 Foundation Bridge — Arabic Support")
        st.markdown(f"""
        <div class='gmc-card gold'>
            <p>Since you're in the <strong>Foundation Phase</strong>, we bridge concepts through Arabic explanations 
            so nothing is left unclear.</p>
            <a href='{ARABIC_VIDEOS.get(selected_day, "#")}' target='_blank' 
               style='color:#f5c518; font-weight:600; text-decoration:none;'>
               📺 Watch Today's Arabic Bridge Video →
            </a>
        </div>
        """, unsafe_allow_html=True)

    # Nicos Weg
    st.markdown("### 📺 Nicos Weg — Today's Episode")
    nicos_url = NICOS_WEG_EPISODES.get(selected_day, "https://www.dw.com/de/nicos-weg/s-52164")
    st.markdown(f"""
    <div class='gmc-card red'>
        <p>Follow Nico's story and absorb German naturally through immersive storytelling.</p>
        <a href='{nicos_url}' target='_blank' 
           style='color:#f5c518; font-weight:600; text-decoration:none;'>
           🎬 Watch Episode {selected_day} on DW →
        </a>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### ✅ 120-Minute Daily Checklist")

    # Task key for this specific day
    day_key = f"day_{selected_day}"
    if day_key not in st.session_state.daily_tasks:
        st.session_state.daily_tasks[day_key] = {
            "anki":   False,
            "nicos":  False,
            "youglish": False,
            "writing": False,
        }

    tasks = st.session_state.daily_tasks[day_key]

    c1, c2 = st.columns(2)
    with c1:
        tasks["anki"]    = st.checkbox("🃏 **Anki Reviews** (30 min) — Review deck + add 10 new cards", value=tasks["anki"],    key=f"anki_{selected_day}")
        tasks["nicos"]   = st.checkbox("📺 **Nicos Weg** (30 min) — Watch + shadow the dialogue",       value=tasks["nicos"],   key=f"nicos_{selected_day}")
    with c2:
        tasks["youglish"]= st.checkbox("🔊 **YouGlish Practice** (30 min) — Find 5 words, mimic natives",value=tasks["youglish"],key=f"youglish_{selected_day}")
        tasks["writing"] = st.checkbox("✍️ **Writing Practice** (30 min) — Write 5 sentences + journal",  value=tasks["writing"], key=f"writing_{selected_day}")

    st.session_state.daily_tasks[day_key] = tasks

    completed_count = sum(tasks.values())
    progress_pct    = completed_count / 4

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f"**Day Progress: {completed_count}/4 tasks**")
    st.progress(progress_pct)

    if completed_count == 4 and selected_day not in st.session_state.completed_days:
        st.markdown("<div class='gold-btn'>", unsafe_allow_html=True)
        if st.button(f"🏆 Mark Day {selected_day} as COMPLETE — Earn 10 ⭐"):
            st.session_state.completed_days.add(selected_day)
            st.session_state.total_stars += 10
            # update leaderboard
            name = st.session_state.user_name
            if name in st.session_state.leaderboard:
                st.session_state.leaderboard[name]["stars"] += 10
            st.balloons()
            st.success(f"🎉 Wunderbar! Day {selected_day} complete! You earned 10 ⭐")
        st.markdown("</div>", unsafe_allow_html=True)
    elif selected_day in st.session_state.completed_days:
        st.success(f"✅ Day {selected_day} already completed! Ausgezeichnet! 🌟")

    # YouGlish quick link
    st.markdown("---")
    st.markdown("### 🔊 Quick Practice Links")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <a href='https://youglish.com/german' target='_blank' class='resource-link'>
            🎙️ <strong>YouGlish German</strong><br>
            <span style='color:#888; font-size:0.85rem;'>Hear any word spoken by natives on YouTube</span>
        </a>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <a href='https://ankiweb.net' target='_blank' class='resource-link'>
            🃏 <strong>AnkiWeb</strong><br>
            <span style='color:#888; font-size:0.85rem;'>Review your flashcard decks online</span>
        </a>
        """, unsafe_allow_html=True)

# ─────────────────────────────────────────────
#  PAGE: PROGRESS
# ─────────────────────────────────────────────
elif page == "📊 Progress":
    st.markdown(f"# 📊 Your Progress — {st.session_state.user_name}")

    days_done  = len(st.session_state.completed_days)
    total_pct  = days_done / 90
    streak     = compute_streak(st.session_state.completed_days)

    st.markdown(f"### Overall Journey: {days_done}/90 days")
    st.progress(total_pct)
    st.markdown(f"<p style='color:#888; font-size:0.85rem;'>{total_pct*100:.1f}% complete — {90-days_done} days remaining</p>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    c1.metric("🔥 Current Streak", f"{streak} days")
    c2.metric("⭐ Total Stars",     stars_for_user())
    c3.metric("📅 Days Completed", days_done)

    # Phase breakdown
    st.markdown("---")
    st.markdown("## Phase Breakdown")
    for phase, days in PHASES.items():
        done_here = len([d for d in days if d in st.session_state.completed_days])
        pct = done_here / len(days)
        st.markdown(f"**{phase}** — {done_here}/{len(days)} days")
        st.progress(pct)
        st.markdown("<br>", unsafe_allow_html=True)

    # Calendar heatmap (simple grid)
    st.markdown("---")
    st.markdown("## 📆 90-Day Completion Map")
    cols_per_row = 10
    all_day_cols = st.columns(cols_per_row)
    for i in range(90):
        day_num = i + 1
        col = all_day_cols[i % cols_per_row]
        if day_num in st.session_state.completed_days:
            col.markdown(f"<div title='Day {day_num}' style='background:#cc0000;border-radius:4px;width:100%;padding:4px 0;text-align:center;font-size:0.7rem;margin-bottom:4px;color:white;'>{day_num}</div>", unsafe_allow_html=True)
        elif day_num == get_current_day():
            col.markdown(f"<div title='Day {day_num} (Today)' style='background:#f5c518;border-radius:4px;width:100%;padding:4px 0;text-align:center;font-size:0.7rem;margin-bottom:4px;color:black;font-weight:700;'>{day_num}</div>", unsafe_allow_html=True)
        else:
            col.markdown(f"<div title='Day {day_num}' style='background:#1a1a1a;border:1px solid #2e2e2e;border-radius:4px;width:100%;padding:4px 0;text-align:center;font-size:0.7rem;margin-bottom:4px;color:#555;'>{day_num}</div>", unsafe_allow_html=True)

    st.markdown("<br><span style='color:#888; font-size:0.82rem;'>🔴 Completed &nbsp;|&nbsp; 🟡 Today &nbsp;|&nbsp; ⬛ Upcoming</span>", unsafe_allow_html=True)

    # Reset (admin)
    st.markdown("---")
    with st.expander("⚙️ Admin Controls"):
        day_to_add = st.number_input("Mark day as complete (testing)", 1, 90, 1)
        if st.button("✅ Add Day"):
            st.session_state.completed_days.add(day_to_add)
            st.success(f"Day {day_to_add} marked complete!")
        if st.button("🔄 Reset All Progress", type="secondary"):
            st.session_state.completed_days = set()
            st.session_state.daily_tasks = {}
            st.session_state.total_stars = 0
            st.success("Progress reset!")

# ─────────────────────────────────────────────
#  PAGE: LEADERBOARD
# ─────────────────────────────────────────────
elif page == "🏆 Leaderboard":
    st.markdown("# 🏆 Leaderboard")
    st.markdown("*The fire of competition keeps the flame of learning alive.*")
    st.markdown("<br>", unsafe_allow_html=True)

    # Update current user in leaderboard
    name = st.session_state.user_name
    if name in st.session_state.leaderboard:
        st.session_state.leaderboard[name]["stars"]  = max(st.session_state.leaderboard[name]["stars"], stars_for_user())
        st.session_state.leaderboard[name]["streak"] = max(st.session_state.leaderboard[name]["streak"], compute_streak(st.session_state.completed_days))

    sorted_lb = sorted(st.session_state.leaderboard.items(), key=lambda x: x[1]["stars"], reverse=True)
    medals    = ["🥇", "🥈", "🥉"] + ["🏅"] * 20

    tab1, tab2 = st.tabs(["⭐ Stars Ranking", "🔥 Streak Ranking"])

    with tab1:
        for rank, (uname, data) in enumerate(sorted_lb):
            is_you = uname == st.session_state.user_name
            border = "border: 2px solid #f5c518 !important;" if is_you else ""
            you_tag = " <span style='background:#f5c518;color:#000;border-radius:4px;padding:1px 8px;font-size:0.75rem;font-weight:700;'>YOU</span>" if is_you else ""
            st.markdown(f"""
            <div class='leader-row' style='{border}'>
                <span class='leader-rank'>{medals[rank]}</span>
                <span class='leader-name'>{uname}{you_tag}</span>
                <span style='color:#888; font-size:0.85rem; margin-right:20px;'>🔥 {data["streak"]}d streak</span>
                <span class='leader-stars'>⭐ {data["stars"]}</span>
            </div>
            """, unsafe_allow_html=True)

    with tab2:
        streak_sorted = sorted(st.session_state.leaderboard.items(), key=lambda x: x[1]["streak"], reverse=True)
        for rank, (uname, data) in enumerate(streak_sorted):
            is_you = uname == st.session_state.user_name
            border = "border: 2px solid #cc0000 !important;" if is_you else ""
            you_tag = " <span style='background:#cc0000;color:#fff;border-radius:4px;padding:1px 8px;font-size:0.75rem;font-weight:700;'>YOU</span>" if is_you else ""
            st.markdown(f"""
            <div class='leader-row' style='{border}'>
                <span class='leader-rank'>{medals[rank]}</span>
                <span class='leader-name'>{uname}{you_tag}</span>
                <span class='leader-stars'>🔥 {data["streak"]} days</span>
            </div>
            """, unsafe_allow_html=True)

    # How to earn stars
    st.markdown("---")
    st.markdown("### ⭐ How to Earn Stars")
    st.markdown("""
    <div class='gmc-card gold'>
        <div style='display:grid; grid-template-columns:1fr 1fr; gap:12px;'>
            <div>✅ Complete all 4 daily tasks → <strong style='color:#f5c518;'>+10 ⭐</strong></div>
            <div>🔥 7-day streak → <strong style='color:#f5c518;'>+25 ⭐ bonus</strong></div>
            <div>📝 Submit writing to mentor → <strong style='color:#f5c518;'>+5 ⭐</strong></div>
            <div>🏁 Complete a full phase → <strong style='color:#f5c518;'>+50 ⭐</strong></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ─────────────────────────────────────────────
#  PAGE: PHONETICS LAB
# ─────────────────────────────────────────────
elif page == "🔬 Phonetics Lab":
    st.markdown("# 🔬 Phonetics Lab")
    st.markdown("*Master the sounds that confuse Arabic speakers most. Click any card to open its YouTube guide.*")
    st.markdown("<br>", unsafe_allow_html=True)

    # Sound cards grid
    cols = st.columns(3)
    for i, ph in enumerate(PHONETICS):
        with cols[i % 3]:
            st.markdown(f"""
            <a href='{ph["yt"]}' target='_blank' style='text-decoration:none;'>
                <div class='phonetic-card'>
                    <div class='phonetic-symbol'>{ph["symbol"]}</div>
                    <div style='font-weight:700; color:white; margin-top:8px;'>{ph["name"]}</div>
                    <div class='phonetic-desc'>{ph["desc"]}</div>
                    <div style='color:#cc0000; font-size:0.8rem; margin-top:10px;'>▶ Watch Guide</div>
                </div>
            </a>
            <br>
            """, unsafe_allow_html=True)

    # Minimal pairs practice
    st.markdown("---")
    st.markdown("## 👂 Minimal Pairs Practice")
    minimal_pairs = [
        ("bitten",  "bieten",  "to ask / to offer"),
        ("Hölle",   "Höhle",   "hell / cave"),
        ("Städte",  "stehte",  "cities / stood"),
        ("suchen",  "suchen",  "to search"),
        ("Bach",    "Buch",    "stream / book"),
        ("fahren",  "fähren",  "to drive / ferries"),
    ]
    for a, b, meaning in minimal_pairs:
        st.markdown(f"""
        <div style='display:flex; align-items:center; background:#1a1a1a; border:1px solid #2e2e2e; 
                    border-radius:10px; padding:12px 18px; margin-bottom:8px; gap:12px;'>
            <span style='font-size:1.2rem; color:#f5c518; font-weight:700; width:100px;'>{a}</span>
            <span style='color:#555;'>vs</span>
            <span style='font-size:1.2rem; color:#cc0000; font-weight:700; width:100px;'>{b}</span>
            <span style='color:#888; font-size:0.85rem; margin-left:auto;'>{meaning}</span>
        </div>
        """, unsafe_allow_html=True)

    # YouGlish embed tip
    st.markdown("---")
    st.markdown("### 🎙️ Practice with Real Voices")
    st.markdown("""
    <div class='gmc-card gold'>
        <p>Type any word into <strong>YouGlish</strong> to hear it spoken by hundreds of native Germans in authentic YouTube clips.</p>
        <p style='margin-top:10px;'>
            <a href='https://youglish.com/german' target='_blank' style='color:#f5c518; font-weight:700; text-decoration:none;'>
                🌐 Open YouGlish German →
            </a>
        </p>
    </div>
    """, unsafe_allow_html=True)

# ─────────────────────────────────────────────
#  PAGE: RESOURCES
# ─────────────────────────────────────────────
elif page == "📚 Resources":
    st.markdown("# 📚 Resource Library")
    st.markdown("*Every link you need — organised and ready.*")
    st.markdown("<br>", unsafe_allow_html=True)

    categories = sorted(set(r["cat"] for r in RESOURCES))
    tabs = st.tabs(categories)

    for tab, cat in zip(tabs, categories):
        with tab:
            for res in [r for r in RESOURCES if r["cat"] == cat]:
                st.markdown(f"""
                <a href='{res["url"]}' target='_blank' class='resource-link'>
                    <strong>{res["name"]}</strong><br>
                    <span style='color:#555; font-size:0.82rem;'>{res["url"]}</span>
                </a>
                """, unsafe_allow_html=True)

    # Google Sheet sample structure
    st.markdown("---")
    st.markdown("## 📋 Google Sheet Template")
    st.markdown("Copy this structure for your content sheet:")

    sample_df = pd.DataFrame({
        "Day_Number":           [1, 2, 3],
        "Phase":                ["Foundation", "Foundation", "Foundation"],
        "Topic":                ["Alphabet & Phonetics", "Numbers 1-20", "Greetings"],
        "Video_Link_Arabic":    ["https://youtube.com/...", "https://youtube.com/...", "https://youtube.com/..."],
        "Video_Link_NicosWeg":  ["https://dw.com/...", "https://dw.com/...", "https://dw.com/..."],
        "Anki_Task":            ["Add 15 alphabet cards", "Add 20 number cards", "Add 10 greeting cards"],
        "Pronunciation_Task":   ["Practice ä ö ü",  "Practice numbers aloud", "Record yourself greeting"],
        "Writing_Task":         ["Write the alphabet x3", "Write 1-20 in German",  "Write 5 greetings"],
    })
    st.dataframe(sample_df, use_container_width=True)
    st.markdown("""
    <div class='gmc-card'>
        <p><strong>Steps to connect your sheet:</strong></p>
        <ol style='color:#888; line-height:2;'>
            <li>Create a Google Sheet with the columns above</li>
            <li>Go to File → Share → Publish to web → CSV format</li>
            <li>Paste the URL in the sidebar's "Google Sheet" field</li>
            <li>Click "Load Data" — your daily content will populate automatically ✅</li>
        </ol>
    </div>
    """, unsafe_allow_html=True)

# ─────────────────────────────────────────────
#  PAGE: MENTOR CORNER
# ─────────────────────────────────────────────
elif page == "🌍 Mentor Corner":
    st.markdown("# 🌍 Native Mentor Corner")

    current_week = min((len(st.session_state.completed_days) // 7) + 1, 4)

    st.markdown(f"""
    <div class='gmc-card flag'>
        <h3 style='color:#f5c518; margin-top:0;'>What is a Native Mentor?</h3>
        <p style='line-height:1.9;'>
            Your <strong>Native Mentor</strong> is a native German speaker who joins this camp as a cultural bridge. 
            They don't just correct your grammar — they share <em>how Germans actually live, think, and speak</em>.
        </p>
        <p style='line-height:1.9; margin-top:10px;'>
            Every week, your mentor drops a <strong style='color:#f5c518;'>Cultural Drop</strong> — a story, 
            a tradition, or a slice of German daily life that no textbook will teach you.
        </p>
        <p style='line-height:1.9; margin-top:10px; color:#888;'>
            <em>"Sprache ohne Kultur ist wie ein Körper ohne Seele."</em><br>
            Language without culture is like a body without a soul.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("## 📦 Weekly Cultural Drops")

    for drop in CULTURAL_DROPS:
        is_current = drop["week"] == current_week
        border_style = "border-left: 4px solid #f5c518;" if is_current else ""
        week_tag = " <span style='background:#f5c518;color:#000;border-radius:4px;padding:1px 8px;font-size:0.75rem;'>CURRENT WEEK</span>" if is_current else ""

        st.markdown(f"""
        <div class='gmc-card' style='{border_style}'>
            <div style='display:flex; align-items:center; gap:10px; margin-bottom:10px;'>
                <span style='color:#888; font-size:0.8rem; text-transform:uppercase; letter-spacing:.05em;'>Week {drop["week"]}</span>
                {week_tag}
            </div>
            <h3 style='margin:0 0 8px; color:{"#f5c518" if is_current else "#fff"};'>{drop["title"]}</h3>
            <p style='line-height:1.8; color:#ccc;'>{drop["body"]}</p>
        </div>
        """, unsafe_allow_html=True)

    # Mentor tasks
    st.markdown("---")
    st.markdown("## 📝 Weekly Mentor Challenges")
    mentor_tasks = [
        "Write a 50-word paragraph about your hometown in German and submit it to your mentor.",
        "Record a 30-second voice message in German — any topic — and share it in the WhatsApp group.",
        "Find a German word that has no Arabic equivalent and explain what it means.",
        "Watch a 10-minute YouTube clip entirely in German (no subtitles) and summarize it in 3 sentences.",
    ]
    for i, task in enumerate(mentor_tasks, 1):
        st.markdown(f"""
        <div style='display:flex; align-items:flex-start; background:#1a1a1a; border:1px solid #2e2e2e;
                    border-radius:10px; padding:14px 18px; margin-bottom:8px; gap:14px;'>
            <span style='background:#cc0000; color:white; border-radius:50%; width:28px; height:28px; 
                         display:flex; align-items:center; justify-content:center; 
                         font-weight:700; flex-shrink:0; font-size:0.85rem;'>{i}</span>
            <span style='line-height:1.6;'>{task}</span>
        </div>
        """, unsafe_allow_html=True)

# ─────────────────────────────────────────────
#  FOOTER
# ─────────────────────────────────────────────
st.markdown("---")
st.markdown("""
<div style='text-align:center; color:#555; font-size:0.82rem; padding:10px 0 20px;'>
    🇩🇪 German Mastery Camp &nbsp;|&nbsp; Built with ❤️ for serious learners &nbsp;|&nbsp; 
    <em>Viel Erfolg! (Good luck!)</em>
</div>
""", unsafe_allow_html=True)
