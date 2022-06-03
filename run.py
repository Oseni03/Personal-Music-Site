from app import create_app
from app.myadmin.admin import *
app = create_app()


if __name__ == "__main__":
    app.run()
    
