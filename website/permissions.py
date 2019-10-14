from django.shortcuts import redirect

class SuperUserRequired(object):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        return redirect('home')

class StaffUserRequired(object):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_staff:
            return super().dispatch(request, *args, **kwargs)
        return redirect('home')


# class GuideAccessRequired(object):
#     def dispatch(self, request, *args, **kwargs):
#         if request.user.is_authenticated:
#             if request.user.has_active_guide:
#                 return super().dispatch(request, *args, **kwargs)
#         return redirect('my-account')


# class PastIssuesAccessRequired(object):
#     def dispatch(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         if request.user.is_authenticated:
#             if request.user.get_subscription():
#                 if request.user.user_type == 'premium':
#                     return super().dispatch(request, *args, **kwargs)
#                 else:
#                     start_issue = request.user.get_subscription().current_issue
#                     if not request.user.get_subscription().plan.recurring:
#                         if start_issue == self.object:
#                             return super().dispatch(request, *args, **kwargs)
#                     else:
#                         start_date = date(start_issue.release_year, start_issue.release_month, 1)
#                         end_date = start_date + timedelta(days=365)
#                         current_issue_date = date(self.object.release_year, self.object.release_month, 1)
#                         if start_date <= current_issue_date <= end_date:
#                             return super().dispatch(request, *args, **kwargs)
#         request.session['no_access'] = True
#         return redirect('journal_latest_issue')

# class NewsAccessRequired(object):
#     def dispatch(self, request, *args, **kwargs):
#         if Story.objects.published().get(slug=self.kwargs['slug']).is_members_only == False:
#             return super().dispatch(request, *args, **kwargs)
#         else:
#             if request.user.is_authenticated:
#                 if request.user.get_subscription():
#                     return super().dispatch(request, *args, **kwargs)
#         request.session['no_access'] = True
#         return redirect('news')
