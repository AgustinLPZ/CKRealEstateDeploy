from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
from .forms import ListingForm
from .models import Listing, Agent
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm


def index(request):
    all_listings = Listing.objects.all()
    return render(request, 'catalog/index.html', {'listings': all_listings })


def report(request):
    return render(request, 'catalog/report.html')


def detailed_property(request, property_id):
    listing = get_object_or_404(Listing, pk=property_id)
    return render(request, 'catalog/detailed_property.html', {'property_id': property_id})


def listings(request):
    all_listings = Listing.objects.all()  # Get all listings from the database
    return render(request, 'catalog/listings.html', {'listings': all_listings})


def agent_listings(request):
    all_listings = Listing.objects.all()
    return render(request, 'catalog/agent_listings.html', {'listings': all_listings })


def edit_listing(request, listing_id):
    return render(request, 'catalog/edit_listing.html', {'listing_id': listing_id})


def agent_profile(request):

    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            name = contact_form.cleaned_data['name']
            email = contact_form.cleaned_data['email']
            message = contact_form.cleaned_data['message']

            # Send email logic goes here
            send_mail(
                subject=f"Message from {name}",
                message=message,
                from_email=email,
                recipient_list=['carloskosala0@gmail.com'],  # Email to send to, can be agent's email
                fail_silently=False,
            )

            return redirect('agent_profile')  # Redirect after POST to avoid resubmitting
    else:
        contact_form = ContactForm()

    context = {
        'contact_form': contact_form  # Pass the form to the template
    }
    return render(request, 'catalog/agent_profile.html', context)


def discover(request):
    return render(request, 'catalog/discover.html')


def agent_home(request):
    all_listings = Listing.objects.all()
    return render(request, 'catalog/agent_home.html', {'listings': all_listings})


def agent_detailed_property(request):
    return render(request, 'catalog/agent_detailed_property.html')


def agent_discover(request):
    return render(request, 'catalog/agent_discover.html')


def agent_agent_profile(request):
    return render(request, 'catalog/agent_agent_profile.html')


class LogoutViewGET(LogoutView):
    next_page = reverse_lazy('index')  # Redirect after logout

    def get(self, request, *args, **kwargs):
        """Handle logout by a GET request."""
        return self.post(request, *args, **kwargs)


def add_listing(request):
    if request.method == 'POST':
        form = ListingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/listings/')  # Redirect to a new URL or a success page
    else:
        form = ListingForm()
    return render(request, 'catalog/add_listing.html', {'form': form})


def listing_detail(request, pk):
    listing = get_object_or_404(Listing, pk=pk)
    return render(request, 'catalog/listings.html', {'listing': listing})





