#!/usr/bin/env python3
"""Generate all 20 professional demo HTML pages."""

import json
import os

BASE = "/Users/jackserver/.openclaw/workspace/wildrose-lead-manager"

# Business data: slug, name, city, email, phone, has_logo, accent_color, color_name, industry, services, about_text, stats, tagline, hero_text
businesses = [
    # HANDYMAN
    {
        "slug": "kino-handyman",
        "name": "Kino Handyman",
        "full_name": "Kino Handyman & Construction Services",
        "city": "Edmonton",
        "email": "kinoconstructionservices@gmail.com",
        "phone": "(780) 231-4071",
        "has_logo": True,
        "accent": "#D4AF37",
        "accent_light": "#E8C84A",
        "dark": "#1a1a1a",
        "charcoal": "#222222",
        "nav_bg": "#1a1a1a",
        "industry": "handyman",
        "tagline": "Your Home Renovation Specialists",
        "hero_title_line1": "Quality",
        "hero_title_line2": "Craftsmanship",
        "hero_sub": "Since 2010, Kino Handyman & Construction Services has been Edmonton's go-to choice for top-notch home and office renovations. Over a decade of experience. 100% customer satisfaction guaranteed.",
        "services": [
            ("Full Home Renovations", "Complete residential renovations from concept to completion — kitchens, bathrooms, basements, and full-home makeovers tailored to your vision."),
            ("Kitchen & Bathroom", "Expert kitchen and bathroom makeovers with premium materials, modern designs, and quality craftsmanship that transforms your space."),
            ("Fence & Deck Construction", "Custom wood and composite fence and deck construction — built to last and designed to complement your home's architecture."),
            ("Framing & Drywall", "Professional framing, drywall, mudding, and taping services with precision and attention to detail on every project."),
            ("Flooring Installation", "Expert installation of vinyl, laminate, tile, and carpet flooring — transforming your rooms with durable, beautiful surfaces."),
            ("Painting & Finishing", "Interior and exterior painting services with premium products and meticulous preparation for a flawless, lasting finish."),
        ],
        "strip_items": ["Basement Renovations", "Kitchen Makeovers", "Deck Construction", "Flooring Installation", "Free Estimates"],
        "about_title": "Committed to Excellence",
        "about_text": "Since 2010, Kino Handyman & Construction Services located in Edmonton, has been your go-to choice for top-notch home and office renovations. With over a decade of experience, our skilled team specializes in basement, bathroom, and kitchen makeovers, fence and deck construction, along with expert framing, drywall, flooring, and painting.",
        "about_features": [
            "Over a decade of hands-on renovation experience",
            "100% customer satisfaction guaranteed",
            "Free estimates within 10 km radius",
            "Referral discounts for friends and family",
            "Licensed and insured for your peace of mind",
        ],
        "stats": [("15+", "Years Experience"), ("500+", "Projects Completed"), ("100%", "Satisfaction Rate"), ("10+", "Services Offered")],
        "testimonial": '"Kino and his team transformed our basement beyond our expectations. Professional, on time, and the quality of work is outstanding."',
        "testimonial_author": "Homeowner, Edmonton",
        "contact_select": ["Full Home Renovation", "Kitchen Remodel", "Bathroom Renovation", "Deck or Fence", "Flooring", "Painting", "Other"],
    },
    {
        "slug": "handyman-reality",
        "name": "Handyman Reality",
        "full_name": "Handyman Reality",
        "city": "Edmonton",
        "email": "kewlguy@handymanreality.com",
        "phone": "(780) 000-0000",
        "has_logo": False,
        "accent": "#2563EB",
        "accent_light": "#3B82F6",
        "dark": "#0f172a",
        "charcoal": "#1e293b",
        "nav_bg": "#0f172a",
        "industry": "handyman",
        "tagline": "Professional Handyman Services in Edmonton",
        "hero_title_line1": "Your Project,",
        "hero_title_line2": "Our Priority",
        "hero_sub": "Handyman Reality delivers reliable, professional handyman services across Edmonton. From small repairs to full renovations, we bring quality craftsmanship to every job.",
        "services": [
            ("General Repairs", "Quick, reliable repairs for doors, windows, fixtures, and more — no job too small for our experienced team."),
            ("Renovations", "Full kitchen, bathroom, and basement renovations designed to transform your living space within budget."),
            ("Drywall & Painting", "Expert drywall installation, repair, and professional painting services for a flawless finish."),
            ("Plumbing & Electrical", "Licensed plumbing and electrical work for repairs, upgrades, and new installations."),
            ("Carpentry", "Custom carpentry including shelving, trim work, built-ins, and structural modifications."),
            ("Property Maintenance", "Ongoing property maintenance plans to keep your home or building in top condition year-round."),
        ],
        "strip_items": ["General Repairs", "Renovations", "Plumbing", "Electrical", "Carpentry"],
        "about_title": "Built on Reliability",
        "about_text": "Handyman Reality was founded on a simple idea — homeowners deserve a handyman service that shows up on time, does quality work, and charges fair prices. We've built our reputation in Edmonton one satisfied customer at a time.",
        "about_features": [
            "Licensed and insured professionals",
            "Transparent, upfront pricing",
            "On-time guarantee",
            "Clean and respectful crew",
            "Satisfaction guaranteed on every job",
        ],
        "stats": [("1000+", "Jobs Completed"), ("5-Star", "Reviews"), ("Same Day", "Service Available"), ("100%", "Satisfaction")],
        "testimonial": '"They showed up exactly when they said they would, did excellent work, and cleaned up perfectly. I couldn\'t ask for more."',
        "testimonial_author": "Homeowner, Edmonton",
        "contact_select": ["General Repair", "Full Renovation", "Plumbing", "Electrical", "Painting", "Other"],
    },
    {
        "slug": "delano-maintenance",
        "name": "Delano Maintenance",
        "full_name": "Delano Maintenance",
        "city": "Edmonton",
        "email": "info@delanomaintenance.ca",
        "phone": "(780) 000-0000",
        "has_logo": False,
        "accent": "#0D9488",
        "accent_light": "#14B8A6",
        "dark": "#134e4a",
        "charcoal": "#1a3a38",
        "nav_bg": "#134e4a",
        "industry": "handyman",
        "tagline": "Edmonton's Trusted Maintenance Professionals",
        "hero_title_line1": "Reliable",
        "hero_title_line2": "Maintenance",
        "hero_sub": "Delano Maintenance provides comprehensive property maintenance and handyman services across Edmonton. Professional, dependable, and committed to quality in every project we take on.",
        "services": [
            ("Property Maintenance", "Regular and one-time property maintenance services to keep your residential or commercial property in peak condition."),
            ("General Repairs", "Fast, reliable repair services for all areas of your property — from plumbing fixtures to structural fixes."),
            ("Painting Services", "Interior and exterior painting with premium materials and professional preparation for lasting results."),
            ("Flooring", "Installation and repair of all flooring types — laminate, vinyl, tile, and hardwood."),
            ("Drywall & Finishing", "Expert drywall installation, repair, mudding, and taping with smooth, flawless finishes."),
            ("Seasonal Services", "Seasonal maintenance including weatherization, eavestrough cleaning, and winter preparation."),
        ],
        "strip_items": ["Property Maintenance", "General Repairs", "Painting", "Flooring", "Seasonal Services"],
        "about_title": "Dependable by Nature",
        "about_text": "Delano Maintenance was built on the principle that property maintenance should be hassle-free. We serve Edmonton homeowners and businesses with a commitment to reliability, quality workmanship, and transparent communication.",
        "about_features": [
            "Comprehensive property maintenance solutions",
            "Licensed and insured team",
            "Flexible scheduling to fit your needs",
            "Competitive and transparent pricing",
            "One call handles it all",
        ],
        "stats": [("8+", "Years in Business"), ("300+", "Satisfied Clients"), ("24/7", "Emergency Service"), ("5+", "Service Categories")],
        "testimonial": '"Delano Maintenance handles all of our property needs. They are reliable, professional, and always do excellent work."',
        "testimonial_author": "Property Manager, Edmonton",
        "contact_select": ["Property Maintenance", "General Repair", "Painting", "Flooring", "Seasonal", "Other"],
    },
    {
        "slug": "bahm-contracting",
        "name": "BAHM Contracting",
        "full_name": "BAHM Contracting",
        "city": "Edmonton",
        "email": "aaron@bahmcontracting.com",
        "phone": "(780) 000-0000",
        "has_logo": False,
        "accent": "#DC2626",
        "accent_light": "#EF4444",
        "dark": "#1c1917",
        "charcoal": "#292524",
        "nav_bg": "#1c1917",
        "industry": "handyman",
        "tagline": "Quality Contracting in Edmonton",
        "hero_title_line1": "Built",
        "hero_title_line2": "Right",
        "hero_sub": "BAHM Contracting delivers quality construction and renovation services across Edmonton. From concept to completion, we bring expertise, reliability, and superior craftsmanship to every project.",
        "services": [
            ("General Contracting", "Full-service general contracting for residential and commercial construction projects of all sizes."),
            ("Renovations", "Complete home and commercial renovations — kitchens, bathrooms, basements, and full build-outs."),
            ("New Construction", "Ground-up construction services with project management from permits to final inspection."),
            ("Framing & Structure", "Expert structural framing and carpentry for new builds, additions, and renovations."),
            ("Exterior Work", "Exterior renovations including siding, soffit, fascia, and outdoor living spaces."),
            ("Project Management", "End-to-end project management ensuring your project stays on time and on budget."),
        ],
        "strip_items": ["General Contracting", "Renovations", "New Construction", "Framing", "Project Management"],
        "about_title": "Building With Integrity",
        "about_text": "BAHM Contracting is an Edmonton-based contracting company committed to building things right. We combine old-school craftsmanship with modern techniques to deliver projects that exceed expectations.",
        "about_features": [
            "Licensed, bonded, and insured",
            "Detailed project proposals and timelines",
            "Quality materials and superior workmanship",
            "Clean job sites and respectful crew",
            "On-time and on-budget delivery",
        ],
        "stats": [("10+", "Years Experience"), ("200+", "Projects Done"), ("Licensed", "& Insured"), ("100%", "Satisfaction")],
        "testimonial": '"Aaron and his team did an incredible job on our renovation. Professional from start to finish and the results speak for themselves."',
        "testimonial_author": "Homeowner, Edmonton",
        "contact_select": ["General Contracting", "Renovation", "New Construction", "Exterior Work", "Other"],
    },
    {
        "slug": "handyman-yyc",
        "name": "Handyman YYC",
        "full_name": "Colsons Renovation & Repairs",
        "city": "Calgary",
        "email": "info@handymanyyc.ca",
        "phone": "(403) 830-4657",
        "has_logo": True,
        "accent": "#1e3a5f",
        "accent_light": "#2c5282",
        "dark": "#0f1a2e",
        "charcoal": "#1a2a44",
        "nav_bg": "#0f1a2e",
        "industry": "handyman",
        "tagline": "Licensed, Bonded & Insured",
        "hero_title_line1": "Professional",
        "hero_title_line2": "Handyman",
        "hero_sub": "With more than 20 years of experience, Colsons General Contracting delivers service that is fast, guaranteed and affordable. Licensed, bonded and insured — your trusted partner for commercial and residential projects in Calgary.",
        "services": [
            ("Residential Services", "Complete interior and exterior renovation services — bathrooms, kitchens, basement development, and more."),
            ("Commercial Services", "Professional commercial services for offices, retail spaces, rental properties, and lease hold improvements."),
            ("General Handyman", "From plumbing fixture replacement to humidifier installation — no job too large or too small."),
            ("Renovations", "Full renovation services with consistent, punctual, and superior workmanship in a professional environment."),
            ("Emergency Repairs", "Fast response for emergency repairs — we understand that some things just can't wait."),
            ("Maintenance Plans", "Ongoing maintenance plans to keep your property in top condition and prevent costly future repairs."),
        ],
        "strip_items": ["Residential", "Commercial", "Licensed & Bonded", "20+ Years", "Free Estimates"],
        "about_title": "Quality You Can Trust",
        "about_text": "With more than 20 years of experience in the industry, Colsons General Contracting delivers service that is fast, guaranteed and affordable. We are a licensed, bonded and insured company that delivers quality you can trust and service you can rely on.",
        "about_features": [
            "Over 20 years of industry experience",
            "Licensed, bonded, and insured",
            "Consistent, punctual, superior workmanship",
            "Exceptional communication with management",
            "Commercial and residential expertise",
        ],
        "stats": [("20+", "Years Experience"), ("1000+", "Projects Done"), ("Licensed", "& Bonded"), ("100%", "Guaranteed")],
        "testimonial": '"Colsons team was fast, efficient and ever so polite. Wonderful to do business with someone who operates with the customer\'s needs as a priority."',
        "testimonial_author": "Adam M., Calgary",
        "contact_select": ["Residential Service", "Commercial Service", "Renovation", "Repair", "Maintenance", "Other"],
    },
    # CLEANING
    {
        "slug": "sunset-maintenance",
        "name": "Sunset Maintenance",
        "full_name": "Sunset Maintenance Services",
        "city": "Red Deer",
        "email": "bmjserv@telus.net",
        "phone": "(403) 346-3465",
        "has_logo": False,
        "accent": "#EA580C",
        "accent_light": "#F97316",
        "dark": "#1c1917",
        "charcoal": "#292524",
        "nav_bg": "#1c1917",
        "industry": "cleaning",
        "tagline": "Keeping Red Deer's Businesses Sparkling",
        "hero_title_line1": "Spotless",
        "hero_title_line2": "Clean",
        "hero_sub": "Sunset Maintenance Services provides top-quality commercial and industrial cleaning services throughout Red Deer. We create clean, healthy environments for your employees and customers.",
        "services": [
            ("Janitorial Services", "Daily, weekly, and monthly janitorial services for offices, retail spaces, restaurants, and more."),
            ("Floor Cleaning", "Professional floor cleaning services including stripping, refinishing, and deep cleaning of all floor types."),
            ("Construction Cleanup", "Post-construction cleaning services to make your new or renovated space move-in ready."),
            ("Office Cleaning", "Thorough office cleaning including desks, cubicles, interior windows, washrooms, and common areas."),
            ("Commercial Cleaning", "Comprehensive commercial cleaning for businesses of all sizes throughout Red Deer and surrounding areas."),
            ("Deep Cleaning", "Intensive deep cleaning services for spaces that need extra attention — one-time or scheduled."),
        ],
        "strip_items": ["Janitorial Service", "Floor Cleaning", "Construction Cleanup", "Daily/Weekly/Monthly", "Red Deer"],
        "about_title": "Dedicated to Clean",
        "about_text": "Stop worrying about when you'll have time to clean your space and have Sunset Maintenance Services do it for you. Our top priority is providing a clean and healthy environment for your employees and customers using top-quality cleaning products.",
        "about_features": [
            "Serving Red Deer and surrounding areas",
            "Experienced with offices, retail, restaurants, schools",
            "Top-quality cleaning products and equipment",
            "Flexible scheduling — daily, weekly, or monthly",
            "Free quotes available",
        ],
        "stats": [("15+", "Years in Business"), ("100+", "Regular Clients"), ("Daily", "Service Available"), ("100%", "Satisfaction")],
        "testimonial": '"Sunset Maintenance has kept our office spotless for years. Reliable, thorough, and always professional."',
        "testimonial_author": "Business Owner, Red Deer",
        "contact_select": ["Janitorial Service", "Floor Cleaning", "Construction Cleanup", "Office Cleaning", "Deep Clean", "Other"],
    },
    {
        "slug": "mm-janitorial",
        "name": "M&M Janitorial",
        "full_name": "M&M Janitorial & Property Maintenance",
        "city": "Red Deer",
        "email": "info@mmjanitorial.ca",
        "phone": "(403) 586-0410",
        "has_logo": True,
        "accent": "#1e3a5f",
        "accent_light": "#2563EB",
        "dark": "#0f172a",
        "charcoal": "#1e293b",
        "nav_bg": "#0f172a",
        "industry": "cleaning",
        "tagline": "Commercial & Corporate Cleaning Services",
        "hero_title_line1": "Clean",
        "hero_title_line2": "Environment",
        "hero_sub": "M&M Janitorial and Property Maintenance ensures your business operates with a clean, safe, and healthy environment. Professional janitorial services in Red Deer with the latest tools and technologies.",
        "services": [
            ("Commercial Cleaning", "Consistent, thorough commercial cleaning for offices, retail spaces, and industrial sites."),
            ("Sanitation & Disinfection", "Professional sanitation services using the latest tools to guard against germs — not just surface cleaning."),
            ("Property Maintenance", "Comprehensive property maintenance including landscape grooming and workspace sanitation."),
            ("Office Cleaning", "Detailed office cleaning services that create a healthy, productive work environment."),
            ("Floor Care", "Expert floor cleaning, stripping, and refinishing for all types of commercial flooring."),
            ("Janitorial Services", "Full janitorial service packages customized to your business needs and schedule."),
        ],
        "strip_items": ["Commercial Cleaning", "Sanitation", "Property Maintenance", "Floor Care", "Red Deer"],
        "about_title": "Professional Clean, Every Time",
        "about_text": "M&M Janitorial and Property Maintenance serves Red Deer businesses with professional cleaning and property maintenance. Our experienced team uses the latest tools and technologies to deliver results you can see and feel.",
        "about_features": [
            "Serving Red Deer, Alberta",
            "Latest cleaning tools and technologies",
            "Commercial and corporate specialists",
            "Customized cleaning schedules",
            "Eco-friendly cleaning options available",
        ],
        "stats": [("10+", "Years Serving Red Deer"), ("50+", "Commercial Clients"), ("Daily", "Service Available"), ("100%", "Satisfaction")],
        "testimonial": '"M&M has been maintaining our office for over two years. Their attention to detail and professionalism is outstanding."',
        "testimonial_author": "Office Manager, Red Deer",
        "contact_select": ["Commercial Cleaning", "Sanitation Service", "Property Maintenance", "Office Cleaning", "Floor Care", "Other"],
    },
    {
        "slug": "performance-maintenance",
        "name": "Performance Building Maintenance",
        "full_name": "Performance Building Maintenance Inc.",
        "city": "Red Deer",
        "email": "info@performancemaint.com",
        "phone": "(403) 358-9256",
        "has_logo": True,
        "accent": "#00154D",
        "accent_light": "#1a2f6d",
        "dark": "#0a0f1a",
        "charcoal": "#111827",
        "nav_bg": "#0a0f1a",
        "industry": "cleaning",
        "tagline": "Top-Quality Commercial Cleaning in Red Deer",
        "hero_title_line1": "Top-Quality",
        "hero_title_line2": "Commercial Cleaning",
        "hero_sub": "Performance Building Maintenance is your trusted source for professional commercial cleaning services in Red Deer. Over two decades of experience in janitorial services, office cleaning, and commercial maintenance.",
        "services": [
            ("Commercial Cleaning", "Consistent and thorough commercial cleaning for offices, retail spaces, and industrial sites with trained professionals."),
            ("Carpet Cleaning", "Deep carpet cleaning with powerful equipment and eco-friendly solutions — routine maintenance or one-time service."),
            ("Office Cleaning", "Professional office cleaning that makes the right impression — regular schedules or one-time deep cleans."),
            ("Janitorial Services", "Full janitorial service packages designed to keep your business clean, healthy, and welcoming."),
            ("Floor Care", "Complete floor care including stripping, waxing, polishing, and deep cleaning for all floor types."),
            ("Construction Cleanup", "Post-construction cleaning to make your new or renovated commercial space ready for business."),
        ],
        "strip_items": ["Commercial Cleaning", "Carpet Cleaning", "Office Cleaning", "20+ Years", "Red Deer"],
        "about_title": "Your Cleaning Partner",
        "about_text": "With over two decades of hands-on experience, Performance Building Maintenance specializes in top-tier janitorial services, office cleaning, and commercial cleaning that businesses and property owners can rely on. We're more than a cleaning company — we're your partner in keeping your environment healthy and well-maintained.",
        "about_features": [
            "Over 20 years of experience",
            "Friendly, dedicated cleaning professionals",
            "Eco-friendly cleaning solutions",
            "Customized cleaning schedules",
            "Serving Red Deer and surrounding areas",
        ],
        "stats": [("20+", "Years Experience"), ("200+", "Clients Served"), ("Trained", "Professionals"), ("100%", "Satisfaction")],
        "testimonial": '"Performance Building Maintenance has been instrumental in keeping our facility clean and professional. Their team is reliable and thorough."',
        "testimonial_author": "Facility Manager, Red Deer",
        "contact_select": ["Commercial Cleaning", "Carpet Cleaning", "Office Cleaning", "Janitorial Service", "Floor Care", "Other"],
    },
    {
        "slug": "mancuso-cleaning",
        "name": "Mancuso Carpet Cleaning",
        "full_name": "Mancuso Cleaning Services",
        "city": "Red Deer",
        "email": "cynthia@mancuso-cleaning.com",
        "phone": "(403) 347-1845",
        "has_logo": False,
        "accent": "#0284C7",
        "accent_light": "#38BDF8",
        "dark": "#0c4a6e",
        "charcoal": "#164e63",
        "nav_bg": "#0c4a6e",
        "industry": "cleaning",
        "tagline": "Where Quality Comes First",
        "hero_title_line1": "Carpet",
        "hero_title_line2": "Cleaning Experts",
        "hero_sub": "Mancuso Cleaning Services has a team of experienced carpet cleaners in Red Deer. Over 60 years of excellent service — trusted by hundreds of businesses and homeowners for quality cleaning at economical prices.",
        "services": [
            ("Carpet Cleaning", "Deep carpet cleaning with professional-grade equipment to remove tough stains, grime, and allergens from your carpets."),
            ("Residential Cleaning", "Complete residential cleaning services — carpets, upholstery, rugs, and all textile surfaces in your home."),
            ("Commercial Cleaning", "Professional commercial cleaning services for offices, retail spaces, and commercial properties in Red Deer."),
            ("Upholstery Cleaning", "Expert upholstery cleaning to refresh your furniture and extend its life — safe for all fabric types."),
            ("Stain Removal", "Specialized stain removal treatments for tough stains — pet stains, wine, ink, and more."),
            ("Rug Cleaning", "Professional rug cleaning services that bring back the beauty and freshness of your area rugs."),
        ],
        "strip_items": ["Carpet Cleaning", "Residential", "Commercial", "60+ Years", "Eco-Friendly"],
        "about_title": "Red Deer's Preferred Cleaners",
        "about_text": "When you're looking for carpet cleaning specialists you can rely on, look no further than Mancuso Cleaning Services. Trusted by hundreds of businesses and homeowners, we clean to required hygiene standards at economical prices using environmentally friendly products safe for pets and kids.",
        "about_features": [
            "Over 60 years of excellent service",
            "Environmentally friendly cleaning agents",
            "Safe for pets and children",
            "No residue cleaning process",
            "Economical prices with quality results",
        ],
        "stats": [("60+", "Years of Service"), ("500+", "Happy Clients"), ("Eco", "Friendly Products"), ("100%", "Satisfaction")],
        "testimonial": '"Mancuso Cleaning brought our carpets back to life. Their team is professional, thorough, and the results are incredible."',
        "testimonial_author": "Homeowner, Red Deer",
        "contact_select": ["Carpet Cleaning", "Residential Cleaning", "Commercial Cleaning", "Upholstery", "Stain Removal", "Other"],
    },
    {
        "slug": "mcwinn-filter",
        "name": "McWinn Air Filter",
        "full_name": "McWinn Air Filter Cleaning Systems",
        "city": "Edmonton",
        "email": "info@mcwinnfiltercleaningsystems.ca",
        "phone": "(780) 483-4193",
        "has_logo": False,
        "accent": "#EA580C",
        "accent_light": "#FB923C",
        "dark": "#1c1917",
        "charcoal": "#292524",
        "nav_bg": "#1c1917",
        "industry": "cleaning",
        "tagline": "Air Filter Cleaning Services — Edmonton & Across Canada",
        "hero_title_line1": "Air Filter",
        "hero_title_line2": "Cleaning Systems",
        "hero_sub": "McWinn Air Filter Cleaning Systems sells air filter cleaning machines across Canada. Our patented dry cleaning system can clean your filter to perform like new — saving you money and helping the environment.",
        "services": [
            ("Air Filter Cleaning", "Professional air filter cleaning services using our patented dry process — clean your filter 8-10 times vs. 2-3 with washing."),
            ("Cleaning Equipment Sales", "Purchase our industrial-strength air filter cleaning machines for in-house use or to start your own business."),
            ("Licensing Opportunities", "Get licensed to start your own air filter cleaning business in a specific geographic territory."),
            ("Equipment Leasing", "Flexible leasing options for our air filter cleaning systems — perfect for businesses wanting to try before they buy."),
            ("Construction & Mining", "Specialized cleaning solutions for heavy-duty air filters used in construction and mining operations."),
            ("Consultation", "Expert consultation on air filter maintenance programs and equipment selection for your specific needs."),
        ],
        "strip_items": ["Air Filter Cleaning", "Equipment Sales", "Licensing", "Leasing Options", "Canada-Wide"],
        "about_title": "The Original Manufacturers",
        "about_text": "We are the original manufacturers of our air filter cleaning machine. Our patented dry cleaning process combines rapid spinning with injected air and vacuum to clean filter paper of all restricting particles — allowing you to clean your filter 8-10 times instead of throwing it away.",
        "about_features": [
            "Original manufacturers of our cleaning system",
            "Patented dry cleaning process",
            "Clean filters 8-10 times vs. 2-3 with washing",
            "Environmentally friendly — reduce landfill waste",
            "Serve construction, mining, and industrial clients",
        ],
        "stats": [("Patented", "Technology"), ("8-10x", "Filter Life"), ("Canada", "Wide Service"), ("100%", "Dry Process")],
        "testimonial": '"The McWinn system has saved us thousands in filter replacement costs. The quality of cleaning is outstanding every time."',
        "testimonial_author": "Operations Manager, Edmonton",
        "contact_select": ["Filter Cleaning Service", "Equipment Purchase", "Licensing", "Leasing", "Consultation", "Other"],
    },
    {
        "slug": "clean-getaway",
        "name": "Clean Getaway",
        "full_name": "The Clean Getaway",
        "city": "Red Deer",
        "email": "michelle@thecleangetaway.ca",
        "phone": "(780) 709-2666",
        "has_logo": True,
        "accent": "#8B5E3C",
        "accent_light": "#A0724D",
        "dark": "#373435",
        "charcoal": "#2a2829",
        "nav_bg": "#373435",
        "industry": "cleaning",
        "tagline": "Alberta's Event Take-Down Experts",
        "hero_title_line1": "Event",
        "hero_title_line2": "Take-Down",
        "hero_sub": "The Clean Getaway is Alberta's event take-down specialist. Bringing down the house, so you don't have to. After months of planning your big day, you deserve to enjoy it to the very end.",
        "services": [
            ("Event Take-Down", "Complete event take-down services — décor removal, packing, cleanup, and venue restoration so you can enjoy your event."),
            ("Hands on Deck", "Extra hands on deck service — hire our team to help with your event in any capacity to ensure it runs smoothly."),
            ("Decor Removal", "Professional décor removal and packing — centrepieces, signs, ceremony décor, linens, gifts, and more."),
            ("Venue Cleanup", "Thorough post-event venue cleanup that meets venue requirements and time limitations."),
            ("Packing & Transport", "Careful packing and transport of all personal items, rental décor, gifts, and leftover items."),
            ("Event Support", "Flexible event support team available throughout your event for whatever needs may arise."),
        ],
        "strip_items": ["Event Take-Down", "Decor Removal", "Venue Cleanup", "All of Alberta", "Flexible Hours"],
        "about_title": "Don't Stop the Party",
        "about_text": "Wouldn't it be nice to have extra help taking down décor, packing up, and cleaning at the end of your event? Relieve yourself, your friends and your family of this stress. After months of planning your big day, you deserve to enjoy it to the very end.",
        "about_features": [
            "Unlimited correspondence via email",
            "Pre-event meeting or phone call",
            "Flexible team at your convenience",
            "Comply with venue time limitations",
            "Servicing all of Alberta",
        ],
        "stats": [("500+", "Events Served"), ("All", "Alberta"), ("24/7", "Availability"), ("100%", "Satisfaction")],
        "testimonial": '"The Clean Getaway team was a lifesaver after our wedding. They handled everything while we got to enjoy our reception to the very end."',
        "testimonial_author": "Wedding Client, Alberta",
        "contact_select": ["Event Take-Down", "Hands on Deck", "Decor Removal", "Venue Cleanup", "Full Service", "Other"],
    },
    # LANDSCAPING
    {
        "slug": "edmonton-stone",
        "name": "Edmonton Stone Designers",
        "full_name": "Edmonton Stone Designers",
        "city": "Edmonton",
        "email": "edmontonstone@shaw.ca",
        "phone": "(780) 478-0111",
        "has_logo": True,
        "accent": "#8B6914",
        "accent_light": "#B8860B",
        "dark": "#1a1814",
        "charcoal": "#2d2820",
        "nav_bg": "#1a1814",
        "industry": "landscaping",
        "tagline": "Making Alberta Beautiful, One Yard at a Time",
        "hero_title_line1": "Experienced",
        "hero_title_line2": "Landscape Designers",
        "hero_sub": "Edmonton Stone Designers has been in the business for over 41 years. We are a one-stop-shop company offering dependable landscaping services to transform your yard into a great outdoor space.",
        "services": [
            ("Landscape Design", "Professional landscape design services incorporating your budget, taste, and requirements into a beautiful plan."),
            ("Retaining Walls", "Expert retaining wall construction — our best-selling service — using premium materials and proven techniques."),
            ("Paving Stone Driveways", "Beautiful paving stone driveway construction that adds value and curb appeal to your property."),
            ("Patios & Walkways", "Custom patio and walkway design and installation to create functional, beautiful outdoor living spaces."),
            ("Stone Work", "Natural and manufactured stone installation for walls, borders, accents, and features."),
            ("Seasonal Maintenance", "Complete seasonal maintenance services to keep your landscape looking its best year-round."),
        ],
        "strip_items": ["Landscape Design", "Retaining Walls", "Paving Stones", "41+ Years", "Sturgeon County"],
        "about_title": "Since 1984",
        "about_text": "Our landscape company began as a family-run business in 1984. Over the years, we have remained true to our roots and continued to adhere to our values. With over 41 years of experience, we can give you the yard of your dreams, no matter what it may be.",
        "about_features": [
            "Family-run business since 1984",
            "Over 41 years of experience",
            "One-stop-shop for all landscaping needs",
            "Principal designer on-site every day",
            "Serving Edmonton and Sturgeon County",
        ],
        "stats": [("41+", "Years in Business"), ("1000+", "Projects Done"), ("Family", "Run Since 1984"), ("One-Stop", "Shop")],
        "testimonial": '"Edmonton Stone Designers transformed our yard completely. Their experience really shows in the quality of their work and attention to detail."',
        "testimonial_author": "Homeowner, Sturgeon County",
        "contact_select": ["Landscape Design", "Retaining Wall", "Paving Stones", "Patio", "Stone Work", "Other"],
    },
    {
        "slug": "greenland-landscaping",
        "name": "Greenland Landscaping",
        "full_name": "Greenland Landscaping Ltd.",
        "city": "Edmonton",
        "email": "greenlandcontracting79@gmail.com",
        "phone": "(780) 729-7908",
        "has_logo": True,
        "accent": "#2E7D32",
        "accent_light": "#43A047",
        "dark": "#1a2e1a",
        "charcoal": "#1b3a1b",
        "nav_bg": "#1a2e1a",
        "industry": "landscaping",
        "tagline": "One-Stop-Shop for All Your Landscaping Needs",
        "hero_title_line1": "Your",
        "hero_title_line2": "Landscaping Partner",
        "hero_sub": "Greenland Landscaping Ltd. is a fully licensed and insured company established in 1999. We are a one-stop shop for all your landscaping needs — serving Edmonton and surrounding areas.",
        "services": [
            ("Lawn Replacement", "Complete lawn replacement services including sodding, grading, and soil preparation for a lush, healthy lawn."),
            ("Paving Stones", "Professional paving stone installation for driveways, patios, and walkways with lasting quality."),
            ("Retaining Walls", "Expert retaining wall construction to manage grading and create beautiful, functional outdoor spaces."),
            ("Trees & Shrubs", "Tree and shrub planting, selection, and maintenance to enhance your landscape for years to come."),
            ("Patios & Firepits", "Custom patio and firepit design and construction — create the outdoor living space you've always wanted."),
            ("Bobcat Services", "Professional bobcat services for grading, excavation, and material spreading on your property."),
        ],
        "strip_items": ["Lawn Replacement", "Paving Stones", "Retaining Walls", "Trees & Shrubs", "Free Estimates"],
        "about_title": "Established 1999",
        "about_text": "Greenland Landscaping Ltd. was established in 1999 and is operated out of Edmonton. We are a one-stop shop for all your landscaping needs, dedicated to providing excellent services and meeting your expectations.",
        "about_features": [
            "Fully licensed and insured",
            "Established in 1999",
            "Commercial and residential services",
            "Free estimates available",
            "Serving Edmonton and surrounding areas",
        ],
        "stats": [("25+", "Years in Business"), ("500+", "Projects Done"), ("Licensed", "& Insured"), ("100%", "Satisfaction")],
        "testimonial": '"Greenland did an amazing job on our front yard. Professional, on time, and the result exceeded our expectations."',
        "testimonial_author": "Homeowner, Edmonton",
        "contact_select": ["Lawn Replacement", "Paving Stones", "Retaining Wall", "Trees & Shrubs", "Patio/Firepit", "Other"],
    },
    {
        "slug": "mowsnowpros",
        "name": "MowSnowPros",
        "full_name": "MowSnowPros",
        "city": "Edmonton",
        "email": "aidan@mowsnowpros.com",
        "phone": "(780) 000-0000",
        "has_logo": False,
        "accent": "#4CAF50",
        "accent_light": "#66BB6A",
        "dark": "#1a2e1a",
        "charcoal": "#2a3f2a",
        "nav_bg": "#1a2e1a",
        "industry": "landscaping",
        "tagline": "On-Demand Yard Care",
        "hero_title_line1": "Yard Services",
        "hero_title_line2": "On Demand",
        "hero_sub": "MowSnowPros offers no-contract snow removal and lawn mowing — one-time service or the entire season. See the price before you request, get updates every step, and pay online. Over 200,000 jobs completed.",
        "services": [
            ("Lawn Mowing", "On-demand lawn mowing with upfront pricing — no contracts, no commitments. Book in seconds from your phone."),
            ("Snow Removal", "Fast, reliable snow removal when you need it. One-time or seasonal service with no long-term contracts."),
            ("Yard Clean-Up", "Spring and fall yard clean-up services to get your property looking its best for the new season."),
            ("Lawn Care", "Comprehensive lawn care including fertilization, aeration, and weed control for a healthy, green yard."),
            ("Seasonal Service", "Flexible seasonal packages — choose one-time service or recurring schedules that fit your needs."),
            ("On-Demand Service", "Request service instantly through our app. See pricing upfront, track progress, and rate the results."),
        ],
        "strip_items": ["Lawn Mowing", "Snow Removal", "No Contracts", "200K+ Jobs", "On-Demand"],
        "about_title": "The Flexible Way to Yard Care",
        "about_text": "We made it easier than ever to get snow removal, lawn mowing and yard services. The most flexible service delivery with no long-term contracts — see the price before you book, get updates, and pay online.",
        "about_features": [
            "No long-term contracts required",
            "See pricing before you book",
            "Real-time updates on every job",
            "Rate and pay online",
            "Over 200,000 jobs completed",
        ],
        "stats": [("200K+", "Jobs Completed"), ("No", "Contracts"), ("On", "Demand"), ("Multiple", "Cities")],
        "testimonial": '"They were fast, efficient and ever so polite. It is wonderful to do business with someone who operates with the customer\'s needs as a priority."',
        "testimonial_author": "Jennifer P., via Facebook Reviews",
        "contact_select": ["Lawn Mowing", "Snow Removal", "Yard Clean-Up", "Lawn Care", "Seasonal", "Other"],
    },
    {
        "slug": "rcl-canada",
        "name": "RCL Canada",
        "full_name": "RCL Landscaping",
        "city": "Edmonton",
        "email": "info@rclcanada.com",
        "phone": "(780) 910-3046",
        "has_logo": False,
        "accent": "#2E7D32",
        "accent_light": "#4CAF50",
        "dark": "#1a2e1a",
        "charcoal": "#1b3a1b",
        "nav_bg": "#1a2e1a",
        "industry": "landscaping",
        "tagline": "Design. Build. Enjoy.",
        "hero_title_line1": "Professional",
        "hero_title_line2": "Landscape Contractors",
        "hero_sub": "RCL has nearly 40 years of designing and landscaping beautiful backyards and lawns. From design to supply to service — we manage all of your Edmonton landscaping needs with creativity and dependability.",
        "services": [
            ("Landscape Design", "Professional landscape design services that combine creativity with practical solutions for your property."),
            ("Stone Work", "Expert stone work including retaining walls, walkways, patios, and decorative stone features."),
            ("Water Features", "Beautiful water feature design and installation — ponds, fountains, and waterfalls for your outdoor space."),
            ("Sod & Irrigation", "Professional sod installation and irrigation systems to keep your lawn green and healthy all season."),
            ("Landscape Lighting", "Outdoor lighting design and installation to enhance the beauty and safety of your property."),
            ("Fences & Decks", "Custom fence and deck construction built to last and designed to complement your landscape."),
        ],
        "strip_items": ["Design & Build", "Stone Work", "Water Features", "Since 1979", "Edmonton"],
        "about_title": "Since 1979",
        "about_text": "With nearly 40 years' worth of designing and landscaping beautiful backyards and lawns, RCL has expanded into a retail outlet where consumers can enjoy browsing through irrigation supplies, pond products, landscaping supplies and lighting. We're passionate about our planet — locally sourced materials, new equipment, and reduced waste.",
        "about_features": [
            "Partnering dependability with creativity since 1979",
            "Retail outlet for landscaping supplies",
            "Locally sourced materials (up to 90%)",
            "New vehicles and equipment — minimal emissions",
            "Comprehensive waste reduction practices",
        ],
        "stats": [("40+", "Years Experience"), ("26+", "5-Star Reviews"), ("Retail", "Outlet"), ("Eco", "Friendly")],
        "testimonial": '"RCL did a fantastic job with our residential driveway replacement and landscaping. Very impressed with their professionalism and quality of work."',
        "testimonial_author": "Ryan Carson, Edmonton",
        "contact_select": ["Landscape Design", "Stone Work", "Water Features", "Sod & Irrigation", "Lighting", "Other"],
    },
    {
        "slug": "enviromulch",
        "name": "Enviromulch",
        "full_name": "Enviromulch",
        "city": "Edmonton",
        "email": "shelby@enviromulch.com",
        "phone": "(780) 000-0000",
        "has_logo": False,
        "accent": "#1B5E20",
        "accent_light": "#2E7D32",
        "dark": "#0d1f0d",
        "charcoal": "#1a301a",
        "nav_bg": "#0d1f0d",
        "industry": "landscaping",
        "tagline": "Environmentally Responsible Mulch & Landscaping",
        "hero_title_line1": "Green",
        "hero_title_line2": "Landscaping",
        "hero_sub": "Enviromulch provides environmentally responsible mulch and landscaping services across Edmonton. Sustainable practices, quality materials, and beautiful results for your outdoor space.",
        "services": [
            ("Mulch Supply", "Premium mulch supply and delivery — a variety of natural mulch products for gardens, beds, and pathways."),
            ("Landscape Supply", "Comprehensive landscape supply delivery including mulch, soil, rock, and decorative stone."),
            ("Garden Bed Design", "Professional garden bed design and installation with sustainable mulch solutions."),
            ("Erosion Control", "Erosion control services using natural mulch and landscape techniques to protect your property."),
            ("Commercial Landscaping", "Commercial mulch and landscaping services for businesses, developments, and municipal properties."),
            ("Residential Services", "Complete residential landscaping services with environmentally-friendly practices and materials."),
        ],
        "strip_items": ["Mulch Supply", "Landscape Materials", "Eco-Friendly", "Delivery", "Edmonton"],
        "about_title": "Environmentally Responsible",
        "about_text": "Enviromulch is committed to providing environmentally responsible landscaping solutions. Our sustainable mulch products and eco-friendly practices help create beautiful outdoor spaces while protecting the environment.",
        "about_features": [
            "Environmentally responsible practices",
            "Natural, sustainable mulch products",
            "Delivery services available",
            "Commercial and residential services",
            "Serving Edmonton and surrounding areas",
        ],
        "stats": [("10+", "Years in Business"), ("Eco", "Friendly"), ("Delivery", "Available"), ("100%", "Natural Products")],
        "testimonial": '"Enviromulch transformed our garden beds with their premium mulch. Great quality, fast delivery, and very professional service."',
        "testimonial_author": "Homeowner, Edmonton",
        "contact_select": ["Mulch Supply", "Landscape Materials", "Garden Design", "Erosion Control", "Delivery", "Other"],
    },
    {
        "slug": "rockscapes",
        "name": "Rockscapes",
        "full_name": "Rockscapes Landscaping",
        "city": "Edmonton",
        "email": "info.rockscapes@gmail.com",
        "phone": "(780) 235-2829",
        "has_logo": False,
        "accent": "#689F38",
        "accent_light": "#8BC34A",
        "dark": "#1a2e1a",
        "charcoal": "#2d3a2d",
        "nav_bg": "#1a2e1a",
        "industry": "landscaping",
        "tagline": "If It Can Be Imagined, It Can Be Created",
        "hero_title_line1": "Rock",
        "hero_title_line2": "Landscapes",
        "hero_sub": "Rockscapes provides rock retaining walls, garden walls, cobblestone edging, patios, firepits, and permanent LED lighting in Edmonton and surrounding areas. If it can be imagined, it can be created.",
        "services": [
            ("Retaining Walls", "Rock retaining and garden walls built with skill, quality materials, and attention to detail."),
            ("Cobblestone Edging", "Beautiful cobblestone edging installations to define and enhance your garden beds and pathways."),
            ("Patios & Firepits", "Custom patio and firepit construction creating the ultimate outdoor living space for your home."),
            ("Paving Stones", "Professional paving stone installation for driveways, walkways, and outdoor living areas."),
            ("Trees & Shrubs", "Tree and shrub planting with expert selection for soil conditions, light, and aesthetic appeal."),
            ("Trimlight LED", "Permanent outdoor LED lighting systems to beautifully illuminate your home year-round."),
        ],
        "strip_items": ["Rock Walls", "Cobblestone", "Patios & Firepits", "Paving Stones", "Trimlight LED"],
        "about_title": "Creating Outdoor Living Spaces",
        "about_text": "At Rockscapes, landscaping is more than digging holes and spreading dirt. It's about creating an outdoor living space that you and your family can fully enjoy. We provide reliable, professional service with unwavering attention to detail.",
        "about_features": [
            "Reliable, professional service",
            "Unwavering attention to detail",
            "Ongoing client communication",
            "Serving Edmonton, Leduc, Beaumont & acreages",
            "Comprehensive landscape plans and estimates",
        ],
        "stats": [("10+", "Years in Business"), ("500+", "Projects Done"), ("Free", "Estimates"), ("Multiple", "Services")],
        "testimonial": '"Rockscapes turned our front yard into something beautiful. Their cobblestone edging and rock work is absolutely stunning."',
        "testimonial_author": "Homeowner, Edmonton",
        "contact_select": ["Retaining Wall", "Cobblestone Edging", "Patio/Firepit", "Paving Stones", "Trimlight LED", "Other"],
    },
    {
        "slug": "downunder-landscaping",
        "name": "Downunder Landscaping",
        "full_name": "Downunder Landscaping Ltd.",
        "city": "Edmonton",
        "email": "brad@downunderlandscaping.ca",
        "phone": "(780) 000-0000",
        "has_logo": True,
        "accent": "#C62828",
        "accent_light": "#E53935",
        "dark": "#1a1414",
        "charcoal": "#2d2020",
        "nav_bg": "#1a1414",
        "industry": "landscaping",
        "tagline": "We Design and Build It, So You Can Enjoy It",
        "hero_title_line1": "Perfect",
        "hero_title_line2": "Yard",
        "hero_sub": "Downunder Landscaping designs and builds outdoor spaces you can truly enjoy. From planning to hard surfacing, water features to lighting — no property too big or too small.",
        "services": [
            ("Landscape Planning", "Expert landscape planning and design to create the perfect yard for your property and lifestyle."),
            ("Retaining Walls", "Professional retaining wall, firepit, patio, and paving stone construction with quality craftsmanship."),
            ("Rock Work", "Expert rock work and stone features to add natural beauty and structure to your landscape."),
            ("Water & Lighting", "Water features and landscape lighting for the ultimate outdoor experience — day and night."),
            ("Plant Selection", "Expert guidance on which plants grow best for your soil, light, shade, and aesthetic preferences."),
            ("Complete Projects", "Full project management from design to completion — we handle every detail so you can enjoy the result."),
        ],
        "strip_items": ["Landscape Design", "Retaining Walls", "Water Features", "Lighting", "Spruce Grove"],
        "about_title": "We Build It, You Enjoy It",
        "about_text": "Downunder Landscaping Ltd. creates beautiful outdoor living spaces for homeowners across the Edmonton area. Our experienced team handles everything from planning and plant selection to hard surfacing and water features.",
        "about_features": [
            "Design and build specialists",
            "No property too big or too small",
            "Water and lighting expertise",
            "Serving Spruce Grove and Edmonton area",
            "Highly recommended by satisfied customers",
        ],
        "stats": [("15+", "Years Experience"), ("300+", "Projects Done"), ("Design", "to Build"), ("100%", "Satisfaction")],
        "testimonial": '"Thanks Brad. Everything looks awesome. Downunder Landscaping came highly recommended and they did not disappoint."',
        "testimonial_author": "Rob & Jolene, Spruce Grove",
        "contact_select": ["Landscape Design", "Retaining Wall", "Water Feature", "Lighting", "Full Project", "Other"],
    },
    # ROOFING
    {
        "slug": "central-roofing",
        "name": "Central Roofing",
        "full_name": "Central Roofing",
        "city": "Calgary",
        "email": "crcalg@telus.net",
        "phone": "(403) 000-0000",
        "has_logo": False,
        "accent": "#B71C1C",
        "accent_light": "#D32F2F",
        "dark": "#0f172a",
        "charcoal": "#1e293b",
        "nav_bg": "#0f172a",
        "industry": "roofing",
        "tagline": "Calgary's Trusted Roofing Professionals",
        "hero_title_line1": "Expert",
        "hero_title_line2": "Roofing",
        "hero_sub": "Central Roofing provides professional roofing services in Calgary and surrounding areas. Quality workmanship, reliable service, and protection for your most important investment.",
        "services": [
            ("Residential Roofing", "Complete residential roofing services — repairs, replacements, and new installations for homes of all sizes."),
            ("Commercial Roofing", "Professional commercial roofing solutions for businesses, warehouses, and multi-unit properties."),
            ("Roof Repairs", "Fast, reliable roof repair services to address leaks, damage, and wear before they become major problems."),
            ("Roof Replacement", "Full roof replacement services with premium materials and expert installation for lasting protection."),
            ("Inspection & Maintenance", "Comprehensive roof inspections and maintenance programs to extend the life of your roof."),
            ("Emergency Service", "Emergency roofing services for storm damage, severe leaks, and other urgent situations."),
        ],
        "strip_items": ["Residential", "Commercial", "Repairs", "Replacements", "Calgary"],
        "about_title": "Protecting Calgary Homes",
        "about_text": "Central Roofing is a Calgary-based roofing company dedicated to protecting homes and businesses with quality roofing solutions. Our experienced team delivers reliable service and superior workmanship on every project.",
        "about_features": [
            "Calgary-based roofing specialists",
            "Licensed and insured professionals",
            "Premium materials from trusted brands",
            "Competitive pricing and free estimates",
            "Serving Calgary and surrounding areas",
        ],
        "stats": [("15+", "Years in Business"), ("500+", "Roofs Done"), ("Licensed", "& Insured"), ("Same Day", "Quotes")],
        "testimonial": '"Central Roofing replaced our entire roof in just two days. Professional crew, clean job site, and excellent quality work."',
        "testimonial_author": "Homeowner, Calgary",
        "contact_select": ["Residential Roofing", "Commercial Roofing", "Roof Repair", "Roof Replacement", "Inspection", "Other"],
    },
    {
        "slug": "highlander-roofing",
        "name": "Highlander Roofing",
        "full_name": "Calgary Highlander Roofing",
        "city": "Calgary",
        "email": "highlanderroofing@shaw.ca",
        "phone": "(403) 200-2250",
        "has_logo": True,
        "accent": "#B71C1C",
        "accent_light": "#D32F2F",
        "dark": "#1a1a1a",
        "charcoal": "#292524",
        "nav_bg": "#1a1a1a",
        "industry": "roofing",
        "tagline": "Your Premier Roofing and Siding Experts",
        "hero_title_line1": "You Dream It,",
        "hero_title_line2": "We Build It",
        "hero_sub": "Calgary Highlander Roofing is your go-to destination for top-notch roofing and siding services. Small company, low overhead — translates to savings on your project. Licensed, insured, WCB. Family owned and operated.",
        "services": [
            ("Residential Roofing", "Complete residential roofing services — from repairs to full replacements using premium shingles from trusted brands."),
            ("Commercial Roofing", "Business owners rely on our expertise with renowned brands like IKO and Owens Corning for lasting durability."),
            ("Siding Services", "Top-quality siding installation and repairs that boost your property's curb appeal and energy efficiency."),
            ("Roof Repairs", "Expert roof repair services to protect your home from Calgary's unpredictable weather conditions."),
            ("10-Year Warranty", "Every project backed by a 10-year workmanship warranty — our commitment to lasting quality."),
            ("Free Estimates", "Free, no-obligation estimates with transparent pricing. We help you make the best decision for your property."),
        ],
        "strip_items": ["Residential", "Commercial", "Siding", "10-Year Warranty", "Family Owned"],
        "about_title": "Local Expertise You Can Trust",
        "about_text": "As a locally owned and operated business, we understand the unique challenges that Calgary's climate presents. We're here to provide roofing and siding solutions that withstand the demands of our region — backed by a 10-year workmanship warranty.",
        "about_features": [
            "Locally owned and operated",
            "10-year workmanship warranty",
            "Premium materials from IKO and Owens Corning",
            "Licensed, insured, and WCB covered",
            "Family owned — low overhead means savings for you",
        ],
        "stats": [("10-Year", "Warranty"), ("Licensed", "& Insured"), ("Family", "Owned"), ("Premium", "Materials")],
        "testimonial": '"Highlander Roofing was professional from start to finish. They completed our roof ahead of schedule and the quality is outstanding."',
        "testimonial_author": "Homeowner, Calgary",
        "contact_select": ["Residential Roofing", "Commercial Roofing", "Siding", "Roof Repair", "Free Estimate", "Other"],
    },
]

