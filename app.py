from sanic import Sanic
from sanic import response
from opentelemetry import trace,baggage
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
import os

app = Sanic(__name__)

# Resource can be required for some backends, e.g. Splunk
# If resource wouldn't be set - traces wouldn't appears in Splunk
resource = Resource(attributes={
    "service.name": os.getenv('OTEL_SERVICE_NAME')
})
trace.set_tracer_provider(TracerProvider(resource=resource))
tracer = trace.get_tracer(__name__)
otlp_exporter = OTLPSpanExporter(endpoint=os.getenv('OTEL_EXPORTER_OTLP_ENDPOINT'), insecure=True)
span_processor = BatchSpanProcessor(otlp_exporter)
trace.get_tracer_provider().add_span_processor(span_processor)

# app.py
@app.route("/")
async def test(request):
    # start new span
        with tracer.start_as_current_span("ww-span"):
                return response.json({"test": True})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)
