#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parent

NAV = [
    ("index.php", "HOME", "Northeast Ohio Auto Repair, Racing Fabrication, Welding and Fabrication"),
    ("about.php", "ABOUT US", "About Mad Mike's Motorsports"),
    ("racing.php", "RACING", "Racing Products & Services"),
    ("videos.php", "VIDEOS", "Racing Videos"),
    ("services.php", "AUTO SERVICES", "Our Services"),
    ("gallery.php", "GALLERY", "Photo Gallery"),
    ("contact.php", "CONTACT US", "Request a Quote"),
]

CITIES = (
    "Call (330) 874-5351 for affordable Auto Repair & Race Car Fabrication in Northeast OH area near the following cities: "
    "Baltic OH, Barnhill Oh, Barrs Mills Oh, Beartown Oh, Bernice Oh, Blackband Oh, Bolivar Oh, Booth Oh, Brightwood Oh, "
    "Coalport Oh, Columbia Oh, Dennison Oh, Dover Oh, Dundee Oh, Eastport Oh, Fiat Oh, Gilmore Oh, Glasgow Oh, Gnadenhutten Oh, "
    "Goshen Oh, Johnston Oh, Joyce Oh, Lock Seventeen Oh, Loudon Oh, Midvale Oh, Mineral City Oh, Mizers Oh, New Cumberland Oh, "
    "New Philadelphia Oh, Newcomerstown Oh, Newport Oh, Parral Oh, Peoli Oh, Port Washington Oh, Postboy Oh, Ragersville Oh, "
    "Riverside Park Oh, Roanoake Oh, Rock Oh, Rockford Oh, Roswell Oh, Sandyville Oh, Schoenbrunn Oh, Shanesville Oh, Somerdale Oh, "
    "South Side Oh, Stillwater Oh, Stone Creek Oh, Strasburg Oh, Sugarcreek Oh, Tuscarawas Oh, Uhrichsville Oh, Wainwright Oh, "
    "West Chester Oh, Winfield Oh, Winklepleck Oh, Grove Oh, Wolf Oh, Yorktown Oh, Zoar Oh, Zoarville Oh, Alliance Oh, Amherst Oh, "
    "Heights Oh, Aultman Oh, Avondale Oh, Banker Heights Oh, Battlesburg Oh, Beach City Oh, Beechwood Oh, Belfort Oh, Bolton Oh, "
    "Brewster Oh, Cairo Oh, Camp Creek Oh, Canal Fulton Oh, Canton Oh, Canton Road Oh, Charity Rotch Oh, Clearview Oh, Columbia Oh, "
    "Crossroads Oh, Crystal Springs Oh, East Canton Oh, East Greenville Oh, East Sparta Oh, Edgefield Oh, Elms Acres Oh, Elton Oh, "
    "Fairhope Oh, Freeburg Oh, Gambrinus Oh, Goodland Acres Oh, Greentown Oh, Greenwood Acres Oh, Harmon Oh, Harrisburg Oh, Hartville Oh, "
    "Hillcrest Oh, Hills and Dales Oh, Howenstine Oh, Justus Oh, Kendall Heights Oh, Lake Cable Oh, Lake Slagle Oh, Lawndale Oh, "
    "Lexington Oh, Limaville Oh, Louisville Oh, Magnolia Oh, Mapleton Oh, Marlboro Oh, Massillon Oh, Maximo Oh, Mayflower Village Oh, "
    "McDonaldsville Oh, Meyers Lake Oh, Middlebranch Oh, Minerva Oh, Moffitt Heights Oh, Mount Pleasant Oh, Mount Union Oh, Myers Oh, "
    "Navarre Oh, New Baltimore Oh, New England Oh, New Franklin Oh, Newman Oh, North Brewster Oh, North Canton Oh, North Industry Oh, "
    "North Lawrence Oh, Oak Ridge Oh, Paris Oh, Perry Heights Oh, Pigeon Run Oh, Pleasant View Oh, Reedurban Oh, Richville Oh, "
    "Robertsville Oh, Rockville Oh, Sippo Oh, Sippo Heights Oh, Smoketown Oh, Stanwood Oh, Uniontown Oh, Urban Hill Oh, Waco Oh, "
    "Walnut Hills Oh, Waynesburg Oh, West Brookfield Oh, West Park Oh, Westarado Oh, Whipple Heights Oh, Wilmot Oh,"
)

