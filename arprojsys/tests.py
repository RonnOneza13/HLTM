from django.test import TestCase
from arprojsys.views import MainPage
from .models import HealthyContact

class HomePageTest(TestCase):
	def test_mainpage_as_seen_client(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'mainpage.html')

	def test_save_POST_request(self):
		response = self.client.post('/', {'name' :'Aron Dale',
	 		'email': 'oneza@gmail.com',
	 		'review': 'Delicious'})
		self.assertEqual(HealthyContact.objects.count(),1)
		inputData = HealthyContact.objects.first()
		self.assertEqual(inputData.PName1, 'Aron Dale')
		self.assertEqual(inputData.PEmail1, 'oneza@gmail.com')
		self.assertEqual(inputData.PReview1, 'Delicious')

	def test_only_saves_items_if_necessary(self):
		self.client.get('/')
		self.assertEqual(HealthyContact.objects.count(), 0)

	def test_post_redirect(self):
		response = self.client.post('/', {'name' :'Aron Dale',
	 		'email': 'oneza@gmail.com',
	 		'review': 'Delicious'})
		self.assertEqual(response.status_code, 302)
		self.assertEqual(response['location'], '/')


class ORMTEST(TestCase):
	def test_saving_retrive(self):
		HealthyContact1 = HealthyContact()
		HealthyContact1.PName1 = 'Aron Dale'
		HealthyContact1.PEmail1 = 'oneza@gmail.com'
		HealthyContact1.PReview1 = 'Delicious'
		HealthyContact1.save()

		HealthyContact2 = HealthyContact()
		HealthyContact2.PName1 = 'Ronn Dale'
		HealthyContact2.PEmail1= 'smoothpudding13@gmail.com'
		HealthyContact2.PReview1= 'Sarap'
		HealthyContact2.save()

		HealthyContact_file = HealthyContact.objects.all()
		self.assertEqual(HealthyContact_file.count(), 2)

		d1 = HealthyContact_file[0]
		d2 = HealthyContact_file[1]

		self.assertEqual(d1.PName1, 'Aron Dale')
		self.assertEqual(d1.PEmail1, 'oneza@gmail.com')
		self.assertEqual(d1.PReview1, 'Delicious')

		self.assertEqual(d2.PName1, 'Ronn Dale')
		self.assertEqual(d2.PEmail1, 'smoothpudding13@gmail.com')
		self.assertEqual(d2.PReview1, 'Sarap')


	def test_template_display_list(self):
		HealthyContact.objects.create(PName1 = 'Aron',
			PEmail1 = 'ronnonez@gmail.com',
			PReview1 = 'Deliciou')

		HealthyContact.objects.create(PName1 = 'Ronn',
			PEmail1= 'smoothpudding1@gmail.com',
			PReview1 = 'Sara')

		response = self.client.get('/')
		self.assertIn('1: Aron, ronnonez@gmail.com, Deliciou', response.content.decode())
# 		self.assertIn('2: Ronn, smoothpudding1@gmail.com, Sara', response.content.decode())