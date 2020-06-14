from main.main import flask_app


#print(flask_app.config)

if __name__ == '__main__':    
    flask_app.run('0.0.0.0', 5000)