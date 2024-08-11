from django.urls import reverse
from assemblyaimodule import views
from unittest.mock import patch
from rest_framework.test import APITestCase
from rest_framework import status

class TranscribeTestCase(APITestCase):

    # Test 1: Test transcribe() invalid
    @patch('assemblyaimodule.views.AudioFileSerializer')
    def test_transcribe_invalid(self, MockSerializer):

        # Mock serializer object as invalid with error
        mock_serializer = MockSerializer.return_value
        mock_serializer.is_valid.return_value = False
        test_error = "This is a testing error"
        mock_serializer.errors = test_error

        # Mock a POST request
        response = self.client.post(reverse('transcribe'))

        # Assert the response
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, test_error)

        # Assert function calls
        MockSerializer.assert_called_once()
    
    # Test 2: Test transcribe() valid
    @patch('assemblyaimodule.views.TS.transcribe')
    @patch('assemblyaimodule.views.FileSystemStorage')
    @patch('assemblyaimodule.views.AudioFileSerializer')
    def test_transcribe_valid(self, MockSerializer, MockStorage, MockTranscribe):

        # Mock serializer object as valid
        mock_serializer = MockSerializer.return_value
        mock_serializer.is_valid.return_value = True

        # Mock uploaded file
        mock_storage = MockStorage.return_value
        mock_storage.save.return_value = "saved_file"

        # Mock transcription tesult
        test_text = "I am testing, testing."
        transcription_result = {'transcription': test_text}
        MockTranscribe.return_value = test_text

        # Mock a POST request
        response = self.client.post(reverse('transcribe'))

        # Assert the response
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, transcription_result)

        # Assert function calls  
        MockSerializer.assert_called_once()
        mock_serializer.is_valid.assert_called_once()
        MockStorage.assert_called_once()
        mock_storage.save.assert_called_once()
        mock_storage.save.assert_called_with(mock_serializer.validated_data['audio_file'].name, mock_serializer.validated_data['audio_file'])
        mock_storage.delete.assert_called_once()
        mock_storage.delete.assert_called_with(mock_storage.save.return_value)
        MockTranscribe.assert_called_once()
        MockTranscribe.assert_called_with(views.UPLOAD_DIRECTORY_PATH + mock_storage.save.return_value)

    # Test 3: Test transcribe_with_speakers() invalid
    @patch('assemblyaimodule.views.AudioFileSerializer')
    def test_transcribe_speaker_invalid(self, MockSerializer):

        # Mock serializer object as invalid with error
        mock_serializer = MockSerializer.return_value
        mock_serializer.is_valid.return_value = False
        test_error = "This is a testing error"
        mock_serializer.errors = test_error

        # Mock a POST request
        response = self.client.post(reverse('transcribe_with_speakers'))

        # Assert the response
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, test_error)

        # Assert function calls
        MockSerializer.assert_called_once()
    
    # Test 4: Test transcribe_with_speakers() valid
    @patch('assemblyaimodule.views.TS.transcribe_with_speakers')
    @patch('assemblyaimodule.views.FileSystemStorage')
    @patch('assemblyaimodule.views.AudioFileSerializer')
    def test_transcribe_speaker_valid(self, MockSerializer, MockStorage, MockTranscribe):

        # Mock serializer object as valid
        mock_serializer = MockSerializer.return_value
        mock_serializer.is_valid.return_value = True

        # Mock uploaded file
        mock_storage = MockStorage.return_value
        mock_storage.save.return_value = "saved_file"

        # Mock transcription tesult
        test_text = "I am testing, testing."
        transcription_result = {'transcription': test_text}
        MockTranscribe.return_value = test_text

        # Mock a POST request
        response = self.client.post(reverse('transcribe_with_speakers'))

        # Assert the response
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, transcription_result)

        # Assert function calls  
        MockSerializer.assert_called_once()
        mock_serializer.is_valid.assert_called_once()
        MockStorage.assert_called_once()
        mock_storage.save.assert_called_once()
        mock_storage.save.assert_called_with(mock_serializer.validated_data['audio_file'].name, mock_serializer.validated_data['audio_file'])
        mock_storage.delete.assert_called_once()
        mock_storage.delete.assert_called_with(mock_storage.save.return_value)
        MockTranscribe.assert_called_once()
        MockTranscribe.assert_called_with(views.UPLOAD_DIRECTORY_PATH + mock_storage.save.return_value)





        

    

        