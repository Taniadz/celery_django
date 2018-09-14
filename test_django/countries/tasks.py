
from test_django.celery import app
from .models import Country
import xml.etree.ElementTree as ET
from celery.decorators import task
import requests


@task()
def get_dummy_data():

    data_xml = requests.get("http://127.0.0.1:5000/send_data", headers={"User-Agent": "Mozilla/5.0"})
    root = ET.fromstring(data_xml.content)
    for country in root.findall('country'):
        name = country.find('name').text
        id = int(country.find('id').text)
        Country.objects.get_or_create(id=id, name=name)

    return




