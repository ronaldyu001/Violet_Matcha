from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware



# --- create FastAPI app ---
app = FastAPI()


# ----- Allow your frontend origin(s) -----
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],   # <-- must allow OPTIONS
    allow_headers=["*"],   # <-- allow Content-Type: application/json, etc.
)


# ----- register routes -----


# ----- startup events -----
