from app import create_app
import os 
from dotenv import load_dotenv

# accionar que permite levantar la app
config_name = os.getenv('FLASK_CONFIG') or 'default'
app = create_app(config_name)

if __name__ == '__main__':
    app.run()