# Finance AI Agent

## 📌 Overview
Finance AI Agent is an intelligent financial assistant that fetches the latest analyst recommendations and news for a given stock symbol. It utilizes AI models and APIs to provide real-time market insights in a structured and explainable manner.

## 🔥 Features
- Retrieves analyst recommendations for a given stock.
- Summarizes recent financial news.
- Uses AI-based automation for data retrieval and response generation.
- Interactive chatbot-like response.

## 🏗️ Tech Stack
- **Programming Language**: Python
- **Framework**: AI-powered automation (phi/agent)
- **APIs Used**: GROQ API, Financial Market Data APIs
- **Environment Management**: Python Virtual Environment (venv)

## 🛠️ Installation
### 1️⃣ Clone the Repository
```sh
$ git clone https://github.com/the-madhankumar/FinanceAgent.git
$ cd finance-ai-agent
```
### 2️⃣ Create a Virtual Environment
```sh
$ python -m venv env
$ source env/bin/activate  # On macOS/Linux
$ env\Scripts\activate    # On Windows
```
### 3️⃣ Install Dependencies
```sh
$ pip install -r requirements.txt
```
### 4️⃣ Set Up API Keys
Ensure that your **GROQ_API_KEY** is properly set in your environment variables or in a `.env` file.
#### Method 1: Set Environment Variable
```sh
$ setx GROQ_API_KEY "your-api-key-here"
```
#### Method 2: Use a `.env` File
Create a `.env` file in the project directory and add:
```env
GROQ_API_KEY=your-api-key-here
```

## 🚀 Usage
### Running the Financial Agent
```sh
$ python financial_agent.py
```
### Example Query
Once the script is running, you can interact with it using natural language queries:
```sh
Summarize analyst recommendation and share the latest news for NVDA
```
### Expected Output
- A structured table containing analyst recommendations, price targets, and dates.
- A brief summary of the latest financial news related to the requested stock.

## ❓ Troubleshooting
### 1️⃣ "GROQ_API_KEY not set" Error
- Ensure the API key is correctly set as an environment variable or in the `.env` file.
- Restart your terminal or IDE after setting the environment variable.
- Run the following command to verify:
  ```sh
  $ echo %GROQ_API_KEY%  # Windows
  $ echo $GROQ_API_KEY   # macOS/Linux
  ```
### 2️⃣ Dependencies Issue
If you face errors related to missing packages, try reinstalling:
```sh
$ pip install -r requirements.txt --force-reinstall
```

## 👨‍💻 Author & Contributors
- **MADHAN KUMAR M** - Project Lead

## 📜 License
This project is licensed under [MIT License](LICENSE).

---

If you have any questions or need further assistance, feel free to reach out! 🚀

