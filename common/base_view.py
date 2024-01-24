from django.views import View


class BaseView(View):
    template_name = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["active_tab"] = self.active_tab
        return context
