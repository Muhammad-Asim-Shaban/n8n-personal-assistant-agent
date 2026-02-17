# Personal Assistant Agent (n8n + Ollama + GLM-5)

This project is an autonomous **Personal Assistant Agent** built using **n8n workflow automation** and powered by the **GLM-5 language model** through **Ollama**.

The goal of this project was to explore how AI agents can automate daily productivity tasks by integrating with Google services.

---

## Features

The Personal Assistant can perform the following tasks:

- Answer questions on various topics  
- Schedule meetings and calendar events using **Google Calendar**  
- Read emails, send replies, and summarize messages through **Gmail**  
- Manage tasks and to-do lists with **Google Tasks**  
- Take quick notes directly in **Google Docs**  
- Track expenses and budgeting using **Google Sheets**

---

## Tech Stack Used

- **n8n** – Workflow automation platform  
- **Ollama** – Running the AI model locally  
- **GLM-5 Model** – Core language model for assistant responses  
- **Google APIs** – Calendar, Gmail, Tasks, Docs, Sheets integration  
- **Python** – Used for additional custom logic (if required)

---

## Project Structure
```bash
personal-assistant-agent/
│
├── workflow/
│   └── personal-assistant.json   # Exported n8n workflow
│
├── scripts/
│   └── main.py                  # Python helper script
│
├── README.md                    # Project documentation
```
## 🚀 How to Use This Project
1. Clone the Repository
```bash
git clone https://github.com/yourusername/n8n-personal-assistant-agent.git
cd personal-assistant-agent
```
2. Import Workflow in n8n
3. Setup Google Credentials
4. Run Ollama locally
4.1. Install Ollama and pull the GLM-5 model:
```bash
ollama pull glm5
```
4.2. Start Ollama before running the workflow:
```bash
ollama serve
```
## 🌱 Future Improvements

- Add more autonomous decision-making capabilities
- Improve email understanding and context awareness
- Add voice input/output support
- Deploy the assistant on the cloud instead of local hosting

## 👤 Author
Developed by Muhammad Asim Shaban
Learning and building autonomous AI agents using n8n and LLMs.
