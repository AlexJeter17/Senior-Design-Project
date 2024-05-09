import unittest
from concurrent.futures import ThreadPoolExecutor, as_completed
from main import generate_response 

class TestModelGeneration(unittest.TestCase):

    ### THE FOLLOWING ARE GENERAL TESTS ###

    def test_generate_response(self):
        """Test that the generate_response function returns a non-empty string."""
        prompt = "Hello, world!"
        response = generate_response(prompt)
        self.assertIsInstance(response, str)
        self.assertTrue(len(response) > 0)

    def test_response_content(self):
        """Test that the response correctly contains expected content."""
        prompt = "What day is today?"
        response = generate_response(prompt)
        # This is a basic check; adjust the expected string based on your model's training and capabilities
        self.assertIn("day", response)

    def test_empty_prompt(self):
        """Test the response to an empty prompt."""
        response = generate_response('')
        self.assertEqual(response, "Error: Unable to generate a response.")

    def test_null_input(self):
        """Test the function with None as input."""
        with self.assertRaises(TypeError):
            generate_response(None)

    def test_output_type(self):
        """Ensure that output is always a string."""
        prompt = "Check output type."
        response = generate_response(prompt)
        self.assertIsInstance(response, str)

    # def test_maximum_length(self):
    #     """Test that the response does not exceed 50 tokens."""
    #     prompt = "Generate a long response to test the maximum length of the output."
    #     response = generate_response(prompt)
    #     self.assertTrue(len(tokenize.tokenize(response)) <= 50)

    def test_prompt_sensitivity(self):
        """Test that different prompts result in different responses."""
        prompt1 = "What is the weather today?"
        prompt2 = "What is the weather tomorrow?"
        response1 = generate_response(prompt1)
        response2 = generate_response(prompt2)
        self.assertNotEqual(response1, response2)

    def test_keyword_inclusion(self):
        """Ensure specific keywords are included in the response."""
        prompt = "Tell me about artificial intelligence."
        expected_keywords = ["AI", "machine learning", "data"]
        response = generate_response(prompt)
        self.assertTrue(any(keyword in response for keyword in expected_keywords))

    def test_unusual_characters(self):
        """Test the response to prompts containing unusual characters."""
        prompt = "Hello, world! @#$%^&*()"
        response = generate_response(prompt)
        self.assertIsInstance(response, str)

    def test_consistency(self):
        """Check that the same prompt returns the same response on multiple invocations."""
        prompt = "Consistency check for the same prompt."
        response1 = generate_response(prompt)
        response2 = generate_response(prompt)
        self.assertEqual(response1, response2)

    def test_long_prompt_handling(self):
        """Test the function's ability to handle very long prompts."""
        prompt = "a" * 1000  # A very long string
        response = generate_response(prompt)
        self.assertTrue(len(response) > 0)

    def test_performance(self):
        """Benchmark the time it takes to generate a response to ensure performance standards."""
        import time
        start_time = time.time()
        prompt = "Performance testing with a standard prompt."
        generate_response(prompt)
        elapsed_time = time.time() - start_time
        self.assertLess(elapsed_time, 5)  # Assert the response is generated in less than 5 seconds


    ### THE FOLLOWING ARE SARCASTIC DETECTION TESTS ###

    def test_sarcastic_praise(self):
        """Test response to sarcastic praise."""
        prompt = "Oh great, another email from the boss at midnight."
        response = generate_response(prompt)
        self.assertIn("late", response)  # Expecting a response acknowledging the lateness.
    
    def test_sarcastic_complaint(self):
        """Test response to a sarcastic complaint about technology."""
        prompt = "I just love it when my computer crashes during an unsaved project."
        response = generate_response(prompt)
        self.assertIn("sorry", response)  # Check for an apologetic or understanding tone.
    
    def test_sarcastic_thank_you(self):
        """Test handling of a sarcastic thank you."""
        prompt = "Thanks for stepping on my new shoes, really appreciated that!"
        response = generate_response(prompt)
        self.assertNotIn("welcome", response)  # Ensure it doesn't respond with "You're welcome."
    
    def test_sarcastic_suggestion(self):
        """Test response to sarcastic suggestion."""
        prompt = "Sure, let's have the meeting at 6 AM, that would be so convenient."
        response = generate_response(prompt)
        self.assertIn("early", response)  # Looking for acknowledgment of the inconvenience.
    
    def test_sarcastic_disappointment(self):
        """Test model's understanding of sarcastic disappointment."""
        prompt = "Oh fantastic, it's raining again on my day off!"
        response = generate_response(prompt)
        self.assertIn("rain", response)  # The response should relate to weather disappointment.

