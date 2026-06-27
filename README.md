# 🎨 AI-Powered Content Structuring Tool
👉 [RizzPPTs App](https://rizzppts.up.railway.app)

An AI-powered tool that helps users create **concise, relevant slides** in seconds — without spending hours manually designing presentations.  

## 🚨 Problem

Creating presentations is often slow and overwhelming:  

❌ Slides are **text-heavy**, making them hard to follow  
❌ People have **limited attention span and memory**, remembering less when slides are crowded  
❌ Manual slide creation is **time-consuming**, especially for long content  

As a result, outputs are often **dense, boring, or take hours to prepare**.  

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

No manual formatting. No cluttered structure. Minimal time and cognitive load.  

## ✨ Key Features

🎨 AI-generated slides with **relevant, concise content**  
🖼️ Optional images per slide  
🌗 Dark/light theme  
📥 Export slides as **PDF**  
⌨️ Keyboard navigation for faster workflow  
⚡ ChatGPT-style interactive UI  

## 🧪 MVP / Prototype Development

This project was built to validate:  

> Can users automatically transform long content into structured, easy-to-understand learning blocks, reducing cognitive overload?  

**Approach:**  

- Backend-first prototype using **FastAPI**  
- Frontend with **HTML/CSS**, lightweight and responsive  
- **Gemini API** for AI-powered slide generation  
- Focused on **speed of iteration** and **user-centered clarity**  

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