def generate_svg_icon(letter, color):
    return f'''<svg width="40" height="40" viewBox="0 0 40 40" fill="none" xmlns="http://www.w3.org/2000/svg"><rect width="40" height="40" rx="4" fill="{color}" fill-opacity="0.12"/><text x="50%" y="55%" dominant-baseline="middle" text-anchor="middle" fill="{color}" font-family="Inter,sans-serif" font-weight="700" font-size="18">{letter}</text></svg>'''

def generate_html(b):
    slug = b["slug"]
    accent = b["accent"]
    accent_light = b["accent_light"]
    dark = b["dark"]
    charcoal = b["charcoal"]
    nav_bg = b["nav_bg"]
    
    # Logo HTML
    if b["has_logo"]:
        logo_html = f'''<img src="assets/{slug}/logo.png" alt="{b["name"]}" style="height:40px;width:auto;display:inline-block;vertical-align:middle;margin-right:0.5rem;background:white;border-radius:8px;padding:4px;" />'''
    else:
        logo_html = ""
    
    # Background image
    bg_img = f"assets/{slug}/img0.jpg" if True else ""
    
    # Service icons (using letter-based SVG approach)
    service_letters = ["W", "K", "D", "F", "P", "C"]
    
    # Build service cards HTML
    svc_cards = ""
    for i, (name, desc) in enumerate(b["services"]):
        letter = service_letters[i % len(service_letters)]
        svc_cards += f'''
      <div class="svc-card">
        <div class="svc-icon">{generate_svg_icon(letter, accent)}</div>
        <div class="svc-name">{name}</div>
        <p class="svc-desc">{desc}</p>
      </div>'''
    
    # Build strip items
    strip_html = ""
    for i, item in enumerate(b["strip_items"]):
        if i > 0:
            strip_html += '<div class="os-div"></div>\n    '
        strip_html += f'<div class="os-item">{item}</div>'
    
    # Build about features
    features_html = ""
    for f in b["about_features"]:
        features_html += f'\n        <div class="af"><div class="af-dot"></div>{f}</div>'
    
    # Build stats
    stats_html = ""
    for num, label in b["stats"]:
        stats_html += f'''
        <div class="stat">
          <div class="stat-num">{num}</div>
          <div class="stat-label">{label}</div>
        </div>'''
    
    # Build select options
    select_html = ""
    for s in b["contact_select"]:
        select_html += f'<option>{s}</option>\n          '
    
    # Testimonial
    testimonial = b.get("testimonial", "")
    testimonial_author = b.get("testimonial_author", "")
    
    # Phone for contact
    phone = b.get("phone", "")
    email = b["email"]
    city = b["city"]
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{b["name"]} | {b["city"]}, AB</title>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Barlow+Condensed:wght@600;700;800&display=swap" rel="stylesheet" />
  <style>
    *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
    :root {{
      --accent: {accent};
      --accent-light: {accent_light};
      --dark: {dark};
      --charcoal: {charcoal};
      --nav-bg: {nav_bg};
      --mid: #2e3848;
      --bg: #f4f5f7;
      --surface: #ffffff;
      --border: #dde2ec;
      --warm: #f0f2f8;
      --muted: #6a7890;
    }}
    html {{ scroll-behavior: smooth; }}
    body {{ font-family: 'Inter', sans-serif; background: var(--bg); color: var(--dark); overflow-x: hidden; }}

    nav {{
      position: fixed; top: 0; left: 0; right: 0; z-index: 100;
      display: flex; align-items: center; justify-content: space-between;
      padding: 0 6%; height: 66px;
      background: var(--nav-bg);
      border-bottom: 2px solid var(--accent);
    }}
    .nav-brand {{ font-family: 'Barlow Condensed', sans-serif; font-size: 1.3rem; font-weight: 700; color: white; text-decoration: none; text-transform: uppercase; letter-spacing: 0.05em; display:flex;align-items:center; }}
    .nav-brand span {{ color: var(--accent); }}
    .nav-links {{ display: flex; gap: 1.5rem; list-style: none; align-items: center; }}
    .nav-links a {{ color: rgba(255,255,255,0.65); text-decoration: none; font-size: 0.78rem; font-weight: 500; letter-spacing: 0.04em; text-transform: uppercase; transition: color 0.2s; }}
    .nav-links a:hover {{ color: white; }}
    .nav-cta {{ background: var(--accent) !important; color: white !important; padding: 0.42rem 1.2rem; border-radius: 3px; font-weight: 700; transition: background 0.2s !important; }}
    .nav-cta:hover {{ background: var(--accent-light) !important; }}

    .hero {{ margin-top: 66px; position: relative; min-height: calc(100vh - 66px); display: flex; align-items: center; overflow: hidden; }}
    .hero-bg {{ position: absolute; inset: 0; background: url('assets/{slug}/img0.jpg') center/cover no-repeat; filter: brightness(0.25); }}
    .hero-content {{ position: relative; z-index: 2; padding: 5rem 8%; max-width: 780px; }}
    .hero-eyebrow {{ font-size: 0.62rem; font-weight: 700; letter-spacing: 0.2em; text-transform: uppercase; color: var(--accent); display: flex; align-items: center; gap: 0.8rem; margin-bottom: 1.25rem; }}
    .hero-eyebrow::before {{ content: ''; display: block; width: 24px; height: 2px; background: var(--accent); }}
    .hero h1 {{ font-family: 'Barlow Condensed', sans-serif; font-size: clamp(3rem, 6.5vw, 6.5rem); font-weight: 800; text-transform: uppercase; line-height: 0.95; color: white; margin-bottom: 1.25rem; }}
    .hero h1 span {{ color: var(--accent); display: block; }}
    .hero p {{ font-size: 0.92rem; color: rgba(255,255,255,0.55); line-height: 1.9; max-width: 480px; margin-bottom: 2rem; }}
    .hero-buttons {{ display: flex; gap: 1rem; flex-wrap: wrap; margin-bottom: 2.5rem; }}
    .btn-accent {{ background: var(--accent); color: white; padding: 0.85rem 2rem; text-decoration: none; font-size: 0.8rem; font-weight: 700; letter-spacing: 0.08em; text-transform: uppercase; border-radius: 3px; transition: background 0.2s; display: inline-block; }}
    .btn-accent:hover {{ background: var(--accent-light); }}
    .btn-ghost {{ border: 2px solid rgba(255,255,255,0.2); color: white; padding: 0.85rem 2rem; text-decoration: none; font-size: 0.8rem; font-weight: 600; letter-spacing: 0.08em; text-transform: uppercase; border-radius: 3px; transition: border-color 0.2s; display: inline-block; }}
    .btn-ghost:hover {{ border-color: white; }}
    .hero-trust {{ display: flex; gap: 2rem; flex-wrap: wrap; padding-top: 1.5rem; border-top: 1px solid rgba(255,255,255,0.08); }}
    .trust-item {{ font-size: 0.78rem; color: rgba(255,255,255,0.4); display: flex; align-items: center; gap: 0.5rem; }}
    .trust-dot {{ width: 5px; height: 5px; background: var(--accent); border-radius: 50%; flex-shrink: 0; }}

    .accent-strip {{ background: var(--accent); padding: 1rem 8%; display: flex; align-items: center; justify-content: center; gap: 3rem; flex-wrap: wrap; }}
    .os-item {{ font-size: 0.78rem; font-weight: 700; letter-spacing: 0.08em; text-transform: uppercase; color: white; }}
    .os-div {{ width: 1px; height: 14px; background: rgba(255,255,255,0.3); }}

    section {{ padding: 5rem 8%; }}
    .sec-eyebrow {{ font-size: 0.62rem; font-weight: 700; letter-spacing: 0.2em; text-transform: uppercase; color: var(--accent); display: flex; align-items: center; gap: 0.7rem; margin-bottom: 0.75rem; }}
    .sec-eyebrow::before {{ content: ''; display: block; width: 20px; height: 2px; background: var(--accent); }}
    .sec-title {{ font-family: 'Barlow Condensed', sans-serif; font-size: clamp(2rem, 4vw, 3rem); font-weight: 800; text-transform: uppercase; color: var(--dark); line-height: 1; margin-bottom: 1rem; }}
    .sec-sub {{ color: var(--muted); font-size: 0.88rem; line-height: 1.85; max-width: 560px; }}

    #services {{ background: var(--surface); }}
    .svc-grid {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 1.5rem; margin-top: 2.5rem; }}
    .svc-card {{ border: 1px solid var(--border); border-top: 3px solid var(--accent); padding: 2rem 1.5rem; border-radius: 0 0 4px 4px; transition: box-shadow 0.2s, transform 0.2s; }}
    .svc-card:hover {{ box-shadow: 0 6px 20px rgba(14,19,24,0.08); transform: translateY(-3px); }}
    .svc-icon {{ margin-bottom: 0.75rem; }}
    .svc-icon svg {{ display: block; }}
    .svc-name {{ font-family: 'Barlow Condensed', sans-serif; font-size: 1.2rem; font-weight: 700; text-transform: uppercase; color: var(--dark); margin-bottom: 0.4rem; }}
    .svc-desc {{ font-size: 0.8rem; color: var(--muted); line-height: 1.7; }}

    #about {{ background: var(--charcoal); display: grid; grid-template-columns: 1fr 1fr; gap: 0; }}
    .about-img img {{ width: 100%; height: 100%; min-height: 480px; object-fit: cover; display: block; filter: brightness(0.75); }}
    .about-body {{ padding: 5rem 4rem; display: flex; flex-direction: column; justify-content: center; }}
    #about .sec-title {{ color: white; }}
    #about .sec-sub {{ color: rgba(255,255,255,0.5); margin-bottom: 0.85rem; }}
    .about-features {{ display: flex; flex-direction: column; gap: 0.75rem; margin-top: 2rem; }}
    .af {{ display: flex; gap: 0.75rem; font-size: 0.83rem; color: rgba(255,255,255,0.5); align-items: flex-start; }}
    .af-dot {{ width: 5px; height: 5px; background: var(--accent); border-radius: 50%; margin-top: 0.4rem; flex-shrink: 0; }}

    #stats {{ background: var(--surface); border-top: 1px solid var(--border); border-bottom: 1px solid var(--border); }}
    .stats-grid {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 2rem; text-align: center; }}
    .stat {{ padding: 1.5rem; }}
    .stat-num {{ font-family: 'Barlow Condensed', sans-serif; font-size: 2.8rem; font-weight: 800; color: var(--accent); line-height: 1; }}
    .stat-label {{ font-size: 0.75rem; color: var(--muted); text-transform: uppercase; letter-spacing: 0.08em; margin-top: 0.5rem; }}

    #testimonial {{ background: var(--warm); text-align: center; }}
    .testimonial-card {{ max-width: 700px; margin: 2rem auto 0; background: white; border: 1px solid var(--border); padding: 3rem; border-radius: 4px; position: relative; }}
    .testimonial-card::before {{ content: '"'; position: absolute; top: -10px; left: 2rem; font-size: 5rem; color: var(--accent); opacity: 0.15; font-family: Georgia, serif; line-height: 1; }}
    .testimonial-text {{ font-size: 1.1rem; font-style: italic; color: var(--dark); line-height: 1.8; margin-bottom: 1.5rem; }}
    .testimonial-author {{ font-size: 0.78rem; font-weight: 600; color: var(--accent); text-transform: uppercase; letter-spacing: 0.08em; }}

    #contact {{ background: var(--dark); }}
    #contact .sec-title {{ color: white; }}
    .contact-grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 5rem; margin-top: 2.5rem; }}
    .ci {{ display: flex; gap: 1rem; margin-bottom: 1.25rem; }}
    .ci-icon {{ width: 40px; height: 40px; background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1); border-radius: 3px; display: flex; align-items: center; justify-content: center; font-size: 1rem; flex-shrink: 0; color: var(--accent); }}
    .ci-label {{ font-size: 0.6rem; text-transform: uppercase; letter-spacing: 0.12em; color: var(--accent); margin-bottom: 0.2rem; }}
    .ci-val {{ font-size: 0.9rem; color: rgba(255,255,255,0.6); }}
    .ci-val a {{ color: rgba(255,255,255,0.6); text-decoration: none; }}
    .fg {{ margin-bottom: 0.9rem; }}
    .fg label {{ font-size: 0.62rem; letter-spacing: 0.12em; text-transform: uppercase; color: rgba(255,255,255,0.35); display: block; margin-bottom: 0.4rem; }}
    .fg input, .fg textarea, .fg select {{ width: 100%; background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1); border-bottom: 2px solid rgba(255,255,255,0.1); padding: 0.78rem 1rem; color: white; font-family: 'Inter', sans-serif; font-size: 0.875rem; outline: none; transition: border-color 0.2s; }}
    .fg input:focus, .fg textarea:focus, .fg select:focus {{ border-bottom-color: var(--accent); }}
    .fg textarea {{ height: 110px; resize: vertical; }}
    .fg select option {{ background: var(--charcoal); }}
    .fr {{ display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; }}
    .btn-submit {{ background: var(--accent); color: white; border: none; width: 100%; padding: 1rem; font-family: 'Inter', sans-serif; font-size: 0.8rem; font-weight: 700; letter-spacing: 0.08em; text-transform: uppercase; cursor: pointer; border-radius: 3px; transition: background 0.2s; }}
    .btn-submit:hover {{ background: var(--accent-light); }}

    footer {{ background: #080c10; padding: 1.5rem 8%; display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 1rem; border-top: 2px solid var(--accent); }}
    .footer-brand {{ font-family: 'Barlow Condensed', sans-serif; font-size: 1rem; font-weight: 700; text-transform: uppercase; color: white; letter-spacing: 0.05em; }}
    .footer-brand span {{ color: var(--accent); }}
    .footer-copy {{ font-size: 0.72rem; color: rgba(255,255,255,0.2); }}
    .footer-demo {{ font-size: 0.65rem; color: rgba(255,255,255,0.15); }}

    @media (max-width: 1024px) {{ .svc-grid {{ grid-template-columns: repeat(2, 1fr); }} .stats-grid {{ grid-template-columns: repeat(2, 1fr); }} }}
    @media (max-width: 860px) {{
      nav .nav-links {{ display: none; }}
      .nav-mobile-cta {{ display: inline-block !important; }}
      section {{ padding: 4rem 6%; }}
      #about {{ grid-template-columns: 1fr; }}
      .about-img img {{ min-height: 260px; height: 260px; }}
      .about-body {{ padding: 3rem 6%; }}
      .contact-grid {{ grid-template-columns: 1fr; gap: 3rem; }}
      .accent-strip {{ gap: 1.5rem; flex-direction: column; align-items: flex-start; padding: 1rem 6%; }}
      .os-div {{ display: none; }}
    }}
    @media (max-width: 600px) {{
      .hero h1 {{ font-size: 3rem; }}
      .svc-grid {{ grid-template-columns: 1fr; }}
      .stats-grid {{ grid-template-columns: 1fr 1fr; }}
      .fr {{ grid-template-columns: 1fr; }}
      footer {{ flex-direction: column; align-items: flex-start; }}
    }}
  </style>
</head>
<body>

  <nav>
    <a href="#" class="nav-brand">{logo_html}{b["name"].split()[0]} <span>{" ".join(b["name"].split()[1:]) if len(b["name"].split()) > 1 else ""}</span></a>
    <ul class="nav-links">
      <li><a href="#services">Services</a></li>
      <li><a href="#about">About</a></li>
      <li><a href="#contact" class="nav-cta">Get a Quote</a></li>
    </ul>
    <a href="#contact" class="nav-mobile-cta" style="display:none; font-size:0.72rem; font-weight:700; background:var(--accent); color:white; padding:0.45rem 1rem; border-radius:3px; text-decoration:none;">Quote</a>
  </nav>

  <div class="hero">
    <div class="hero-bg"></div>
    <div class="hero-content">
      <div class="hero-eyebrow">{b["city"]}, Alberta · {b["tagline"]}</div>
      <h1>{b["hero_title_line1"]}<br /><span>{b["hero_title_line2"]}</span></h1>
      <p>{b["hero_sub"]}</p>
      <div class="hero-buttons">
        <a href="#contact" class="btn-accent">Get a Quote</a>
        <a href="#services" class="btn-ghost">Our Services</a>
      </div>
      <div class="hero-trust">
        <div class="trust-item"><div class="trust-dot"></div>Licensed & Insured</div>
        <div class="trust-item"><div class="trust-dot"></div>Free Estimates</div>
        <div class="trust-item"><div class="trust-dot"></div>{b["city"]} & Area</div>
      </div>
    </div>
  </div>

  <div class="accent-strip">
    {strip_html}
  </div>

  <section id="services">
    <div class="sec-eyebrow">What We Do</div>
    <div class="sec-title">Our Services</div>
    <p class="sec-sub">Professional {b["industry"]} services to meet your needs.</p>
    <div class="svc-grid">{svc_cards}
    </div>
  </section>

  <section id="about" style="padding:0;">
    <div class="about-img">
      <img src="assets/{slug}/img1.jpg" alt="{b["name"]}" />
    </div>
    <div class="about-body">
      <div class="sec-eyebrow">About Us</div>
      <div class="sec-title">{b["about_title"]}</div>
      <p class="sec-sub">{b["about_text"]}</p>
      <div class="about-features">{features_html}
      </div>
    </div>
  </section>

  <section id="stats">
    <div class="stats-grid">{stats_html}
    </div>
  </section>

  <section id="testimonial">
    <div class="sec-eyebrow" style="justify-content:center;">What Clients Say</div>
    <div class="sec-title" style="text-align:center;">Testimonials</div>
    <div class="testimonial-card">
      <p class="testimonial-text">{testimonial}</p>
      <div class="testimonial-author">— {testimonial_author}</div>
    </div>
  </section>

  <section id="contact">
    <div class="sec-eyebrow">Get in Touch</div>
    <div class="sec-title" style="color:white;">Request a Quote</div>
    <div class="contact-grid">
      <div>
        {"<div class='ci'><div class='ci-icon'><svg width=\"16\" height=\"16\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\"><path d=\"M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.127.96.361 1.903.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0 1 22 16.92z\"></path></svg></div><div><div class='ci-label'>Phone</div><div class='ci-val'><a href=\"tel:{phone}\">{phone}</a></div></div></div>" if phone else ""}
        <div class="ci"><div class="ci-icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline></svg></div><div><div class="ci-label">Email</div><div class="ci-val"><a href="mailto:{email}">{email}</a></div></div></div>
        <div class="ci"><div class="ci-icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg></div><div><div class="ci-label">Location</div><div class="ci-val">{city}, Alberta</div></div></div>
      </div>
      <div>
        <div class="fr">
          <div class="fg"><label>First Name</label><input type="text" placeholder="Your first name" /></div>
          <div class="fg"><label>Last Name</label><input type="text" placeholder="Your last name" /></div>
        </div>
        <div class="fg"><label>Company</label><input type="text" placeholder="Your company name" /></div>
        <div class="fg"><label>Phone</label><input type="tel" placeholder="780-000-0000" /></div>
        <div class="fg"><label>Email</label><input type="email" placeholder="you@example.com" /></div>
        <div class="fg">
          <label>Service Needed</label>
          <select>
            <option value="" disabled selected>Select a service...</option>
            {select_html}
          </select>
        </div>
        <div class="fg"><label>Project Details</label><textarea placeholder="Tell us about your project..."></textarea></div>
        <button class="btn-submit" type="button" onclick="submitForm()">Submit Request</button>
        <div id="cf-status" style="margin-top:12px;font-size:0.8rem;display:none;padding:10px 14px;border-radius:4px;"></div>
      </div>
    </div>
  </section>

  <script>
  function submitForm() {{
    const status = document.getElementById('cf-status');
    status.style.display = 'block';
    status.style.background = 'rgba(34,197,94,0.1)';
    status.style.color = '#22c55e';
    status.style.border = '1px solid rgba(34,197,94,0.3)';
    status.textContent = 'Thank you! Your request has been received. We will be in touch shortly.';
  }}
  </script>

  <footer>
    <div class="footer-brand">{b["name"].split()[0]} <span>{" ".join(b["name"].split()[1:]) if len(b["name"].split()) > 1 else b["name"]}</span></div>
    <div class="footer-copy">&copy; 2026 {b["full_name"]} &middot; {city}, AB</div>
    <div class="footer-demo">Powered by Wildrose Automations</div>
  </footer>

</body>
</html>'''
    return html

# Fix mowsnowpros stats (bad tuple)
for b in businesses:
    # Ensure stats are proper tuples
    fixed_stats = []
    for s in b["stats"]:
        if isinstance(s, tuple) and len(s) == 2:
            fixed_stats.append(s)
        else:
            fixed_stats.append(("—", str(s)))
    b["stats"] = fixed_stats

for b in businesses:
    html = generate_html(b)
    path = os.path.join(BASE, f'{b["slug"]}-demo.html')
    with open(path, 'w') as f:
        f.write(html)
    print(f"Generated {b['slug']}-demo.html")

print("\nAll 20 demos generated!")
