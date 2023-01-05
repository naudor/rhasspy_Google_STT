FROM djfil/rhasspy:arm64

COPY ./GCloudSpeech /GCloudSpeech

WORKDIR /GCloudSpeech

RUN mkdir -p Archives directory /var/cache/apt/arm64/archives/partial
RUN apt-get autoclean
RUN apt-get -y install python3-venv 
RUN ./setup-venv.sh

WORKDIR /
