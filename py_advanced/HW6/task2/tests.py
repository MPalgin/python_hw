import pytest
from Python_course.py_advanced.HW6.task2.functions import folder_creator
TEST_DATA = {
    'Test1': [
        {'token': '', 'folder_name': '123',
         'response': 201},
        {'token': '', 'folder_name': '456',
         'response': 201}
    ],
    'Test2': [
        {'token': '', 'folder_name': '123',
         'response': 409},
        {'token': '', 'folder_name': '123456/123',
         'response': 409},
        {'token': '123', 'folder_name': '123', 'response': 401},

    ]
}

class TestFolders:
    @pytest.mark.parametrize('testdata', TEST_DATA['Test1'])
    def test_success_folder_creation(self, testdata):
        assert folder_creator(testdata['folder_name'], testdata['token']) == testdata['response']

    @pytest.mark.parametrize('testdata', TEST_DATA['Test2'])
    def test_folder_creation_with_error(self, testdata):
        assert folder_creator(testdata['folder_name'], testdata['token']) == testdata['response']
