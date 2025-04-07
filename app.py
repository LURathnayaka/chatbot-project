from flask import Flask, render_template, request, jsonify
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()  

app = Flask(__name__)


llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", google_api_key=os.getenv("GOOGLE_API_KEY"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def get_response():
    user_message = request.form["message"]
    
    try:
        
        response = llm.invoke(user_message)
        return jsonify({"response": response.content})
    except Exception as e:
        return jsonify({"response": f"Sorry, an error occurred: {str(e)}"})

if __name__ == "__main__":
    app.run(debug=True)