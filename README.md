# ✦ Agentic AI Replica (Offline Mode)

An interactive, purely offline replica of an **Agentic AI** demonstrating the **ReAct (Reasoning and Acting)** framework visually in the browser. 

This project was built to showcase the core concepts of Agentic AI—tool execution, autonomous looping, and intent routing—without relying on paid Large Language Model (LLM) APIs like OpenAI or Google Gemini.

---

## 🧠 What is Agentic AI?
Unlike traditional chatbot AI that simply writes a response based on its training data, an Agentic AI acts as a **Digital Worker**. Given a goal, it enters an autonomous loop:
1. **Thought:** "What do I need to do to achieve your goal?"
2. **Action:** Uses a provided tool (e.g., calculator, file reader, or web search).
3. **Observation:** Reviews the output of the tool.
4. **Repeat:** It analyzes the observation and takes subsequent actions until the final goal is achieved.

## 🚀 The No-API Natural Language Engine
True Agentic AIs require robust Neural Network Language Models to interpret user goals. 
Because this demo functions entirely offline, we engineered a **Generalized Natural Language Engine** directly into the frontend JavaScript. 

Instead of hard-coded keyword matching, this engine dynamically reads plain English to extract mathematical and contextual intents.

### Equipped Tools:
* `[calculator]`: Dynamically rips out and safely evaluates strict mathematical operations from user input or file data.
* `[read_file]`: Automatically fetches and parses local data (like `data.txt`).
* `[word_counter]`: A basic string utility to count words after extracting text via English natural-language boundaries.

---

## 💻 How to Run the Demo

This demonstration requires absolutely no server setup or dependencies. It runs strictly within your local environment.

1. Clone the repository.
   ```bash
   git clone https://github.com/Indrakaran1411/agentic-ai-demo.git
   ```
2. Open the directory. 
3. Double click **`index.html`** to open the Agentic AI directly in your web browser (Chrome recommended).

*(Note: A terminal-based python version `simple_agent.py` is also included in the repository for CLI interaction).*

---

## 🧪 Try These Master Prompts
Copy and paste these exact inputs into the web UI. Watch the Agent identify missing data, use tools sequentially, and build dynamic equations on the fly.

**Multi-Step Data Analysis:**
* _"Read the data file and find the average sales"_
* _"Give me the percentage of the last 2 months"_
* _"Show me the lowest value in the file"_

**Dynamic Natural Equation Parsing:**
* _"What is (450 * 12) / 3?"_
* _"What is 15% of 600?"_
* _"Calculate 400 multiplied by 5"_
* _"What is 2 to the power of 10?"_
* _"Calculate the square root of 1000"_

**Tool Utilization:**
* _"Count words in this sentence → The quick brown fox jumps over the lazy dog"_

---
_A fully autonomous workflow showcase designed from scratch._
