import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        "frameworks.web.api:app",
        host="0.0.0.0",
        port=8000,
        reload=True  # ← Solo para desarrollo
    )