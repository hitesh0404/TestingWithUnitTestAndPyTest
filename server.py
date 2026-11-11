from fastapi import FastAPI,Request

app = FastAPI()

@app.get("/get_data/{id}")
def get_data(id:int):
    data = {
        "id":id,
        "name":"Rupam",
        "subject":"AI"
    }

    return data


@app.post("/post_data")
async def post_data(request:Request ):
    payload = await request.json()
    print(payload)
    return {
            "id" : payload.get("id"),
            "name": payload.get("name")    
            }