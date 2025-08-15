# 🌦️ AI-Powered Weather Analysis System (Society of Mind Architecture)

This project is an AI-driven weather analysis tool that uses **real-time weather data** and a **multi-agent architecture** inspired by the _Society of Mind_ framework. It leverages **OpenWeatherMap API**, **OpenAI GPT-4o**, and **Autogen** to deliver contextual weather insights through a simple **Streamlit app**.

---

## 🧠 What is Society of Mind (SoM)?

Inspired by Marvin Minsky’s concept, the **Society of Mind** architecture treats intelligence as the cooperation of specialized agents, each responsible for a small piece of a complex task. In this project, each agent plays a defined role in analyzing weather data:

            ┌─────────────────────────┐
            │       Human User         │
            └─────────────────────────┘
                       ▲
                       │ (input via Streamlit)
                       ▼
            ┌─────────────────────────┐
            │     UserProxyAgent      │
            │ (input & coordination)  │
            └─────────────────────────┘
                       ▲
                       │
                       ▼
            ┌─────────────────────────┐
            │   WeatherSoMTeam (SoM)  │
            │ (outer coordinator)     │
            └─────────────────────────┘
                       │
   ┌───────────────────┼────────────────────┐
   ▼                   ▼                    ▼
            ┌─────────────────────────┐
            │       Human User         │
            └─────────────────────────┘
                       ▲
                       │ (input via Streamlit)
                       ▼
            ┌─────────────────────────┐
            │     UserProxyAgent      │
            │ (input & coordination)  │
            └─────────────────────────┘
                       ▲
                       │
                       ▼
            ┌─────────────────────────┐
            │   WeatherSoMTeam (SoM)  │
            │ (outer coordinator)     │
            └─────────────────────────┘
                       │
   ┌───────────────────┼────────────────────┐
   ▼                   ▼                    ▼
            ┌─────────────────────────┐
            │       Human User         │
            └─────────────────────────┘
                       ▲
                       │ (input via Streamlit)
                       ▼
            ┌─────────────────────────┐
            │     UserProxyAgent      │
            │ (input & coordination)  │
            └─────────────────────────┘
                       ▲
                       │
                       ▼
            ┌─────────────────────────┐
            │   WeatherSoMTeam (SoM)  │
            │ (outer coordinator)     │
            └─────────────────────────┘
                       │
   ┌───────────────────┼────────────────────┐
   ▼                   ▼                    ▼
┌────────────────┐ ┌────────────────────┐ ┌────────────────────────┐
│ WeatherFetcher │ │ WeatherTrendAgent │ │ WeatherSummaryGenerator│
│ (fetches API) │ │ (analyzes forecast)│ │ (natural language sum) │
└────────────────┘ └────────────────────┘ └────────────────────────┘



---

## 🚀 Features

- 🔍 Real-time weather data + 5-day forecast
- 🧠 Multi-agent weather analysis using GPT-4o
- 📊 Detects weather trends (temperature, rain, etc.)
- 📝 Natural language summary with recommendations
- 🌐 Streamlit web UI
- ⚙️ Built with OpenAI Autogen

---

## 📦 Tech Stack

- [OpenWeatherMap API](https://openweathermap.org/api)
- [OpenAI GPT-4o](https://platform.openai.com/)
- [Autogen (OpenAI)](https://github.com/microsoft/autogen)
- [Streamlit](https://streamlit.io/)
- Python 3.9+

---

## 🛠️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/
cd weather-society-of-mind
2. Create and configure .env file
OPENAI_API_KEY=your_openai_api_key
WEATHER_API_KEY=your_openweather_api_key


✅ Get OpenWeatherMap API key: https://openweathermap.org/appid
✅ Get OpenAI key: https://platform.openai.com/account/api-keys

3. Install dependencies
pip install -r requirements.txt


If you don’t have a requirements.txt yet, here's a basic one:

openai
python-dotenv
requests
streamlit
autogen-agentchat
autogen-core

▶️ Run the App
streamlit run app.py


Then go to: http://localhost:8501

🧪 Example Use Case

Enter: London

Output:

Rain expected midweek.

Temperatures rising slightly.

Expect high humidity by Friday. ☔