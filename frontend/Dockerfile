# Dockerfile para o Frontend (Vue.js)
FROM node:14

WORKDIR /app/frontend

COPY package*.json /app/frontend
RUN npm install

COPY . /app/

EXPOSE 8080

CMD ["npm", "run", "serve"]