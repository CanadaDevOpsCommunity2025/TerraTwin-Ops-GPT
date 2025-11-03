# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from google.adk import Agent
from google.adk.a2a.utils.agent_to_a2a import to_a2a
from google.genai import types
from a2a.types import AgentCard

root_agent = Agent(
    model="gemini-2.5-flash",
    name="analyst_agent",
    description="Explains GitHub repositories for analysts",
    instruction="""
You are a Terraform explainer agent. Your purpose is to explain terraform code in a business friendly language.
you should also explain Terraform concepts and CLI commands
""",
    generate_content_config=types.GenerateContentConfig(
        safety_settings=[
            types.SafetySetting(
                category=types.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
                threshold=types.HarmBlockThreshold.OFF,
            ),
        ]
    ),
)

my_agent_card = AgentCard(
    name="analyst_agent",
    url="https://analyst-agent-535350394773.us-central1.run.app",
    description="Explains GitHub repositories for analysts",
    version="1.0.0",
    capabilities={},
    skills=[],
    defaultInputModes=["text/plain"],
    defaultOutputModes=["text/plain"],
    supportsAuthenticatedExtendedCard=False
)


a2a_app = to_a2a(root_agent, host="localhost", port=8080, agent_card=my_agent_card)