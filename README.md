Comics Universe
Comics Universe is a web-based comic reading platform developed as part of an MCA academic curriculum. Designed to provide a fun and inclusive experience, it targets children in BUDS schools and disabled students who benefit from visual storytelling. The platform features a mix of curated comics (e.g., Batman & Spiderman, Watchmen) and an original AI-generated comic, Spectrum Squad, created with generative AI tools for images and dialogues. Built with HTML, CSS, and JavaScript, it offers a Netflix-like gallery, PDF viewer, dark mode, and responsive design with zoom-in animations for an engaging user experience.
Features

Homepage: Showcases three featured comics (Spectrum Squad Malayalam, Spectrum Squad English, Batman & Spiderman) with zoom-in animation on the "Explore More" button.
About Section: Details the project's purpose and features, with a hover zoom-in effect on the comic-themed image.
Comics Section: Displays three comics with hover zoom-in animations on each card for a dynamic effect.
Comics Gallery: A Netflix-like grid of all nine comics, with hover effects to highlight "Read Now" overlays.
Comic Details: Displays comic details (title, description, writer, issue date) and an interactive PDF viewer with page navigation and download option.
Responsive Design: Mobile-friendly layout with collapsible navbar and adaptive grids (tested at 850px, 600px, 470px).
Dark Mode: Toggle for eye comfort, with smooth transitions.
Multilingual Support: Includes Spectrum Squad in English and Malayalam.
AI-Generated Content: Spectrum Squad uses AI for images and dialogues, showcasing innovative storytelling.
Animations: Subtle zoom-in effects on hover for the "Explore More" button, About image, and comic cards.

Screenshots
Below are placeholders for six screenshots showcasing key features of Comics Universe. (Note: Add actual screenshot files to the screenshots/ directory and update the paths below.)

Homepage OverviewDisplays the header with the "Explore More" button (hover to see zoom-in effect), navbar, and featured comics section.
![Homepage](screenshots/1.png)
About SectionShows the About section with the comic-themed image (hover for zoom-in animation) and project description.
![Gallery](screenshots/gallery.png)
Comics SectionHighlights the three featured comics with hover zoom-in effects on each card.
![Gallery](screenshots/gallery.png)
Comics GalleryPresents the Netflix-like gallery with all nine comics and "Read Now" hover overlays.
![Gallery](screenshots/gallery.png)
Comic Details PageShows the comic details page with cover image, details, and PDF viewer (e.g., for Watchmen, ID 4).
![Gallery](screenshots/gallery.png)
Responsive DesignDemonstrates the mobile view (e.g., at 470px) with collapsed navbar and stacked layout.


To add screenshots: Create a screenshots/ directory in the project root, place the PNG files, and update the paths above.
Project Structure
COMIC_CREATIONS/
├── assets/
│   ├── img/
│   │   ├── about.webp          # Header background and About section image
│   │   ├── mountain.png        # Navbar logo
│   │   ├── menu-btn.png        # Mobile menu toggle
│   │   ├── img1.png            # Spectrum Squad cover (IDs 1, 2)
│   │   ├── img2.png            # Batman & Spiderman cover (ID 3)
│   │   ├── watchemen.png       # Watchmen cover (ID 4)
│   │   ├── invincible.png      # Invincible cover (ID 5)
│   │   ├── asian.png           # Asian Comics cover (ID 6)
│   │   ├── good bye, eri.png   # Goodbye, Eri cover (ID 7)
│   │   ├── demons.png          # Demon Slayer cover (ID 8)
│   │   ├── manga.png           # Manga Guide to Physics cover (ID 9)
│   ├── pdfs/
│   │   ├── GEN AO.pdf                                  # ID 1
│   │   ├── GEN AO1.pdf                                 # ID 2
│   │   ├── DC Marvel Comics - Batman & Spiderman.pdf   # ID 3
│   │   ├── Watchmen By Alan Moore And Dave Gibbons.pdf # ID 4
│   │   ├── Invincible (Comic).pdf                      # ID 5
│   │   ├── Asian Comics.pdf                            # ID 6
│   │   ├── Goodbye, Eri.pdf                            # ID 7
│   │   ├── Demon Slayer.pdf                            # ID 8
│   │   ├── The Manga Guide to Physics.pdf              # ID 9
├── css/
│   ├── style.css               # Main styles, including animations
│   ├── responsive.css          # Responsive design rules
├── js/
│   ├── script.js               # Interactivity (menu, dark mode, scroll)
├── screenshots/                # (Create this for screenshots)
│   ├── homepage.png            # Placeholder
│   ├── about.png               # Placeholder
│   ├── comics.png              # Placeholder
│   ├── gallery.png             # Placeholder
│   ├── comic-details.png       # Placeholder
│   ├── responsive.png          # Placeholder
├── index.html                  # Homepage with 3 comics
├── comics-gallery.html         # Gallery of all comics
├── comic-details.html          # Comic details and PDF viewer
├── README.md                   # Project documentation