GALLERY = [
    "2.jpg", "3.jpg", "4.jpg", "5.jpg", "5_0.jpg", "6.jpg", "7.jpg", "008.jpg", "8.jpg",
    "009.jpg", "9.jpg", "010.jpg", "10.jpg", "10_0.jpg", "011.jpg", "12.jpg", "12_0.jpg",
    "023.jpg", "28.jpg", "155.jpg", "156.jpg", "275.jpg", "276.jpg", "277.jpg", "278.jpg",
    "361.jpg", "363.jpg", "364.jpg", "365.jpg", "371.jpg", "373.jpg", "378.jpg", "472.jpg",
    "473.jpg", "479.jpg", "480.jpg", "481.jpg", "482.jpg", "483.jpg", "490.jpg", "491.jpg",
    "494.jpg", "625.jpg", "638.jpg", "643.jpg", "644.jpg", "fg_91.jpg", "fg_92.jpg",
    "fg_93.jpg", "fg_94.jpg", "fg_95.jpg", "fg_96.jpg", "fg_97.jpg", "fg_112.jpg",
    "fg_121.jpg", "fg_122.jpg", "fg_131.jpg", "fg_132.jpg", "fg_133.jpg", "fg_139.jpg",
    "fg_140.jpg", "fg_141.jpg", "fg_142.jpg", "fg_144.jpg", "fg_145.jpg", "fg_218.jpg",
    "fg_220.jpg", "fg_221.jpg", "fg_222.jpg", "fg_223.jpg", "pict0054.jpg", "pict0058.jpg",
    "1.jpg", "2_0.jpg",
]


def shell(title, description, keywords, current, main, extra_class=""):
    nav_items = []
    for href, label, ttitle in NAV:
        active = ' class="is-active"' if href == current else ""
        nav_items.append(f'        <li><a href="{href}" title="{ttitle}"{active}>{label}</a></li>')
    footer_links = "\n".join(
        f'      <a href="{href}">{label}</a>' for href, label, _ in NAV
    )
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <meta name="keywords" content="{keywords}">
  <meta name="geo.region" content="US-OH">
  <meta name="geo.placename" content="Strasburg">
  <meta name="geo.position" content="40.622277;-81.435419">
  <meta name="ICBM" content="40.622277, -81.435419">
  <meta name="robots" content="index, follow, archive">
  <link rel="icon" href="images/logo.gif">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Libre+Baskerville:ital,wght@1,700&family=Oswald:wght@400;500;600;700&family=Source+Sans+3:ital,wght@0,400;0,600;0,700;1,400&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="css/site.css">
</head>
<body class="{extra_class}">
  <a class="skip" href="#content">Skip to content</a>
  <header class="site-header">
    <div class="checker-strip" aria-hidden="true"></div>
    <div class="header-inner">
      <a class="brand" href="index.php" title="Mad Mike's Motorsports">
        <img class="brand-logo" src="images/logo.gif" alt="Mad Mike's Motorsports">
        <span class="wordmarks">
          <img src="images/Mad-Mikes.png" alt="Mad Mike's">
          <img src="images/motorsports.png" alt="Motorsports">
        </span>
      </a>
      <div class="header-meta">
        <a class="phone" href="tel:3308785351" title="Call Today!">330-878-5351</a>
        <p class="addr">7736 Ft. Laurens Rd NW<br>Strasburg, OH 44680</p>
      </div>
      <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="site-nav">Menu</button>
    </div>
    <nav id="site-nav" class="site-nav">
      <ul>
{chr(10).join(nav_items)}
      </ul>
    </nav>
  </header>
{main}
  <footer class="site-footer">
    <div class="checker-strip thick" aria-hidden="true"></div>
    <div class="footer-inner">
      <p class="footer-url">www.madmikesmotorsports.com</p>
      <nav class="footer-nav">
{footer_links}
      </nav>
      <p class="copy">&copy; 2010 Mad Mike’s Motorsports. All Rights Reserved. &nbsp; Web Design by <a href="http://www.maxwellpcconsulting.com">Maxwell PC Consulting, LLC</a></p>
    </div>
    <p class="cities">{CITIES}</p>
  </footer>
  <script src="js/site.js"></script>
