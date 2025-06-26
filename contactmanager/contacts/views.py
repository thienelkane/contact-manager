from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact
from django.contrib import messages
from .forms import ContactForm

def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, "contacts/contact_list.html", {'contacts': contacts})

def contact_add(request):
    if request.method == "POST":
        email = request.POST.get("email")
        if Contact.objects.filter(email=email).exists():
            messages.error(request, "Ce contact existe déjà avec cet email.")
            return redirect("contact_add") 

        Contact.objects.create(
            first_name=request.POST.get("first_name"),
            last_name=request.POST.get("last_name"),
            email=email,
            phone=request.POST.get("phone")
        )
        messages.success(request, "Contact ajouté avec succès.")
        return redirect("contact_list")

    return render(request, "contacts/contact_form.html")

def contact_edit(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('contact_list')
    else:
        form = ContactForm(instance=contact)
    return render(request, 'contacts/contact_form.html', {'form': form})

def contact_delete(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    contact.delete()
    return redirect('contact_list')