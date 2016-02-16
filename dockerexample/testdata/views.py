import logging
import socket

from django.shortcuts import render
from testdata.forms import DataForm
from testdata.models import Data

log = logging.getLogger(__name__)


def home(request):
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    context = {
        "hostname": hostname,
        "ipaddr": ip,
    }

    if request.method == 'POST':
        data_form = DataForm(request.POST)
        if data_form.is_valid():
            f = data_form.cleaned_data
            key = f['key']
            value = f['value']
            data = Data(key=key, value=value)
            data.save()
    else:
        data_form = DataForm()

    log.info("Main page")
    saved_data = Data.objects.all()
    context['data'] = saved_data
    context['data_form'] = data_form
    return render(request, 'testdata/home.html', context)
