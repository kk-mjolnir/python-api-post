I have developed a Python REST API, containerized it using Docker, and deployed it on Siemens Industrial Edge using Industrial Edge Management (IEM).

The API is intended to receive HTTP POST requests from a Mendix application and then publish the received data to an external MQTT broker (Industrial Edge / Mosquitto).

However, HTTP POST requests from Mendix are not reaching the API running in Industrial Edge, even though the application is running successfully.

I am looking for guidance on networking, port exposure, and best practices for making REST APIs accessible from external applications (Mendix) in Industrial Edge