</body>
</html>
"""


def rail(extra=""):
    return f"""    <aside class="rail">
      <div class="hours-card" title="Business Hours">
        <div class="checker-strip" aria-hidden="true"></div>
        <h3>Business Hours</h3>
        <dl>
          <dt>Monday - Friday</dt>
          <dd>8am - 5pm</dd>
          <dt>Saturday</dt>
          <dd>By Appointment Only</dd>
          <dt>Sunday</dt>
          <dd>Closed</dd>
        </dl>
        <p class="hours-note">Closed Holidays</p>
      </div>
      <img class="pay-badge" src="images/visa_mc.jpg" alt="Visa and MasterCard accepted">
{extra}    </aside>"""

RAIL = rail()
RAIL_RACE = rail('      <img class="race-photo" src="images/race.png" alt="Custom race car built at Mad Mike\'s Motorsports">\n')


def inner(title, body, sidebar=None):
    side = RAIL if sidebar is None else sidebar
    return f"""  <main id="content" class="page">
    <div class="page-title">
      <h1>{title}</h1>
    </div>
    <div class="layout">
{side}
      <div class="article">
{body}
      </div>
    </div>
  </main>"""


PAGES = {}

PAGES["index.php"] = (
    "Northeast Ohio Drag Racing, Auto Repair, Race Car Building",
    "We do it all. Ohio Drag Racing Headquarters - Designing, Building, Re-build, Custom Dragsters, Junior Dragsters, NHRA & IHRA Certified chassis. Northeast Ohio auto repair - engine, transmission, rear end, exhaust, body, interior and more.",
    "drag racing,nhra drag racing,drag racing video,drag racing videos,used race car parts,auto repair,auto repair questions,ohio,motorsports,jr motorsports,mad mikes motorsports,co2 dragster,co2 dragsters,dragster,dragsters,ohio auto repair,northeast ohio auto repair,strasburg auto repair,strasburg racing,strasburg drag racing,ohio racing,ohio drag racing,custom drag cars,drag car design,building,NHRA,IHRA,build chassis,motorcycle racing,motorcycle fabrication,chopper design,build motorcycle chopper,frame extensions",
    """  <section class="hero" id="content">
    <div class="hero-copy">
      <p class="eyebrow">Serving Northeast Ohio</p>
      <h1>Ohio drag racing headquarters</h1>
      <p class="lede">The premiere destination in Ohio for all of your racing fabrication needs. We also offer full service automotive repair &amp; general welding and fabrication services.</p>
      <div class="hero-actions">
        <a class="btn" href="racing.php">Racing</a>
        <a class="btn ghost" href="services.php">Auto Services</a>
      </div>
    </div>
  </section>
  <div class="home-grid">
    <section class="panel" title="We do it all!">
      <h2>We do it all</h2>
      <ul class="fab-list">
        <li>Custom Chassis</li>
        <li>Prostreet Back Halfs</li>
        <li>Brakes &amp; Suspension</li>
        <li>Chassis Updates and Repairs</li>
        <li>Full Sheet Metal Shop</li>
        <li>Custom Fitted Lexan Windows mr-10</li>
        <li>Custom Headers</li>
        <li>NOS Installed Plates and Foggers</li>
        <li>Promod 1 Wheel Wheelie Bars</li>
        <li>We Handle Any Racecar Need and Repairs</li>
      </ul>
      <p class="more">And much more! Click <a href="services.php">here</a> for a complete list of all of the services we offer.</p>
    </section>
    <aside class="panel badge-card">
      <img src="images/NHRA2.png" alt="NHRA">
      <p>We build full-tube chassis to NHRA and IHRA specifications.</p>
      <a class="btn" href="contact.php">Request a Quote</a>
    </aside>
  </div>""",
    "home",
)

PAGES["about.php"] = (
    "About Mad Mike's Motorsports. Northeast Ohio Drag Racing",
    "Mad Mike's Motorsports is your one stop shop for all your racing, automotive service and repair needs. We are conveniently located near Interstate 77 and State Route 250 in Strasburg, OH. With 3 service bays, an inspection bay, and ASE certified.",
    "Quality Service at an Affordable Price It is our belief that routine maintenance prolongs the life and safety of your vehicle and is less expensive and more convenient than unscheduled repairs while helping to maintain the value of your vehicle Locally owned and operated,Mad Mike's Motorsports is your one stop shop for all your racing,automotive service and repair needs. We are conveniently located near Interstate 77 and State Route 250 in Strasburg,OH. With 3 service bays,an inspection bay,and ASE certified technicians,we are prepared to meet all of your service needs. Our technicians are experienced and certified experts,who evaluate your immediate needs as well as make logical recommendations for the long-term maintenance and performance of your vehicle. We have customers AND technicians who have been with us for more than 10 years.",
    inner(
        "Quality Service at an Affordable Price",
        """        <p>It is our belief that routine maintenance prolongs the life and safety of your vehicle and is less expensive and more convenient than unscheduled repairs while helping to maintain the value of your vehicle.</p>
        <p>Locally owned and operated, Mad Mike's Motorsports is your one stop shop for all your racing, automotive service and repair needs. We are conveniently located near Interstate 77 and State Route 250 in Strasburg, OH. With 3 service bays, an inspection bay, and ASE certified technicians, we are prepared to meet all of your service needs.</p>
        <p>Our technicians are experienced and certified experts, who evaluate your immediate needs as well as make logical recommendations for the long-term maintenance and performance of your vehicle. We have customers AND technicians who have been with us for more than 10 years. That means whether you are one of our many long-term customers who trust us with multiple vehicles for their family or new to Mad Mike's Motorsports, your experience will be something you can share with your family and friends.</p>
        <p class="motto">We specialize in getting your vehicle back on the road quickly and safely</p>""",
    ),
)

PAGES["racing.php"] = (
    "Drag Racing, Custom Race Cars & Parts Fabrication",
    "Our core business is to build new custom race cars. Mike has over 25 years experience building race cars.",
    "Mad Mike's Motorsports builds custom race cars specific for the application,regardless of class. We will build your car exactly to that class' specifications and then some. We always look for the best for your car. We approach every job so that you get the optimum performance from your car from the moment you first use it. Our race cars are built with high quality. That means that you don't have to spend years working them out. Our goal is customer satisfaction with your car right from the beginning. You're the driver,it's important you're comfortable so we work with you to be sure we meet your expectations. We use only the best components and parts towards that goal. Your race car is totally hand-crafted,not stamped out. We build cars the old fashioned way,by approaching one job at a time and completing it as it needs to be done.",
    inner(
        "Custom Built Race Cars, Parts Fabrication, and Race Car Updates &amp; Repair",
        """        <p>Mad Mike's Motorsports builds custom race cars specific for the application, regardless of class. We will build your car exactly to that class' specifications and then some. We always look for the best for your car. We approach every job so that you get the optimum performance from your car from the moment you first use it.</p>
        <p><a href="videos.php" title="Videos">Click here to view a video from Pink's All Out 2010 in Norwalk, OH which features several vehicles that we have built &amp; raced!</a></p>
        <h2>Build New Race Cars</h2>
        <p>Our core business is to build new custom race cars. Mike has over 25 years experience building race cars. Mike says, "The design of the car is built to exceed whatever the application's requirements would be... every square inch of the car - anything that will help your car perform better than the next one." And the records and championships, that our cars win, show it.</p>
        <h2>Chassis Certification</h2>
        <p>We build full-tube chassis to NHRA and IHRA specifications 6.00, 7.50, and 8.50</p>
        <p>Our race cars are built with high quality. That means that you don't have to spend years working them out. Our goal is customer satisfaction with your car right from the beginning. You're the driver, it's important you're comfortable so we work with you to be sure we meet your expectations. We use only the best components and parts towards that goal. Your race car is totally hand-crafted, not stamped out. We build cars the old fashioned way, by approaching one job at a time and completing it as it needs to be done.</p>
        <p><em>We welcome any feedback as to anything you may want or need as I have the resources to supply and manufacture just about anything. Let us know by calling us at (330) 878-5351 or email using our <a href="contact.php" title="Contact Us">Inquiry Form</a></em>.</p>
        <h2>Part Fabrication</h2>
        <p>We build parts that you can't get anymore. We have the ability to do that. If you need a part that isn't available anymore, we can make (or repair) hard-to-get parts.</p>
        <h2>Race Car Updates and Repair</h2>
        <p>There are updates that you are required to make. We can do those updates for you. For example, one year you might be required to have a certain bar in your car. You just have to get that done. We can take care of it for you.</p>
        <div class="badge-row">
          <img src="images/NHRA.png" alt="We build NHRA Certified Chassis" title="We build NHRA Certified Chassis">
          <img src="images/IHRA.png" alt="We build IHRA Certified Chassis" title="We build IHRA Certified Chassis">
        </div>
        <p class="motto">Experts in Race Car Building &amp; Fabrication</p>""",
        RAIL_RACE,
    ),
)

PAGES["videos.php"] = (
    "Mad Mike's Motorsports. Pinky's All Out - YouTube. Videos",
    "Watch Mad Mike's Motorsports at Pink's All Out 2010 in Norwalk, OH.",
    "racing videos,pinks all out,norwalk ohio,drag racing,mad mikes motorsports",
    inner(
        "Ohio's Racing Headquarters",
        """        <div class="video-wrap">
          <iframe title="Pinks 2010 Norwalk, OH" src="https://www.youtube.com/embed/JkgNjolRTuU?rel=0" allowfullscreen></iframe>
        </div>
        <p class="motto">Ohio's Racing Headquarters</p>""",
    ),
)

