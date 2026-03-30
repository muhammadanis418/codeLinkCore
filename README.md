# CodeLink Core: AI-Agentic System for Java CoE

**CodeLink Core** is an advanced CLI-based AI Agentic System designed to assist the **Java Center of Excellence (CoE)**. It serves as an intelligent assistant that autonomously reasons and performs technical actions such as generating compliant Spring Boot configuration files while enforcing internal architectural best practices through RAG and Self-Reflection.

---

## 🚀 Project Vision
The goal is to speed up routine developer tasks by providing an agent that doesn't just "chat," but "acts." By integrating Groq with a Spring Boot microservice, the system demonstrates a real-world bridge between AI reasoning and Java enterprise development.

## 🛠️ Technology Stack

### AI Orchestration (Python Layer)
* **LLM:** Groq (Llama 3.3 70B)
* **Framework:** LangChain 0.3.0 (Modern Tool-Calling API)
* **Environment:** Python 3.12.3
* **Libraries:** `python-dotenv`, `requests`, `langchain-core`

### Backend Service (Java Layer)
* **Framework:** Spring Boot 4.0.5
* **Build Tool:** Maven
* **java:** 21
* **Communication:** REST API (JSON payload)
* **Default Port:** `8081`

---

## 🏗️ The Five Pillars (Capstone Requirements)

1. **RAG Pipeline & Reasoning**: The agent analyzes user requests against a `KNOWLEDGE_BASE` to fetch specific Java CoE standards (e.g., MongoDB ports, security audit requirements).
2. **Autonomous Tool-Calling**: Using the `create_tool_calling_agent` pattern, the agent decides when to fetch context and when to trigger the Spring Boot generator.
3. **Spring Boot Integration**: Implements a professional Tool-Calling mechanism where the AI interacts directly with a Java-based REST API to perform work.
4. **Self-Reflection & Evaluation**: After generating a file, the agent performs a mandatory "Reflection" step to verify the output meets the CoE's security compliance.
5. **Technical Sophistication**: Handles complex multistep workflows including contextualization, tool execution, and final validation summary.

---
## 🏗️ Project Architecture

The system follows a modular "Agentic" flow, bridging the Python AI Layer with the Java Enterprise Layer.

```mermaid
graph TD
    User((Developer)) -->|Input Query| Agent[CodeLink Core AI Agent]
    
    subgraph Python_AI_Layer [Python AI Layer]
        Agent -->|1. Reasoning| LLM[Groq]
        Agent -->|2. RAG Retrieval| KB[(Mock Knowledge Base)]
        Agent -->|4. Reflection| LLM
    end

    subgraph Java_Enterprise_Layer [Java Enterprise Layer]
        Agent -->|3. Tool Call: POST| SB[Spring Boot Microservice]
        SB -->|Generate Config| Logic[Config Generator Logic]
        Logic -->|Return .properties| SB
    end

    SB -->|HTTP 200| Agent
    Agent -->|5. Final Validated Response| User 
  ```

---

## 🚦 Installation & Setup

### 1. Spring Boot Backend
* Ensure your Spring Boot service is running on **Port 8081**.
* The endpoint `POST /api/v1/generator/config` must be available to accept `serviceName` and `database` parameters.

### 2. Python Agent Environment
1. **Create Virtual Environment**:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate

### 3. Run the Test Scenario
   Once both the Backend and Environment are ready, trigger the agent.

1. Run the main script:

2. What to look for in the logs:
```bash
* [Action]: The agent calling RetrieveJavaCoEContext.

* [Action]: The agent calling GenerateConfigFile '(Spring Boot)'.

* [Reflection]: The agent checking if 'spring.security.audit=true' exists in the output.
```

---

### 🤖 Agent in Action
<div align="center">
  <video src="https://github.com/user-attachments/assets/d017ac2b-34db-4fe7-9f00-096566f362ed" width="100%" controls autoplay muted loop>
  </video>
</div>