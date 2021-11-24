# sanic-otel-splunk
Testing - Instrumenting Sanic framework with Opentelemetry

Test with python 3.8.10, sanic 20.12.2

Step to instrument
1. pip install -r requirements.txt
2. install Splunk Otel Collector
3. export required parameters
```
export OTEL_SERVICE_NAME='xxx'
export OTEL_EXPORTER_OTLP_ENDPOINT='http://localhost:4317'
export OTEL_RESOURCE_ATTRIBUTES='deployment.environment=xxx'
```
4. run 
```
python3 app.py
```
7. check span by running 
```
lynx http://localhost:55679/debug/tracez
```
