from django import forms
from django.contrib.auth.models import User
from liquor_locator.models import UserProfile, Comment

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture')


#<input type="text" class="form-control" placeholder="Username" aria-describedby="basic-addon1">
class CommentForm(forms.ModelForm):
    comment = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control input-lg', 'placeholder': 'Comment',
        'aria-describedby': 'addon1'}))

    class Meta:
        # Provide an association between the ModelForm and a model
        model = Comment
        fields = ('comment',)

        # What fields do we want to include in our form?
        # This way we don't need every field in the model present.
        # Some fields may allow NULL values, so we may not want to include them...
        # Here, we are hiding the foreign key.
        # we can either exclude the category field from the form,
        # exclude = ('category',)
        #or specify the fields to include (i.e. not include the category field)
        #fields = ('title', 'url', 'views')

class EditForm(forms.ModelForm):
	comment = forms.CharField(max_length=123, help_text="Edit:", initial="")

	class Meta:
		model = Comment
		fields = ('comment',)