SERVICES = [
    (
        "ENGINE, FUEL SYSTEMS, EMISSIONS, AND PERFORMANCE",
        [
            "Engine Performance Service (Diagnostics)",
            "Standard & Electronic Ignition Systems",
            "Fuel Injection Service & Component Analysis",
            "Emission Controls",
            "Pattern Failure Analysis",
            "Fuel Pump Service (Mechanical & Electric)",
            "Carburetor Rebuilding & Set-Up Service",
            "Emission 4-Gas Analysis",
            "Fuel Tank Replacement & Services",
            "Gas Gauge & Fuel Tank Sending Unit Service",
            "Diesel Injection Service",
            "Throttle Body Repairs & Clean and Service",
        ],
    ),
    (
        "COOLING SYSTEM SERVICE AND REPAIRS",
        [
            "Radiator Repairs & Cooling System Pressure Tests",
            "New Replacement Radiators (limited lifetime warranty)",
            "Water Pump Service",
            "Thermostats",
            "Freeze Plug (Expansion Plug) Service",
            "Cylinder Head Gasket & Cylinder Head Service",
            "Cooling System Flush",
            "Coolant Exchange Service (when flush is not needed) Using Necessary Coolant",
            "Thermostatically Controlled Circuits",
            "Electrical Fan & Motor Assemblies",
            "Cooling System Re-Hose Service (There are many hoses that do NOT get replaced because of location and availability)",
            "Electrical Repairs to Dashboard Monitoring Lights & Gauges that Affect the Operation of the Cooling System",
        ],
    ),
    (
        "ENGINE MECHANICAL REPAIR AND SERVICES",
        [
            "Engine Replacement:",
            "Engine Replacement Through Major Manufacturers such as: Jasper, OE, ACDelco, and Motorcraft.",
            "Engine Cleaning",
            "Engine Rebuild",
            "Timing Chain & Timing Belt Service",
            "Valve Work, Valve Grinding, and Cylinder Head Repairs",
            "Engine Oil Leaks: diagnose, clean, and recommended repairs",
            "Internal Gaskets",
        ],
    ),
    (
        "CHARGING AND STARTING SYSTEMS",
        [
            "Battery Service (Several different brands w/ Nationwide service & warranty)",
            "Complete Re-Wire Service",
            "Burn Damage Repairs",
            "Alternator Replacement",
            "Drive Belt Replacement",
            "Shorts & Opens that Affect Electrical Integrity",
            "Starter Assemblies, Switches, & Cables",
            "Trailer Wiring & Diagnosis",
        ],
    ),
    (
        "AIR CONDITIONING AND HEATER SERVICE",
        [
            "Heater Service (includes diagnose failure & components that are needed)",
            "Heater Core Replacement",
            "Heater Hose Service",
            "Thermostat (Mechanical & Electrical)",
            "Dash Control Components",
            "Automatic Temperature Control Systems",
            "A/C Evacuate & Recharge Service (w/ EPA Approved Equipment)",
            "Component Replacement or Repair where applicable of a failed component",
            "Evaporator, Compressor, A/C Hose, Condenser, Drier, & All Related Components",
            "We use the proper refrigerants that are designed for the vehicle. We do NOT use any blends; R-12 or R134a are the accepted standards",
        ],
    ),
    (
        "ELECTRICAL CIRCUITS, SWITCHES, AND ELECTRONICS",
        [
            "Computer Controlled Circuit Repairs",
            "Power Windows, Power Doors, Power Seats, & Power Antennas",
            "Cruise Controls",
            "Electrical Shorts",
            "Re-wiring for Harness Damage",
            "Dash Gauges & Related Switch Service",
            "Turn Signals, Flasher, & Headlight Circuits",
            "Window Wipers & Washers",
            "Radio & Related Components. We can remove & take to authorized center for repair & reinstall.",
        ],
    ),
    (
        "BRAKE SYSTEMS, AXLE SERVICE/REPLACEMENT, WHEELS, AND TIRES",
        [
            "Brake Replacement (Disc & Drum)",
            "Brake Calipers & Wheel Cylinders",
            "Master Cylinder & Brake Bleeding",
            "Power Brake Boosters",
            "Hydro-Vac Units (Hydro-Boost)",
            "ABS Diagnosis & Repair",
            "Brake Fluid Flushing",
            "Emergency Brake Repairs",
            "Machine Service (for all types of drums & rotors)",
            "On-Car Brake Lathe Service (for some applications)",
            "Wheel Bearing Replacement & Repack (when applicable)",
            "Front & Rear CV (constant velocity) Axle Service & Boot Service",
            "Differential Repairs (both front & rear trans-axle & conventional)",
            "Drive-Shaft Service",
            "Suspension Inspection & Service",
            "Wheel Alignment (front & rear)",
            "Wheel Balance (using the Latest Technology w/ Force Variation available)",
            "We carry the COOPER brand of tires, and we can supply whatever our customers request",
            "Tire Rotation Service",
            "Tire Repair",
            "Power Steering Repairs",
            "Power Steering Flush Service",
            "Customer Wheel Service",
        ],
    ),
    (
        "MAINTENANCE SERVICES AVAILABLE",
        [
            "Oil & Filter Changes",
            "Tire Rotation",
            "Wheel Balance",
            "Wheel Alignment",
            "Headlight Aiming",
            "Transmission Fluid Service",
            "Lighting (bulb replacement)",
            "Windshield Wipers",
            "Belts & Hoses",
            "Vehicle Inspection",
            "Battery Change-over & Charging",
            "Cooling System Flush & Exchange",
            "CV (constant velocity) Maintenance",
            "Engine Pressure Clean",
            "Look-up & Provide Technical Bulletins (when apply)",
            "Vehicle Value & Car Pricing Service (when shopping for another vehicle)",
            "7,500, 15k, 30k, & 60k Mile Maintenance Schedules (what is needed & what is recommended)",
        ],
    ),
    (
        "TRANSMISSION AND CLUTCH SERVICE",
        [
            "Transmission Fluid Service",
            "Automatic Transmission Internal Repairs",
            "Automatic Transmission Re-Sealing",
            "Electronically Controlled Systems",
            "Replacement Transmission Service (Jasper units w/ nationwide warranty)",
            "Automatic Transaxle Service",
            "Standard Transmission Rebuilding Service",
            "Clutch & Pressure Plate Service (Regular & Hydraulic)",
            "Hydraulic Master Cylinder & Slave Cylinder Repairs",
            "Flywheel Machining (w/repairs)",
        ],
        True,
    ),
]


