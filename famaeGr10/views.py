import textwrap

from django.http import HttpResponse
from django.views.generic.base import View


class TestPage(View):

    def dispatch(self, request, *args, **kwargs):
        response_text = textwrap.dedent('''\
            <html>
            <head>
                <title>Famae Project</title>
            </head>
            <body>
                <h1> Carte ''' + kwargs['zip_code'] + '''</h1>
            </body>
            </html>
        ''')
        return HttpResponse(response_text)