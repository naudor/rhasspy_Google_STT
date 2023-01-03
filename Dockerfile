FROM djfil/rhasspy:arm64

COPY ./GCloudSpeech /GCloudSpeech

WORKDIR /GCloudSpeech

RUN mkdir -p Archives directory /var/cache/apt/arm64/archives/partial
RUN apt-get autoclean
#RUN pip3 install --upgrade setuptools
#RUN pip3 install --upgrade pip
#RUN pip3 install ez_setup 
#RUN python3 -m pip install --upgrade setuptools
#RUN pip3 install --no-cache-dir  --force-reinstall -Iv grpcio==1.51.1
RUN apt-get -y install python3-venv 
RUN ./setup-venv.sh

WORKDIR /
