from fasthtml.common import *

def Layout(title: str, content: list):
    """
    Main application layout with dark mode styling and HTMX support.
    """
    return Html(
        Head(
            Title(title),
            Meta(charset="utf-8"),
            Meta(name="viewport", content="width=device-width, initial-scale=1"),
            # PicoCSS for instant professional styling
            Link(rel="stylesheet", href="https://cdn.jsdelivr.net/npm/@picocss/pico@latest/css/pico.min.css"),
            # Custom Styles for Retina
            Style("""
                :root { --primary: #00E5FF; --background: #0f172a; --card-bg: #1e293b; }
                body { background-color: var(--background); color: white; max-width: 1200px; margin: 0 auto; padding: 20px; }
                .card { background: var(--card-bg); padding: 20px; border-radius: 10px; border: 1px solid #334155; margin-bottom: 20px; }
                .metric { font-size: 2em; font-weight: bold; color: var(--primary); }
                .heatmap { width: 100%; border-radius: 8px; border: 1px solid #334155; }
                .upload-box { border: 2px dashed #334155; padding: 40px; text-align: center; border-radius: 10px; cursor: pointer; }
                .upload-box:hover { border-color: var(--primary); background: rgba(0, 229, 255, 0.05); }
                h1, h2, h3 { color: white; }
            """),
            Script(src="https://unpkg.com/htmx.org@1.9.10")
        ),
        Body(
            Header(
                H1("Retina", style="margin-bottom: 0;"),
                P("Visual Physics & UX Audit Engine", style="color: #94a3b8;"),
                style="border-bottom: 1px solid #334155; padding-bottom: 20px; margin-bottom: 40px;"
            ),
            Main(*content),
            Footer(
                P("Powered by OpenCV + Gemini 2.5 model", style="text-align: center; opacity: 0.5; font-size: 0.8rem;")
            )
        )
    )