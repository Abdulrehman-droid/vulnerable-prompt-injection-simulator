

import gradio as gr
from groq import Groq
import os

# ============================================
# GROQ API
# ============================================

# Retrieve GROQ_API_KEY from environment variables
# It's good practice to get API keys from secure environment variables
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

client = Groq(api_key=GROQ_API_KEY)

# ============================================
# AI FUNCTION
# ============================================

def inject_vulnerability(safe_code):
    '''Uses the Groq API to inject a vulnerability into the provided safe code.'''
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "You are an AI assistant specialized in identifying and injecting security vulnerabilities into Python code. Your goal is to take 'safe' Python code and modify it to include a specific, common vulnerability, explaining the vulnerability and how to exploit it. Focus on one vulnerability type at a time unless explicitly asked for more. Respond only with the vulnerable code and a brief explanation."
                },
                {
                    "role": "user",
                    "content": f'''Inject a common and exploitable vulnerability into the following Python code. Explain the vulnerability you introduced and how it can be exploited. Focus on vulnerabilities like SQL injection, XSS (if applicable), insecure deserialization, command injection, path traversal, or insecure direct object references. Provide only the vulnerable code block, followed by an explanation of the vulnerability and its exploitation.

```python
{safe_code}
```'''
                }
            ],
            model="llama3-8b-8192",  # Using a suitable LLM model
            temperature=0.7,
            max_tokens=1024,
            top_p=1,
            stop=None,
            stream=False
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        return f"An error occurred during AI generation: {e}"

# ============================================
# UI
# ============================================

with gr.Blocks() as demo:

    # --------------------------------------------
    # TITLE
    # --------------------------------------------

    gr.Markdown("# 🛡️ Vulnerable Prompt Injection - Simulator")

    gr.Markdown(
        '''AI-powered vulnerability injection simulator using LLM model Llama.

**Disclaimer:** This tool is for educational purposes only. Do not use for malicious activities.'''
    )

    # --------------------------------------------
    # MAIN LAYOUT
    # --------------------------------------------

    with gr.Row():

        # ----------------------------------------
        # LEFT SIDE
        # ----------------------------------------

        with gr.Column(scale=2):

            code_input = gr.Code(
                label="Enter Safe Code",
                language="python",
                lines=20,
                value='''
def login(username, password):
    users = {"admin": "admin123", "user": "pass123"}
    if username in users and users[username] == password:
        return "Login successful"
    else:
        return "Invalid credentials"
'''
            )

            # BUTTON BELOW INPUT
            btn = gr.Button(
                "🚨 Inject Vulnerability",
                variant="primary"
            )

            output = gr.Textbox(
                label="Generated Vulnerable Code",
                lines=20
            )

        # ----------------------------------------
        # RIGHT SIDE
        # ----------------------------------------

        with gr.Column(scale=1):

            gr.Markdown("## 📘 How To Use")

            gr.Markdown('''
### Steps:
1. Copy any safe Python code
2. Paste it into the left box or use a sample.
3. Click **Inject Vulnerability**.
4. AI will generate vulnerable code and an explanation.
5. Study the security weaknesses and learn how to prevent them.
'''
            )

            gr.Markdown("## 🧪 Sample Safe Test Cases")

            gr.Code(
                value='''
def login(password):
    if password == "admin123":
        return "Access Granted"
    return "Access Denied"
''',
                language="python",
                label="Test Case 1"
            )

            gr.Code(
                value='''
def divide(a, b):
    if b == 0:
        return "Cannot divide"
    return a / b
''',
                language="python",
                label="Test Case 2"
            )

            gr.Code(
                value='''
def get_user(users, index):
    if index < len(users):
        return users[index]
    return None
''',
                language="python",
                label="Test Case 3"
            )

    # --------------------------------------------
    # BUTTON ACTION
    # --------------------------------------------

    btn.click(
        fn=inject_vulnerability,
        inputs=code_input,
        outputs=output
    )

# ============================================n# LAUNCH
# ============================================

demo.launch(
    share=True,
    
)
