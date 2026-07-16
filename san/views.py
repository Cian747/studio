# from django.shortcuts import render

# # Create your views here.

# def index(request):
#     return render(request, 'home.html')

# def gallery(request):
#     return render(request, 'gallery.html')

# def services(request):
#     return render(request, 'services.html')

# def contact(request):
#     return render(request, 'contact.html')

# def pricing(request):
#     return render(request, 'pricing.html')

from django.shortcuts import render, redirect
from django.contrib import messages


# ─── Studio data ────────────────────────────────────────────────────────────
# Move to Django models/admin when you're ready to manage this via the CMS.

STATS = [
    {"value": "500+",   "label": "Sessions delivered"},
    {"value": "4",      "label": "Core disciplines"},
    {"value": "24 hr",  "label": "Image turnaround"},
    {"value": "100%",   "label": "Client satisfaction"},
]

DISCIPLINES = [
    {
        "slug": "sports",
        "icon": "🏊",
        "title": "Sports & Swimming",
        "headline": "Where split-seconds become <em>lasting memories.</em>",
        "description": (
            "Competitive sport demands a photographer who understands the rhythm "
            "of a race. We capture the decisive moment — the dive, the turn, the "
            "finish-line surge — with technical precision and an eye for the emotion "
            "that follows. From club galas to national championships, we deliver "
            "images that athletes, coaches and families will treasure for years."
        ),
        "long_description": (
            "Competitive sport is defined by fractions of a second, and our work "
            "reflects that. We use professional-grade sports photography equipment "
            "capable of burst-shooting at speed, ensuring no moment of peak "
            "performance is missed. Whether you need medal portraits that command "
            "attention, dynamic in-water action shots, podium documentation, or "
            "team photography for your club's end-of-season archive, we have the "
            "experience and the gear to deliver consistently excellent results — "
            "even in challenging pool lighting and outdoor meet conditions."
        ),
        "tags": ["Swimming", "Athletics", "Team Sports", "Galas & Meets", "Medal Portraits"],
        "deliverables": [
            "In-water race action",
            "Start & dive sequences",
            "Medal & podium portraits",
            "Team & relay group shots",
            "Warm-up & candid coverage",
            "Finish-line captures",
            "Club & season archives",
            "High-res & web-ready files",
        ],
    },
    {
        "slug": "governmental",
        "icon": "🏛️",
        "title": "Governmental & Corporate",
        "headline": "Official moments demand <em>official documentation.</em>",
        "description": (
            "Institutions, ministries and organisations carry a responsibility "
            "to record their work with accuracy and gravitas. We bring that same "
            "standard to every assignment — whether a cabinet-level function, a "
            "corporate launch, a conference or a ceremonial event. Our images are "
            "clean, authoritative and press-ready."
        ),
        "long_description": (
            "Government and corporate photography requires discretion, punctuality "
            "and an understanding of protocol. We work seamlessly within official "
            "environments — adhering to access requirements, dress codes and "
            "scheduling demands — while delivering images that accurately represent "
            "your institution's authority and professionalism. From ministerial "
            "press calls and parliamentary sessions to NGO project documentation "
            "and corporate annual reports, our work is trusted by public-sector "
            "bodies and private organisations across Kenya."
        ),
        "tags": ["State Functions", "Corporate Events", "Conferences", "NGO Projects", "Annual Reports"],
        "deliverables": [
            "Event & function coverage",
            "Executive & board portraits",
            "Conference & panel sessions",
            "Press-release-ready images",
            "Ceremonial & protocol events",
            "Project documentation",
            "Corporate headshots",
            "Branded gallery delivery",
        ],
    },
    {
        "slug": "environmental",
        "icon": "🌿",
        "title": "Environmental",
        "headline": "Kenya's landscapes, <em>told with honesty.</em>",
        "description": (
            "The natural world deserves a photographer who approaches it with "
            "patience and respect. We work with conservation organisations, "
            "research institutions and development agencies to document landscapes, "
            "ecosystems and communities — producing imagery that informs, advocates "
            "and moves audiences to action."
        ),
        "long_description": (
            "Environmental photography at its best is both evidence and art. "
            "Whether documenting the impact of a reforestation programme, "
            "capturing Kenya's varied ecosystems for a conservation NGO, or "
            "producing imagery for a development agency's impact report, we "
            "bring the same rigour and visual intelligence we apply to all our "
            "work. We understand field conditions, long hours and the importance "
            "of authentic representation. We are as comfortable in a nature "
            "reserve at dawn as we are in a boardroom at noon."
        ),
        "tags": ["Conservation", "Wildlife", "Landscape", "Community Documentation", "Impact Reports"],
        "deliverables": [
            "Ecosystem & habitat photography",
            "Wildlife & nature imagery",
            "Before & after documentation",
            "Community & field work coverage",
            "Impact report imagery",
            "Drone-perspective compositions",
            "Long-form project archives",
            "Print & publication files",
        ],
    },
    {
        "slug": "portrait",
        "icon": "🖼️",
        "title": "Portrait",
        "headline": "Portraits that carry <em>genuine presence.</em>",
        "description": (
            "A great portrait does more than record a likeness — it reveals "
            "character. We work with individuals and organisations to create "
            "portrait imagery that communicates confidence, approachability "
            "and authenticity. From executive headshots to editorial portraits, "
            "personal branding sessions to graduate photography, we take the "
            "time to make every subject look and feel their best."
        ),
        "long_description": (
            "Our portrait work spans studio and on-location sessions. We offer "
            "executive and professional headshots for LinkedIn profiles, company "
            "websites and press use; editorial portrait sessions for magazines "
            "and publications; personal branding photography for entrepreneurs "
            "and public figures; and graduation and milestone portraits for "
            "individuals. Every session begins with a consultation to understand "
            "your goals and the context in which the images will be used, ensuring "
            "the final results are not just technically excellent but strategically "
            "right for your purpose."
        ),
        "tags": ["Executive Headshots", "Personal Branding", "Editorial", "Graduate Portraits", "Studio & Location"],
        "deliverables": [
            "Studio or on-location sessions",
            "Executive & professional headshots",
            "Personal branding imagery",
            "Graduate & milestone portraits",
            "Editorial portrait work",
            "Multiple outfit & look options",
            "Retouched & natural finishes",
            "Digital & print-ready delivery",
        ],
    },
]

