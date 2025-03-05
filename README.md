# Industrial Safety Chatbot

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Flask](https://img.shields.io/badge/Flask-2.0%2B-green)
![ChatterBot](https://img.shields.io/badge/ChatterBot-1.0.8-yellow)
![spaCy](https://img.shields.io/badge/spaCy-3.0%2B-orange)

A simple chatbot that provides industrial safety measures and precautions to laborers (end-users). The chatbot uses **Natural Language Processing (NLP)** to understand user queries and respond with relevant safety information.

---

## **Features**

- **Safety Information**: Provides safety measures for fire, machinery, PPE, and more.
- **NLP Integration**: Uses `spaCy` for intent recognition and entity extraction.
- **User-Friendly Interface**: Simple web-based interface built with Flask.
- **Customizable**: Easily extendable with additional safety topics.

---

## **Technologies Used**

- **Python**: Core programming language.
- **Flask**: Web framework for the chatbot interface.
- **ChatterBot**: Library for building the chatbot.
- **spaCy**: NLP library for intent recognition and entity extraction.
- **HTML/CSS/JavaScript**: Front-end for the chatbot interface.

---

## **Installation**

Follow these steps to set up the project locally:

1. **Clone the repository**:
   ```bash
   https://github.com/Anbarasan-P/Safety-Chatbot-using-python.git
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
3.**Download spaCy model**:
   ```bash
    python -m spacy download en_core_web_sm