def esc(s):
    return (
        s.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )


cards = []
for item in SERVICES:
    title, items, *rest = item
    lis = "\n".join(f"          <li>{esc(x)}</li>" for x in items)
    extra = ""
    if rest:
        extra = '\n          <img class="mustang" src="images/mustang.png" alt="Shop project at Mad Mike\'s Motorsports">'
    cards.append(
        f"""      <article class="card">
        <h2>{esc(title)}</h2>
        <ul>
{lis}
        </ul>{extra}
      </article>"""
    )

PAGES["services.php"] = (
    "Mad Mike's Motorsports - Services Page. Auto Repair, Racing",
    "Racing fabrication, full service automotive repair & general welding and fabrication services",
    "auto repair,racing fabrication,welding,strasburg ohio,mad mikes motorsports",
    f"""  <main id="content" class="page">
    <p class="service-lead motto" style="margin-top:0">Racing fabrication, full service automotive repair &amp; general welding and fabrication services</p>
    <div class="service-grid">
{chr(10).join(cards)}
    </div>
    <p class="cta-band motto">Call today for an appointment (330) 878-5351</p>
  </main>""",
)

gallery_links = []
for name in GALLERY:
    alt = name.rsplit(".", 1)[0]
    gallery_links.append(
        f'      <a data-lightbox href="data/images1/{name}" title="{alt}"><img src="data/thumbnails1/{name}" alt="{alt}"></a>'
    )

