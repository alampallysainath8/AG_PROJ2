import asyncio
import os
import requests
from dotenv import load_dotenv
from autogen_agentchat.agents import AssistantAgent, SocietyOfMindAgent, UserProxyAgent
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_agentchat.conditions import TextMentionTermination
from autogen_agentchat.ui import Console
from autogen_core.tools import FunctionTool

# Load environment variables
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
weather_api_key = os.getenv("WEATHER_API_KEY")

if not openai_api_key or not weather_api_key:
    raise ValueError("Set both OPENAI_API_KEY and WEATHER_API_KEY in your .env file.")

# OpenAI Client
model_client = OpenAIChatCompletionClient(model="gpt-4o", api_key=openai_api_key)

# =========== TOOL: Fetch Weather Data ==============

async def fetch_weather_data(city: str) -> dict:
    """
    Fetch current weather and 5-day forecast for a given city using OpenWeatherMap API
    """
    base_url = "http://api.openweathermap.org/data/2.5"
    
    current_url = f"{base_url}/weather?q={city}&appid={weather_api_key}&units=metric"
    forecast_url = f"{base_url}/forecast?q={city}&appid={weather_api_key}&units=metric"

    current_response = requests.get(current_url).json()
    forecast_response = requests.get(forecast_url).json()

    if current_response.get("cod") != 200:
        return {"error": current_response.get("message", "City not found")}

    return {
        "city": city,
        "current": current_response,
        "forecast": forecast_response
    }

weather_tool = FunctionTool(fetch_weather_data, description="Fetch current weather and 5-day forecast for a city")

# =========== Inner Team Agents ============

# Agent that fetches weather data
data_fetcher = AssistantAgent(
    name="WeatherDataFetcher",
    model_client=model_client,
    system_message="You are a weather data fetcher. Use the tool to get current and forecast weather for a city.",
    tools=[weather_tool]
)

# Agent that analyzes trends
trend_analyzer = AssistantAgent(
    name="WeatherTrendAnalyzer",
    model_client=model_client,
    system_message="You analyze the forecast data and identify temperature or weather condition trends over the next 5 days."
)

# Agent that summarizes weather
summary_generator = AssistantAgent(
    name="WeatherSummaryGenerator",
    model_client=model_client,
    system_message="You summarize the weather trends in human-friendly language with recommendations if needed (e.g., carry umbrella, expect heatwave)."
)

# Inner team as Society of Mind
inner_team = RoundRobinGroupChat(
    [data_fetcher, trend_analyzer, summary_generator],
    max_turns=3
)

society_of_mind = SocietyOfMindAgent(
    name="WeatherSoMTeam",
    model_client=model_client,
    team=inner_team,
    instruction="Coordinate with internal team to fetch and analyze weather data for a given city."
)

# ========== Outer Team =============

# User Proxy Agent (for optional approval)
user_proxy = UserProxyAgent(
    name="UserProxy",
    description="Represents the human user. Confirm or provide inputs when asked.",
    input_func=input
)

team = RoundRobinGroupChat([society_of_mind, user_proxy], max_turns=4)

# ========== Main Function ==========

async def main():
    print("🌤️ Starting Weather Analysis...")

    city = input("Enter city name: ").strip()
    task_message = f"Get current weather and 5-day trend for {city} and summarize it."
    print(f"🔍 Task: {task_message}")
    
    stream = team.run_stream(task=task_message)

    print("Please wait while agents fetch and analyze the weather data...")
    await Console(stream)

if __name__ == "__main__":
    asyncio.run(main())
