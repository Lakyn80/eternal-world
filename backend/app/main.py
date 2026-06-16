from fastapi import FastAPI

app = FastAPI(title="Eternal World API")

@app.get("/")
def root():
    return {"message": "Eternal World API is running"}

@app.get("/health")
def health():
    return {"status": "ok"}
