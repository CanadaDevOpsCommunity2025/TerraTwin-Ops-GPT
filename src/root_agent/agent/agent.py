import os
from google.adk.agents.remote_a2a_agent import AGENT_CARD_WELL_KNOWN_PATH
from google.adk.agents.remote_a2a_agent import RemoteA2aAgent
from google.adk.agents.llm_agent import Agent
from google.genai import types

# Load Cloud Run base URL from environment variable
ANALYST_AGENT_CARD_BASE_URL = os.getenv("ANALYST_AGENT_CARD_BASE_URL")
DEVELOPER_AGENT_CARD_BASE_URL = os.getenv("DEVELOPER_AGENT_CARD_BASE_URL")

if not ANALYST_AGENT_CARD_BASE_URL:
    raise ValueError("Missing required environment variable: AGENT_CARD_BASE_URL")

if not DEVELOPER_AGENT_CARD_BASE_URL:
    raise ValueError("Missing required environment variable: AGENT_CARD_BASE_URL")

# Construct full agent card URL
analyst_agent_card_url = f"{ANALYST_AGENT_CARD_BASE_URL.rstrip('/')}/{AGENT_CARD_WELL_KNOWN_PATH}"
developer_agent_card_url = f"{DEVELOPER_AGENT_CARD_BASE_URL.rstrip('/')}/{AGENT_CARD_WELL_KNOWN_PATH}"

analyst_agent = RemoteA2aAgent(
    name="analyst_agent",
    description="Helpful Git assistant that can crawl your code repo and provide insights.",
    agent_card=analyst_agent_card_url,
)

developer_agent = RemoteA2aAgent(
    name="developer_agent",
    description="A Helpful agent that can answer terraform questions from a technical perspective",
    agent_card=developer_agent_card_url,
)

root_agent = Agent(
    model="gemini-2.0-flash",
    name="root_agent",
    instruction="""
      You are a helpful assistant answer questions about terraform in general, and about particular terraform code in Github repositories
      You delegate 
      Follow these steps:
      1. If the user asks for explaining code, or general questions about terraform, use analyst_agent
      2. If the user asks for help with writing terraform code, use the developer_agent
      Always clarify the results before proceeding.
    """,
    global_instruction=(
        "You are a Bot call TerraTwin, your purpose is to explain terraform code to a variety of audiences and help them write production grade terraform code"
    ),
    sub_agents=[analyst_agent, developer_agent],
    generate_content_config=types.GenerateContentConfig(
        safety_settings=[
            types.SafetySetting(  # avoid false alarm about rolling dice.
                category=types.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
                threshold=types.HarmBlockThreshold.OFF,
            ),
        ]
    ),
)
