# HealthWellnessBuddy

Here is a professional, engaging, and emoji-enhanced `README.md` file for your **HealthWellnessBuddy** project that clearly explains the folder structure and setup process in simple steps.

---

```markdown
# 🌿 HealthWellnessBuddy 🧘‍♀️🤖

Welcome to **HealthWellnessBuddy** — your friendly AI-powered health and wellness companion!  
This app provides helpful guidance on health-related topics such as weight management, diet plans, medical issues, and more using an interactive Streamlit frontend and powerful backend tools. 💪🥗💬

---

## 📁 Project Structure Overview

Here's what each file and folder does:

```

HealthWellnessBuddy/
│
├── client/                  # Frontend tools and assets (built with Vite, Tailwind, etc.)
│
├── server/                  # Backend logic (API, tools, agents) using OpenAI Agents SDK
│
├── shared/                 # Shared utilities and modules used by both frontend and backend
│
├── streamlit\_app.py        # 🎨 Main Streamlit entry point (beautiful UI + emoji-rich assistant)
│
├── mock\_api.py             # Fake/mock data used for testing or UI demos
│
├── requirements.txt        # 🐍 Python dependencies for Streamlit and backend
│
├── package.json            # 📦 Node.js project config for frontend (Vite, Tailwind)
├── package-lock.json       # Dependency lock for reproducible installs
│
├── tailwind.config.ts      # 💅 TailwindCSS styling config
├── postcss.config.js       # CSS post-processor config
├── tsconfig.json           # TypeScript config for client-side code
├── vite.config.ts          # Vite bundler config
│
├── drizzle.config.ts       # Database & ORM (Drizzle) setup config
│
├── Dockerfile              # 🐳 Docker image for frontend (Streamlit UI)
├── Dockerfile.api          # 🐳 Docker image for backend (API)
├── docker-compose.yml      # 🔧 Combines frontend + backend into one dev/test environment
│
├── runtime.txt             # Runtime version (for deployment platforms like Heroku)
├── Procfile                # Heroku deployment process instructions
│
├── components.json         # Shared component metadata (used in building UI or agent logic)
│
├── README\_streamlit.md     # Extra instructions or style guide for Streamlit app
├── replit.md               # Setup steps for Replit environment
│
└── README.md               # 👋 You are here!

````

---

## 🚀 How to Run This Project

### 1. 📦 Install Backend (Python) Requirements

```bash
pip install -r requirements.txt
````

### 2. 💻 Run the Streamlit App

```bash
streamlit run streamlit_app.py
```

This launches your health buddy in the browser! 🌐🧠

---

## 🐳 Optional: Run with Docker

To run both frontend and backend using Docker:

```bash
docker-compose up --build
```

This pulls dependencies and starts the entire app automatically.

---

## 🌐 Folder Setup Guide (How I Created It)

1. **Created project folder**:

   ```bash
   mkdir HealthWellnessBuddy && cd HealthWellnessBuddy
   ```

2. **Frontend (client)**:

   ```bash
   npm create vite@latest client --template react-ts
   cd client && npm install
   npm install tailwindcss postcss autoprefixer
   npx tailwindcss init -p
   ```

3. **Backend (server)**:

   * Created `server/` folder with tools and OpenAI agent modules.
   * Added API endpoints, tools, and models.

4. **Streamlit UI**:

   * Built a beautiful app using `streamlit_app.py`
   * Included emojis 🌟, animated backgrounds, health assistant logo, and UI enhancements.

5. **Docker + Compose**:

   * Added `Dockerfile`, `Dockerfile.api`, and `docker-compose.yml`.

6. **Deployment files**:

   * Added `Procfile`, `runtime.txt`, `replit.md`, `README_streamlit.md`.

---

## ❤️ Features

✅ AI-powered health planner
✅ Supports diet, fitness, wellness tips
✅ Beautiful UI with emojis, animated backgrounds
✅ Fully Dockerized (frontend + backend)
✅ Works in Replit and Heroku

---

## 🧠 Built With

* **🧠 OpenAI Agents SDK** – Custom tools + health prompts
* **🎨 Streamlit** – Beautiful frontend
* **⚛️ Vite + React + TailwindCSS** – For modern UI components
* **🐍 Python** – Backend agents and logic
* **🐳 Docker** – Easy deployment
* **🔗 Drizzle ORM** – (Optional) for data handling

---

## 👩‍💻 Made by Ammara Dawood

*Empowering health with a touch of tech!* ✨
 🌐 Portfolio | 💖 GitHub](#)

---
🎉💻 Enjoy full-stack HealthWellnessBuddy right on Replit – AI chat, stylish UI, and backend brains, all in one place! 🚀🧘‍♂️🌷💻
--- 
```
