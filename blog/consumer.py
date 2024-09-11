from multiprocessing import Pool
import redis
import json
from elasticsearch import Elasticsearch

redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)
es = Elasticsearch([{'scheme': 'http', 'host': 'localhost', 'port': 9200}])

def consume_queue():
    while True:
        blog_data = redis_client.blpop('blog_queue')

        if blog_data:
            blog = json.loads(blog_data[1])
            print(f"Processing blog: {blog['title']}")
            es.index(index='blogs', body={
                'title': blog['title'],
                'text': blog['text'],
                'user_id': blog['user_id']
            })
            print(f"Indexed blog: {blog['title']}")

def execute():
    """Execute function that starts the processing pool to run the blog task asynchronously."""
    pool_size = 1 
    pool = Pool(pool_size)
    pool.apply_async(consume_queue) 
    pool.close() 
    pool.join()   

# Start execution
if __name__ == '__main__':
    execute()