Setup Instructions

Clone or Download:

Download the project to C:\Users\HP\Desktop\COMIC_CREATIONS or clone the repository (if hosted).


Verify Assets:

Ensure all images are in assets/img/ and PDFs are in assets/pdfs/ (see Project Structure).
If missing, create placeholders:
Images: 300x400px PNGs with comic titles (e.g., "Watchmen" for watchemen.png).
PDFs: Single-page PDFs with comic titles.




Run a Local Server:

Open a terminal in C:\Users\HP\Desktop\COMIC_CREATIONS:cd C:\Users\HP\Desktop\COMIC_CREATIONS
python -m http.server 8000


Alternatively, use VS Code with the Live Server extension (port 5500).
Open http://localhost:8000/index.html in a browser (Chrome, Firefox recommended).


Test the Application:

Homepage: Verify the navbar, header ("Explore More" zoom-in), About section (image zoom-in), and Comics section (card zoom-in).
Gallery: Check comics-gallery.html for all nine comics with hover effects.
Comic Details: Test comic-details.html?id=1 to id=9, ensuring cover images and PDFs load (especially IDs 4–9).
Responsiveness: Resize browser to 850px, 600px, 470px to confirm mobile-friendly layout.
Console: Open F12 → Console to check for net::ERR_FILE_NOT_FOUND errors.



Dependencies

FontAwesome 4.7.0: For icons (navbar, dark mode toggle, PDF navigation, scroll-to-top).
Loaded via CDN: https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css


jQuery 3.6.0: For menu toggle, dark mode, and scroll functionality.
Loaded via CDN: https://code.jquery.com/jquery-3.6.0.min.js


PDF.js 3.11.174: For rendering PDFs in the comic details page.
Loaded via CDN: https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.min.js
Worker: https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.worker.min.js


Google Fonts: Lora, Montserrat, Roboto for typography.
Included in HTML <head> (no external setup needed).



No local installations are required, as all dependencies are loaded via CDNs.
Testing
To ensure the project works as expected:

Homepage (index.html):

Confirm mountain.png, menu-btn.png, about.webp, img1.png, img2.png load.
Hover over "Explore More" to see zoom-in effect.
Hover over About image (about.webp) for zoom-in.
Hover over each comic card to verify zoom-in animation.
Test dark mode toggle and scroll-to-top button.


Comics Gallery (comics-gallery.html):

Verify all nine comic covers load (img1.png, watchemen.png, good bye, eri.png, etc.).
Check hover effects ("Read Now" overlay).
Click each comic to navigate to comic-details.html?id=<id>.


Comic Details (comic-details.html):

Test IDs 1–9 (e.g., http://localhost:8000/comic-details.html?id=4 for Watchmen).
Ensure cover images and PDFs load (PDF.js or <iframe> fallback).
Verify page navigation and download button.
Check console for PDF errors, especially for IDs 4–9.


Responsiveness:

Resize browser to 850px (navbar collapses), 600px (smaller fonts), 470px (stacked layout).
Confirm animations work across breakpoints.


Error Handling:

If images/PDFs are missing, console logs will indicate net::ERR_FILE_NOT_FOUND.
Replace missing files in assets/img/ or assets/pdfs/ to resolve.



Contributing
This is an academic project submitted as part of an MCA curriculum. Contributions are not accepted, but feedback from instructors or peers is welcome for evaluation purposes.
License
This project is for academic purposes only and not licensed for commercial use. All curated comics (e.g., Batman & Spiderman, Watchmen) are sourced from public repositories, and Spectrum Squad is an original creation by Team Three.
Credits

Developed by: Team Three (MCA students)
Resources:
Spectrum Squad: Created using generative AI tools for images and dialogues.
Curated comics: Sourced from public repositories.
FontAwesome, jQuery, PDF.js: Open-source libraries via CDN.
Google Fonts: Lora, Montserrat, Roboto for typography.



Created with ❤️ for visual storytelling and accessibility.
