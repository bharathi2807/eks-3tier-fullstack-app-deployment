# -------- Build Stage --------
FROM node:20-alpine AS build
WORKDIR /app

# Install Chromium for tests
RUN apk add --no-cache chromium
ENV CHROME_BIN=/usr/bin/chromium-browser

COPY package*.json ./
# Install dependencies
RUN npm ci
# Copy source code
COPY . .

# Run CI checks inside the container
RUN npm run lint
# Run tests in headless mode
RUN npm run test -- --watch=false --browsers=ChromeHeadlessCI
# Build the app
RUN npm run build -- --configuration production

# -------- Runtime Stage --------
FROM nginx:alpine
COPY --from=build /app/dist/register-app/ /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
