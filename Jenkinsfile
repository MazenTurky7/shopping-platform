pipeline {
    agent any

    stages {
        stage('Build and Test') {
            steps {
                script {
                    // Build Docker images and run tests for each service
                    docker.build("authentication-service")
                    // Run unit tests for authentication service
                    sh "docker run authentication-service pytest"

                    docker.build("product-catalog-service")
                    // Run unit tests for product catalog service
                    sh "docker run product-catalog-service pytest"

                    docker.build("order-processing-service")
                    // Run unit tests for order processing service
                    sh "docker run order-processing-service pytest"
                }
            }
        }

        stage('Push Docker Images to Registry') {
            steps {
                script {
                    // Push Docker images to Docker Hub or your container registry
                    docker.withRegistry('https://registry.hub.docker.com', 'docker-hub-credentials') {
                        docker.image("authentication-service").push()
                        docker.image("product-catalog-service").push()
                        docker.image("order-processing-service").push()
                    }
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                script {
                    // Deploy to Kubernetes using kubectl
                    sh "kubectl apply -f authentication_service_deployment.yml"
                    sh "kubectl apply -f product_catalog_service_deployment.yml"
                    sh "kubectl apply -f order_processing_service_deployment.yml"
                }
            }
        }
    }

    post {
        always {
            // Clean up
            script {
                // Clean up Docker images
                docker.image("authentication-service").remove()
                docker.image("product-catalog-service").remove()
                docker.image("order-processing-service").remove()
            }
        }
        success {
            echo 'Pipeline succeeded!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
