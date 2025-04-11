# 🎓 Student Advisory Bot

A GenAI-powered student advisory system designed for Middle Eastern universities. This smart assistant provides personalized academic guidance, course recommendations, and university support, helping students make better decisions throughout their academic journey.

## 🚀 Project Overview

The Student Advisory Bot leverages cutting-edge Generative AI and data analytics to:
- Offer tailored academic advice based on student profiles and academic history.
- Recommend courses, majors, and extracurricular paths aligned with student goals.
- Assist with Elective Recomendation.
- Support multilingual and culturally-aware interaction.

## 💡 Key Features

- 🔍 **Personalized Guidance**: Adapts advice based on individual academic records, goals, and preferences.
- 🧠 **AI-Powered Conversations**: Uses natural language understanding for a smooth chat-based experience.
- 📚 **Academic Planning**: Suggests optimal course paths and checks for prerequisite fulfillment.
- 🏫 **University Info Access**: Answers queries about programs, departments, deadlines, and more.
- 🌐 **Multilingual Support**: Built with regional language considerations in mind (Arabic/English).

## 🧱 Tech Stack

- **Backend**: Python, FastAPI
- **AI/ML**: OpenAI GPT, LangChain, custom academic recommendation models
- **Frontend**: React / Next.js (optional for UI)
- **Database**: PostgreSQL / MongoDB (depending on setup)
- **Deployment**: Docker, Vercel / AWS / Azure (configurable)

## 🗂️ Project Structure

```bash
student-advisory-bot/
├── advisory_modules          # Optional React interface
├── data/              # Sample datasets (anonymized)
└── README.md
```

## ⚙️ Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/student-advisory-bot.git
   cd student-advisory-bot
   ```

2. **Set Up Environment Variables**
   Copy `.env.example` to `.env` and fill in your API keys and DB info.

3. **Run with Docker**
   ```bash
   docker-compose up --build
   ```

4. **Access the Bot**
   - API: `http://localhost:8000`
   - UI (if enabled): `http://localhost:3000`

## 📊 Datasets Used

The bot works with anonymized university data such as:
- Student academic records
- Course catalogs and degree plans
- Program requirements
- Enrollment and scheduling data

> 💡 *Data privacy and student confidentiality are strictly maintained.*

## 📌 Future Enhancements

- ✅ Integration with university SIS platforms
- ✅ Arabic language support
- 🕓 Predictive analytics for student success
- 📱 Mobile chatbot interface
- 🧑‍🏫 Advisor dashboard with analytics

