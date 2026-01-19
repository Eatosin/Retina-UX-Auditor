from fasthtml.common import fast_app
from src.web.routes.analyze import analyze_route

# Initialize FastHTML with explicit static file handling if needed
app, rt = fast_app()

# Register Routes
analyze_route(app)

# Expose 'app' for Uvicorn/Docker
application = app