from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
import httpx

app = FastAPI()

# Define service URLs
SERVICE_URLS = {
    "address_book": "http://address_book_service:8000",
    "container": "http://container_service:8000",
    "draft": "http://draft_service:8000",
    "payment": "http://payment_service:8000",
    "quote": "http://quote_service:8000",
    "tariff": "http://tariff_service:8000",
}

@app.api_route("/{path:path}", methods= ["GET", "POST", "PUT", "DELETE"])
async def getway(request: Request, path: str):
    # Determine which service to route to based on the path
    service = next((s for s in SERVICE_URLS if path.startswith(s)), None)
    if not service:
        raise HTTPException(status_code=404, detail="Service not found")
    
    # Construct the full URL for the downstream service
    url = f"{SERVICE_URLS[service]}/{path}"

    # Forwad the request to the appropiete service 
    async with httpx.AsyncClient() as client:
        response = await client.request(
            method=request.method,
            url=url,
            headers=request.headers,
            params=request.query_params,
            content=await request.body()
        )

    # Return the response from the downstream service
    return JSONResponse(
        content=response.json(),
        status_code=response.status_code,
        headers=dict(response.headers)
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)