PACKAGES = [
    {
        "name": "Starter",
        "slug": "starter",
        "price": 2500,
        "unit": "per individual",
        "best_value": False,
        "features": [
            "5 fully edited images",
            "Single session or event",
            "Private download gallery",
            "24-hour delivery",
        ],
    },
    {
        "name": "Athlete Pack",
        "slug": "athlete-pack",
        "price": 4500,
        "unit": "per athlete, full meet",
        "best_value": True,
        "features": [
            "20+ edited images",
            "Medal & podium portraits",
            "Race action coverage",
            "Start & turn sequences",
            "High-res + web-optimised",
        ],
    },
    {
        "name": "Team / Group",
        "slug": "team-group",
        "price": 6000,
        "unit": "up to 6 people",
        "best_value": False,
        "features": [
            "Group & individual shots",
            "Full event coverage",
            "Shared private album",
            "30+ edited images",
            "24-hour delivery",
        ],
    },
    {
        "name": "Full Event",
        "slug": "full-event",
        "price": 18000,
        "unit": "complete event coverage",
        "best_value": False,
        "features": [
            "Unlimited subject coverage",
            "All sessions & formats",
            "Candid & documentary shots",
            "Logo watermarking available",
            "Dedicated online gallery",
            "Next-morning delivery",
        ],
    },
    {
        "name": "Season / Retainer",
        "slug": "season-retainer",
        "price": 45000,
        "unit": "3 events, priority booking",
        "best_value": False,
        "features": [
            "3 full event coverages",
            "Season highlight archive",
            "Social media crops included",
            "Dedicated client gallery",
            "Priority scheduling",
            "Print-ready files as standard",
        ],
    },
]

