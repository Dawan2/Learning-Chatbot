# ChatBot

Welcome to the ChatBot project! This simple ChatBot is designed to engage in conversations and learn from user input. It uses a basic JSON data file to retrieve responses and can dynamically update its dataset based on user interactions.

## Features

- **Conversation Handling**: The ChatBot interacts with users through a console interface, providing responses based on pre-defined data.
- **Learning Capability**: If the ChatBot encounters an input it doesn't understand, it asks for clarification from the user and learns from the correct response.
- **Data Storage**: The bot's knowledge is stored in a JSON file ("data.json") that can be updated dynamically during conversations.

## How It Works

1. **Initialization:**
   - The script starts by loading a JSON file ("data.json") containing predefined responses.

2. **User Interaction:**
   - The ChatBot prompts the user for input and waits for responses.

3. **Response Retrieval:**
   - The input is processed, and the ChatBot looks for a matching response in its dataset.

4. **Handling Unknown Input:**
   - If the input is not recognized, the ChatBot attempts to find a close match in its dataset using the `get_closest_match` function from the `difflib` library.

5. **Learning from Users:**
   - If the ChatBot cannot find a suitable response, it asks the user for clarification and learns from the correct response.

6. **Data Update:**
   - The updated information is added to the dataset, and the JSON file is updated to include the new knowledge.

7. **Termination:**
   - The user can exit the conversation by typing 'quit.'

## Dependencies

- **colorama**: Used for colored console output.
- **difflib**: Utilized for finding close matches in the dataset.

## How to Use

1. **Install Dependencies:**
   - Make sure to install the required dependencies using `pip install colorama` and `pip install difflib`.

2. **Run the Script:**
   - Execute the script in your terminal or preferred Python environment:
     ```bash
     python chatbot.py
     ```

3. **Interact with the ChatBot:**
   - Engage in a conversation with the ChatBot by entering text responses.

4. **Quit the Conversation:**
   - To end the conversation, type 'quit.'

## Usage Example

Let's see how ChatBot handles a conversation:

```plaintext
You: Hello
ChatBot: Sorry, I am not sure how to respond to that. Can you help me understand?
You: Hi there!
ChatBot: Thank you! I will remember that next time.
You: Hello
ChatBot: Hi there!
