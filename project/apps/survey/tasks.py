import csv
from .models import HealthStateSequenceUpload, SurveyPath

def update_health_sequences(sequence_upload_id):
    sequence = HealthStateSequenceUpload.objects.get(pk=sequence_upload_id)

    # TODO: Confirm that re-uploading marks all un-done!  Put
    SurveyPath.objects.all().delete()

    order = 0
    for row in csv.reader(sequence.csv_file.file):
        order += 1
        SurveyPath.objects.create(
            order=order,
            state_1=row[0],
            state_2=row[1],
            state_3=row[2],
            state_4=row[3],
            state_5=row[4],
            state_6=row[5],
            state_7=row[6],
            state_8=row[7],
        )
