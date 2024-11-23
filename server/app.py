#import logging

from fastapi import FastAPI

from .api import router_api

#logger= logging.getLogger(__name__)
app = FastAPI()

# Incluimos el reouter principal a la instancia de FastAPI
app.include_router(router_api)

#@app.on_event('startup')
#async def startup_event():
#    print('\033[92m', 'API Iniciada', '\033[0m')
#    logger.debug('API Iniciada')
    

#@app.on_event('shutdown')
#def shutdown_event():
#    print('\033[91m', 'API Finalizada', '\033[0m')
#    logger.debug('API Finalizada')