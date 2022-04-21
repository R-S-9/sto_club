import json

from django.views.generic import ListView

from ..models import ServiceSTO, UUIDEncoder


class InfoListView(ListView):
    model = ServiceSTO

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qs_json"] = json.dumps(
            list(ServiceSTO.objects.values()), cls=UUIDEncoder
        )

        return context
