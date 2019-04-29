# diff way of doing login logic
#not fully complete
if request.method == 'POST':
        #form = LoginForm(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('home/'))
            else:
                return HttpResponse("Account Not Active Sorry MATE :(")

        else:
            print("Login Failed")
            return HttpResponse("Wrong Password Or Username")
    else:
    
    context = {'form': form}
    http_response = render(request, 'login.html')
    return HttpResponse(http_response)
