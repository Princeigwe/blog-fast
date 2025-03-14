from fastapi import File, UploadFile
from utils.s3_media import media_upload

async def upload_file(file: UploadFile = File(...)):
  file_name = file.filename
  file_content = file.file.read()
  return media_upload(file_name, file_content)