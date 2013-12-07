from utils.test_helpers import skip, wip, ClearedTransactionTestCase
from utils.factory import Factory
from survey.tasks import _header_row, _csv_row

@wip
class CurrentPageContextTest(ClearedTransactionTestCase):

    def setUp(self):
        super(CurrentPageContextTest, self).setUp()
        self.survey_response = Factory.survey_response()


    def test_header_row(self):
        self.assertEquals(_header_row(), [
            'Internal ID', 'Entrance ID', 'Exit URL', 'Start Time', 'Completion Time', 'Survey Path ID', 
            'Health State 1 ID', 'Health State 2 ID', 'Health State 3 ID', 'Health State 4 ID', 
            'Health State 5 ID', 'Health State 6 ID', 'Health State 7 ID', 'Health State 8 ID', 
            'Age', 'Education', 'Household income', 
            'Diagnosed with serious mental illness', 'Diagnosed with schizophrenia', 
            'Diagnosed with depression', 'Diagnosed with bipolar', 'Diagnosed with other', 
            'Diagnosed with dont know', 'Family diagnosed with serious mental illness', 
            'Family diagnosed with schizophrenia', 'Family diagnosed with depression', 
            'Family diagnosed with bipolar', 'Family diagnosed with other', 
            'Family diagnosed with dont know', 

            'HS 1 - Start Time', 'HS 1 - Completion Time', 'HS 1 - VAS Rating', 'HS 1 - TTO Rating', 
            'HS 1 - Intro Completed', 'HS 1 - Intro Completion Time', 'HS 1 - Video Completed', 
            'HS 1 - Video Completion Time', 'HS 1 - VAS Completed', 'HS 1 - VAS Completion Time', 
            'HS 1 - TTO Completed', 'HS 1 - TTO Completion Time', 'HS 1 - Outro Completed', 
            'HS 1 - Outro Completion Time',

            'HS 2 - Start Time', 'HS 2 - Completion Time', 'HS 2 - VAS Rating', 'HS 2 - TTO Rating', 
            'HS 2 - Intro Completed', 'HS 2 - Intro Completion Time', 'HS 2 - Video Completed', 
            'HS 2 - Video Completion Time', 'HS 2 - VAS Completed', 'HS 2 - VAS Completion Time', 
            'HS 2 - TTO Completed', 'HS 2 - TTO Completion Time', 'HS 2 - Outro Completed', 
            'HS 2 - Outro Completion Time', 

            'HS 3 - Start Time', 'HS 3 - Completion Time', 'HS 3 - VAS Rating', 'HS 3 - TTO Rating', 
            'HS 3 - Intro Completed', 'HS 3 - Intro Completion Time', 'HS 3 - Video Completed', 
            'HS 3 - Video Completion Time', 'HS 3 - VAS Completed', 'HS 3 - VAS Completion Time', 
            'HS 3 - TTO Completed', 'HS 3 - TTO Completion Time', 'HS 3 - Outro Completed', 
            'HS 3 - Outro Completion Time', 

            'HS 4 - Start Time', 'HS 4 - Completion Time', 'HS 4 - VAS Rating', 'HS 4 - TTO Rating', 
            'HS 4 - Intro Completed', 'HS 4 - Intro Completion Time', 'HS 4 - Video Completed', 
            'HS 4 - Video Completion Time', 'HS 4 - VAS Completed', 'HS 4 - VAS Completion Time', 
            'HS 4 - TTO Completed', 'HS 4 - TTO Completion Time', 'HS 4 - Outro Completed', 
            'HS 4 - Outro Completion Time', 

            'HS 5 - Start Time', 'HS 5 - Completion Time', 'HS 5 - VAS Rating', 'HS 5 - TTO Rating', 
            'HS 5 - Intro Completed', 'HS 5 - Intro Completion Time', 'HS 5 - Video Completed', 
            'HS 5 - Video Completion Time', 'HS 5 - VAS Completed', 'HS 5 - VAS Completion Time', 
            'HS 5 - TTO Completed', 'HS 5 - TTO Completion Time', 'HS 5 - Outro Completed', 
            'HS 5 - Outro Completion Time', 

            'HS 6 - Start Time', 'HS 6 - Completion Time', 'HS 6 - VAS Rating', 'HS 6 - TTO Rating', 
            'HS 6 - Intro Completed', 'HS 6 - Intro Completion Time', 'HS 6 - Video Completed', 
            'HS 6 - Video Completion Time', 'HS 6 - VAS Completed', 'HS 6 - VAS Completion Time', 
            'HS 6 - TTO Completed', 'HS 6 - TTO Completion Time', 'HS 6 - Outro Completed', 
            'HS 6 - Outro Completion Time', 

            'HS 7 - Start Time', 'HS 7 - Completion Time', 'HS 7 - VAS Rating', 'HS 7 - TTO Rating', 
            'HS 7 - Intro Completed', 'HS 7 - Intro Completion Time', 'HS 7 - Video Completed', 
            'HS 7 - Video Completion Time', 'HS 7 - VAS Completed', 'HS 7 - VAS Completion Time', 
            'HS 7 - TTO Completed', 'HS 7 - TTO Completion Time', 'HS 7 - Outro Completed', 
            'HS 7 - Outro Completion Time', 

            'HS 8 - Start Time', 'HS 8 - Completion Time', 'HS 8 - VAS Rating', 'HS 8 - TTO Rating', 
            'HS 8 - Intro Completed', 'HS 8 - Intro Completion Time', 'HS 8 - Video Completed', 
            'HS 8 - Video Completion Time', 'HS 8 - VAS Completed', 'HS 8 - VAS Completion Time', 
            'HS 8 - TTO Completed', 'HS 8 - TTO Completion Time', 'HS 8 - Outro Completed', 
            'HS 8 - Outro Completion Time', 
        ])

    def test_csv_row(self):
        expected = [
            self.survey_response.pk,  # "Internal ID",
            self.survey_response.entrance_id,  # "Entrance ID",
            self.survey_response.exit_url,  # "Exit URL",
            self.survey_response.start_time,  # "Start Time",
            self.survey_response.finish_time,  # "Completion Time",
            self.survey_response.survey_path_id,  # "Survey Path ID",
            self.survey_response.state_1.number,  # "Health State 1 ID",
            self.survey_response.state_2.number,  # "Health State 2 ID",
            self.survey_response.state_3.number,  # "Health State 3 ID",
            self.survey_response.state_4.number,  # "Health State 4 ID",
            self.survey_response.state_5.number,  # "Health State 5 ID",
            self.survey_response.state_6.number,  # "Health State 6 ID",
            self.survey_response.state_7.number,  # "Health State 7 ID",
            self.survey_response.state_8.number,  # "Health State 8 ID",
            self.survey_response.age,
            self.survey_response.education,
            self.survey_response.household_income,
            self.survey_response.diagnosed_with_serious_mental_illness,
            self.survey_response.diagnosed_with_schizophrenia,
            self.survey_response.diagnosed_with_depression,
            self.survey_response.diagnosed_with_bipolar,
            self.survey_response.diagnosed_with_other,
            self.survey_response.diagnosed_with_dont_know,
            self.survey_response.family_diagnosed_with_serious_mental_illness,
            self.survey_response.family_diagnosed_with_schizophrenia,
            self.survey_response.family_diagnosed_with_depression,
            self.survey_response.family_diagnosed_with_bipolar,
            self.survey_response.family_diagnosed_with_other,
            self.survey_response.family_diagnosed_with_dont_know,
        ]
        for r in self.survey_response.ratings.order_by("order").all():
            expected.extend([
                r.start_time,
                r.finish_time,
                r.vas_rating,
                r.tto_rating,
                r.intro_completed,
                r.intro_completed_time,
                r.video_completed,
                r.video_completed_time,
                r.vas_completed,
                r.vas_completed_time,
                r.tto_completed,
                r.tto_completed_time,
                r.outro_completed,
                r.outro_completed_time,
            ])

        self.assertEquals(_csv_row(self.survey_response), expected)
