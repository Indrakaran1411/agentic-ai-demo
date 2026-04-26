import re
import os
import time

class SimpleAgent:
    def __init__(self):
        # 1. Define the tools our agent is allowed to use.
        self.tools = {
            "calculator": self.calculator_tool,
            "word_counter": self.word_counter_tool,
            "read_file": self.read_file_tool
        }
        
    def calculator_tool(self, expression):
        """A simple tool to evaluate math expressions."""
        try:
            return str(eval(expression))
        except Exception as e:
            return f"Error: {e}"

    def word_counter_tool(self, text):
        """A simple tool to count words in a text block."""
        return str(len(text.split()))

    def read_file_tool(self, filepath):
        """A simple tool to read data from a local file."""
        try:
            base_dir = os.path.dirname(os.path.abspath(__file__))
            full_path = os.path.join(base_dir, filepath)
            with open(full_path, 'r') as f:
                return f.read().strip()
        except FileNotFoundError:
            return f"Error: File '{filepath}' not found."
        except Exception as e:
            return f"Error reading file: {e}"

    def think_and_act(self, goal):
        print(f"\n🎯 [GOAL RECEIVED]: {goal}\n")
        time.sleep(1) # Artificial delay for dramatic effect in demo
        
        step = 1
        observation = ""
        
        # 2. THE MULTI-STEP AGENTIC LOOP
        while True:
            print(f"--- Step {step} ---")
            time.sleep(0.5)
            
            # --- THOUGHT PROCESS ---
            thought, action_name, action_input = self.simulated_brain(goal, observation)
            print(f"🤔 THOUGHT: {thought}")
            time.sleep(1)
            
            # If finished, break out of loop
            if action_name == "FINISH":
                print(f"✅ FINAL ANSWER: {action_input}")
                break
                
            print(f"🛠️  ACTION: Using tool '{action_name}' with input '{action_input}'...")
            time.sleep(1.5) # Look like it's taking time to "work"
            
            # --- ACTION & OBSERVATION ---
            tool_function = self.tools.get(action_name)
            if tool_function:
                observation = tool_function(action_input)
                print(f"👀 OBSERVATION: The tool returned -> \n{observation}\n")
            else:
                observation = f"Tool {action_name} not found."
                print(f"👀 OBSERVATION: {observation}\n")
                
            time.sleep(1)
            step += 1
            if step > 5:
                print("Too many steps. Quitting to prevent infinite loop.")
                break

    def simulated_brain(self, goal, previous_observation):
        """
        Our "Simulated Brain" without using an API.
        """
        goal_lower = goal.lower()
        
        if previous_observation.replace('.', '').replace('-', '').isdigit() or "Error" in previous_observation:
            return "I have the final calculated result.", "FINISH", previous_observation
            
        if "sales:" in previous_observation.lower() and ("total" in goal_lower or "sum" in goal_lower or "calculate" in goal_lower):
            numbers = re.findall(r'\d+', previous_observation)
            if len(numbers) >= 2:
                expression = f"{numbers[0]} + {numbers[1]}"
                return f"I see the sales numbers in the file. Now I will use the calculator to add {expression}.", "calculator", expression

        if ("data.txt" in goal_lower or "file" in goal_lower) and previous_observation == "":
             return "I need to read the data from 'data.txt' before I can do anything.", "read_file", "data.txt"

        if "calculate" in goal_lower or "+" in goal_lower or "*" in goal_lower:
            match = re.search(r'[\d\+\-\*\/\s\.]+', goal_lower)
            if match:
                expression = match.group(0).strip()
                return f"I need to solve a math problem. I will use my calculator.", "calculator", expression
                
        if "word count" in goal_lower or "count" in goal_lower:
            if ":" in goal:
                text = goal.split(":", 1)[1].strip()
            else:
                text = goal_lower.replace("count words in", "").strip()
            return f"I need to count the words. I will use the word_counter tool.", "word_counter", text
        
        return "I do not understand the goal.", "FINISH", "I'm sorry, I cannot do that yet."

if __name__ == "__main__":
    print("\n" + "="*55)
    print("🤖 AGENTIC AI LIVE DEMO MODE STARTED")
    print("="*55)
    print("Available tools: [calculator], [read_file], [word_counter]")
    print("(Type 'exit' to quit)\n")
    
    agent = SimpleAgent()
    
    # Interactive chat loop for demonstration
    while True:
        try:
            user_input = input("👤 YOU -> ")
            if user_input.lower() in ['exit', 'quit']:
                print("Goodbye!")
                break
            if not user_input.strip():
                continue
            
            agent.think_and_act(user_input)
            print("-" * 55 + "\n")
            
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break

