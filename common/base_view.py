from django.views import View


class BaseView(View):
    template_name = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["active_tab"] = self.active_tab
        return context


def user_context(request):
    user_attributes = ["student", "teacher", "parent"]
    profile = None
    user_type = None

    if request.user.is_authenticated:
        for user in user_attributes:
            if hasattr(request.user, user):
                user_type = user
                profile = getattr(request.user, user)

    return {"user_type": user_type, "profile": profile}
