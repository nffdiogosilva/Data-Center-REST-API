from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import DataCenterSetupSerializer


@api_view(['GET'])
def best_datacenter_setup(request):
    """
    API View responsible of returning the minimum DEs necessary and the best Data Center for a given
    Data Centers Setup.
    """

    serializer = DataCenterSetupSerializer(data=request.GET)

    if serializer.is_valid(): # Make sure the data is valid first
        # If everything is okay with the data than return the expected output
        return Response(serializer.get_return_data(), status=status.HTTP_200_OK)
        
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
