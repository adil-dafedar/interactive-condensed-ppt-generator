# 🎨 Interactive Condensed PPT Generator
👉 [RizzPPTs App](https://rizzppts.up.railway.app)
An AI-powered tool that helps users create **concise, relevant slides** in seconds — without spending hours manually designing presentations.  

## 🚨 Problem

Creating presentations is often slow and overwhelming:  

❌ Slides are **text-heavy**, making them hard to follow  
❌ People have **limited attention span and memory**, remembering less when slides are crowded  
❌ Manual slide creation is **time-consuming**, especially for long content  

As a result, presentations are either **dense, boring, or take hours to prepare**.  

## 🎯 Users

- Students preparing lectures or assignments  
- Professionals creating reports and presentations  
- Non-designers who want **effective slides quickly**  

## 💡 Solution

This project enables users to:  

- Paste or type content  
- Automatically generate **concise slides** (one idea per slide)  
- Optionally add **AI-generated images**  
- Download slides as **PDF**  
- Navigate easily with **keyboard shortcuts**  

No manual formatting. No cluttered slides. Minimal time and cognitive load.  

## ✨ Key Features

🎨 AI-generated slides with **relevant, concise content**  
🖼️ Optional images per slide  
🌗 Dark/light theme  
📥 Export slides as **PDF**  
⌨️ Keyboard navigation for faster workflow  
⚡ ChatGPT-style interactive UI  

## 🧪 MVP / Prototype Development

This project was built to validate:  

> Can users automatically generate concise, clear slides from long content, saving time and reducing cognitive overload?  

**Approach:**  

- Backend-first prototype using **FastAPI**  
- Frontend with **HTML/CSS**, lightweight and responsive  
- **Gemini API** for AI-powered slide generation  
- Focused on **speed of iteration** and **user-centered slide clarity**  

**Trade-offs:**  

❌ No persistent storage yet  
❌ Limited image customization (future improvement)  
❌ Basic styling for fast MVP delivery  

## 🏗️ Tech Stack

- **Backend:** FastAPI  
- **Frontend:** HTML/CSS  
- **AI:** Gemini API  

## ⚙️ How It Works

1. User inputs content  
2. AI analyzes text → generates **concise slides, one idea per slide**  
3. Optional AI images added  
4. Slides displayed in **interactive UI**  
5. Download PDF or navigate with keyboard  

## 🚀 Running Locally

```bash
git clone <repo-url>
cd ppt-generator
pip install -r requirements.txt
uvicorn main:app --reload
```
Open: http://localhost:8000

## 📸 Demo Flow
Paste syllabus topic
Click Generate Slides

<img width="1062" height="782" alt="image" src="https://github.com/user-attachments/assets/c5fffd76-03c1-4b7f-9aa8-ea3d2c6208ed" />

Review AI-generated slides

<img width="1893" height="899" alt="image" src="https://github.com/user-attachments/assets/4f9f9427-5279-4abd-9b0b-1934807d6c68" />

<img width="1886" height="876" alt="image" src="https://github.com/user-attachments/assets/16d09df3-f269-42e2-8930-58e5b284347c" />

Download as PDF or navigate with keyboard shortcuts

## 📈 Future Improvements

## 🌐 Multi-language support
🖼️ Enhanced AI image options
📅 Automatic slide structuring suggestions
📱 Collaboration features for teams
🎥 AI-generated video presentations

## 🌐 Live Demo
Check it out here:  
👉 [RizzPPTs App](https://rizzppts.up.railway.app)
