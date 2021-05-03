from datetime import datetime

from rest_framework import status
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


@api_view()
@permission_classes((AllowAny,))
def ping(request):
    base_url = f"{request.scheme}://{request.get_host()}{request.path}"
    doc_url = base_url + 'api/v1/docs/'
    api_root_url = base_url + 'api/v1/'

    return Response(
        {
            "error": False,
            "time-stamp": datetime.now(),
            "api_root": api_root_url,
            "docs": doc_url,
        },
        status=status.HTTP_200_OK)
