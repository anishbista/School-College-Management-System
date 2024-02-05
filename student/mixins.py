from django.shortcuts import redirect


class StudentRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        if not hasattr(request.user, "student"):
            return redirect("login")

        return super().dispatch(request, *args, **kwargs)
