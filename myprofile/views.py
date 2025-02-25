from django.db import transaction
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import *
from .models import Profile


class ProfileList(ListView):
    model = Profile


class ProfileCreate(CreateView):
    model = Profile
    fields = ['first_name', 'last_name']


class ProfileFamilyMemberCreate(CreateView):
    model = Profile
    fields = ['first_name', 'last_name']
    success_url = reverse_lazy('profile-list')

    def get_context_data(self, **kwargs):
        data = super(ProfileFamilyMemberCreate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['familymembers'] = FamilyMemberFormSet(self.request.POST)
            data['edu'] = EduFormSet(self.request.POST)
        else:
            data['familymembers'] = FamilyMemberFormSet()
            data['edu'] = EduFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        familymembers = context['familymembers']
        edu = context['edu']
        with transaction.atomic():
            self.object = form.save()

            if familymembers.is_valid():
                familymembers.instance = self.object
                familymembers.save()

            if edu.is_valid():
                edu.instance = self.object
                edu.save()
        return super(ProfileFamilyMemberCreate, self).form_valid(form)


class ProfileUpdate(UpdateView):
    model = Profile
    success_url = '/'
    fields = ['first_name', 'last_name']


class ProfileFamilyMemberUpdate(UpdateView):
    model = Profile
    fields = ['first_name', 'last_name']
    success_url = reverse_lazy('profile-list')

    def get_context_data(self, **kwargs):
        data = super(ProfileFamilyMemberUpdate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['familymembers'] = FamilyMemberFormSet(self.request.POST, instance=self.object)
            data['edu'] = EduFormSet(self.request.POST, instance=self.object)
        else:
            data['familymembers'] = FamilyMemberFormSet(instance=self.object)
            data['edu'] = EduFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        familymembers = context['familymembers']
        edu = context['edu']
        with transaction.atomic():
            self.object = form.save()

            if familymembers.is_valid():
                familymembers.instance = self.object
                familymembers.save()

            if edu.is_valid():
                edu.instance = self.object
                edu.save()
        return super(ProfileFamilyMemberUpdate, self).form_valid(form)


class ProfileDelete(DeleteView):
    model = Profile
    success_url = reverse_lazy('profile-list')
