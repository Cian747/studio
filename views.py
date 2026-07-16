from django.shortcuts import render, redirect
from django.contrib import messages


# ─── Data (move to database models when ready) ─────────────────────────────

STATS = [
    {"value": "500+",    "label": "Athletes Shot"},
    {"value": "24hr",    "label": "Turnaround"},
    {"value": "RAW+JPG", "label": "Delivered"},
    {"value": "100%",    "label": "Waterproof Gear"},
]

SERVICES = [
    {
        "icon": "🥇",
        "title": "Medal & Podium Portraits",
        "description": "Professional close-up medal shots and podium portraits — the hero image every athlete deserves. Delivered same day or next morning in high resolution.",
        "featured": True,
    },
    {
        "icon": "⚡",
        "title": "Race Action Shots",
        "description": "Split-second captures of your stroke, turn, and finish. Freeze the moment at peak performance.",
        "featured": False,
    },
    {
        "icon": "🏊",
        "title": "Team & Club Photos",
        "description": "Squad shots, relay teams, and group portraits for clubs, schools, and associations.",
        "featured": False,
    },
    {
        "icon": "🎽",
        "title": "Start & Dive Sequences",
        "description": "Multi-frame burst sequences of your race start, turn-wall, and dive entry — technical analysis meets stunning imagery.",
        "featured": False,
    },
    {
        "icon": "📸",
        "title": "Warm-Up & Behind the Scenes",
        "description": "Candid preparation shots that tell the full story of your competition day.",
        "featured": False,
    },
]

PACKAGES = [
    {
        "name": "Starter",
        "slug": "starter",
        "price": 2500,
        "unit": "per athlete",
        "best_value": False,
        "features": [
            "5 edited photos",
            "1 race or event",
            "Digital download",
            "24hr delivery",
        ],
    },
    {
        "name": "Athlete Pack",
        "slug": "athlete-pack",
        "price": 4500,
        "unit": "per athlete, full meet",
        "best_value": True,
        "features": [
            "20+ edited photos",
            "Medal & podium shots",
            "Action race captures",
            "Start & turn sequences",
            "High-res + web sizes",
        ],
    },
    {
        "name": "Relay Team",
        "slug": "relay-team",
        "price": 6000,
        "unit": "per team (up to 6)",
        "best_value": False,
        "features": [
            "Team & individual shots",
            "Race action coverage",
            "Group podium photo",
            "30+ edited photos",
            "Shared album link",
        ],
    },
    {
        "name": "Full Meet",
        "slug": "full-meet",
        "price": 18000,
        "unit": "whole event, all athletes",
        "best_value": False,
        "features": [
            "Unlimited athlete coverage",
            "All races & finals",
            "Coach & officials candids",
            "Club logo watermarking",
            "Online gallery for all",
            "Next-morning delivery",
        ],
    },
    {
        "name": "Club Season",
        "slug": "club-season",
        "price": 45000,
        "unit": "3 meets, priority booking",
        "best_value": False,
        "features": [
            "3 full meet coverages",
            "Season highlight reel",
            "Social media cut-downs",
            "Dedicated online gallery",
            "Priority scheduling",
            "Print-ready files included",
        ],
    },
]


# ─── Views ──────────────────────────────────────────────────────────────────

def home(request):
    """Landing page — hero, services teaser, pricing, gallery teaser, CTA."""
    context = {
        "stats": STATS,
        "services": SERVICES,
        "packages": PACKAGES,
        "recent_photos": [],   # swap with Photo.objects.order_by('-taken_at')[:6]
    }
    return render(request, "sanwan/home.html", context)


def services(request):
    """Full services page."""
    context = {"services": SERVICES}
    return render(request, "sanwan/services.html", context)


def pricing(request):
    """Standalone pricing page."""
    context = {"packages": PACKAGES}
    return render(request, "sanwan/pricing.html", context)


def gallery(request):
    """Photo gallery page."""
    context = {
        "photos": [],  # swap with Photo.objects.all()
    }
    return render(request, "sanwan/gallery.html", context)


def contact(request):
    """Contact / booking enquiry form."""
    package_slug = request.GET.get("package", "")
    preselected = next(
        (p for p in PACKAGES if p["slug"] == package_slug), None
    )

    if request.method == "POST":
        # Basic form handling — plug in Django forms or modelforms as you grow
        name    = request.POST.get("name", "").strip()
        email   = request.POST.get("email", "").strip()
        phone   = request.POST.get("phone", "").strip()
        package = request.POST.get("package", "").strip()
        event   = request.POST.get("event_date", "").strip()
        message = request.POST.get("message", "").strip()

        if name and email:
            # TODO: send email via Django's send_mail() or save to a model
            messages.success(
                request,
                f"Thanks {name}! We've received your enquiry and will be in touch within 24 hours."
            )
            return redirect("contact")
        else:
            messages.error(request, "Please fill in your name and email address.")

    context = {
        "packages": PACKAGES,
        "preselected": preselected,
    }
    return render(request, "sanwan/contact.html", context)
