import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.tools import Tool
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_community.callbacks.streamlit import StreamlitCallbackHandler
from langchain_experimental.tools import PythonAstREPLTool
from langchain_classic.chains import LLMChain
from langchain_classic.agents import initialize_agent, AgentType

## Streamlit UI Setup
st.set_page_config(page_title="Universal Math & Logic Assistant", page_icon="🧮")
st.title("🧮 Universal Math Problem Solver")

groq_api_key = st.sidebar.text_input(label="Groq API Key", type="password")

if not groq_api_key:
    st.info("Please add your Groq API key to continue")
    st.stop()

## High-capability model for math reasoning
llm = ChatGroq(model="llama-3.3-70b-versatile", groq_api_key=groq_api_key, temperature=0)

## 1. Python REPL Tool (Handles ALL Math: Algebra, Calculus, Statistics, Equations)
python_tool = PythonAstREPLTool()
python_tool.name = "Python_Math_Solver"
python_tool.description = (
    "A tool for solving ANY mathematical question by executing Python code. "
    "Use this for algebra, solving equations, calculus, matrices, geometry, and complex arithmetic. "
    "You can import standard libraries like 'sympy', 'math', and 'numpy' inside your code."
)

## 2. Wikipedia Search Tool (For definitions, constants, physics/math facts)
wikipedia_wrapper = WikipediaAPIWrapper()
wikipedia_tool = Tool(
    name="Wikipedia",
    func=wikipedia_wrapper.run,
    description="A tool for looking up real-world information, formulas, and math definitions."
)

## 3. Step-by-Step Reasoning Tool
reasoning_prompt = PromptTemplate(
    input_variables=["question"],
    template=(
        "You are an expert mathematician. Work through the following mathematical question "
        "step-by-step, showing all formulas, derivations, and explanations clearly.\n\n"
        "Question: {question}\n\n"
        "Detailed Solution:"
    )
)
reasoning_chain = LLMChain(llm=llm, prompt=reasoning_prompt)
reasoning_tool = Tool(
    name="Reasoning_Tool",
    func=reasoning_chain.run,
    description="A tool for explaining math concepts step-by-step or breaking down word problems logically."
)

## Initialize the Agent with universal tools
assistant_agent = initialize_agent(
    tools=[python_tool, wikipedia_tool, reasoning_tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=False,
    handle_parsing_errors=True
)

if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "Hi! I can solve any math question—from arithmetic and word problems to quadratic equations, calculus, and linear algebra."}
    ]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg['content'])

## Interaction handling
question = st.text_area(
    "Enter your math question:",
    "Solve the equation x^2 - 5x + 6 = 0 and explain the roots."
)

if st.button("Solve Problem"):
    if question.strip():
        with st.spinner("Solving problem..."):
            st.session_state.messages.append({"role": "user", "content": question})
            st.chat_message("user").write(question)

            st_cb = StreamlitCallbackHandler(st.container(), expand_new_thoughts=False)
            
            response = assistant_agent.invoke(
                {"input": question},
                config={"callbacks": [st_cb]}
            )
            
            output_text = response["output"]
            st.session_state.messages.append({'role': 'assistant', "content": output_text})
            st.write('### Solution:')
            st.success(output_text)
    else:
        st.warning("Please enter a question.")