from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        
        user = User.objects.create_user(username=username, email=email, password=password)
        login(request, user)
        return redirect('sort')  
    return render(request, 'signup.html')



def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('sort')  
    return render(request, 'login.html')


@login_required(login_url='login')
def user_logout(request):
    logout(request)
    return redirect('login')  




def sort_view(request):
    sorted_arr = None
    original_arr = None 
    input_arr = None

    if request.method == 'POST':
        algorithm = request.POST.get('algorithm')
        data = request.POST.get('data')

        input_arr = [int(num) for num in data.split(',') if num.strip()]

        original_arr = input_arr.copy()
        
        if algorithm == 'bubble':
            sorted_arr = bubble_sort(original_arr)
        elif algorithm == 'selection':
            sorted_arr = selection_sort(original_arr)
        elif algorithm == 'insertion':
            sorted_arr = insertion_sort(original_arr)

    return render(request, 'sort.html', {'sorted_arr': sorted_arr, 'original_arr': input_arr})



def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr



def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
