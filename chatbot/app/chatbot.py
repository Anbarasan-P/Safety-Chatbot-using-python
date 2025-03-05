import spacy
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer

# Load the spaCy English model
nlp = spacy.load("en_core_web_sm")

# Create a chatbot instance
chatbot = ChatBot('SafetyBot')

def train_chatbot():
    # Train with general English data
    trainer = ChatterBotCorpusTrainer(chatbot)
    trainer.train("chatterbot.corpus.english")

    # Train with custom safety-related data
    custom_data = [
        "What is PPE?",
        "PPE stands for Personal Protective Equipment, such as helmets, gloves, and safety goggles.",
        "What should I do in case of fire?",
        "In case of fire, use fire extinguishers, follow evacuation routes, and avoid elevators.",
        "What are the safety measures for machinery?",
        "Ensure machines are properly guarded and follow lockout-tagout procedures during maintenance."
    ]

    trainer = ListTrainer(chatbot)
    trainer.train(custom_data)

def get_chatbot_response(user_input):
    # Process user input with spaCy
    doc = nlp(user_input)

    # Extract intents and entities
    intent = None
    entities = []

    # Check for specific keywords in the user input
    for token in doc:
        if token.text.lower() in ["ppe", "personal protective equipment"]:
            intent = "ppe"
        elif token.text.lower() in ["fire", "emergency"]:
            intent = "fire"
        elif token.text.lower() in ["machinery", "machine", "equipment"]:
            intent = "machinery"

    # Generate response based on intent
    if intent == "ppe":
        return "PPE stands for Personal Protective Equipment, such as helmets, gloves, and safety goggles."
    elif intent == "fire":
        return "In case of fire, use fire extinguishers, follow evacuation routes, and avoid elevators."
    elif intent == "machinery":
        return "Ensure machines are properly guarded and follow lockout-tagout procedures during maintenance."
    else:
        # Use the chatbot's default response
        return str(chatbot.get_response(user_input))