from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routers import courier, uploads

app = FastAPI(title="ALUR Logistik API", version="1.0.0")

# Mount folder static untuk akses file upload foto proof
app.mount("/static", StaticFiles(directory="static"), name="static")

# Daftarkan router kurir dan uploads
app.include_router(courier.router)
app.include_router(uploads.router)

@app.get("/")
async def root():
    return {"message": "ALUR Logistik API is running!"}