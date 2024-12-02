
# MeETU - Retrieval-Augmented Generation (RAG) Model

MeETU is an Retrieval-Augmented Generation (RAG) chatbot designed to provide intelligent question-answering and recommendations based on METU's (Middle East Technical University) FAQs and website content. The project leverages state-of-the-art technologies such as the **meta-llama/Llama-3.2-3B-Instruct** model from Hugging Face, FAISS, and Streamlit to deliver accurate and efficient responses.

---

## **Features**

- Advanced RAG architecture using `meta-llama/Llama-3.2-3B-Instruct` for natural language processing.
- Handles question-answering and recommendation tasks.
- Powered by FAISS for efficient embedding storage and retrieval.
- User-friendly interface via Streamlit.


![Demo of MeETU](https://github.com/halildonmezbilek/MeETU/raw/main/Diagrams/demo.gif)


## **Installation**

### 1. Clone the Repository

```bash
git clone https://github.com/halildonmezbilek/MeETU.git
cd MeTU
```

### 2. Install Dependencies
Ensure you have Python 3.10 or above and install the required packages:
```bash
pip install -r requirements.txt
```

### 3. Run the Application
Start the Streamlit app:
```bash
python run RAG_Model/flask_meetu.py
```

---




# Nginx Configuration for MeETU
Please use your own domain name. This guide is an example for "halildonmezbilek.com" domain.
This guide explains how to configure Nginx to route traffic for the MeETU application on a Debian system. The configuration forwards traffic to:
- Flask application on `http://localhost:5000`.
- Streamlit application on `http://localhost:8501`.

---

## Configuration Details

- `http://meetu.halildonmezbilek.com`: Routes to Flask application on port `5000`.
- `http://meetu.halildonmezbilek.com/streamlit/`: Routes to Streamlit application on port `8501`.

---

## **Step 1: Install Nginx**

Install and start Nginx:
```bash
sudo apt update
sudo apt install nginx -y
sudo systemctl enable nginx
sudo systemctl start nginx
```

---

## **Step 2: Configure Nginx**
1. Open a new configuration file for your server:
   ```bash
   sudo nano /etc/nginx/sites-available/meetu
   ```

2. Add the following configuration:
   ```nginx
   server {
       listen 9897;
       server_name meetu.halildonmezbilek.com;

       location / {
           proxy_pass http://localhost:5000;
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
           proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
           proxy_set_header X-Forwarded-Proto $scheme;
       }

       location /streamlit/ {
           rewrite ^/streamlit/(.*)$ /$1 break;
           proxy_pass http://localhost:8501;
           proxy_set_header Host $host;
           proxy_http_version 1.1;
           proxy_set_header Upgrade $http_upgrade;
           proxy_set_header Connection "upgrade";
       }
   }
   ```

3. Save and close the file (Ctrl + O, Enter, Ctrl + X).

---

## **Step 3: Enable the Configuration**

1. Create a symbolic link to enable the configuration:
   ```bash
   sudo ln -s /etc/nginx/sites-available/meetu /etc/nginx/sites-enabled/
   ```

2. Test the Nginx configuration:
   ```bash
   sudo nginx -t
   ```

3. Reload Nginx to apply the changes:
   ```bash
   sudo systemctl reload nginx
   ```

---

## **Step 4: Ensure the Required Ports Are Open**

1. Open the required port (9897) in the firewall:
   ```bash
   sudo ufw allow 9897
   ```

2. If you're using a cloud provider, ensure port `9897` is open in the security group or network configuration.

---

## **Optional: Use Cloudflare Tunnel (Recommended)**

Cloudflare Tunnel is an optional, secure way to expose local applications to the internet without opening ports on your firewall.

1. Install Cloudflare Tunnel:
   ```bash
   sudo apt update
   sudo apt install cloudflared
   ```

2. Authenticate Cloudflare Tunnel with your Cloudflare account:
   ```bash
   cloudflared login
   ```

3. Configure a tunnel for the MeETU application:
   ```bash
   cloudflared tunnel create meetu
   ```

4. Add a configuration file for the tunnel:
   ```bash
   sudo nano /etc/cloudflared/config.yml
   ```

   Add the following content:
   ```yaml
   tunnel: meetu
   credentials-file: /home/user/.cloudflared/meetu.json

   ingress:
     - hostname: meetu.halildonmezbilek.com
       service: http://localhost:9897
     - service: http_status:404
   ```

5. Start the Cloudflare Tunnel:
   ```bash
   sudo cloudflared tunnel run meetu
   ```

Now your MeETU application is securely accessible through Cloudflare.

---

## **Step 5: Test the Configuration**

Access the Flask app by visiting:
```
http://meetu.halildonmezbilek.com/
```



---

## **Optional: Set Up HTTPS with Let's Encrypt**

1. Install Certbot:
   ```bash
   sudo apt install certbot python3-certbot-nginx -y
   ```

2. Obtain and configure an SSL certificate:
   ```bash
   sudo certbot --nginx -d meetu.halildonmezbilek.com
   ```

3. Reload Nginx:
   ```bash
   sudo systemctl reload nginx
   ```

Your Nginx server will now redirect HTTP to HTTPS and secure the connection.

---



## **Configuration**

- **Environment Variables**:
  - `.env` file stores sensitive information like API keys.
- **Ignored Files**:
  Files such as `models/`, `user_history/`, and some others are excluded from version control.

---

## **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## **Contact**

If you have any questions or suggestions, feel free to reach out to me:
- **Email**: halil.donmezbilek@gmail.com
- **Docker Hub**: [halildonmezbilek](https://hub.docker.com/r/halildonmezbilek)


