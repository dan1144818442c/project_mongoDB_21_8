from fastapi import FastAPI ,Request
from  manager import  Manager
import uvicorn
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
uri = os.environ.get("uri")
db_name = os.environ.get("db_name")

app = FastAPI(title="Data Loader API (MongoDB)")

manager1 = Manager(uri=uri , db_name=db_name)

@app.get("/data")
async def get_data():
    return  manager1.get_df_as_list_of_json()

if __name__ == "__main__":

    uvicorn.run(app, host="localhost", port=8000)
