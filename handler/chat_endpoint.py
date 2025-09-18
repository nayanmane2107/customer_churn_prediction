from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM

model = OllamaLLM(model="llama3.1:8b")

def generate_retention_email(churn_prediction: bool) -> str:
    """Generate a personalized customer retention email based on churn prediction."""

    global model

    template = """You are an assistant that generates company customer retention emails. 
    Always follow company's tone of voice and structure guidelines.

    Tone of Voice:
    - Friendly and approachable: warm, conversational, avoid jargon
    - Clear and concise: short sentences, easy to read, bullet points where possible
    - Positive and reassuring: highlight benefits, address concerns empathetically
    - Professional and trustworthy: accurate, respectful, reliable

    Email Structure:
    1. Subject line: Friendly, enticing, personalized
    2. Greeting: Warm, include customer's first name
    3. Introduction: Short, thank the customer or explain the purpose
    4. Body: Highlight offers, benefits, or service improvements
    - Use bullet points for clarity
    - Personalize based on customer details (contract, tenure, services, etc.)
    5. Call to Action: Clear and compelling
    6. Closing: Warm and appreciative
    7. Signature: Professional but friendly (e.g., company Customer Care Team)

    Input:
    - will churn: {churn_prediction} (1 for yes, 0 for no)

    Task:
    Generate a personalized customer retention email following company tone of voice and structure.
    Keep it under 200 words. Ensure consistency and professionalism."""

    prompt = ChatPromptTemplate.from_template(template)

    chain = prompt | model

    results = chain.invoke({"churn_prediction": churn_prediction})

    return results