### THE FOLLOWING IS FOR CONTEXT RETENTION ###

    def setUp(self):
        # Setting an initial context
        self.initial_prompt = "I just moved to a new city for a new job."
        generate_response(self.initial_prompt)

    def test_job_related_follow_up(self):
        prompt = "How should I commute to work?"
        response = generate_response(prompt)
        self.assertIn("bus", response)  # Example: Expecting suggestions related to city commuting.

    def test_city_related_follow_up(self):
        prompt = "What's there to do here on weekends?"
        response = generate_response(prompt)
        self.assertIn("parks", response)  # Example: Assuming the city is known for parks or outdoor activities.

    def test_housing_related_follow_up(self):
        prompt = "Where is a good place to find an apartment?"
        response = generate_response(prompt)
        self.assertIn("downtown", response)  # Example: Suggesting a common residential area.

    def test_cultural_adaptation_follow_up(self):
        prompt = "Any tips on getting used to this place?"
        response = generate_response(prompt)
        self.assertIn("meet", response)  # Example: Suggesting meeting new people or joining local groups.

    def test_weather_related_follow_up(self):
        prompt = "What’s the weather usually like?"
        response = generate_response(prompt)
        self.assertIn("variable", response)  # Example: General information about weather.

    def test_food_related_follow_up(self):
        prompt = "What's a popular dish here?"
        response = generate_response(prompt)
        self.assertIn("seafood", response)  # Assuming a coastal city.

    def test_transport_options_follow_up(self):
        prompt = "Is it better to drive or use public transport?"
        response = generate_response(prompt)
        self.assertIn("public transport", response)  # Assuming a well-connected city.

    def test_socializing_options_follow_up(self):
        prompt = "How can I make new friends here?"
        response = generate_response(prompt)
        self.assertIn("clubs", response)  # Suggesting joining clubs or social groups.

    def test_safety_related_follow_up(self):
        prompt = "Is it safe to walk around at night?"
        response = generate_response(prompt)
        self.assertIn("generally safe", response)  # General safety advice.

    def test_recreational_activities_follow_up(self):
        prompt = "Are there any good hiking trails?"
        response = generate_response(prompt)
        self.assertIn("trails", response)  # Suggesting popular hiking trails.

### THE FOLLOWING IS FOR EMOTIONALLY CHARGED PROMPTS ###

    def test_joyful_event_response(self):
        prompt = "I just graduated from college!"
        response = generate_response(prompt)
        self.assertIn("congratulations", response)

    def test_sorrowful_event_response(self):
        prompt = "It's the anniversary of my mother's passing today."
        response = generate_response(prompt)
        self.assertIn("sorry", response)

    def test_exciting_event_response(self):
        prompt = "We're going on a safari next week!"
        response = generate_response(prompt)
        self.assertIn("exciting", response)

    def test_nervous_event_response(self):
        prompt = "I have my first job interview tomorrow."
        response = generate_response(prompt)
        self.assertIn("good luck", response)

    def test_anger_frustration_response(self):
        prompt = "My flight got canceled last minute."
        response = generate_response(prompt)
        self.assertIn("frustrating", response)

    def test_surprise_event_response(self):
        prompt = "My best friend just surprised me with a visit."
        response = generate_response(prompt)
        self.assertIn("surprised", response)

    def test_anxious_event_response(self):
        prompt = "I'm feeling really anxious about the news today."
        response = generate_response(prompt)
        self.assertIn("understand", response)

    def test_relief_event_response(self):
        prompt = "Finally, my medical results came back clear!"
        response = generate_response(prompt)
        self.assertIn("relieved", response)

