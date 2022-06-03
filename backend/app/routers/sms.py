from fastapi import APIRouter
from app import schemas
import boto3

router = APIRouter()

@router.post(
    "/sendsms",
    summary="Send SMS with cart list"
)
async def send_sms(sms: schemas.SMS):
    sns = boto3.client('sns', region_name='us-east-1')
    response = sns.list_sms_sandbox_phone_numbers(MaxResults=30)
    print(response)
    user_phone = next(
        (phone for phone in response['PhoneNumbers'] if phone["PhoneNumber"] == sms.number), None)
    if user_phone == None or user_phone['Status'] == 'Pending':
        sns.create_sms_sandbox_phone_number(
            PhoneNumber=sms.number,
            LanguageCode='es-ES'
        )
        response = 'Not Verified'
    else:
        sns.publish(PhoneNumber=sms.number, Message=sms.message)
        response = 'Verified'
    return response
