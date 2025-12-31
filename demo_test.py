from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
 
app = FastAPI(title="Simple Calculator API", version="1.0")
 
 
# -----------------------------
# Request Models
# -----------------------------
class CalculationRequest(BaseModel):
    operation: str
    a: float
    b: float
 
 
class BatchCalculationRequest(BaseModel):
    calculations: List[CalculationRequest]
 
 
# -----------------------------
# Core Calculator Logic
# -----------------------------
def calculate(operation: str, a: float, b: float):
    operation = operation.lower()
 
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "modulus":
        return a % b
    else:
        raise HTTPException(
            status_code=400,
            detail="Invalid operation. Allowed: add, subtract, multiply, modulus"
        )
 
 
# -----------------------------
# API Endpoints
# -----------------------------
@app.post("/calculate")
def single_calculation(request: CalculationRequest):
    result = calculate(request.operation, request.a, request.b)
 
    return {
        "operation": request.operation,
        "a": request.a,
        "b": request.b,
        "result": result
    }
 
 
@app.post("/calculate/batch")
def batch_calculation(request: BatchCalculationRequest):
    results = []
 
    for calc in request.calculations:
        result = calculate(calc.operation, calc.a, calc.b)
        results.append({
            "operation": calc.operation,
            "a": calc.a,
            "b": calc.b,
            "result": result
        })
 
    return {
        "total_calculations": len(results),
        "results": results
    }
 
 
# -----------------------------
# Health Check
# -----------------------------
@app.get("/health")
def health_check():
    return {"status": "Calculator API is running"}


# -----------------------------
# Health Check
# -----------------------------

@app.get("/health")