### THE FOLLOWING IS TO TEST LOAD AND STRESS ON THE LLM

    def test_peak_load(self):
        """Test handling of peak simulated user load."""
        prompts = ["What is the capital of France?"] * 100  # Simulate 100 concurrent requests
        with ThreadPoolExecutor(max_workers=100) as executor:
            future_to_prompt = {executor.submit(generate_response, prompt): prompt for prompt in prompts}
            for future in as_completed(future_to_prompt):
                prompt = future_to_prompt[future]
                try:
                    response = future.result()
                except Exception as exc:
                    print('%r generated an exception: %s' % (prompt, exc))
                else:
                    self.assertIn("Paris", response)  # Assuming the model responds consistently

    def test_high_volume_simple_queries(self):
        """Test the model's ability to handle a high volume of simple queries."""
        prompts = ["Tell me the time."] * 200  # Simulate 200 simple time inquiries
        responses = []
        with ThreadPoolExecutor(max_workers=50) as executor:
            futures = [executor.submit(generate_response, prompt) for prompt in prompts]
            for future in as_completed(futures):
                responses.append(future.result())
        # Check all responses contain expected keywords
        self.assertTrue(all("time" in response.lower() for response in responses))

    def test_data_intensive_requests(self):
        """Test handling of requests that require deep data processing."""
        prompts = ["Explain quantum physics in detail."] * 50  # Challenging queries requiring more processing
        responses = []
        with ThreadPoolExecutor(max_workers=50) as executor:
            futures = [executor.submit(generate_response, prompt) for prompt in prompts]
            for future in as_completed(futures):
                responses.append(future.result())
        # Ensure responses are valid and contain expected deep topic content
        self.assertTrue(all("quantum" in response.lower() for response in responses))

    def test_mixed_request_types(self):
        """Simulate a mix of different types of queries to see how the model copes with varied inputs."""
        prompts = ["What is the weather in New York?", "Calculate the square root of 144.", "Translate 'hello' to Spanish.", "What is Elon Musk's latest tweet?"] * 25
        responses = []
        with ThreadPoolExecutor(max_workers=50) as executor:
            futures = [executor.submit(generate_response, prompt) for prompt in prompts]
            for future in as_completed(futures):
                responses.append(future.result())
        # Basic check to ensure no empty responses
        self.assertTrue(all(response for response in responses))

    def test_sustained_load_over_time(self):
        """Apply a constant moderate load over an extended period to monitor for performance degradation."""
        prompts = ["Give me a brief history of the Roman Empire."] * 100
        responses = []
        with ThreadPoolExecutor(max_workers=30) as executor:
            futures = [executor.submit(generate_response, prompt) for prompt in prompts]
            for future in as_completed(futures):
                responses.append(future.result())
        # Check for consistency in response quality
        self.assertTrue(all("roman" in response.lower() for response in responses))

    def test_geographical_distribution(self):
        """Test response times and integrity from various simulated geographic locations."""
        # This would typically require more setup or an external tool to simulate geo-locations
        prompts = ["What time is it in Tokyo?"] * 100
        responses = []
        with ThreadPoolExecutor(max_workers=50) as executor:
            futures = [executor.submit(generate_response, prompt) for prompt in prompts]
            for future in as_completed(futures):
                responses.append(future.result())
        # Check responses are appropriate for the geographic query
        self.assertTrue(all("time" in response.lower() for response in responses))




if __name__ == '__main__':
    unittest.main()
