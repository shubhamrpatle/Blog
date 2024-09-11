# Blog Service
The Blog Service project is a Django application with the following APIs:
1. **Submit Blog** - API for submitting blog entries.
2. **Search Blog** - API for searching blog entries.
The project uses Redis for queuing and Elasticsearch for storing blog entries.

## Prerequisites
Ensure you have the following installed:
- Python 3.x
- Django
- Redis
- Elasticsearch
- Any other dependencies listed in `requirements.txt`

## Setup
1. **Clone the Repository**
   ```bash
   git clone https://github.com/shubhamrpatle/blog_service.git
   cd blog_service

1. **Clone the Repository**
  pip install -r requirements.txt
2. **Install Dependencies**
  python manage.py migrate
3. **Running the Django Server**
  python manage.py runserver
4. **Starting the Consumer Worker**
  python blog/consumer.py

## project screenshot 
![image](https://github.com/user-attachments/assets/8b609975-7083-4b3f-9d84-626079e35b10)
![image](https://github.com/user-attachments/assets/4f385e7d-3de8-4c3a-a7f7-e4124d1113af)
![image](https://github.com/user-attachments/assets/47d90e9b-6120-4441-85f4-25c880e27770)



 
