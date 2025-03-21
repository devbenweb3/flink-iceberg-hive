FROM openjdk:8-jre-slim

WORKDIR /opt/ranger-trino

COPY target/ranger-2.4.0-trino-plugin.tar.gz /opt/ranger-trino/
RUN tar -xvzf ranger-2.4.0-trino-plugin.tar.gz && rm ranger-2.4.0-trino-plugin.tar.gz

CMD [ "tail", "-f", "/dev/null" ]
