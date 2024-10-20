from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # replace '*' with our own origin link
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "basic screen"}

@app.post("/upload_resume")
async def upload_resume(file: UploadFile = File(...)):
    # Process the resume file, parse it for text
    # Embed it in the vector database
    return {"message": "Resume uploaded and embedded"}

@app.get("/parse_resume/{user_id}")
async def parse_resume(user_id: int):
    # Retrieve the embedded resume, extract info (e.g., name, skills)
    return {"parsed_data": "Relevant info extracted"}

@app.post("/generate_suggestions/{user_id}")
async def generate_suggestions(user_id: int):
    # Run parsed resume data through a generative AI model (e.g., OpenAI API)
    suggestions = "Generated suggestions based on resume"
    return {"suggestions": suggestions}

@app.get("/suggestions/{user_id}")
async def get_suggestions(user_id: int):
    # Fetch the suggestions from the database or cache
    return {"suggestions": "AI suggestions for the resume"}

