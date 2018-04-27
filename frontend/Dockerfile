FROM node:9.4

WORKDIR /code
ADD . /code

EXPOSE 8080

RUN npm --production=false install

CMD ["npm", "run", "dev"]
