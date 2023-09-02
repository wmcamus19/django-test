from django.middleware.common import CommonMiddleware

# TODO: For experiment only.


class CustomLocaleMiddleware(CommonMiddleware):
    def process_template_response(self, request, response):
        # Modify a string in the context before rendering the template
        if 'aw' in response.context_data:
            response.context_data['aw'] = "welcome"

        return response
