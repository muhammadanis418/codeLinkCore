package org.ciklum.codelinkcore.controller;
import org.ciklum.codelinkcore.request.ConfigRequest;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/api/v1/generator")
public class ConfigGeneratorController {

    /**
     * The Spring Boot Tool endpoint that the Python AI agent calls.
     * Generates configuration content based on the agent's request.
     */
    @PostMapping("/config")
    public String generateConfig(@RequestBody ConfigRequest request) {

        String serviceNameLower = request.serviceName().toLowerCase();
        String dbNameLower = request.database().toLowerCase();

        if ("mongodb".equals(dbNameLower)) {
            // This config includes the mandatory security standard check for reflection
            return String.format("""
                # Standard application.properties for %s
                
                # Ciklum Standard Server Port
                server.port=8081
                
                # MongoDB Configuration (Internal Standard)
                spring.data.mongodb.uri=mongodb://localhost:27017/%s_db
                
                # Standard Logging Configuration
                logging.level.com.ciklum.%s=INFO
                
                # MANDATORY Ciklum Security Standard (Required by RAG context)
                spring.security.audit=true
                
                # Ensure Health Check is enabled
                management.endpoint.health.enabled=true
                """, request.serviceName(), serviceNameLower.replace("project", ""), serviceNameLower);

        } else if ("mysql".equals(dbNameLower)) {
            return String.format("""
                # Standard application.properties for %s
                
                # Ciklum Standard Server Port
                server.port=8081
                
                # MySQL Configuration 
                spring.datasource.url=jdbc:mysql://localhost:3306/%s_db
                spring.datasource.username=user
                spring.datasource.password=password
                """, request.serviceName(), serviceNameLower.replace("project", ""));
        } else {
            return "Error: Unsupported configuration request. Only 'mongodb' or 'mysql' databases are supported.";
        }
    }
}
