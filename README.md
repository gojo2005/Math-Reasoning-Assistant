# 🧮 Math Reasoning Assistant

A Streamlit application built using **LangChain** and **Groq (Gemma2-9B-It)** that acts as an AI-powered math and reasoning assistant. Ask it a math problem or a logic-based question, and it will reason through it step by step to give you a clear, detailed answer.

---

## ✨ Features

- 🔢 Solves mathematical problems step by step
- 🧠 Performs logical and reasoning-based problem solving
- 📚 Retrieves factual information from Wikipedia
- 🤖 Uses LangChain Agents to automatically choose the appropriate tool
- 💬 Interactive chat interface built with Streamlit
- ⚡ Supports real-time reasoning and calculations

---

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)
![Groq](https://img.shields.io/badge/Groq-F55036?style=for-the-badge&logo=groq&logoColor=white)

- **Python**
- **Streamlit**
- **LangChain**
- **LangChain Community**
- **LangChain Groq**
- **Wikipedia API**
- **LLMMathChain**
- **Prompt Engineering**

---

## 📁 Project Structure

```
Math-Reasoning-Assistant/
├── app.py                # Main Streamlit application - handles UI and agent logic
├── requirements.txt       # Python dependencies required to run the project
└── README.md               # Project documentation
```

- **`app.py`** – Sets up the Streamlit chat interface, initializes the LangChain agent with the Groq LLM, and connects tools like `LLMMathChain` and the Wikipedia API so the agent can decide which tool to use for a given question.
- **`requirements.txt`** – Lists all the Python packages needed to run the app.

---

## ⚙️ Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd Math-Reasoning-Assistant
```

2. Install the dependencies:

```bash
pip install -r requirements.txt
```

3. Run the application:

```bash
streamlit run app.py
```

---

## 🚀 Usage

1. **Enter your Groq API key** in the sidebar when the app launches.
2. **Ask a math or reasoning question** in the chat input box.
3. **Receive a detailed, step-by-step AI-generated answer** in the chat window.

---

## 💡 Example Questions

Try asking the assistant things like:

1. "What is the sum of the first 20 prime numbers?"
2. "If a train travels 60 km/h for 2.5 hours, how far does it go?"
3. "I have 5 apples, I give away 2, and buy 7 more. How many do I have now?"
4. "Who invented the telephone, and in what year?"
5. "A rectangle has a length of 12 cm and a width of 5 cm. What is its area and perimeter?"

---

## 📸 Screenshots

<!-- Add screenshots of your app below -->

<img width="1636" height="818" alt="Screenshot 2026-08-07 011858" src="https://github.com/user-attachments/assets/70dba7b4-e9c3-4610-829d-3ef81f94c47a" />



---

## 🔮 Future Improvements

- 🧵 Conversation memory for follow-up questions
- 🌐 Web search integration
- 📄 PDF question answering
- 🎙️ Voice input support
- 📷 Image-based math solving
- 🔀 Multiple LLM support

---

## 👤 Author

**Prithviraj Mukhiya**

- 🎓 Final-year B.Tech (ECE) student at IIIT Kota
- 🚀 Aspiring Data Scientist and AI/ML Engineer
- 🛠️ Skilled in Machine Learning, Deep Learning, NLP, Computer Vision, Generative AI, LangChain, and MLOps
- 💡 Passionate about building practical AI applications and open-source projects
- 🔗 GitHub: [gojo2005](https://github.com/gojo2005)
- 💼 LinkedIn: [Add your LinkedIn URL here](https://linkedin.com/in/your-profile)
