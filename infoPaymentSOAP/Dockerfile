FROM node:14-alpine

WORKDIR /usr/src/app
COPY package*.json ./
RUN npm install
COPY . .

EXPOSE 3016
CMD ["node", "server.js"]