Prerequiste:
Faust: stream processing library, using the async/away paradigm and requires python 3.6+
Kafka: we will use the confluent version for kafka as our streaming platform
MLFlow: an open-source platform used to monitor and save machine learning models after training

Step1:
Serving the model as rest API:
mlflow.sklearn.save_model(model, path='./credit_card_score_prediction')


Step2:
start a terminal in the root of our project and type the following command:
mlflow models serve -m credit_card_score_prediction

Listening at: http://127.0.0.1:8088

Step3:
docker-compose up
The docker-compose will start zookeper on port 2181 , a kafka broker on port 8088

Step4:
faust -A predict_credit_score_worker worker -l info

Unit Test Case:
!curl http://127.0.0.1:5000/inAttributeocations -H 'Content-Type: application/json' -d '{
    "columns":["Attribute1","Attribute2","Attribute3","Attribute4","Attribute5","Attribute6","Attribute7","Attribute8","Attribute9","Attribute10","Attribute11","Attribute12","Attribute13","Attribute14","Attribute15","Attribute16","Attribute17","Attribute18","Attribute19","Attribute20","Attribute21","Attribute22","Attribute23","Attribute24","Attribute25","Attribute26","Attribute27","Attribute28","Amount"],
    "data":[[12.8,0.029,0.48,0.98,6.2,29.1,3.33,1.2,0.39,75.1,0.66,1.2,1.3,44.2,12.8,0.029,0.48,0.98,6.2,29,3.33,1.2,0.39,75.3,0.66,1.2,1.3,44.2,1.1]]
}'
