from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "TikTok USDS API is running"}

@app.get("/data")
def get_data():
    data = [
        {"user_id": 1, "region": "US", "data_center": "Texas", "status": "Compliant"},
        {"user_id": 2, "region": "EU", "data_center": "Frankfurt", "status": "Non-Compliant"},
        {"user_id": 3, "region": "US", "data_center": "California", "status": "Compliant"}
    ]
    return {"users": data}
