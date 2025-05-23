
# Comics Universe 🎨📚

**Comics Universe** is a web-based comic reading platform developed as part of an MCA academic curriculum. It aims to make visual storytelling accessible and inclusive, especially for children in BUDS schools and students with disabilities. The platform features a mix of curated comics (e.g., *Batman & Spiderman*, *Watchmen*) and an original AI-generated comic series — **Spectrum Squad** — created using generative AI tools for images and dialogues.

Built with **HTML**, **CSS**, and **JavaScript**, Comics Universe offers a Netflix-like gallery, interactive PDF viewer, dark mode, multilingual support, and responsive design to deliver a fun and engaging experience.

---

## 🌟 Features

- **Homepage**: Showcases three featured comics with zoom-in animation on the **Explore More** button.
- **About Section**: Describes the project's purpose and features, with a hover-based zoom-in on the comic-themed image.
- **Comics Section**: Highlights three comics with animated hover effects for each card.
- **Comics Gallery**: A Netflix-style grid displaying all nine comics with "Read Now" hover overlays.
- **Comic Details Page**:
  - Comic metadata: title, description, writer, issue date.
  - Embedded PDF viewer with page navigation and download functionality.
- **Responsive Design**: Fully mobile-friendly layout with collapsible navbar and adaptive grids (tested at 850px, 600px, 470px).
- **Dark Mode**: Toggle for eye comfort with smooth transition effects.
- **Multilingual Support**: Spectrum Squad available in English and Malayalam.
- **AI-Generated Content**: Spectrum Squad uses generative AI for both visuals and story dialogues.
- **Animations**: Subtle zoom-in effects on buttons, images, and comic cards for a dynamic UI.

---

## 📸 Screenshots

> All images are located in the `screenshots/` directory.

1. **Homepage**  
   ![Homepage](screenshots/1.PNG)  
   Features header, navbar with logo and dark mode toggle, and "Explore More" button animation.

2. **About Page**  
   ![About Page](screenshots/2.PNG)  
   Comic-themed image with zoom-in effect and project description.

3. **Comics Page**  
   ![Comics Page](screenshots/3.PNG)  
   Highlights featured comics with interactive hover effects.

4. **Comics Gallery**  
   ![Comics Gallery](screenshots/4.PNG)  
   Netflix-style comic grid with overlay on hover.

5. **Comic Details**  
   ![Comic Details](screenshots/5.PNG)  
   Details view with embedded PDF reader for comics.

---

## 🚀 Getting Started

### 📁 Clone or Download

Download the project or clone the repository (if hosted):

```bash
cd C:\Users\HP\Desktop\COMIC_CREATIONS
```

### 📂 Verify Assets

Ensure all required files are in place:

- **Images** → `assets/img/`
- **PDFs** → `assets/pdfs/`

> 🛠️ If missing, create placeholders:
- **Images**: 300x400px PNGs (e.g., `watchmen.png`)
- **PDFs**: Single-page files named by title (e.g., `watchmen.pdf`)

### 🖥️ Run a Local Server

Using Python:

```bash
cd C:\Users\HP\Desktop\COMIC_CREATIONS
python -m http.server 8000
```

Or with **VS Code + Live Server** (recommended, port 5500):

Open in browser:  
[http://localhost:8000/index.html](http://localhost:8000/index.html)

---

## ✅ Testing the Application

- **Homepage**: Check navbar, dark mode toggle, Explore More animation.
- **Gallery**: Open `comics-gallery.html`, confirm hover overlays.
- **Comic Details**: Test `comic-details.html?id=1` to `id=9`.
- **Responsiveness**: Resize window to 850px, 600px, 470px.
- **Dev Tools**: Open Console (`F12`) → Check for missing asset errors.

---

## 📜 Project Structure

```
COMIC_CREATIONS/
├── index.html
├── comics.html
├── comics-gallery.html
├── comic-details.html
├── assets/
│   ├── img/         # Comic cover images
│   ├── pdfs/        # Comic PDFs
├── css/
├── js/
├── screenshots/
```

---

## 🧑‍💻 Contributing

This is an academic project submitted for the MCA curriculum. External contributions are not accepted. However, feedback from instructors or peers is welcome for evaluation purposes.

---

## 📄 License

**Academic Use Only** – Not licensed for commercial distribution.  
- Curated comics (e.g., *Batman & Spiderman*, *Watchmen*) are sourced from public repositories.  
- Spectrum Squad is an original creation using generative AI.

---

## 🙌 Credits

- **Developed by**: *Team Three* (MCA Students)
- **AI Comic Content**: *Spectrum Squad* — generated with AI tools.
---

**Created with ❤️ for visual storytelling and accessibility.**
