# 🚀 ViralGen AI - AI-Powered Social Media Content Generator

ViralGen AI is an advanced **AI-driven social media content generator** designed to help marketers, influencers, and brands create **viral social media posts instantly**. This project uses **Flask (Python) for the backend** and **React (Next.js) for the frontend**, integrating with **OpenAI GPT-4** for AI-generated content.

---

## **📌 Features**
✅ AI-Powered Social Media Content Generation  
✅ Light/Dark Mode UI for better UX  
✅ Flask Backend with OpenAI Integration  
✅ React Frontend with Smooth Animations  
✅ Fully Responsive & Modern UI  

---

## **🛠️ Tech Stack**
### **Frontend**
- **React (Next.js)**
- **CSS3 + Custom Styling**
- **Fetch API for Backend Communication**

### **Backend**
- **Flask (Python)**
- **OpenAI GPT-4 API**
- **RESTful API**
- **PostgreSQL Database (Future Implementation)**

---

## **🚀 Project Setup & Installation**
### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/Will-Langhart/viralgen-ai.git
cd viralgen-ai
```
🔧 Backend Setup (Flask API)

2️⃣ Create a Virtual Environment
```bash
cd backend
python3 -m venv venv  # Create virtual environment
source venv/bin/activate  # Activate (Mac/Linux)
venv\Scripts\activate  # Activate (Windows)
```
3️⃣ Install Required Dependencies
```bash
pip install -r requirements.txt
```
4️⃣ Set Up Environment Variables

Create a .env file inside the backend/ folder:
```bash
OPENAI_API_KEY=your_openai_api_key_here
FLASK_ENV=development
```
5️⃣ Run the Flask Backend
```bash
flask run --port=5001
```
🖥️ Frontend Setup (React)

6️⃣ Install Frontend Dependencies
```bash
cd frontend
npm install
```
7️⃣ Run the Frontend
```bash
npm start
```
The React app should now be running at http://localhost:3000/.

⚡ Deploying the Full Stack App

8️⃣ Build the React App & Move to Backend
```bash
cd frontend
npm run build
mv build ../backend/
```
9️⃣ Restart Flask to Serve the Frontend
```bash
cd ../backend
flask run --port=5001
```
Now http://127.0.0.1:5001/ will serve both backend and frontend.

🛠 API Endpoints

🎯 Generate AI-Generated Social Media Content
	•	Endpoint: /generate
	•	Method: POST
	•	Request Body:
```bash
{
  "prompt": "Best strategies for viral marketing"
}
```
•	Response:
 ```bash
 {
  "generated_content": "The key to viral marketing is..."
}
 ```
🛠 Troubleshooting

❌ Flask not starting?
Run:
```bash
pkill -f flask  # Stop any existing Flask processes
flask run --port=5001
```
❌ React not loading?
Check backend/build/ folder exists, if not:
```bash
cd frontend
npm run build
mv build ../backend/
```
❌ Styling Issues?
Force refresh your browser:
	•	Windows/Linux: Ctrl + Shift + R
	•	Mac: Cmd + Shift + R

🛠 Future Features

🔹 AI-powered Hashtag Generator
🔹 Integration with Instagram, Twitter API
🔹 Scheduled Post Automation
🔹 SEO-optimized Blog Post Generation

📝 License

This project is MIT Licensed - Feel free to use and modify it.

💡 Contributors

👨‍💻 Developed by: Will Langhart
📬 Want to contribute? Fork the repo and submit a PR! 🚀

🎉 Ready to Make Social Media Viral with AI? Start Now!
```bash
git clone https://github.com/Will-Langhart/viralgen-ai.git
cd viralgen-ai
bash auto_update.sh  # Runs everything automatically!
```

