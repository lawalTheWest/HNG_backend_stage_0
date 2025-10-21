from datetime import datetime
from django.shortcuts import render
from django.utils import timezone
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
import requests

@api_view(['GET'])
def profile_endpoint(request):
    """
    GET /me endpoint that returns profile information with a dynamic cat fact
    """
    try:
        # Fetch cat fact from external API with timeout
        cat_fact_response = requests.get(
            'https://catfact.ninja/fact',
            timeout=5  # 5 second timeout
        )
        cat_fact_response.raise_for_status()
        cat_fact = cat_fact_response.json().get('fact', 'No cat fact available')
    except requests.exceptions.Timeout:
        cat_fact = 'Cat fact service timed out'
    except requests.exceptions.RequestException as e:
        cat_fact = 'Unable to fetch cat fact at this time'
    except Exception as e:
        cat_fact = 'Error retrieving cat fact'
    
    # Get current UTC timestamp in ISO 8601 format
    current_timestamp = datetime.utcnow().isoformat(timespec='milliseconds') + 'Z'
    
    # Build response data
    response_data = {
        "status": "success",
        "user": {
            "email": "lwltjdn@gmail.com",
            "name": "Lawal Tajudeen Ogunsola",
            "stack": "Python/Django REST Framework"
        },
        "timestamp": current_timestamp,
        "fact": cat_fact
    }
    
    return Response(response_data, status=status.HTTP_200_OK)