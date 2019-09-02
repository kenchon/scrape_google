FROM nikolaik/python-nodejs:latest

COPY ./* /home/app/
WORKDIR /home/app

RUN npm install
RUN pip install requests && \
    pip install bs4 && \
    pip install lxml

EXPOSE 3000

CMD ["node", "index.js"]
