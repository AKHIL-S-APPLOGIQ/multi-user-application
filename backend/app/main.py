import uvicorn
from configuration.config import main_app

# Base.metadata.create_all(bind=engine)

from api.student.router import user,app

main_app.include_router(user)    
main_app.include_router(app)

if __name__ == "__main__":
    uvicorn.run("main:main_app", host="127.0.0.1", port=7000, reload=True)
