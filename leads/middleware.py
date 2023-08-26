from django.middleware.common import CommonMiddleware

# dev: For experiment only.


class CustomLocaleMiddleware(CommonMiddleware):
    def process_template_response(self, request, response):
        # Modify a string in the context before rendering the template
        if 'my_string' in response.context_data:
            response.context_data['my_string'] = "welcome"

        return response
