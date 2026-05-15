
---
title: VulnPrompt-AI Simulator
emoji: 🛡️
colorFrom: red
colorTo: purple
sdk: gradio
sdk_version: 4.31.0 # Or your specific Gradio version
app_file: app.py
---

# 🛡️ Vulnerable Prompt Injection - Simulator

![Gradio App Screenshot](https://raw.githubusercontent.com/Abdulrehman-droid/vulnerable-prompt-injection-simulator/main/screenshot.png) <!-- Replace with an actual screenshot URL -->

AI-powered vulnerability injection simulator using the Groq API (Llama models) and a Gradio interface. This project is designed for educational purposes to help users understand common security vulnerabilities in Python code.

## ✨ Features

*   **AI-Powered Vulnerability Generation**: Utilizes Groq's Llama models to dynamically inject security flaws into provided safe Python code.
*   **Cybersecurity Education**: Provides explanations of the introduced vulnerabilities and potential exploitation methods.
*   **Interactive Gradio Interface**: A user-friendly web interface for inputting safe code and receiving vulnerable outputs.
*   **Hugging Face Spaces Deployment**: Optimized for easy deployment and sharing on Hugging Face Spaces.

## 🚀 How To Use

### Using the Hosted Application (Hugging Face Space)

1.  Visit the deployed application on Hugging Face Spaces (e.g., [Abdulrehman965/vulnerable-prompt-injection-simulator](https://huggingface.co/spaces/Abdulrehman965/vulnerable-prompt-injection-simulator)).
2.  Copy any safe Python code into the "Enter Safe Code" text area.
3.  Click the "🚨 Inject Vulnerability" button.
4.  The AI will process the code and generate a vulnerable version along with an explanation in the "Generated Vulnerable Code" output box.
5.  Study the identified weaknesses and learn how to prevent them in real-world scenarios.

### Local Setup

To run this application locally, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Abdulrehman-droid/vulnerable-prompt-injection-simulator.git
    cd vulnerable-prompt-injection-simulator
    ```

2.  **Install dependencies:**
    Ensure you have Python 3.8+ installed. Then install the required libraries:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Set up Groq API Key:**
    You'll need a Groq API key. Get one from [GroqCloud](https://console.groq.com/keys).
    Set it as an environment variable:
    ```bash
    export GROQ_API_KEY="your_groq_api_key_here"
    ```
    (On Windows, use `set GROQ_API_KEY="your_groq_api_key_here"`)

4.  **Run the application:**
    ```bash
    python app.py
    ```
    This will start the Gradio application, usually accessible at `http://127.0.0.1:7860` in your web browser.

## ⚠️ Disclaimer

This tool is developed **solely for educational and research purposes**. It is intended to help users understand common security vulnerabilities and learn best practices for secure coding. **Do not use this tool for any malicious activities or to exploit real-world systems.** The developers are not responsible for any misuse or damage caused by this application.

## 🤝 Contributing

Contributions are welcome! If you have suggestions for new features, improvements, or bug fixes, please open an issue or submit a pull request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
