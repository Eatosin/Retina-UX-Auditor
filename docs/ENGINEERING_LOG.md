# 🛠️ Engineering Log: Building Retina

**Date:** January 2026
**Lead Architect:** Owadokun Tosin Tobi
**Status:** Production Stable

## 📋 Executive Summary
Retina represents a shift from "Wrapper" architectures to "Hybrid Inference" systems. This log documents the critical engineering challenges encountered while integrating deterministic Computer Vision (OpenCV) with probabilistic LLMs (Gemini) in a serverless Docker environment.

---

## 1. The "Headless" Vision Challenge
### 🔴 The Issue
Early builds failed on deployment with `ImportError: libGL.so.1: cannot open shared object file`.
*   **Context:** Computer Vision libraries usually expect a GUI (windowing system). Cloud containers (Docker/Render/HF) are "Headless" (no screen).
*   **Root Cause:** The base `python:3.11-slim` image lacks the low-level graphics drivers required by OpenCV's C++ core.

### 🟢 The Fix: Infrastructure Layering
We rebuilt the `Dockerfile` to inject system-level dependencies before the Python layer.
```dockerfile
# Added to Dockerfile
RUN apt-get update && apt-get install -y libgl1 libglib2.0-0
```
**Outcome:** Stability in serverless environments without the bloat of a full OS windowing system.

---

## 2. The Saliency Dependency Conflict
### 🔴 The Issue
The Saliency Engine threw `AttributeError: module 'cv2' has no attribute 'saliency'`.
*   **Root Cause:** The standard `opencv-python-headless` package only contains the core modules. The Saliency algorithms (Spectral Residual) reside in the "Contrib" (Community/Experimental) modules.
*   **The Fix:** Migrated dependency from `opencv-python-headless` to `opencv-contrib-python-headless`.

---

## 3. The Quality Gate Implementation (Type Safety)
### 🔴 The Issue
Initial code reviews failed strict Type Checking (`MyPy`).
*   **Context:** OpenCV (`cv2`) does not provide standard type stubs, leading to `import-untyped` errors. Furthermore, NumPy returns `np.float64` types which caused type-mismatches when functions promised a standard Python `float`.
*   **The Fix:** 
    1. Configured `pyproject.toml` to handle C-extension libraries gracefully.
    2. **Refactor:** Explicitly cast NumPy return types to Python native types (`float(score)`) in `entropy.py` to ensure JSON serialization compatibility in the FastHTML frontend.

---

## 4. The Model Availability Fallback
### 🔴 The Issue
Targeting **Gemini 3.0 Flash (Preview)** introduced availability risks in certain cloud regions.
*   **The Fix:** Implemented a **Smart Router** in `src/core/ai/vision_client.py`.
*   **Logic:** The system attempts to handshake with the SOTA model (3.0). If the API returns a 4xx/5xx error, it gracefully degrades to the Stable model (2.5 Flash) without user interruption.

---

## 5. Architectural Decision: FastHTML vs Streamlit
We opted for **FastHTML** over Streamlit to reduce container size and improve mobile latency.
*   **Result:** The Docker image is significantly lighter than equivalent Streamlit builds by removing heavy dependencies (Arrow, Protobuf) required by Streamlit's WebSocket architecture. This aligns with our "Mobile-First Engineering" mandate.

---