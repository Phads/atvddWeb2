from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class OperationInputs(BaseModel):
    op1: float
    op2: float

@app.get("/mult")
def soma(op1: float, op2: float):
    if op1 is None or op2 is None:
        raise HTTPException(status_code=400, detail="op1 ou op2 não informado")
    result = op1 * op2
    return {"resultado": result}
