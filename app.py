from app import create_app
import os

app = create_app()
# This line explicitly tells Flask where to find your templates
app.template_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')

# This new line explicitly tells Flask where to find your static files
app.static_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')

if __name__ == "__main__":
    app.run(debug=True)