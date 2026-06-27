# 🎨 AI-Powered Content Structuring Tool
👉 [RizzPPTs App](https://rizzppts.up.railway.app)

An AI system that converts long-form content into **concise, structured, slide-ready learning blocks** in seconds.

---

## 🚨 Problem

Creating structured learning content is slow and inefficient:

- ❌ Information-heavy slides reduce clarity  
- ❌ Long content leads to cognitive overload  
- ❌ Manual structuring takes significant time  

Result: low retention and poorly structured learning material.

---

## 💡 Solution

Paste content → get **clean, structured learning slides instantly**:

- 🧠 One idea per slide  
- 🎨 Optional AI-generated visuals  
- 📥 Export as PDF  
- ⌨️ Keyboard navigation for fast review  

Goal: reduce cognitive load and improve understanding.

---

## ✨ Key Features

- 🧠 AI-based content structuring  
- 🎨 Optional image generation per slide  
- 🌗 Light/Dark UI  
- 📥 PDF export  
- ⚡ Fast, interactive navigation  

---

## 🧪 Core Idea (MVP)

Validate a simple question:

> Can AI convert dense content into structured, easy-to-learn formats effectively?

---

## 🏗️ Tech Stack

- FastAPI (Backend)  
- HTML/CSS (Frontend)  
- Gemini API (AI Generation)  

---

## ⚙️ How It Works

1. User inputs raw content  
2. AI breaks it into structured points  
3. Each point becomes a slide  
4. UI renders interactive learning flow  
5. User exports as PDF  

---

## 🚀 Run Locally

```bash
git clone <repo-url>
cd ppt-generator
pip install -r requirements.txt
uvicorn main:app --reload
