# 💬 Django Chat Classifier

A **real-time chat application** built with **Django + Channels (WebSockets)** and powered by **DistilBERT (HuggingFace Transformers)** to detect and flag **offensive or toxic messages** instantly.  

---

## 🚀 Features
- 🔗 **Live Chat** using Django Channels (WebSockets).  
- 🤖 **Offensive Message Detection** with DistilBERT.  
- 🔑 **Authentication**: Register, Login, Logout.  
- 👤 **User Profiles**: Basic user info page.  
- 🏠 **Landing Page**: Simple Bootstrap home page.  
- 🐳 **Dockerized** for easy deployment.  
- 📊 Extendable for moderation dashboard.  

---

## 🛠️ Tech Stack
- **Backend**: Django, Django Channels  
- **Frontend**: Bootstrap 5  
- **Realtime**: Redis (Channels layer)  
- **ML Model**: DistilBERT (HuggingFace Transformers)  
- **Database**: SQLite (dev) / PostgreSQL (prod-ready)  
- **Deployment**: Docker, Docker Compose  

---

## 📂 Project Structure
```
DJANGO_CHAT_CLASSIFIER/
│
├── chat/                 # Chat app (WebSockets, consumers, routing)
│├── templates/           # Chat page templates
│├── consumers.py         # WebSocket logic
│├── routing.py           # WebSocket routes
│
├── user/                 # Auth & profile app
│├── templates/           # Login, Register, Profile
│
├── index/                # Landing/Home app
│├── templates/           # Home page
│
├── django_chat_classifier/   # Project config (settings, urls, asgi)
│
├── templates/            # Global templates
├── manage.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md
```

---

## ⚡ Installation & Setup

### 1️⃣ Clone the repo
```bash
git clone git@github.com:budescode/Real-time-chat-offensive-text-classifier.git
cd django_chat_classifier
```

### 2️⃣ Create virtual environment
```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run migrations
```bash
python manage.py migrate
```

<!-- ### 5️⃣ Start Redis (for WebSockets)
```bash
docker run -p 6379:6379 -d redis:alpine
``` -->

### 6️⃣ Run development server
```bash
python manage.py runserver
```

Visit: 👉 [http://localhost:8000](http://localhost:8000)  

---

## 🐳 Running with Docker
```bash
docker-compose up --build
```

This spins up:  
- Django app (Channels-enabled)  
- Redis (for WebSockets)  

---

## 🤖 Offensive Text Classifier
- Model: **DistilBERT (`distilbert-base-uncased`)** via HuggingFace Transformers.  
- Fine-tuned on offensive language datasets (e.g., Jigsaw Toxic Comment dataset).  
- Each chat message is classified in **real-time**:  
  - ✅ Safe → displayed normally.  
  - 🚫 Offensive → flagged before sending.  

---

## 📸 Pages
- 🏠 **Home Page** (`/`)  
- 🔑 **Login** (`/user/login/`)  
- 📝 **Register** (`/user/register/`)  
- 💬 **Chat** (`/chat/`)  
- 👤 **Profile** (`/user/profile/`)  

---

## 🔮 Future Improvements
- 🚦 Admin dashboard for moderation.  
- 🌍 Multilingual offensive text detection.  
- 🔔 Notifications & typing indicators.  
- 📈 User reputation system.  
- ☁️ Deploy to AWS/GCP with CI/CD.  

---

## 🤝 Contributing
Pull requests are welcome. For major changes, please open an issue first.  

---

## 📜 License
MIT License © 2025 [Osakpolor Emmanuel Omonbude]  
# Real-time-chat-offensive-text-classifier
