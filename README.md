# VideoStream_v2_server
Server Side for the video stream application

Stay away from this code. This is 2nd most ineffcient way to create a livestreaming server. Wrote this very early on into the project, this was development code to understand project + constraints more.


The worst version of this project was when there was a server sending data via HTTPS, expecting real time data via HTTPS POST is impossible.
Latency was off the charts in a bad way.


### Some thoughts if you randomly find this in a google entry:

trust me i've been there many times

#### Strategies + ideas:
- HTTPS POST + Queue (Kafka is poissble, used RabbitMQ)
- Pure Sockets (current repos)
- Websocket
- Something not looked into but should have been is a MQTT implementation
- have python run a ffmpeg terminal command to transform desired video into HLS package, then stream that. (issue was, no real way to do that if the file that needs to be transformed is still being piped to)
- PiCamera Docs had a few interesting ways (if making this for an RPI, like I was)
- use OBS
###### - MOST COMMON METHOD (but not code enough for me) is to configure a RTMP server using NGINX on a RPI

Industry Standard way:
- HLS (apple)
- MPEG DASH (google)
- RTMP (old now)

Issue with the industry standard ways are not many open source examples to go off of (weeks of research amounted to nothing), using the Amazon livestreaming service that transform streams into HLS is SUPER COSTLY, VERY TOUGH to make alone (even if ur experienced, few of the best devs -- the ones that knew about these services anyway-- i know told me this).

Best way to achieve this is by making the thing that is recording into its own web server, however, due to constraints in this project that was impossible.

 New strategy has been taken although that repo is private.
