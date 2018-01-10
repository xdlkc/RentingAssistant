FROM ubuntu:16.04

RUN rm /etc/apt/sources.list
COPY DockerConf/sources.list /etc/apt/sources.list
RUN apt-get update
RUN cd /usr/local 
RUN wget --no-check-certificate --no-cookies --header "Cookie: oraclelicense=accept-securebackup-cookie"  http://download.oracle.com/otn-pub/java/jdk/8u151-b12/e758a0de34e24606bca991d704f6dcbf/jdk-8u151-linux-x64.tar.gz
RUN wget http://www-eu.apache.org/dist/maven/maven-3/3.5.2/binaries/apache-maven-3.5.2-bin.tar.gz
ENV JAVA_HOME=/usr/local/jdk1.8.0_151 CLASSPATH=$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar PATH=$PATH:$JAVA_HOME/bin
ENV MAVEN_HOME=/usr/local/apache-maven-3.5.2 PATH=$PATH:$MAVEN_HOME/bin
RUN mkdir /code
WORKDIR /code
COPY WebServer /code