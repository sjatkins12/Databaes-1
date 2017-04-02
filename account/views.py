from django.shortcuts import render, redirect
from account.forms import UserForm, UserProfileForm
from django.views.generic import View
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
class UserFormView(View):
    form1_class = UserForm
    form2_class = UserProfileForm
    template_name = 'register/registration_form.html'
    
    # Displays blank form 
    def get(self, request):
        user_form = self.form1_class(None)
        profile_form = self.form2_class(None)
        return render(request, self.template_name, {'user_form': user_form, 'profile_form': profile_form})
    
    @csrf_exempt
    # Process form data
    def post(self, request):
        user_form = self.form1_class(request.POST)
        profile_form = self.form2_class(request.POST)
        
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            username = user_form.cleaned_data['username']
            password = user_form.cleaned_data['password']
            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()
            
            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            
            #Returns User objects if credentials are correct
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    # Grab user session info
                    # name = request.user.username
                    return redirect('homepage')
                    
                    
                    
        return render(request, self.template_name, {'user_form': user_form, 'profile_form': profile_form})
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            