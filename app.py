from flask import Flask
from blog import blog_bp

app = Flask(__name__)

app.register_blueprint(blog_bp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)