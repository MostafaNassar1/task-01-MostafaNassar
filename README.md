# 🤖 Project 1: Rule-Based AI Chatbot

**Author:** Mostafa Nassar
**Organization:** DecodeLabs AI Internship
**Project:** Project 1 – Rule-Based AI Chatbot

## 📌 Project Overview

This project is a simple **Rule-Based AI Chatbot** developed in Python. The chatbot interacts with users by responding to predefined questions and commands using a dictionary-based knowledge base.

The purpose of this project is to understand the fundamentals of Artificial Intelligence, including:

* User input handling
* Intent matching
* Response generation
* Rule-based decision making
* Basic Natural Language Processing concepts

## 🚀 Features

* Greets users with different welcome messages.
* Answers basic questions such as:

  * What is AI?
  * Who made the chatbot?
  * How are you?
* Provides a help menu.
* Responds to gratitude messages.
* Handles unknown questions gracefully.
* Allows users to exit the chatbot using:

  * `exit`
  * `quit`
  * `bye`

## 🧠 How It Works

The chatbot stores all predefined questions and responses inside a Python dictionary called `responses`.

1. The user enters a message.
2. The input is converted to lowercase and cleaned using `.lower()` and `.strip()`.
3. The program searches for the user's input in the dictionary.
4. If a match is found, the corresponding response is displayed.
5. Otherwise, the chatbot returns a default message indicating that it does not understand the request.

Dictionary lookups in Python have an average time complexity of **O(1)**, making the chatbot efficient for predefined responses.

## 🛠 Technologies Used

* Python 3
* Dictionaries
* Loops
* Conditional Statements
* String Manipulation

## 📂 Project Structure

```text
Project1_RuleBasedChatbot/
│
├── chatbot.py
└── README.md
```

## ▶️ How to Run

1. Install Python 3 on your computer.
2. Download or clone the project.
3. Open a terminal in the project folder.
4. Run the following command:

```bash
python chatbot.py
```

## 💬 Example Conversation

```text
You: hello
Bot: Hey there! I'm DecodBot. How can I help you today?

You: what is ai
Bot: AI is the simulation of human intelligence by machines using logic, data, and algorithms.

You: thanks
Bot: You're welcome! Happy to help.

You: exit
Bot: Goodbye! See you in Project 2.
```

## 🎯 Learning Outcomes

By completing this project, I learned how to:

* Build a rule-based conversational system.
* Use dictionaries for efficient data retrieval.
* Process and sanitize user input.
* Implement intent matching and response generation.
* Design the foundation of an AI chatbot.

## 📜 Conclusion

This project serves as an introduction to conversational AI and demonstrates how simple rule-based systems can simulate human interaction. It provides a strong foundation for building more advanced AI applications such as intelligent assistants and machine learning-based chatbots in future projects.
