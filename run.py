from app import create_app # import the flask app from the function that creates it.

CONFIG_TYPE = "development" # set the necessary config enviroment from the config.py file
app = create_app(CONFIG_TYPE)

if __name__ == '__main__': # run the flask app
    app.run()