from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout, authenticate, login

# Sign Up view
def sign_up(request):
    if request.user.is_authenticated:  # Check if the user is already authenticated
        return redirect('home')  # Redirect to home or another page if user is authenticated

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        try:
            if form.is_valid():
                form.save()
                messages.success(request, 'Registration successfully completed.')
                return redirect('accounts:sign_in')
        except Exception as e:
            messages.error(request, str(e))  # Display the actual error message
            return redirect('accounts:sign_up')
    else:
        form = SignUpForm()

    context = {
        'form': form
    }
    return render(request, 'registration/sign_up.html', context)


# Sign In view
def sign_in(request):
    if request.user.is_authenticated:  # Check if the user is already authenticated
        return redirect('home')  # Redirect to home or another page if user is authenticated

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                messages.success(request, 'You have signed in successfully.')
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password.')
                return redirect('accounts:sign_in')
        else:
            messages.error(request, 'Username and password didn\'t match!')
            return redirect('accounts:sign_in')
    
    else:
        form = AuthenticationForm()

    context = {
        'form': form,
    }

    return render(request, 'registration/sign_in.html', context)


# Sign Out view
def sign_out(request):
    try:
        logout(request)
        messages.success(request, 'You have signed out successfully!')
        return redirect('accounts:sign_in')
    except Exception as e:
        messages.error(request, 'There was an error logging you out.')
        return redirect('home')
