from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm


def contact(request):
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            msg = form.save()
            # Optional email notification
            if settings.CONTACT_EMAIL:
                try:
                    send_mail(
                        subject=f"Portfolio Contact: {msg.subject}",
                        message=f"From: {msg.name} <{msg.email}>\n\n{msg.message}",
                        from_email=settings.DEFAULT_FROM_EMAIL,
                        recipient_list=[settings.CONTACT_EMAIL],
                        fail_silently=True,
                    )
                except Exception:
                    pass
            messages.success(request, "✅ Your message has been sent! I'll get back to you soon.")
            return redirect('contact:contact')
        else:
            messages.error(request, "⚠️ Please correct the errors below.")

    return render(request, 'contact/contact.html', {'form': form})
