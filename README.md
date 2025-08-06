# MERN Project

This repository contains a full-stack MERN (MongoDB, Express.js, React.js, Node.js) application. The project is designed for scalability, efficient communication between client and server, and production-level deployment with load balancing and custom domain configuration.

## Features

- **Backend**: Node.js with Express.js, connected to MongoDB.
- **Frontend**: React.js for a responsive user interface.
- **API Communication**: RESTful API ensures efficient data exchange between frontend and backend.
- **Deployment**: Configured for deployment on AWS EC2 instances.
- **Load Balancing**: Supports horizontal scaling with multiple application instances.
- **Custom Domain**: Integration with Cloudflare for DNS and security.

---

## Getting Started

### Prerequisites

- Node.js (v14+)
- npm or yarn
- MongoDB (local or hosted)
- AWS Account (for EC2)
- Cloudflare Account (for custom domain)

### Setup

#### 1. Backend Setup

1. Navigate to the backend directory:
    ```bash
    cd backend
    ```
2. Install dependencies:
    ```bash
    npm install
    ```
3. Set up environment variables in a `.env` file (refer to `.env.example`).
4. Start the backend server:
    ```bash
    npm start
    ```

#### 2. Frontend Setup

1. Navigate to the frontend directory:
    ```bash
    cd frontend
    ```
2. Install dependencies:
    ```bash
    npm install
    ```
3. Configure API endpoints in environment variables.
4. Start the development server:
    ```bash
    npm start
    ```

---

## Deployment

### 1. Deploy on AWS EC2

- Create and configure an EC2 instance with necessary security groups.
- Install Node.js, npm, and a process manager (e.g., PM2).
- Clone this repository to your EC2 instance.
- Set up both backend and frontend as shown above.
- Build the frontend for production:
    ```bash
    npm run build
    ```
- Serve the built frontend using a web server (e.g., Nginx or serve).
- Use PM2 or a similar tool to keep backend processes running.

### 2. Load Balancing

- Launch multiple EC2 instances with the application.
- Set up an AWS Elastic Load Balancer (ELB) to distribute traffic.
- Ensure all instances are registered with the load balancer.

### 3. Connect Custom Domain via Cloudflare

- Register your domain with Cloudflare.
- Point your domain's DNS to the AWS load balancer using Cloudflare's dashboard.
- Set up SSL/TLS and security settings through Cloudflare.

---

## Communication Between Frontend and Backend

- The frontend communicates with the backend via RESTful APIs.
- Configure the frontend `.env` to point to the backend API endpoint (e.g., the load balancer's DNS).

---

## License

This project is licensed under the MIT License.

---

## Contact

For questions or support, please open an issue in this repository.
