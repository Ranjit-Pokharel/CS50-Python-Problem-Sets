# ConvAI

#### Video Demo: [Link to Youtube Video](https://youtu.be/A-umfYKxYn8)

#### Description:  
This project is an **AI Conversational Assistant** short for  **ConvAI** built in Python that 
interacts with users in a conversational format. It supports saving and loading conversation history, 
custom system-level AI configurations, and real-time emoji conversion while typing inputs.

The project uses the **Ollama AI model** for generating responses and provides a seamless experience with 
features like **clearing the screen and limited customizable settings**. 
Below are the key details of the project.

---

### Features:
1. **AI-Powered Conversations**:
   - Communicates with users using the Ollama AI model.
   - Stores and retrieves conversation history from a JSON file.

2. **System-Level Customization**:
   - Allows configuration of system prompts to guide the AI's behavior.

3. **Real-Time Emoji Conversion**:
   - Converts text to emojis in real-time while the user types their input.

4. **Persistent Memory**:
   - Saves conversations in a JSON file and reloads them when restarted.

5. **Clear Screen Functionality**:
   - Clears the terminal to provide a clutter-free interface.

---

### Design Choices:
1. **Why Ollama AI?**
   - Ollama offers robust conversational capabilities suitable for AI-powered projects.

2. **Why JSON for Memory?**
   - JSON provides a lightweight and human-readable format for saving and retrieving conversation data.
   - JSON can also be use in future for fine tunning ai model.

3. **Real-Time Emoji Conversion**:
   - Adds a fun and engaging element to user interactions.

4. **Use of `prompt_toolkit`**:
   - Enables advanced interactive prompts, enhancing user experience.

---

### How to Run:
1. Install all dependencies:
    ```bash
    pip install -r requirements.txt
    ```
2. Run the program:
    ```bash
    python project.py
    ```

### Known Issues:
- only tested in Linux base system.
- Missing Dependencies: ollma (visit webside [ollama](https://ollama.com/) to setup **ollama**)

