from fastapi import FastAPI, Form

app = FastAPI(debug=True)
users = {}
@app.post("/api/factorial")
async def fac(number : int = Form(), action : str = Form()): 
    if action != 'factorial':
        return {
            "status":"0",
            "message":"Please type 'factorial'"
        }
    else:
        result = 1
        for i in range(1, number+1):
            result *= i
        return {
            "status": 1,
            "parameter": number,
            "action": "factorial",
            "result": result
}   

@app.post("/api/median")
async def med(numbers: list = Form(), action: str = Form()):
    
    if action != 'median':
        return {
            "status":"0",
            "message":"Please type 'median'"
        }
    result = 0
    if action == 'median'and len(numbers) % 2 != 0:
        numbers = [int(num) for num in numbers]
        result = numbers[len(numbers)//2] 
        return {
                "status": 1,
                "parameter": numbers,
                "action": "median",
                "result": result
}
    if action == 'median'and len(numbers) % 2 == 0:
        numbers = [int(num) for num in numbers]
        result = (numbers[len(numbers)//2-1] + numbers[len(numbers)//2])/2   
        return {
                "status": 1,
                "parameter": numbers,
                "action": "median",
                "result": result
        } 
@app.post("/api/variance")
async def var(numbers: list = Form(), action: str = Form()):
    
    if action != 'variance':
        return {
            "status":"0",
            "message":"Please type 'variance'"
        }
    else:
        numbers = [int(num) for num in numbers]
        mean = sum(numbers) / len(numbers)
        squared_diffs = [(x - mean) ** 2 for x in numbers]
        sum_squared_diffs = sum(squared_diffs)
        result = sum_squared_diffs / (len(numbers) - 1)
        return {
                "status": 1,
                "parameter": numbers,
                "action": "variance",
                "result": result
        }
@app.post("/api/pstdev")
async def pstdev(numbers: list = Form(), action: str = Form()):  
    if action != 'standard':
        return {
            "status":"0",
            "message":"Please type 'variance'"
        }
    else:
        numbers = [int(num) for num in numbers]
        mean = sum(numbers) / len(numbers)
        squared_diffs = [(x - mean) ** 2 for x in numbers]
        variance = sum(squared_diffs) / (len(numbers) - 1)
        result = variance ** 0.5
        return {
                "status": 1,
                "parameter": numbers,
                "action": "standard",
                "result": result
        }