from fastapi import FastAPI

app = FastAPI()


@app.get("/health")
def status():
    return {"message": "Water Conditions API", "status": "Running"}
