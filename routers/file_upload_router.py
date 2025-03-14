from fastapi import UploadFile, File, APIRouter
from services import file_upload_service

router = APIRouter()

@router.post("/file-upload")
async def upload_file(file: UploadFile):
  return await file_upload_service.upload_file(file)