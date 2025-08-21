from fastapi import FastAPI ,Request
from  manager import  Manager
import uvicorn
app = FastAPI(title="Data Loader API (MongoDB)")

manager1 = Manager()

@app.get("/data")
async def get_data():
    return  manager1.get_df_as_list_of_json()

if __name__ == "__main__":

    uvicorn.run(app, host="localhost", port=8000)
