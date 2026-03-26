from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from generator import generate_slides
import html

app = FastAPI()

# Mount static folder
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Interactive Condensed PPT Generator</title>
        <link rel="stylesheet" href="/static/style.css">
    </head>
    <body>
        <div class="container">
            <h1>What do you want to learn today?</h1>
            <form method="post" action="/generate">
                <input name="topic" placeholder="Enter your topic" required/><br>
                <input name="slides" type="number" placeholder="Max slides" required/><br>
                <input name="words" type="number" placeholder="Max words per slide" required/><br>
                <button type="submit">Generate Slides</button>
            </form>
            <div class="theme-toggle">
                <label>
                    <input type="checkbox" id="themeSwitch"> Dark Mode
                </label>
            </div>
        </div>

        <script>
            const switchToggle = document.getElementById('themeSwitch');
            switchToggle.addEventListener('change', function() {
                if(this.checked){
                    document.body.classList.add('dark-theme');
                } else {
                    document.body.classList.remove('dark-theme');
                }
            });
        </script>
    </body>
    </html>
    """
@app.post("/generate", response_class=HTMLResponse)
def generate(topic: str = Form(...), slides: int = Form(...), words: int = Form(...)):
    if slides < 1 or words < 1:
        return HTMLResponse("<h2>Error: Slides and words must be positive numbers.</h2>")

    try:
        slides_text = generate_slides(topic, slides, words)

        import re, html
        # Extract slides and optional image URLs like "Slide 1: Text | image:url"
        slide_matches = re.findall(r"Slide \d+:\s*(.*)", slides_text)
        if not slide_matches:
            return HTMLResponse("<h2>Error: No slides generated. Try another topic.</h2>")

        slides_list = []
        for s in slide_matches:
            parts = s.split("|")
            text = html.escape(parts[0].strip())
            img = parts[1].replace("image:", "").strip() if len(parts) > 1 else ""
            slides_list.append({"text": text, "img": img})

    except Exception as e:
        return HTMLResponse(f"<h2>Error generating slides:</h2><pre>{str(e)}</pre>")

    # Build slide deck HTML
    slides_html = ""
    for i, s in enumerate(slides_list):
        img_tag = f'<img src="{s["img"]}" alt="slide image" class="slide-img">' if s["img"] else ""
        slides_html += f'<div class="slide" id="slide{i}">'
        slides_html += f'<div class="slide-number">{i+1}</div>'
        slides_html += f'<div class="title">{s["text"]}</div>{img_tag}</div>'

    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{html.escape(topic)} - Slide Deck</title>
        <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap" rel="stylesheet">
        <link rel="stylesheet" href="/static/slide-style.css">
    </head>
    <body class="bright">
        {slides_html}
        <button class="nav-btn" id="prev">&#8592;</button>
        <button class="nav-btn" id="next">&#8594;</button>
        <button id="downloadBtn">Download PDF</button>
        <button id="themeToggle">Toggle Theme</button>

        <script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js"></script>
        <script>
            let current = 0;
            const slides = document.querySelectorAll('.slide');
            const body = document.body;
            function showSlide(index){{
                slides.forEach(s=>s.classList.remove('active'));
                slides[index].classList.add('active');
            }}
            document.getElementById('prev').addEventListener('click', ()=> {{
                current = (current - 1 + slides.length) % slides.length; showSlide(current);
            }});
            document.getElementById('next').addEventListener('click', ()=> {{
                current = (current + 1) % slides.length; showSlide(current);
            }});
            document.addEventListener('keydown', e=> {{
                if(e.key==='ArrowRight' || e.key===' ') {{ current = (current + 1) % slides.length; showSlide(current); }}
                else if(e.key==='ArrowLeft') {{ current = (current - 1 + slides.length) % slides.length; showSlide(current); }}
            }});
            // Theme toggle
            document.getElementById('themeToggle').addEventListener('click', ()=> {{
                if(body.classList.contains('bright')){{ body.classList.remove('bright'); body.classList.add('dark'); }}
                else{{ body.classList.remove('dark'); body.classList.add('bright'); }}
            }});
            // Download slides as PDF
            document.getElementById('downloadBtn').addEventListener('click', ()=> {{
                const {{ jsPDF }} = window.jspdf;
                const doc = new jsPDF();
                slides.forEach((s, i)=> {{
                    if(i > 0) doc.addPage();
                    const title = s.querySelector('.title').innerText;
                    doc.setFontSize(20);
                    doc.text(title, 10, 20);
                    const img = s.querySelector('.slide-img');
                    if(img){{
                        doc.addImage(img, 'JPEG', 10, 30, 180, 100);
                    }}
                }});
                doc.save("{topic}_slides.pdf");
            }});
            showSlide(current);
        </script>
    </body>
    </html>
    """
    return HTMLResponse(html_content)