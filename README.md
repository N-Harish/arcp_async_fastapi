# arcp_async_fastapi

* The project is a REST API deployed using FastAPI
* We've used transfer learning on resnet50 model to detect age of person given image
* The API expects a base64 encoded string as input 
* I've used UTKFACE dataset for training
* The model was trained using tensorflow 2.0
* Then it was converted to onnx format
* The model achieved a rmse of 5
* You can also run the project using docker 

## steps to run project using docker
* Build image ```docker build -t <image_name>``` replace <image_name> with the name of your docker image
* Run docker ```docker run --name <name_of_container> <image_name>``` replace <name_of_container> with your container name
