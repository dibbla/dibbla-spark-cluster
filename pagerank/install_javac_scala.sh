#!/bin/bash

# Install sudo
apt-get install sudo -y

# Install the corresponding javac
sudo apt install openjdk-17-jdk -y

export JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
export PATH=$JAVA_HOME/bin:$PATH

# Install Scala  2.12.18
cd /opt/pagerank
tar -xvzf scala-2.12.18.tgz
sudo mv scala-2.12.18 /usr/local/scala

export PATH=/usr/local/scala/bin:$PATH