# FAQs

Owner: Andrés Carrancá
Tags: Process

Welcome to our FAQ page! Here, you can add your questions, and they will be promptly answered. Feel free to browse existing FAQs or submit a new inquiry.

- Why use Docker instead of a Virtual Environment?
    
    1. **Consistency**: Docker ensures the same environment across different machines.
    2. **Isolation**: Docker containers are more isolated from the host system.
    3. **Portability**: Docker images can be easily shared and run on any system with Docker installed.
    4. **Resource efficiency**: Docker containers are generally lighter and faster than virtual environments.
    5. **Scalability**: Docker makes it easier to scale applications in production environments.
    6. **Cross**-**platform** co**m**patibility: Docker containers can run on both Linux and Windows machines, ensuring consistency across different operating systems.
    7. **Package management**: Docker allows you to specify and install all required packages within the container, eliminating conflicts with system-wide packages.
    8. **Version control**: Docker images can be versioned, making it easy to roll back to previous environments if needed.
    9. **Simplified** **deployment**: Docker containers can be easily deployed to various cloud platforms, streamlining the deployment process.
    10. **Dependency management**: Docker eliminates "it works on my machine" problems by packaging all dependencies within the container.
    
- Why I don’t see the changes of my code when I run it?
    
    Most likely the volume is not mounted to the  container. 
    Use **-v** flag as in  **-v .:/app**  to map the current directory where the Dockerfile is present (.) to where the workdir also defined in the Dockerfile.
    Alternatively use --volume=".:/app" 
    check [https://docs.docker.com/engine/storage/volumes/](https://docs.docker.com/engine/storage/volumes/)