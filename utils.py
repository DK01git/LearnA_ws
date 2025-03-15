import os
from dotenv import load_dotenv, find_dotenv

# tload env diel                                                                                                                    
def load_env():
    _ = load_dotenv(find_dotenv())



# load groc api key
def get_groc_api_key():
    load_env()
    groc_api_key = os.getenv("GROQ_API_KEY")
    return groc_api_key

