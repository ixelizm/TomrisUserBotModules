from fastapi import FastAPI
import glob
app = FastAPI()


@app.get("/modules")
async def index():
    modules = glob.glob("modules/*.py")
    temp = {}
    for module in modules:
        with open(module, "r") as f:
            file_content = f.read()
            file_name = module.split("/")[-1].replace(".py", "")
            temp[file_name] = file_content
    return temp
