from api import create_app
from api.config import *

if __name__ == "__main__":
    app = create_app(DevelopmentConf)
    app.run()