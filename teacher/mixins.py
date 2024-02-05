from django.shortcuts import redirect


class TeacherRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        # Check if the user is a teacher
        if not hasattr(request.user, "teacher"):
            return redirect("login")

        # Proceed with the rest of the code
        return super().dispatch(request, *args, **kwargs)
