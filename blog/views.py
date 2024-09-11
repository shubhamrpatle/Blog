from elasticsearch import Elasticsearch
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import BlogSerializer
import redis
import json

redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

class BlogSubmissionView(APIView):
    def post(self, request):
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            # Push the blog data to the Redis queue
            blog_data = json.dumps(serializer.validated_data)
            redis_client.rpush('blog_queue', blog_data)
            return Response({'message': 'Blog submitted to queue'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BlogSearchView(APIView):
    def get(self, request):
        query = request.query_params.get('q')
        if not query:
            return Response({'error': 'Search query missing'}, status=status.HTTP_400_BAD_REQUEST)

        es =Elasticsearch([{'scheme': 'http', 'host': 'localhost', 'port': 9200}])
        search_result = es.search(index='blogs', body={
            'query': {
                'multi_match': {
                    'query': query,
                    'fields': ['title', 'text']
                }
            }
        })

        return Response(search_result['hits']['hits'], status=status.HTTP_200_OK)
