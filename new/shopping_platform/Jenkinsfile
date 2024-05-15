pipeline {
    agent any

    stages {
        stage('Build Docker Images') {
            steps {
                script {
                    // Build Docker images for each service
                    docker.build("authentication-service")
                    docker.build("product-catalog-service")
                    docker.build("order-processing-service")
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
    }
}
