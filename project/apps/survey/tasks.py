import csv
from celery.task.schedules import crontab
from celery.task import periodic_task


def update_health_sequences(sequence_upload_id):
    from .models import HealthStateSequenceUpload, SurveyPath
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


@periodic_task(run_every=crontab(minute="*/5"))
def update_aggregate_tasks():
    from .models import SurveyAggregateStats, SurveyResponse
    stats, _ = SurveyAggregateStats.objects.get_or_create(pk=1)
    total_started = SurveyResponse.objects.exclude(start_time=None).count()
    total_finished = SurveyResponse.objects.exclude(start_time=None).exclude(finish_time=None).count()

    if total_started > 0:
        for s in SurveyResponse.objects.all():
            # TODO do this in sql if it hurts too bad.
            total_progress = 0
            total_dwell_minutes = 0
            for i in reversed(range(1, 9)):
                if s._completed_state(i):
                    total_progress += 1.0 / 8 * i
                    break
            if s.start_time:
                if s.finish_time:
                    total_dwell_minutes += (s.finish_time - s.start_time).total_seconds() / 60.0
                else:
                    for i in reversed(range(1, 9)):
                        if s.ratings.filter(order=i).exclude(finish_time=None).count() > 0:
                            hsr = s.ratings.filter(order=i).exclude(finish_time=None)[0]
                            total_dwell_minutes += (hsr.finish_time - s.start_time).total_seconds() / 60.0
                            break

        # last_updated
        stats.completion_rate = 100.0 * total_finished / total_started
        stats.average_survey_progress = 100.0 * total_progress / total_started
        stats.dwell_time = total_dwell_minutes / total_started
    else:
        stats.completion_rate = None
        stats.average_survey_progress = None
        stats.dwell_time = None
    stats.save()
