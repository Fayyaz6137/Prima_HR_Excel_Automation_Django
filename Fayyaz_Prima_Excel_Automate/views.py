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
            uploaded_file = form.cleaned_data['file']

            # Create a model instance without saving the file yet
            execution = Execution(status='PROCESSING')
            execution.save()  # Save instance to get an ID if needed

            # Save the uploaded file directly as-is
            execution.input_file.save(
                uploaded_file.name,  # keeps the original filename
                uploaded_file        # the UploadedFile object from the form
            )

            # Optionally, save a copy in output field
            output_name = f'output_{execution.id}_{uploaded_file.name}'
            execution.output_file.save(
                output_name,
                uploaded_file        # reuse the same UploadedFile object
            )

            # process_csv should read, modify, and overwrite the same file
            output_file_path = execution.output_file.path
            process_csv(output_file_path)

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