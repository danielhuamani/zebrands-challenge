from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class SmallPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link(),
            },
            'pages': {
                'total_pages': self.page.paginator.num_pages,
                'count': self.page.paginator.count,
                'current': self.page.number
            },
            'results': data
        })
