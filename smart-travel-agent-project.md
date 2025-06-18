
# 🧠 Smart Travel Agent

An intelligent, AI-powered travel assistant built with [LangGraph](https://github.com/langchain-ai/langgraph), [LangChain](https://github.com/langchain-ai/langchain), and the [Model Context Protocol (MCP)](https://github.com/langchain-ai/langgraph/tree/main/libs/mcp). This assistant helps users plan short trips by fetching real-time weather, recommending activities, estimating travel costs, and returning a personalized trip summary—all orchestrated through a graph-based agent architecture.

---

## 🌟 Features

- 🗺️ **Weather Forecasting** — via a tool that fetches city weather (API or mock).
- 🎯 **Activity Recommendations** — suggests indoor or outdoor activities based on weather.
- 💸 **Cost Estimation** — provides travel + lodging cost estimates.
- 🤖 **LangGraph Agent** — uses `create_react_agent()` for tool reasoning and summarization.
- 🧰 **MCP Tools** — tools are modular, pluggable, and externally served using MCP protocol.
- 💬 **Chat Interface** — interact with the agent via a simple CLI loop.

---

## 🧠 Technologies Used

| Tech             | Purpose                                     |
|------------------|---------------------------------------------|
| LangGraph        | Agent state orchestration (via graphs)      |
| LangChain        | LLM and tool integration                    |
| MCP (Model Context Protocol) | External tool communication and discovery |
| Ollama / OpenAI  | Language model backend                      |
| Python 3.10+     | Backend runtime                             |

---

## 🗂 Project Structure

```
smart-travel-agent/
├── agent/
│   └── main_agent.py           # LangGraph agent setup and chat loop
├── tools/
│   ├── weather_tool.py         # MCP server wrapping weather API
│   ├── activity_tool.py        # Suggests activities based on weather
│   ├── cost_tool.py            # Basic math cost estimator
├── mcp_servers/
│   └── start_all.sh            # Shell script to launch all local MCP tools
├── .env                        # API keys (optional)
├── requirements.txt
└── README.md
```

---

## ⚙️ How It Works

1. **User Input**  
   - User types: "Plan a 3-day trip to Barcelona"

2. **Agent Workflow**
   - Calls `get_weather("Barcelona")`
   - Based on weather, calls `recommend_activities(weather)`
   - Then calls `estimate_cost(city="Barcelona", days=3)`
   - Finally uses the LLM to **summarize** the trip plan

3. **Output**
   ```
   Travel Assistant: Here's a 3-day plan for Barcelona...
   ```

---

## 🔧 MCP Tools Overview

| Tool Name              | Transport | Description                             |
|------------------------|-----------|-----------------------------------------|
| `get_weather(city)`    | HTTP/stdio | Fetches real or mock weather data       |
| `recommend_activities(weather)` | stdio | Suggests plans (e.g., beach, museum)   |
| `estimate_cost(city, days)` | stdio | Calculates rough travel + stay cost    |

---

## ✅ Setup Instructions

### 1. Clone the Project

```bash
git clone https://github.com/your-username/smart-travel-agent.git
cd smart-travel-agent
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Pull LLM (Optional - for local)

```bash
ollama pull mistral  # or llama3, phi3, etc.
```

### 4. Run MCP Servers

```bash
bash mcp_servers/start_all.sh
```

### 5. Start the Agent

```bash
python agent/main_agent.py
```

---

## 💬 Sample Interaction

```
================================= Smart Travel Agent =================================
Enter quit or exit to end the chat

Travel Assistant: Hello, I am your smart travel assistant. How can I help you?

You: Plan a 2-day trip to Tokyo

Travel Assistant: Sure! The weather looks sunny, so I suggest visiting Ueno Park and the Tokyo Skytree. The estimated cost is $520 USD.
```

---

## 🧩 Extensions & Ideas

- 🧳 Add a `generate_packing_list()` tool
- 🌍 Add translations for multilingual trip plans
- 🧠 Use LangGraph's conditional nodes to skip tools based on logic
- 🗃️ Connect to a hotel or flight database for real-time pricing

---

## 📜 License

This project is open-source and free to use under the MIT License.

---

## 🙌 Acknowledgments

- [LangGraph by LangChain](https://github.com/langchain-ai/langgraph)
- [Mistral.ai](https://mistral.ai)
- [Ollama](https://ollama.com)
