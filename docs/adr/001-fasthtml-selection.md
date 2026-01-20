# ADR 001: Adoption of FastHTML over Streamlit

*   **Status:** Accepted
*   **Date:** 2026-01-20
*   **Author:** Owadokun Tosin Tobi

## Context
We needed a web framework to serve the Retina UI. The standard choice for Python AI apps is **Streamlit**.

## Decision
We chose **FastHTML**.

## Reasoning
1.  **Latency:** FastHTML serves raw HTML/HTMX, eliminating Streamlit's WebSocket overhead for faster mobile loading in low-bandwidth regions.
2.  **Styling:** FastHTML allows direct CSS/Class manipulation, enabling the custom "Glassmorphism" UI that Streamlit's iframe sandbox restricts.
3.  **Docker Size:** Removes heavy data-science dependencies required by Streamlit, resulting in a lighter container.

## Consequences
*   **Positive:** Faster load times, pixel-perfect CSS control.
*   **Negative:** Requires more boilerplate code for routing compared to Streamlit.