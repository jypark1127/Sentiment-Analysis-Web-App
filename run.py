## this file is used to run Flask application
import sys
sys.path.insert(0, '/Users/JuYoung/Projects(azure)/Sentiment-Analysis-Web-App/app')

from app import app

if __name__ == '__main__':
    app.run(debug=True)

