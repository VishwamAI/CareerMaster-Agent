import unittest
from bs4 import BeautifulSoup
from analyze_linkedin import parse_linkedin_profile, format_resume
import os

class TestAnalyzeLinkedIn(unittest.TestCase):

    def setUp(self):
        with open('sample_linkedin_profile.html', 'r') as file:
            self.html_content = file.read()
        self.profile_data = parse_linkedin_profile(self.html_content)

    def test_parse_linkedin_profile(self):
        self.assertEqual(self.profile_data['name'], 'John Doe')
        self.assertEqual(self.profile_data['headline'], 'Software Engineer at Example Company')
        self.assertEqual(self.profile_data['summary'], 'Experienced software engineer with a passion for developing innovative programs...')
        self.assertEqual(len(self.profile_data['experience']), 2)
        self.assertEqual(self.profile_data['experience'][0]['title'], 'Senior Software Engineer')
        self.assertEqual(self.profile_data['experience'][0]['company'], 'Example Company')
        self.assertEqual(self.profile_data['experience'][0]['date_range'], 'Jan 2020 - Present')
        self.assertEqual(self.profile_data['experience'][0]['location'], 'San Francisco, CA')
        self.assertEqual(len(self.profile_data['education']), 1)
        self.assertEqual(self.profile_data['education'][0]['school'], 'Example University')
        self.assertEqual(self.profile_data['education'][0]['degree'], 'Bachelor of Science')
        self.assertEqual(self.profile_data['education'][0]['field_of_study'], 'Computer Science')
        self.assertEqual(self.profile_data['education'][0]['date_range'], '2015 - 2019')
        self.assertEqual(len(self.profile_data['skills']), 3)
        self.assertIn('Python', self.profile_data['skills'])
        self.assertIn('Java', self.profile_data['skills'])
        self.assertIn('C++', self.profile_data['skills'])
        self.assertEqual(len(self.profile_data['certifications']), 1)
        self.assertEqual(self.profile_data['certifications'][0]['cert_name'], 'Certified Kubernetes Administrator')
        self.assertEqual(self.profile_data['certifications'][0]['issuing_organization'], 'The Linux Foundation')
        self.assertEqual(self.profile_data['certifications'][0]['date_range'], '2021')

    def test_format_resume(self):
        output_file = 'test_resume.docx'
        format_resume(self.profile_data, output_file)
        self.assertTrue(os.path.exists(output_file))
        os.remove(output_file)

if __name__ == '__main__':
    unittest.main()
