FROM public.ecr.aws/lambda/python:3.8

RUN yum -y install wget unzip libX11 GConf2 fontconfig atk at-spi2-atk cups-libs libxkbcommon libXcomposite libXdamage libXrandr pango alsa-lib libXcursor libXScrnSaver gtk3
RUN mkdir /usr/bin/swiftshader/ && ln -s /lib64/libGLESv2.so.2 /usr/bin/swiftshader/libGLESv2.so && ln -s /usr/lib64/libEGL.so.1 /usr/bin/swiftshader/libEGL.so
RUN wget "https://www.googleapis.com/download/storage/v1/b/chromium-browser-snapshots/o/Linux_x64%2F885264%2Fchrome-linux.zip?generation=1621553808408746&alt=media" -O /tmp/chrome-linux.zip && cd /opt && unzip /tmp/chrome-linux.zip && rm /tmp/chrome-linux.zip && ln -s /opt/chrome-linux/chrome /bin/chrome
RUN wget "https://chromedriver.storage.googleapis.com/92.0.4515.107/chromedriver_linux64.zip" -O /tmp/chromedriver_linux64.zip && cd /opt && unzip /tmp/chromedriver_linux64.zip && rm /tmp/chromedriver_linux64.zip && ln -s /opt/chromedriver /bin/chromedriver

COPY app.py requirements.txt /var/task/

RUN python3.8 -m pip install -r requirements.txt -t .

CMD ["app.lambda_handler"]
