from django.shortcuts import redirect


class StaffRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        if not hasattr(request.user, "staff"):
            return redirect("login")
        return super().dispatch(request, *args, **kwargs)
