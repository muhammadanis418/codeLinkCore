import os

import requests
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, ToolMessage, SystemMessage
from langchain_core.tools import tool
from langchain_groq import ChatGroq

# 1. Setup Environment
load_dotenv()
groq_key = os.getenv("GROQ_API_KEY")

# 2. Define Tools (Using strict lowercase names for Gemini compatibility)
@tool("retrieve_coe_context")
def retrieve_coe_context(query: str) -> str:
    """Consults the Java CoE Knowledge Base for standards, ports, and security requirements."""
    standards = {
        "mongodb": "Standard Port: 27017. Required: spring.security.audit=true",
        "mysql": "Standard Port: 3306. Required: spring.security.audit=true",
        "postgresql": "Standard Port: 5432. Required: spring.security.audit=true"
    }
    # Case-insensitive lookup
    for key in standards:
        if key in query.lower():
            return standards[key]
    return "Standard Java CoE compliance: port 8081, audit=true."

@tool("generate_config_file")
def generate_config_file(service_name: str, database: str) -> str:
    """Calls the Spring Boot REST API to generate a .properties configuration file."""
    url = "http://localhost:8081/api/v1/generator/config"
    payload = {"serviceName": service_name, "database": database}
    try:
        response = requests.post(url, json=payload, timeout=10)
        if response.status_code == 200:
            return response.text
        return f"Backend Error: {response.status_code}"
    except Exception as e:
        return f"Connection Failed: {str(e)}"

# 3. Initialize stable LLM
# Using gemini-2.5-flash-lite as it is currently the most stable for tool-calling chains
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    groq_api_key=groq_key,
    temperature=0
).bind_tools([retrieve_coe_context, generate_config_file])

def run_agent():
    print("\n" + "="*50)
    print("🚀 CODELINK CORE: INTERACTIVE AGENT ONLINE")
    print("Type 'exit' to quit.")
    print("="*50)

    # Simple manual conversation loop to prevent metadata 'Name' errors
messages = [
    SystemMessage(content="""You are CodeLink Core, an expert Java CoE Agent. 
    Your strict workflow:
    1. RETRIEVE context first.
    2. ACT by generating the file.
    3. MANDATORY: You must print the FULL content of the generated application.properties file in your final response. 
    4. VERIFY: Confirm that 'spring.security.audit=true' is present in the text you just printed.""")
]

while True:
        user_input = input("\n[USER]: ")
        if user_input.lower() in ["exit", "quit", "q"]:
            break

        messages.append(HumanMessage(content=user_input))

        try:
            # 🧠 First AI Thought & Tool Call
            response = llm.invoke(messages)
            messages.append(response)

            # 🛠️ If the AI wants to use tools, handle them manually (Ensures non-empty names)
            while response.tool_calls:
                for tool_call in response.tool_calls:
                    # Map tool name to function
                    tool_name = tool_call["name"]
                    selected_tool = {"retrieve_coe_context": retrieve_coe_context, "generate_config_file": generate_config_file}[tool_name]

                    # Execute tool
                    print(f"  [LOG]: Invoking {tool_name}...")
                    observation = selected_tool.invoke(tool_call["args"])

                    # Create ToolMessage (This part fixes the 'Name cannot be empty' error)
                    messages.append(ToolMessage(
                        content=str(observation),
                        tool_call_id=tool_call["id"],
                        name=tool_name # Explicitly passing the name back
                    ))

                # Get the next response after tool outputs
                response = llm.invoke(messages)
                messages.append(response)

            print(f"\n[AGENT]: {response.content}")

        except Exception as e:
            print(f"❌ Error: {e}")
            # Reset conversation on error to clear bad state
            messages = [messages[0]]

if __name__ == "__main__":
    run_agent()