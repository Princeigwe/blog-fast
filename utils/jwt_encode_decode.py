import os
from dotenv import load_dotenv
import jwt
from jwt.exceptions import InvalidTokenError
from datetime import datetime, timedelta, timezone

load_dotenv()


expiry_time = datetime.now(timezone.utc) + timedelta(days=1)

SECRET_KEY = os.environ.get("JWT_SECRET")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_DAYS = 1

async def create_access_token(payload: dict):
  payload["exp"] = expiry_time
  token = jwt.encode(payload, SECRET_KEY, ALGORITHM)
  return token



async def decode_access_token(token):
  try:
    decoded_data = jwt.decode(jwt=token, key=SECRET_KEY, algorithms=[ALGORITHM])
    return decoded_data
  except InvalidTokenError as e:
    raise Exception( f"Invalid  token: {e}" )