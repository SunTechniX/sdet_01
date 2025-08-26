# base image
FROM python:3.12

# specify the port number the container should expose
# EXPOSE 5001

ENV APPDIR "/usr/src/app"
WORKDIR $APPDIR

COPY requirements.txt $APPDIR 
RUN apt-get clean && \
    cd $APPDIR && \
    pip3 install --no-cache-dir -r $APPDIR/requirements.txt
RUN wget https://storage.googleapis.com/chrome-for-testing-public/139.0.7258.138/linux64/chromedriver-linux64.zip && \
    unzip chromedriver_linux64.zip && \
    rm -rf /var/lib/apt/lists/* && \
    mkdir $APPDIR/allure

# run the application
CMD pytest --alluredir=$APPDIR/allure

