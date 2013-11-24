from django.core import mail
from django.core.cache import cache
from django.test import TestCase
from utils.factory import Factory
from utils.test_helpers import skip, wip

from survey.models import SurveyResponse, SurveyPath, NEXT_SURVEY_PATH_KEY


class SurveyResponseTest(TestCase):

    def setUp(self):
        SurveyPath.objects.all().delete()
        cache.delete(NEXT_SURVEY_PATH_KEY)

    def test_making_a_new_response_without_a_path_mails_the_admins(self):
        try:
            SurveyResponse.objects.create()
        except:
            pass

        # Test that one message has been sent.
        self.assertEqual(len(mail.outbox), 1)

        # Verify that the subject of the first message is correct.
        self.assertEqual(mail.outbox[0].subject, "[Schizophrenia Survey] CRITICAL: We're out of survey paths!")

    def test_making_a_new_response_sets_its_health_states(self):
        survey_path = Factory.survey_path()
        user, password = Factory.user()

        survey_response = SurveyResponse.objects.create(user=user)

        self.assertEquals(survey_path.state_1, survey_response.state_1.number)
        self.assertEquals(survey_path.state_2, survey_response.state_2.number)
        self.assertEquals(survey_path.state_3, survey_response.state_3.number)
        self.assertEquals(survey_path.state_4, survey_response.state_4.number)
        self.assertEquals(survey_path.state_5, survey_response.state_5.number)
        self.assertEquals(survey_path.state_6, survey_response.state_6.number)
        self.assertEquals(survey_path.state_7, survey_response.state_7.number)
        self.assertEquals(survey_path.state_8, survey_response.state_8.number)

    def test_responses_dont_get_the_same_path(self):
        Factory.survey_path(order=1)
        Factory.survey_path(order=2)
        user, password = Factory.user()
        user2, password = Factory.user()

        survey_response1 = SurveyResponse.objects.create(user=user)
        survey_response2 = SurveyResponse.objects.create(user=user2)

        self.assertNotEquals(survey_response1.survey_path_id, survey_response2.survey_path_id)

    def test_making_a_new_response_creates_the_rating_objects(self):
        survey_path = Factory.survey_path()
        user, password = Factory.user()

        survey_response = SurveyResponse.objects.create(user=user)

        self.assertEquals(survey_response.ratings.get(health_state=survey_path.state_1).health_state.number, survey_path.state_1)
        self.assertEquals(survey_response.ratings.get(health_state=survey_path.state_2).health_state.number, survey_path.state_2)
        self.assertEquals(survey_response.ratings.get(health_state=survey_path.state_3).health_state.number, survey_path.state_3)
        self.assertEquals(survey_response.ratings.get(health_state=survey_path.state_4).health_state.number, survey_path.state_4)
        self.assertEquals(survey_response.ratings.get(health_state=survey_path.state_5).health_state.number, survey_path.state_5)
        self.assertEquals(survey_response.ratings.get(health_state=survey_path.state_6).health_state.number, survey_path.state_6)
        self.assertEquals(survey_response.ratings.get(health_state=survey_path.state_7).health_state.number, survey_path.state_7)
        self.assertEquals(survey_response.ratings.get(health_state=survey_path.state_8).health_state.number, survey_path.state_8)
