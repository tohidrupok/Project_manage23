from django import forms
from django.core import validators


#widgets useing field to html formate
class contactForm(forms.Form):
    name = forms.CharField(label="Full name: ", help_text="bhia limited char 30", required=False,
                           widget = forms.Textarea(attrs={'id':'rupok_area_text','placeholder':'Enter your name boss'}))
    file = forms.FileField()
    email =forms.EmailField(label="email")
    # age =forms.IntegerField()
    # weight = forms.FloatField()
    # balance = forms.DecimalField() 
    age = forms.CharField(widget=forms.NumberInput)
    check =forms.BooleanField()
    birthday = forms.CharField(widget=forms.DateInput( attrs= {'type' : 'date'}))
    appointment = forms.CharField(widget=forms.DateInput(attrs= {'type' : 'datetime-local'}))
    # appointment = forms.CharField(widget=forms.DateInput( attrs= {'type' : 'datetime-local'}))
    
    CHOICES = [('S','Small'),('M','medium'),('S','Medium')]
    size = forms.ChoiceField(choices=CHOICES , widget = forms.RadioSelect )
    MEAL = [('P','Pepproni'),('m',"Medical"),('B',"Beef")]
    PIzza = forms.MultipleChoiceField(choices=MEAL, widget= forms.CheckboxSelectMultiple)
    
class StudentData(forms.Form):
    name = forms.CharField(widget=forms.TextInput, validators=[validators.MaxLengthValidator(10,message='maximum 10 characters are avaibale.')] )
    email = forms.CharField(widget=forms.EmailInput)
    # age = forms.CharField(widget=forms.NumberInput,validators=[validators.MaxValueValidator(40,message='maximum use 40 years old.'),validators.MinValueValidator(18,message="baccha is not allow.")])
    
    age = forms.IntegerField(validators=[validators.MaxValueValidator(34, message="age must be maximum 34"),validators.MinValueValidator(24, message="age must be at least 24")])
    file = forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['pdf','png'], message = 'File Extension must be ended with .pdf')])
    
    
class passwordvalidationproject(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    re_password = forms.CharField(widget=forms.PasswordInput)
    
    def clean(self):
        cleaned_data = super().clean()
        Pass = self.cleaned_data['password']
        re_pas = self.cleaned_data['re_password']
        val_name = self.cleaned_data['name']
        
        if Pass != re_pas:
            raise forms.ValidationError("Does not match password.")   
        
        if len(val_name) < 15:
            raise forms.ValidationError("At least 15 charactors you must be use.")     
    
    
    
    
    
    
    
    
    
    
    
    
    
# class StudentData(forms.Form):
#     name = forms.CharField(widget=forms.TextInput)
#     email = forms.CharField(widget=forms.EmailInput)
#     def clean(self):
#         cleaned_data = super().clean()
#         valname = self.cleaned_data['name']
#         valemail = self.cleaned_data['email']
#         if len(valname) < 10:
#              raise forms.ValidationError("Enter a name with at least 10 characters")    
#         if '.com' not in valemail:
#             raise forms.ValidationError("Your email must contain .com")
    
       
    # def clean_name(self):
    #     valname = self.cleaned_data['name']
    #     if len(valname) < 10:
    #         raise forms.ValidationError("Enter a name with at least 10 characters")
    #     return valname
    
    # def clean_email(self):
    #     valname = self.cleaned_data['email']
    #     if '.com' not in valname:
    #         raise forms.ValidationError("your email must be contain .com")
    #     else:
    #         return valname
        
    
    
    
            
        