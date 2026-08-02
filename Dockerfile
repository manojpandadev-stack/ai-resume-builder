FROM maven:3.9.8-eclipse-temurin-21

WORKDIR /app

COPY . .

RUN mvn clean package -DskipTests

EXPOSE 8080

CMD ["sh", "-c", "java -Xms128m -Xmx256m -XX:MaxMetaspaceSize=128m -jar target/*.jar"]