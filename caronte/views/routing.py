from fastapi import APIRouter


router = APIRouter()


@router.get('/xd')
async def root_again():
    return {'message': 'Hello World xd'}
