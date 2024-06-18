import reverse
class CarsListView(ListView):
    model = Car 
    template_name = 'cars.html'
    context_onject_name = 'cars'

    def get_queryset(self):
        cars = super().get_queryset().order_by('model')
        search = self.request.GET.get('search')
        if search:
            cars = cars.filter(model_icontains=seach)
            returs cars

            lass CarDetailView(DetailView):
            model = Cartemplate_name = 'car_detail.html'

            nethod_decorator(login_required(login_url='login')name='dispatch')
            lass NewCarCreateView(CreatView):
            model = car_detail
