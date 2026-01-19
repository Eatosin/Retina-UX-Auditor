from fasthtml.common import Div, Form, Label, Input, Button, Grid, H3, P, Img, H4
from src.utils.image_processing import load_image_from_bytes, resize_image, encode_image_to_base64
from src.core.physics.entropy import EntropyEngine
from src.core.physics.contrast import ContrastEngine
from src.core.physics.saliency import SaliencyEngine
from src.core.ai.vision_client import DesignCritic
from src.web.components.layout import Layout
import uvicorn

# Initialize Engines
entropy_engine = EntropyEngine()
contrast_engine = ContrastEngine()
saliency_engine = SaliencyEngine()
ai_critic = DesignCritic()

def analyze_route(app):
    
    @app.route("/", methods=["GET"])
    def home():
        return Layout("Retina | UX Auditor", [
            Div(
                Form(
                    Label("Upload UI Screenshot (PNG/JPG)"),
                    Input(type="file", name="file", accept="image/*", required=True),
                    Button("Run Physics Audit", cls="contrast"),
                    hx_post="/analyze",
                    hx_target="#results",
                    hx_swap="innerHTML",
                    hx_encoding="multipart/form-data",
                    cls="upload-box"
                ),
                id="upload-container"
            ),
            Div(id="results") # Target for HTMX
        ])

    @app.route("/analyze", methods=["POST"])
    async def analyze_ui(request):
        try:
            form = await request.form()
            file = form["file"]
            file_bytes = await file.read()
            
            # 1. Preprocessing
            original_img = load_image_from_bytes(file_bytes)
            processed_img = resize_image(original_img)
            
            # 2. Physics Analysis
            clutter_score = entropy_engine.calculate_clutter_score(processed_img)
            contrast_val = contrast_engine.calculate_rms_contrast(processed_img)
            contrast_verdict = contrast_engine.get_accessibility_verdict(contrast_val)
            
            # 3. Saliency Heatmap
            heatmap_img = saliency_engine.generate_heatmap(processed_img)
            focus_score = saliency_engine.get_focus_score(processed_img)
            
            # Convert images for display
            b64_heatmap = encode_image_to_base64(heatmap_img)
            
            # 4. AI Criticism
            metrics = {
                "clutter_score": clutter_score,
                "contrast_verdict": contrast_verdict,
                "focus_score": focus_score
            }
            ai_report = ai_critic.analyze(file_bytes, metrics)
            
            # 5. Render Results
            return Div(
                # Metrics Row
                Grid(
                    Div(H3(f"{clutter_score}%"), P("Visual Entropy"), cls="card"),
                    Div(H3(f"{focus_score}%"), P("Focus Score"), cls="card"),
                    Div(H3(contrast_verdict.split(":")[0]), P("Contrast"), cls="card"),
                ),
                
                # Visuals Row
                Div(
                    H3("Attention Heatmap (Saliency)"),
                    Img(src=b64_heatmap, cls="heatmap"),
                    cls="card"
                ),
                
                # AI Report
                Div(
                    H3("AI Design Audit"),
                    Div(ai_report, style="white-space: pre-wrap;"),
                    cls="card"
                )
            )
            
        except Exception as e:
            return Div(
                H4("Analysis Failed"),
                P(str(e)),
                style="color: #ff8080; background: #3d1a1a; padding: 20px; border-radius: 10px;"
            )
