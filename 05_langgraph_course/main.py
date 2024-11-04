from dotenv import load_dotenv

load_dotenv()

from graphs.graph import app

if __name__ == "__main__":
    print("Hello Advanced RAG")
    print(app.invoke(input={"question": "야구에서 홈런이 뭐야?"}))
