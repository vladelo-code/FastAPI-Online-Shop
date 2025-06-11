import uvicorn
from fastapi import FastAPI

from ecommerce.user.router import router as user_router

app = FastAPI(title='Vladelo Online Shop', version='0.0.1')
app.include_router(user_router)

if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=8000, reload=True)
