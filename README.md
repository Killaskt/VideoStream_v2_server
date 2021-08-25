# VideoStream_v2_server
Server Side for the video stream application


Most ineffcient way to create a livestreaming server. Expecting real time data via HTTPS POST is impossible.

Strategies taken after:
- HTTPS POST + Queue (Kafka is poissble, used RabbitMQ)
- Pure Sockets
- Websocket
- Something not looked into but should have been is a MQTT implementation

Best way to achieve this is by making the thing that is recording into its own web server, however, due to constraints in this project that was impossible.

Latency was off the charts in a bad way. New strategy has been taken although that repo is private.
