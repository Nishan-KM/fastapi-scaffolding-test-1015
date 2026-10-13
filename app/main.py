from fastapi import FastAPI

app = FastAPI(title="SSP Generated Service")

@app.get("/health")
def health():
    return {"status": "ok"}
