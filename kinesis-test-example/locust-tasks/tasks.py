from locust import Locust, TaskSet, task
from boto import kinesis
import time
import gevent
import json
from locust.events import request_success
from locust.events import request_failure

class KinesisTaskSet(TaskSet):
    def on_start(self):
        conn = kinesis.connect_to_region(region_name = "ap-northeast-1")
        self.conn = conn
        print(self.conn)
        
    @task
    def put_record(self):
        start_at = time.time()
        print(start_at)
        try:
            res = self.conn.put_record(
                stream_name="test-stream",
                data="test",
                partition_key="partition_key1"
            )
            print(res)
            request_success.fire(
                request_type='Kinesis put record',
                name='test-stream',
                response_time=int((time.time() - start_at) * 1000),
                response_length=len(json.dumps(res)),
            )
        except Exception as e:
            print(e)
            request_failure.fire(
                request_type='Kinesis put record',
                name='test-stream',
                response_time=int((time.time() - start_at) * 1000),
                exception=e
            )

class KinesisLocust(Locust):
    task_set = KinesisTaskSet
    min_wait = 100
    max_wait = 100