PAGES["gallery.php"] = (
    "Mad Mike's Photo Gallery",
    "Photo gallery of custom race cars, chassis work, and shop projects from Mad Mike's Motorsports in Strasburg, Ohio.",
    "photo gallery,race cars,drag racing,mad mikes motorsports,strasburg ohio",
    f"""  <main id="content" class="page">
    <div class="page-title">
      <h1>Photo Gallery</h1>
    </div>
    <div class="gallery-grid">
{chr(10).join(gallery_links)}
    </div>
  </main>""",
)

PAGES["contact.php"] = (
    "Mad Mike's . Ohio Drag Racing, Building & Parts Fabrication",
    "Contact Mad Mike's today for a free rate quote. Northeast Ohio's destination for Drag Racing, custom Race Car building, Automotive restoration and repair, Motorcycle racing and repair, chassis building, parts fabrication",
    "email,contact us,contact us page,mad mikes motorsports,mike renner,strasburg,ohio,ohio auto repair,ohio drag racing,custom race car,funnycar,dragster,engine,motor,service,oh",
    inner(
        "Call Today. No job too large or small!",
        """        <form class="contact-form" method="post" action="scripts/sendeail.php">
          <input type="hidden" name="ip" value="">
          <input type="hidden" name="httpref" value="">
          <input type="hidden" name="httpagent" value="">
          <label>Name <span class="req">(Required)</span>
            <input type="text" name="name" size="35">
          </label>
          <label>Phone
            <input type="text" name="phone" size="35">
          </label>
          <label>Contact Email <span class="req">(Required)</span>
            <input type="text" name="email" size="35">
          </label>
          <label>Comments / Project Details
            <textarea name="notes" rows="5"></textarea>
          </label>
          <button class="btn" type="submit">Send</button>
        </form>
        <p class="motto">Thank you for visiting Mad Mike's Motorsports</p>""",
    ),
)


def write_page(name, payload):
    if len(payload) == 5:
        title, desc, keys, main, extra = payload
    else:
        title, desc, keys, main = payload
        extra = ""
    html = shell(title, desc.replace('"', "&quot;"), keys.replace('"', "&quot;"), name, main, extra)
    (ROOT / name).write_text(html, encoding="utf-8")
    print("wrote", name, "bytes", len(html))


for name, payload in PAGES.items():
    write_page(name, payload)

import re

for name in PAGES:
    php = (ROOT / name).read_text(encoding="utf-8")
    html = re.sub(r'href="([a-z]+)\.php"', r'href="\1.html"', php)
    html_name = name.replace(".php", ".html")
    (ROOT / html_name).write_text(html, encoding="utf-8")
    print("wrote", html_name)
