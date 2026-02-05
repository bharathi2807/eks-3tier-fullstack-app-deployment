########### Build Stage ###########
FROM maven:3.9.6-eclipse-temurin-17 AS build

WORKDIR /app

# Cache dependencies
COPY pom.xml .
RUN mvn dependency:go-offline

# Copy source code
COPY src ./src

# Build jar without tests
RUN mvn clean package -DskipTests

########### Runtime Stage ###########
FROM eclipse-temurin:17-jre

WORKDIR /app

# Copy the built Spring Boot jar
COPY --from=build /app/target/*.jar app.jar

EXPOSE 8080

CMD ["java", "-jar", "app.jar"]
