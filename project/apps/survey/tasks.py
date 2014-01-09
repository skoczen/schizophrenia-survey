import csv
import tempfile
from django.core.files import File
from celery.task.schedules import crontab
from celery.task import periodic_task, task


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

        print total_progress
        print total_started
        # last_updated
        stats.completion_rate = 100.0 * total_finished / total_started
        stats.average_survey_progress = 100.0 * total_progress / total_started
        stats.dwell_time = total_dwell_minutes / total_started
    else:
        stats.completion_rate = None
        stats.average_survey_progress = None
        stats.dwell_time = None
    stats.save()


def _header_row():
    row = [
        "Internal ID",
        "Entrance ID",
        "Exit URL",
        "Start Time",
        "Completion Time",
        "Survey Path ID",
        "Health State 1 ID",
        "Health State 2 ID",
        "Health State 3 ID",
        "Health State 4 ID",
        "Health State 5 ID",
        "Health State 6 ID",
        "Health State 7 ID",
        "Health State 8 ID",
        "Age",
        "Education",
        "Household income",
        "Diagnosed with serious mental illness",
        "Diagnosed with schizophrenia",
        "Diagnosed with depression",
        "Diagnosed with bipolar",
        "Diagnosed with other",
        "Diagnosed with dont know",
        "Family diagnosed with serious mental illness",
        "Family diagnosed with schizophrenia",
        "Family diagnosed with depression",
        "Family diagnosed with bipolar",
        "Family diagnosed with other",
        "Family diagnosed with dont know"
    ]
    for i in range(1, 9):
        row += [
            "HS %s - Start Time" % i,
            "HS %s - Completion Time" % i,
            "HS %s - VAS Rating" % i,
            "HS %s - TTO Rating" % i,
            "HS %s - Intro Completed" % i,
            "HS %s - Intro Completion Time" % i,
            "HS %s - Video Completed" % i,
            "HS %s - Video Completion Time" % i,
            "HS %s - VAS Completed" % i,
            "HS %s - VAS Completion Time" % i,
            "HS %s - TTO Completed" % i,
            "HS %s - TTO Completion Time" % i,
            "HS %s - Outro Completed" % i,
            "HS %s - Outro Completion Time" % i,
        ]
    return row


def _csv_row(r):
    row = [
        r.pk,  # "Internal ID",
        r.entrance_id,  # "Entrance ID",
        r.exit_url,  # "Exit URL",
        r.start_time,  # "Start Time",
        r.finish_time,  # "Completion Time",
        r.survey_path_id,  # "Survey Path ID",
        r.state_1.number,  # "Health State 1 ID",
        r.state_2.number,  # "Health State 2 ID",
        r.state_3.number,  # "Health State 3 ID",
        r.state_4.number,  # "Health State 4 ID",
        r.state_5.number,  # "Health State 5 ID",
        r.state_6.number,  # "Health State 6 ID",
        r.state_7.number,  # "Health State 7 ID",
        r.state_8.number,  # "Health State 8 ID",
        r.age,
        r.education,
        r.household_income,
        r.diagnosed_with_serious_mental_illness,
        r.diagnosed_with_schizophrenia,
        r.diagnosed_with_depression,
        r.diagnosed_with_bipolar,
        r.diagnosed_with_other,
        r.diagnosed_with_dont_know,
        r.family_diagnosed_with_serious_mental_illness,
        r.family_diagnosed_with_schizophrenia,
        r.family_diagnosed_with_depression,
        r.family_diagnosed_with_bipolar,
        r.family_diagnosed_with_other,
        r.family_diagnosed_with_dont_know,
    ]
    for i in range(1, 9):
        hs = r.ratings.get(order=i)

        row += [
            hs.start_time,
            hs.finish_time,
            hs.vas_rating,
            hs.tto_rating,
            hs.intro_completed,
            hs.intro_completed_time,
            hs.video_watched,
            hs.video_completed_time,
            hs.vas_completed,
            hs.vas_completed_time,
            hs.tto_completed,
            hs.tto_completed_time,
            hs.outro_completed,
            hs.outro_completed_time,
        ]

    return row


@task
def generate_csv():
    from .models import SurveyResponse, SurveyExport

    num_responses = 0
    with tempfile.TemporaryFile() as csvfile:
        csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(_header_row())
        for s in SurveyResponse.objects.all().order_by("id"):
            num_responses += 1
            csv_writer.writerow(_csv_row(s))

        export = SurveyExport.objects.create(num_rows=num_responses)
        export.csv_file = File(csvfile)
        export.save()
