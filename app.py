from flask import Flask, render_template, send_from_directory, abort, Response
import os
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Comic data with normalized file names
comics = [
    {
        "id": 1,
        "title": "Spectrum Squad (Malayalam)",
        "cover": "img/img1.png",
        "description": "Maya and her friends unite as the Spectrum Squad, turning their unique strengths into a force for helping others.",
        "issueDate": "April 2025",
        "writer": "Panchami ",
        "pdfPath": "pdfs/GEN AO.pdf"
    },
    {
        "id": 2,
        "title": "Spectrum  Squad ",
        "cover": "img/img1.png",
        "description": "The Spectrum Squad, led by Maya and her friends, uses their unique talents to spread kindness and champion inclusivity.",
        "issueDate": "April 2025",
        "writer": "Panchami",
        "pdfPath": "pdfs/GEN AO1.pdf"
    },
    {
        "id": 3,
        "title": "Batman & Spiderman - Shadows Across Universes",
        "cover": "img/img2.png",
        "description": "Batman and Spider-Man join forces when their worlds suddenly come together.",
        "issueDate": "April 2025",
        "writer": "Stan Lee",
        "pdfPath": "pdfs/DC Marvel Comics - Batman & Spiderman.pdf"
    },
    {
        "id": 4,
        "title": "Watchmen",
        "cover": "img/watchemen.png",
        "description": "Watchmen is a genre-defining graphic novel set in an alternate 1980s America during the Cold War.",
        "issueDate": "1986 (Collected Edition: 2016)",
        "writer": "Alan Moore (Writer), Dave Gibbons (Illustrator)",
        "pdfPath": "pdfs/Watchmen By Alan Moore And Dave Gibbons.pdf"
    },
    {
        "id": 5,
        "title": "Invincible #001",
        "cover": "img/invincible.png",
        "description": "Invincible #1 marks the explosive debut of Mark Grayson, a seemingly ordinary teenager who inherits incredible powers from his alien superhero father, Omni-Man.",
        "issueDate": "2003 (Digital Release: 2021)",
        "writer": "Robert Kirkman (Writer), Cory Walker (Artist)",
        "pdfPath": "pdfs/Invincible (Comic).pdf"
    },
    {
        "id": 6,
        "title": "Asian Comics",
        "cover": "img/asian.png",
        "description": "Asian Comics by John A. Lent offers an in-depth exploration of the comic art traditions across Asia, covering countries such as Japan, China, Korea, India, Indonesia, the Philippines, and more.",
        "issueDate": "2015",
        "writer": "John A. Lent",
        "pdfPath": "pdfs/Asian Comics.pdf"
    },
    {
        "id": 7,
        "title": "Goodbye, Eri",
        "cover": "img/good bye, eri.png",
        "description": "Goodbye, Eri is a poignant one-shot manga by Tatsuki Fujimoto, exploring themes of grief, memory, and filmmaking through a young boy's emotional journey.",
        "issueDate": "2023",
        "writer": "Tatsuki Fujimoto",
        "pdfPath": "pdfs/Goodbye, Eri.pdf"
    },
    {
        "id": 8,
        "title": "Demon Slayer: Kimetsu no Yaiba Vol. 1",
        "cover": "img/demons.png",
        "description": "Demon Slayer: Kimetsu no Yaiba follows Tanjiro Kamado, a kind-hearted boy whose life is shattered when demons slaughter his family, and his sister Nezuko is turned into a demon.",
        "issueDate": "2018",
        "writer": "Koyoharu Gotouge",
        "pdfPath": "pdfs/Demon Slayer.pdf"
    },
    {
        "id": 9,
        "title": "The Manga Guide to Physics",
        "cover": "img/manga.png",
        "description": "The Manga Guide to Physics presents fundamental physics concepts through a fun and engaging manga storyline.",
        "issueDate": "2009",
        "writer": "Hideo Nitta",
        "pdfPath": "pdfs/The Manga Guide to Physics.pdf"
    }
]

@app.route('/')
def index():
    return render_template('index.html', comics=comics[:3])  # Show first 3 comics

@app.route('/gallery')
def gallery():
    return render_template('comics-gallery.html', comics=comics)

@app.route('/comic-details/<int:id>')
def comic_details(id):
    comic = next((c for c in comics if c['id'] == id), None)
    if comic:
        # Verify file existence
        cover_path = os.path.join('static', comic['cover'])
        pdf_path = os.path.join('static', comic['pdfPath'])
        if not os.path.exists(cover_path):
            logger.error(f"Cover image not found: {cover_path}")
            return render_template('error.html', message=f"Cover image for {comic['title']} not found."), 404
        if not os.path.exists(pdf_path):
            logger.error(f"PDF not found: {pdf_path}")
            return render_template('error.html', message=f"PDF for {comic['title']} not found."), 404
        return render_template('comic-details.html', comic=comic)
    else:
        return render_template('error.html', message="Comic not found."), 404

@app.route('/static/<path:path>')
def serve_static(path):
    try:
        # Set MIME types explicitly
        if path.endswith('.pdf'):
            return send_from_directory('static', path, mimetype='application/pdf')
        elif path.endswith('.webp'):
            return send_from_directory('static', path, mimetype='image/webp')
        return send_from_directory('static', path)
    except FileNotFoundError:
        logger.error(f"Static file not found: {path}")
        abort(404)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html', message="Page or resource not found."), 404

if __name__ == '__main__':
    # For local development
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))