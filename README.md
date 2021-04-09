# arcp_async_fastapi

* The project is a REST API deployed using FastAPI
* We've used transfer learning on resnet50 model to detect age of person given image
* The API expects a base64 encoded string as input 
* I've used UTKFACE dataset for training
* The model was trained using tensorflow 2.0
* Then it was converted to onnx format
* The model achieved a rmse of 5
