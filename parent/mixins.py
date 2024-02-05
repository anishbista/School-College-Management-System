from django.shortcuts import redirect


class ParentRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        if not hasattr(request.user, "parent"):
            return redirect("login")
        return super().dispatch(request, *args, **kwargs)