PILLARS = [
    {
        "icon": "🎯",
        "title": "Pre-shoot consultation",
        "body": "Every assignment begins with a conversation. We invest time in understanding your brief, your audience and your intended use of the images.",
    },
    {
        "icon": "⚡",
        "title": "24-hour turnaround",
        "body": "Edited, colour-graded, high-resolution images delivered to your private gallery within 24 hours of your event or session.",
    },
    {
        "icon": "🖥️",
        "title": "Private online gallery",
        "body": "Every client receives a branded, password-protected online gallery with download options in multiple sizes and formats.",
    },
    {
        "icon": "📐",
        "title": "Print & publication ready",
        "body": "Files delivered at the highest resolution, correctly colour-profiled and ready for print, publication or digital use from day one.",
    },
]

GALLERY_PLACEHOLDERS = [
    {"slug": "sports",        "icon": "🏊", "label": "Sports & Swimming",      "sub": "Race coverage, medals, team"},
    {"slug": "governmental",  "icon": "🏛️", "label": "Governmental & Corporate","sub": "Events, portraits, functions"},
    {"slug": "environmental", "icon": "🌿", "label": "Environmental",           "sub": "Landscapes, conservation, field"},
    {"slug": "portrait",      "icon": "🖼️", "label": "Portrait",               "sub": "Headshots, branding, editorial"},
    {"slug": "sports",        "icon": "🥇", "label": "Medal Portraits",         "sub": "Podium & ceremony"},
    {"slug": "portrait",      "icon": "🎓", "label": "Graduate & Milestone",    "sub": "Graduation sessions"},
]

WORK_PLACEHOLDERS = [
    {"icon": "🏊", "label": "Sports"},
    {"icon": "🏛️", "label": "Government"},
    {"icon": "🌿", "label": "Environment"},
    {"icon": "🖼️", "label": "Portrait"},
]


# ─── Views ──────────────────────────────────────────────────────────────────

def home(request):
    return render(request, "home.html", {
        "stats":         STATS,
        "disciplines":   DISCIPLINES,
        "packages":      PACKAGES,
        "pillars":       PILLARS,
        "recent_photos": [],            # → Photo.objects.order_by('-taken_at')[:4]
        "placeholders":  WORK_PLACEHOLDERS,
        "hero_images":   [],            # → HeroImage.objects.all()[:4]
    })


def services(request):
    return render(request, "services.html", {
        "disciplines": DISCIPLINES,
    })


def pricing(request):
    return render(request, "pricing.html", {
        "packages": PACKAGES,
    })


def gallery(request):
    return render(request, "gallery.html", {
        "photos":       [],             # → Photo.objects.all()
        "placeholders": GALLERY_PLACEHOLDERS,
    })


def contact(request):
    package_slug    = request.GET.get("package", "")
    discipline_slug = request.GET.get("discipline", "")

    preselected            = next((p for p in PACKAGES    if p["slug"] == package_slug), None)
    preselected_discipline = next((d for d in DISCIPLINES if d["slug"] == discipline_slug), None)

    if request.method == "POST":
        name         = request.POST.get("name", "").strip()
        email        = request.POST.get("email", "").strip()
        phone        = request.POST.get("phone", "").strip()
        organisation = request.POST.get("organisation", "").strip()
        discipline   = request.POST.get("discipline", "").strip()
        package      = request.POST.get("package", "").strip()
        event_date   = request.POST.get("event_date", "").strip()
        location     = request.POST.get("location", "").strip()
        message      = request.POST.get("message", "").strip()

        if name and email:
            # TODO: replace with send_mail() or a ContactEnquiry model save
            messages.success(
                request,
                f"Thank you, {name}. We have received your enquiry and "
                f"will be in touch within 24 hours."
            )
            return redirect("contact")
        else:
            messages.error(request, "Please provide your name and email address.")

    return render(request, "contact.html", {
        "packages":               PACKAGES,
        "disciplines":            DISCIPLINES,
        "preselected":            preselected,
        "preselected_discipline": preselected_discipline.get("slug") if preselected_discipline else "",
    })
