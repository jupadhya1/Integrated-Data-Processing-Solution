import faust
from typing import List
import requests
import json

app = faust.App(
    'credit_score_app',
    broker='kafka://localhost:8088',
    value_serializer='raw',
)

kafka_topic = app.topic('test')

@app.agent(kafka_topic)
async def process(transactions):
    async for value in transactions:
        result = requests.post('http://127.0.0.1:5000/invocations', json=json.loads(value))
        print('Input data: ' + str(value))
        print('Credit Score result: ' + str(result.json()))

if __name__ == '__main__':    
    # run the consumer
    app.main()
