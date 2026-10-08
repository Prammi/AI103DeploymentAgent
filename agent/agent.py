import os

from dotenv import load_dotenv
from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import PromptAgentDefinition
from azure.identity import DefaultAzureCredential

load_dotenv()

PROJECT_ENDPOINT = os.environ["PROJECT_ENDPOINT"]
MODEL_DEPLOYMENT_NAME = os.environ["MODEL_DEPLOYMENT_NAME"]

project = AIProjectClient(
    endpoint=PROJECT_ENDPOINT,
    credential=DefaultAzureCredential(),
)

agent = project.agents.create_version(
    agent_name="ai103-g1-cicd-agent",
    definition=PromptAgentDefinition(
        model=MODEL_DEPLOYMENT_NAME,
        instructions=(
            "You are a simple helpful assistant. "
            "Answer questions clearly and concisely."
        ),
    ),
)

print("Agent created successfully.")
print(f"Agent ID: {agent.id}")
print(f"Agent name: {agent.name}")
print(f"Agent version: {agent.version}")