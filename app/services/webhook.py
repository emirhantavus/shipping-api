import requests

def notify_django_shipment_status(tracking_number: str, status: str):
      url = 'http://ecommerce-django-backend:8000/api/order/shipment-status-webhook/'
      
      data = {
            'tracking_number':tracking_number,
            'status':status
      }
      
      try:
            response = requests.post(url, json=data ,timeout=5)
            print('Webhook response:', response.status_code, response.text)
      
      except Exception as e:
            print('Webhook error: ',e)