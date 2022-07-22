from django.forms import ModelForm, inlineformset_factory

from .models import Education, Profile, FamilyMember


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ()


class FamilyMemberForm(ModelForm):
    class Meta:
        model = FamilyMember
        exclude = ()

class EduForm(ModelForm):
    class Meta:
        model = Education
        exclude = ()


FamilyMemberFormSet = inlineformset_factory(Profile, FamilyMember,
                                            form=FamilyMemberForm, extra=1)


EduFormSet = inlineformset_factory(Profile, Education,
                                            form=EduForm, extra=1)
