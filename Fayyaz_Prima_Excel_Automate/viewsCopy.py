from django.shortcuts import render, redirect
from .forms import UploadCSVForm
from .models import Execution
from .services import process_csv
import os
from django.conf import settings
from django.http import FileResponse, Http404



def upload_page(request):
    if request.method == 'POST':
        form = UploadCSVForm(request.POST, request.FILES)
        if form.is_valid():
            execution = Execution.objects.create(
                input_file=form.cleaned_data['file'],
                status='PROCESSING'
            )

            output_name = f'output_{execution.id}.csv'
            output_path = os.path.join(
                settings.MEDIA_ROOT, 'outputs', output_name
            )

            rows_in, rows_out = process_csv(
                execution.input_file.path,
                output_path
            )

            execution.output_file.name = f'outputs/{output_name}'
            execution.input_rows = rows_in
            execution.output_rows = rows_out
            execution.status = 'SUCCESS'
            execution.save()

            return redirect('history')
    else:
        form = UploadCSVForm()

    return render(request, 'Fayyaz_Prima_Excel_Automate/upload.html', {'form': form})


def history_page(request):
    executions = Execution.objects.all().order_by('-created_at')
    return render(request, 'Fayyaz_Prima_Excel_Automate/history.html', {'executions': executions})

def download_output(request, filename):
    file_path = os.path.join(settings.MEDIA_ROOT, 'outputs', filename)
    if os.path.exists(file_path):
        return FileResponse(open(file_path, 'rb'), as_attachment=True)
    else:
        raise Http404("File does not exist")