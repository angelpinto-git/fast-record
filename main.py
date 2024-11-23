import uvicorn

from server.configs import app_settings as settings

if __name__ == '__main__' :
    uvicorn.run('server.app:app', host='localhost', port=settings.PORT, reload=settings.DEV)