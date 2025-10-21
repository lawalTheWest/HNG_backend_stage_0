from django.test import TestCase

class ProfileEndpointTests(TestCase):
    def test_profile_endpoint_status_code(self):
        response = self.client.get('/me/')
        self.assertEqual(response.status_code, 200)

    def test_profile_endpoint_response_structure(self):
        response = self.client.get('/me/')
        data = response.json()
        self.assertIn('status', data)
        self.assertIn('user', data)
        self.assertIn('timestamp', data)
        self.assertIn('fact', data)
        self.assertEqual(data['status'], 'success')
        self.assertIn('email', data['user'])
        self.assertIn('name', data['user'])
        self.assertIn('stack', data['user'])