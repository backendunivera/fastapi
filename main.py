from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def f_index():
    return {
        "FIO": "Иванов Николай Алексеевич"
    }


@app.get('/tools')
async def f_index_t():
    return {
        "PhoneNumber": "88005553535"
    }


@app.get('/users')
async def f_index_u():
    return {
        "skill1": "skill1",
        "skill2": ["skill2_1", "skill2_2"]
    }