# Project 1: Rule-Based AI Chatbot
# Decode Labs | AI Intern | Mostafa Nassar

# ── KNOWLEDGE BASE (dictionary = O(1) lookup) ──────────────────
responses = {
    "hello":        "Hey there! I'm DecodBot. How can I help you today?",
    "hi":           "Hi! Welcome to DecodeLabs. What can I do for you?",
    "hey":          "Hey! Great to see you. Ask me anything.",
    "bye":          "Goodbye! Keep building and keep learning. 🚀",
    "goodbye":      "See you later! Don't forget to push your code to GitHub.",
    "how are you":  "I'm just a rule-based bot, but I'm running perfectly!",
    "what is ai":   "AI is the simulation of human intelligence by machines using logic, data, and algorithms.",
    "who made you": "I was built by Mostafa Nassar as Project 1 of the DecodeLabs AI Internship.",
    "help":         "I can answer: hello, how are you, what is ai, who made you, and more. Type 'exit' to quit.",
    "thanks":       "You're welcome! Happy to help.",
    "thank you":    "Anytime! That's what I'm here for.",
}

# ── CHATBOT ENGINE ──────────────────────────────────────────────
print("=" * 50)
print("   DecodBot — Rule-Based AI Chatbot")
print("   Type 'exit' to quit.")
print("=" * 50)

while True:
    # PHASE 1: Input & Sanitization
    raw_input_text = input("\nYou: ")
    clean_input = raw_input_text.lower().strip()

    # EXIT STRATEGY: Kill command
    if clean_input in ("exit", "quit", "bye"):
        print("Bot: Goodbye! See you in Project 2. 👋")
        break

    # PHASE 2 & 3: Intent Matching + Response Generation (O(1))
    reply = responses.get(clean_input, "I don't understand that yet. Try asking 'help'.")
    print(f"Bot: {reply}")