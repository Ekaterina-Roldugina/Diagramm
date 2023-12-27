import uvicorn
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from database.db_manager import base_manager
from settings import SCRIPTS_TABLES_PATH, SCRIPTS_RIMARY_DATA_PATH
from routers import (fauna_router, artifacts_router, pictures_router, archaeologists_router,
                     excavations_router, investigations_router)

app = FastAPI()

app.include_router(artifacts_router, prefix='/artifacts')
app.include_router(fauna_router, prefix='/fauna')
app.include_router(pictures_router, prefix='/pictures')
app.include_router(archaeologists_router, prefix='/archaeologists')
app.include_router(excavations_router, prefix='/excavations')
app.include_router(investigations_router, prefix='/investigations')



@app.get('/')
def root():
    return RedirectResponse('/docs')


if __name__ == '__main__':
    if not base_manager.check_base():
        base_manager.create_base(SCRIPTS_TABLES_PATH, SCRIPTS_RIMARY_DATA_PATH)
    uvicorn.run(app="start_server:app", host="127.0.0.1",  port=8000, reload=True)