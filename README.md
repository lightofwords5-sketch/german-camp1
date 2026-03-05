# 🇩🇪 German Mastery Camp — Streamlit App

## 🚀 Deploy for Free on Streamlit Cloud (5 minutes)

### Step 1 — Create a GitHub Repository
1. Go to [github.com](https://github.com) → **New repository**
2. Name it: `german-mastery-camp`
3. Set to **Public** → Create

### Step 2 — Upload Files
Upload these two files to your repo:
- `app.py`
- `requirements.txt` (create it with the content below)

**requirements.txt:**
```
streamlit>=1.32.0
pandas>=2.0.0
```

### Step 3 — Deploy on Streamlit Cloud
1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Sign in with GitHub
3. Click **"New app"**
4. Select your `german-mastery-camp` repo → `app.py`
5. Click **Deploy** ✅

Your app will be live at:
`https://your-username-german-mastery-camp.streamlit.app`

---

## 🔗 Connect Your Google Sheet (Optional but Recommended)

### Sheet Structure (8 columns):
| Day_Number | Phase | Topic | Video_Link_Arabic | Video_Link_NicosWeg | Anki_Task | Pronunciation_Task | Writing_Task |
|---|---|---|---|---|---|---|---|
| 1 | Foundation | Alphabet | https://youtube... | https://dw.com... | Add 15 cards | Practice ä ö ü | Write alphabet x3 |

### How to publish:
1. Create the sheet with those columns
2. **File → Share → Publish to web → CSV**
3. Copy the CSV link
4. Paste it in the app's sidebar → **"Load Data"**

> From that point, update the sheet daily — the app pulls content automatically. Zero code changes needed for 90 days! 🎉

---

## ⭐ Features Summary

| Feature | What it does |
|---|---|
| **Daily Dashboard** | 120-min checklist: Anki, Nicos Weg, YouGlish, Writing |
| **Progress Map** | 90-cell visual calendar + phase bars |
| **Leaderboard** | Stars & streak ranking for all participants |
| **Phonetics Lab** | 6 difficult sounds with YouTube guides |
| **Mentor Corner** | Weekly cultural drops from native speaker |
| **Resource Library** | All links organized by category |
| **Mantra of the Day** | Auto-rotates daily motivational quote |
| **Google Sheet sync** | Pull daily content from your live spreadsheet |

---

## 🕵️ Monitoring Participants

The leaderboard shows who is ahead and who has fallen behind.  
Every evening you can:
1. Open the app → **Leaderboard** tab
2. See who completed their day (stars updated)
3. Send a WhatsApp message to your group tagging today's top performers

---

## 🛠️ Local Testing

```bash
pip install streamlit pandas
streamlit run app.py
```

App opens at `http://localhost:8501`
