import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Website.settings')

import django
django.setup()


from Review.models import Building, BuildingRooms




def populate():
    
    buildings = [
        
        {"building_name": "Adam Smith Building",
         
         "building_description": """This is a building that hosts a variety of lecture halls. 
                            Not to be confused with the Adam Smith Business School and Postgraduate Hub.""",
                            
         "building_image": "building_images/adam-smith.jpg",
         "google_map": "55.873868697201004, -4.289791300542604",
         "building_instagram": "https://www.instagram.com/uofgsps?utm_source=ig_web_button_share_sheet&igsh=ZDNlZDc0MzIxNw==",
         "building_website": "https://www.gla.ac.uk/myglasgow/estates/timetabling/roomphotos/adamsmithbuilding/",},
        
        
        
        {"building_name": "Advanced Research Centre (ARC)",
         
         "building_description": """The ARC is Glasgow's Hub for civic engagement and collaborative research. 
                            Some of the projects that are being carried out here range from quantum computing and photonics to water treatment technologies.""",
                            
         "building_image": "building_images/arc.jpg",
         "google_map": "55.87175168640173, -4.296003198136083",
         "building_instagram": "https://www.instagram.com/uofg_arc?utm_source=ig_web_button_share_sheet&igsh=ZDNlZDc0MzIxNw==",
         "building_website": "https://www.gla.ac.uk/research/arc/research/",}, 
        
        
        
        {"building_name": "Adam Smith Business School & Postgraduate Hub (ASBS & PGT Hub)",
         
         "building_description": "This is the new building for the Adam Smith Business School, which offers a wide vaariety of services: from lecture theatres to research ",
         
         "building_image": "building_images/asbs-pgt.jpg",
         "google_map": "55.870848768437355, -4.295702790744707",
         "building_instagram": "https://www.instagram.com/uofgasbs?utm_source=ig_web_button_share_sheet&igsh=ZDNlZDc0MzIxNw==",
         "building_website": "https://www.gla.ac.uk/schools/business/",}, 
        
        
        
        {"building_name": "Boyd Orr Building",
         
         "building_description": """A building that is close to the main building of campus. It hosts a variety of facilities: 
                           lecture theatres, chemistry/biology labs and computing labs """,
                           
         "building_image": "building_images/boyd-orr-image.jpg",
         "google_map": "55.87362127573122, -4.2925958432801075",
         "building_instagram": "",
         "building_website": "https://www.gla.ac.uk/myglasgow/estates/timetabling/roomphotos/boydorrbuilding/#",},
        
        
        
        {"building_name": "25 Bute Gardens",
         "building_description": "A small building which features offices for staff and only one bookable room for studies (lectures etc...).",
         "building_image": "building_images/bute-gardens-25.jpg",
         "google_map": "55.87457727637361, -4.289123729378048",
         "building_instagram": "",
         "building_website": "https://www.gla.ac.uk/myglasgow/estates/timetabling/roomphotos/25butegardens/",},
        
        
        
        {"building_name": "Clarice Pears SHW Building",
         "building_description": "This building was only very recently constructed in 2022 and is the main building for the School of Wellbeing.",
         "building_image": "building_images/clarice-pears.jpg",
         "google_map": "55.87271915884349, -4.2958926097819985",
         "building_instagram": "",
         "building_website": "https://www.gla.ac.uk/myglasgow/campusdevelopment/claricepearsbuilding/#buildinginfo",},
        
        
        
        {"building_name": "Davidson Building",
         "building_description": "",
         "building_image": "building_images/davidson-building.jpg",
         "google_map": "55.87107852405623, -4.291582873555224",
         "building_instagram": "",
         "building_website": "https://www.gla.ac.uk/myglasgow/estates/timetabling/roomphotos/davidson/#",},
        
        
        
        {"building_name": "Gilmorehill Halls",
         "building_description": "",
         "building_image": "building_images/gilmorehill-halls.jpg",
         "google_map": "55.87224231744055, -4.284566934921659",
         "building_instagram": "",
         "building_website": "https://www.gla.ac.uk/myglasgow/estates/timetabling/roomphotos/gilmorehillhalls/",},
        
        
        
        {"building_name": "Graham Kerr Building",
         "building_description": "This building is home to the Zoology Museum.",
         "building_image": "building_images/graham-kerr.jpg",
         "google_map": "55.871471940234656, -4.292963219674271",
         "building_instagram": "",
         "building_website": "https://www.gla.ac.uk/myglasgow/estates/timetabling/roomphotos/grahamkerr/",},
        
        
        
        {"building_name": "Hetherington Building",
         "building_description": "This building is home to offices for staff and small lecture classes. Often this is used for languages classes.",
         "building_image": "building_images/hetherington.jpg",
         "google_map": "55.87432123401185, -4.288896017732136",
         "building_instagram": "",
         "building_website": "https://www.gla.ac.uk/myglasgow/estates/timetabling/roomphotos/hetherington/",},
        
        
        
        {"building_name": "Huntarian Art Gallery",
         "building_description": "This building hosts small lecture theatre opportunities but is mostly a fantastic opportunity to view some classic and modern artwork.",
         "building_image": "building_images/huntarian-art-gallery.jpg",
         "google_map": "55.87313523750443, -4.288886229378081",
         "building_instagram": "",
         "building_website": "https://www.gla.ac.uk/hunterian/visit/ourvenues/hunterianartgallery/",},
        
        
        
        {"building_name": "James McCune Smith Building (JMS)",
         
         "building_description": """This is a relatively new building which features a plethora of space for study and for lectures, equipped with new equipment 
                                    and direct links to floors 4 and 6 of the Boyd Orr Building.""",
                                    
         "building_image": "building_images/jms.jpg",
         "google_map": "55.87328603706041, -4.292423058213483",
         "building_instagram": "",
         "building_website": "https://www.gla.ac.uk/myglasgow/jamesmccunesmith/",},
        
        
        
        {"building_name": "James Watt South Building",
         "building_description": "This is the main building for the School of Engineering and features facilities such as nanofabrication.",
         "building_image": "building_images/james-watt.jpg",
         "google_map": "55.871227584679964, -4.28649638889682",
         "building_instagram": "https://www.instagram.com/uofgengineering?utm_source=ig_web_button_share_sheet&igsh=ZDNlZDc0MzIxNw==",
         "building_website": "https://www.gla.ac.uk/myglasgow/estates/timetabling/roomphotos/jws/",},
        
        
        
        {"building_name": "Joseph Black Building",
         "building_description": "This is home to the School of Chemsitry and is where the majority of chemistry lectures and labs take place on campus.",
         "building_image": "building_images/joseph-black.jpg",
         "google_map": "55.872162901695305, -4.293113902390606",
         "building_instagram": "https://www.instagram.com/uofgstem?utm_source=ig_web_button_share_sheet&igsh=ZDNlZDc0MzIxNw==",
         "building_website": "https://www.gla.ac.uk/myglasgow/estates/timetabling/roomphotos/josephblack/",},
        
        
        
        {"building_name": "Kelvin Building",
         "building_description": "This is home to the school of Physics and Astronomy and where the lectures for these schools are normally conducted.",
         "building_image": "building_images/kelvin.jpg",
         "google_map": "55.872012418419324, -4.291912272825005",
         "building_instagram": "https://www.instagram.com/uofgstem?utm_source=ig_web_button_share_sheet&igsh=ZDNlZDc0MzIxNw==",
         "building_website": "https://www.gla.ac.uk/schools/physics/theschool/kelvinbuilding/",},
        
        
        
        {"building_name": "Kelvin Hall",
         
         "building_description": """This building features partnerships with the University of Glasgow, Glasgow Life and the National Library of Scotland.
                                    It is home to a variety of activities both to student and the general public.""",
                                    
         "building_image": "building_images/kelvin-hall.jpg",
         "google_map": "55.86928126692657, -4.293717886795883",
         "building_instagram": "",
         "building_website": "https://kelvinhall.org.uk/",},
        
        
        
        {"building_name": "Main Building (Gilbert Scott)",
         
         "building_description": """This is the main building for the gilmore hill campus and is the most well known across the world. 
                                    It features the iconic towers and cloisters that tourists flock to snap pictures with.
                                    For the students, there are a variety of antique lecture halls that serve to a variety of schools.""",
                                    
         "building_image": "building_images/main-building.jpg",
         "google_map": "55.87159059219925, -4.288460427939213",
         "building_instagram": "",
         "building_website": "https://www.gla.ac.uk/myglasgow/estates/timetabling/roomphotos/main/",},
        
        
        
        {"building_name": "McIntye Building",
         "building_description": "This building is home to the Student's Representative Council (SRC).",
         "building_image": "building_images/src-building.jpg",
         "google_map": "55.872235482180685, -4.288808000542754",
         "building_instagram": "https://www.instagram.com/glasgowunisrc?utm_source=ig_web_button_share_sheet&igsh=ZDNlZDc0MzIxNw==",
         "building_website": "https://www.gla.ac.uk/myglasgow/estates/timetabling/roomphotos/mcintyrebuilding/",},
        
        
        
        {"building_name": "Molema Building",
         "building_description": "This building is home to the Schools of Humanities (such as Archeology, Earth Science, and Geogrpahy).",
         "building_image": "building_images/molema.jpg",
         "google_map": "55.8741578203428, -4.2927923619091715",
         "building_instagram": "https://www.instagram.com/uofghumanities?utm_source=ig_web_button_share_sheet&igsh=ZDNlZDc0MzIxNw==",
         "building_website": "https://www.gla.ac.uk/myglasgow/estates/timetabling/roomphotos/molema/",},
        
        
        
        {"building_name": "59 Oakfield Avenue",
         "building_description": "This is a small building home to offices for staff and to the School of Nursing and Healthcare.",
         "building_image": "building_images/oakfield-avenue-59.jpg",
         "google_map": "55.873661916849215, -4.285003844719701",
         "building_instagram": "",
         "building_website": "https://www.gla.ac.uk/myglasgow/estates/timetabling/roomphotos/59oakfieldavenue/",},
        
        
        
        {"building_name": "Professors' Square",
         
         "building_description": """ Professors' Square (also known as The Square) comprises 13 terraced townhouses designed by renowned architect Sir George Gilbert Scott. 
                                     The houses were originally built as accommodation for the University's professors in the 1870s, 
                                     and are now home to various college offices and teaching spaces for subjects including Law and Theology, 
                                     as well as administrative departments. """,
         
         "building_image": "building_images/professors-square.jpg",
         "google_map": "55.871572986706475, -4.290460902390643",
         "building_instagram": "",
         "building_website": "https://www.gla.ac.uk/myglasgow/estates/timetabling/roomphotos/profsquare/",},
        
        
        
        {"building_name": "Rankine Building",
         
         "building_description": """This is apart of the James Watt School of engineering and hosts the Finance office and PGR team for the school. 
                                    For students, this is the building targeting Infrastructure & Environment, and Electronics & Nanoscale Engineering.""",
                                    
         "building_image": "building_images/rankine.jpg",
         "google_map": "55.872679773293285, -4.28574130095124",
         "building_instagram": "https://www.instagram.com/uofgengineering?utm_source=ig_web_button_share_sheet&igsh=ZDNlZDc0MzIxNw==",
         "building_website": "https://www.gla.ac.uk/myglasgow/estates/timetabling/roomphotos/rankine/",},
        
        
        
        {"building_name": "Sir Alexander Stone Building",
         "building_description": "This used to be the building for the School of Modern Languages but now houses the School of Law.",
         "building_image": "building_images/alexander-stone.jpg",
         "google_map": "55.87363512139574, -4.290934558213487",
         "building_instagram": "",
         "building_website": "https://www.gla.ac.uk/myglasgow/estates/timetabling/roomphotos/sas/",},
        
        
        
        {"building_name": "Sir Alwyn Williams Building",
         "building_description": "This is the building for the School of Computing Science.",
         "building_image": "building_images/alwyn-williams.jpg",
         "google_map": "55.87401713490754, -4.292009402390506",
         "building_instagram": "",
         "building_website": "https://www.gla.ac.uk/schools/computing/contact/",},
        
        
        
        {"building_name": "Sir Charles Wilson Building",
         "building_description": "This building used to be a church and was converted into a lecture theatre as apart of the University of Glasgow.",
         "building_image": "building_images/charles-wilson.jpg",
         "google_map": "55.87280291544208, -4.283825688896789",
         "building_instagram": "",
         "building_website": "https://www.gla.ac.uk/myglasgow/estates/timetabling/roomphotos/scw/",},
        
        
        
        {"building_name": "Sir James Black Building",
         "building_description": "",
         "building_image": "building_images/james-black.jpg",
         "google_map": "55.871044124152206, -4.292786260061467",
         "building_instagram": "",
         "building_website": "https://www.gla.ac.uk/myglasgow/estates/timetabling/roomphotos/sjb/",},
        
        
        
        {"building_name": "15 Southpark Terrace",
         "building_description": "",
         "building_image": "building_images/southpark-terrace-15.jpg",
         "google_map": "55.8744112767851, -4.286518902390446",
         "building_instagram": "",
         "building_website": "https://www.gla.ac.uk/myglasgow/estates/timetabling/roomphotos/15southparkterrace/",},
        
        
        
        {"building_name": "St Andrew's Building",
         "building_description": "This is home to the School of Education, and is the building furthest away from the main campus.",
         "building_image": "building_images/st-andrews.jpg",
         "google_map": "55.871720080485105, -4.2792438907446915",
         "building_instagram": "https://www.instagram.com/uofgeducation?utm_source=ig_web_button_share_sheet&igsh=ZDNlZDc0MzIxNw==",
         "building_website": "https://www.gla.ac.uk/myglasgow/estates/timetabling/roomphotos/standrews/",},
        
        
        
        {"building_name": "Thomson Building",
         "building_description": "This houses the School of Anatomy and the Huntarian Museum of Anatomy.",
         "building_image": "building_images/thomson-building.jpg",
         "google_map": "55.87167083889537, -4.286817529378182",
         "building_instagram": "",
         "building_website": "https://www.gla.ac.uk/myglasgow/estates/timetabling/roomphotos/thomson/",},
        
        
        
        {"building_name": "University Library",
         
         "building_description": """This is the library at the University of Glasgow and is renowned for its collections of international significance. 
                                    To this date, it currently holds 2.5 million books and journals, along with access to 1.6 million e-books.
                                    It is one of the oldest and largest university libraries in Europe.""",
                                    
         "building_image": "building_images/university-library.jpg",
         "google_map": "55.8734689982542, -4.288870600542669",
         "building_instagram": "https://www.instagram.com/uofglibrary?utm_source=ig_web_button_share_sheet&igsh=ZDNlZDc0MzIxNw==",
         "building_website": "https://www.gla.ac.uk/myglasgow/library/",},
        
        
        
        {"building_name": "University Gardens",
         
         "building_description": """These buildings feature spaces and office facilities for a large number of faculties/schools of Glasgow University. 
                                    This covers subjects within the College of Arts & Humanities.""",
                                    
         "building_image": "building_images/university-gardens.jpg",
         "google_map": "55.87298812269928, -4.290612960061373",
         "building_instagram": "",
         "building_website": "https://www.gla.ac.uk/myglasgow/estates/timetabling/roomphotos/universitygardens/",},
        
        
        
        {"building_name": "Wolfson Medical School",
         "building_description": "This houses the School of Medicine.",
         "building_image": "building_images/wolfson-medical.jpg",
         "google_map": "55.8730291493358, -4.293139043280313",
         "building_instagram": "",
         "building_website": "https://www.gla.ac.uk/myglasgow/estates/timetabling/roomphotos/wolfsonmed/",},
        
    ]
        
        
       
    
    
    adam_smith_rooms = [
        
        {"room_title":"Room 702",
         "room_picture": "room_images/adam-smith-702.jpg"
        },
        
        
        {"room_title":"Room 704",
         "room_picture": "room_images/adam-smith-704.jpg"
        },
        
        
        {"room_title":"Room 706",
         "room_picture": "room_images/adam-smith-706.jpg"
        },
        
        
        {"room_title":"Room 711",
         "room_picture": "room_images/adam-smith-711.jpg"
        },
        
        {"room_title":"Room 712",
         "room_picture": "room_images/adam-smith-712.jpg"
        },
        
        
        {"room_title":"Room 717",
         "room_picture": "room_images/adam-smith-717.jpg"
        },
        
        
        {"room_title":"Room 718",
         "room_picture": "room_images/adam-smith-718.jpg"
        },
        
        
        {"room_title":"Room 901",
         "room_picture": "room_images/adam-smith-901.jpg"
        },
        
        
        {"room_title":"Room 902",
         "room_picture": "room_images/adam-smith-902.jpg"
        },
        
        
        {"room_title":"Room 903",
         "room_picture": "room_images/adam-smith-903.jpg"
        },
        
        
        {"room_title":"Room 904",
         "room_picture": "room_images/adam-smith-904.jpg"
        },
        
        
        {"room_title":"Room 912A Lab",
         "room_picture": "room_images/adam-smith-912A.jpg"
        },
        
        
        {"room_title":"Room 915",
         "room_picture": "room_images/adam-smith-915.jpg"
        },
        
        
        {"room_title":"Room 916",
         "room_picture": "room_images/adam-smith-916.jpg"
        },
        
        
        {"room_title":"Room 1101",
         "room_picture": "room_images/adam-smith-1101.jpg"
        },
        
        
        {"room_title":"Room 1102",
         "room_picture": "room_images/adam-smith-1102.jpg"
        },
        
        
        {"room_title":"Room 1103",
         "room_picture": "room_images/adam-smith-1103.jpg"
        },
        
        
        {"room_title":"Room 1104",
         "room_picture": "room_images/adam-smith-1104.jpg"
        },
        
        
        {"room_title":"Room 1105 Lab",
         "room_picture": "room_images/adam-smith-1105.jpg"
        },
        
        
        {"room_title":"Room 1113 Lab",
         "room_picture": "room_images/adam-smith-1113.jpg"
        },
        
        
        {"room_title":"Room 1115",
         "room_picture": "room_images/adam-smith-1115.jpg"
        },
        
    ]
    
    
    arc_rooms = [
        
        {"room_title": "Room 223",
         "room_picture": "room_images/arc-223.jpg"},
        
        
        {"room_title": "Room 224",
         "room_picture": "room_images/arc-224.jpg"},
        
        
        {"room_title": "Room 225",
         "room_picture": "room_images/arc-225.jpg"},
        
        
        {"room_title": "Room 242",
         "room_picture": "room_images/arc-242.jpg"},
        
        
        {"room_title": "Room 243",
         "room_picture": "room_images/arc-243.jpg"},
        
        
        {"room_title": "Room 244",
         "room_picture": "room_images/arc-244.jpg"},
        
    ]
    
    
    asbs_rooms = [
        
        {"room_title": "Room 141",
         "room_picture": "room_images/asbs-141.jpg"},
        
        
        {"room_title": "Room 142",
         "room_picture": "room_images/asbs-142.jpg"},
        
        
        {"room_title": "Room 281",
         "room_picture": "room_images/asbs-281.jpg"},
        
        
        {"room_title": "Room 381",
         "room_picture": "room_images/asbs-381.jpg"},
        
        
        {"room_title": "Room 383",
         "room_picture": "room_images/asbs-383.jpg"},
        
        
        {"room_title": "Room 386A",
         "room_picture": "room_images/asbs-386A.jpg"},
        
        
        {"room_title": "Room 386B",
         "room_picture": "room_images/asbs-386B.jpg"},
        
        
        {"room_title": "Room 487",
         "room_picture": "room_images/asbs-487.jpg"},
        
        
        {"room_title": "Room 489",
         "room_picture": "room_images/asbs-489.jpg"},
        
        
        {"room_title": "Room 492",
         "room_picture": "room_images/asbs-492.jpg"},
        
        
        {"room_title": "Room 582",
         "room_picture": "room_images/asbs-582.jpg"},
        
        
        {"room_title": "Room 587",
         "room_picture": "room_images/asbs-587.jpg"},
        
        
        {"room_title": "Room 588A",
         "room_picture": "room_images/asbs-588A.jpg"},
        
        
        {"room_title": "Room 588B",
         "room_picture": "room_images/asbs-588B.jpg"},
 
    ]
    
    
    
    boyd_orr_rooms = [
        
        {"room_title": "Room 203 (Lecture Theatre 1)",
         "room_picture": "room_images/boydorr-203.jpg"},
        
        
        {"room_title": "Room 213",
         "room_picture": "room_images/boydorr-213.jpg"},
        
        
        {"room_title": "Room 222 (Lecture Theatre 2)",
         "room_picture": "room_images/boydorr-222.jpg"},
        
        
        {"room_title": "Room 407 (Lecture Theatre A)",
         "room_picture": "room_images/boydorr-407.jpg"},
        
        
        {"room_title": "Room 409",
         "room_picture": "room_images/boydorr-409.jpg"},
        
        
        {"room_title": "Room 411",
         "room_picture": "room_images/boydorr-411.jpg"},
        
        
        {"room_title": "Room 412 (Lecture Theatre B)",
         "room_picture": "room_images/boydorr-412.jpg"},
        
        
        {"room_title": "Room 506",
         "room_picture": "room_images/boydorr-506.jpg"},
        
        
        {"room_title": "Room 507 (Lecture Theatre C)",
         "room_picture": "room_images/boydorr-507.jpg"},
        
        
        {"room_title": "Room 513 (Lecture Theatre D)",
         "room_picture": "room_images/boydorr-513.jpg"},
        
        
        {"room_title": "Room 611 (Lecture Theatre E)",
         "room_picture": "room_images/boydorr-611.jpg"},
        
        
        {"room_title": "Room 709A",
         "room_picture": "room_images/boydorr-709A.jpg"},
        
        
        {"room_title": "Room 709B",
         "room_picture": "room_images/boydorr-709B.jpg"},
        
        
        {"room_title": "Room 711",
         "room_picture": "room_images/boydorr-711.jpg"},
    ]
    
    
    bute_gardens_rooms = [
        
        {"room_title": "Room 130",
         "room_picture": "room_images/bute-gardens-130.jpg"},
        
    ]
    
    
    clarice_pears_rooms = [
        
        {"room_title": "Room 101",
         "room_picture": "room_images/clarice-pears-101.jpg"},
        
        
        {"room_title": "Room 102",
         "room_picture": "room_images/clarice-pears-102.jpg"},
        
        
        {"room_title": "Room 103A",
         "room_picture": "room_images/clarice-pears-103A.jpg"},
        
        
        {"room_title": "Room 103B",
         "room_picture": "room_images/clarice-pears-103B.jpg"},
        
    ]
    
    
    davidson_rooms = [
        
        {"room_title": "Room 208",
         "room_picture": "room_images/davidson-208.jpg"},
    ]
    
    
    
    gilmorehill_halls_rooms = [
        
        {"room_title": "Room 217A",
         "room_picture": "room_images/gilmorehill-217A.jpg"},
        
        {"room_title": "Room 217B",
         "room_picture": "room_images/gilmorehill-217B.jpg"},
    ]
    
    
    graham_kerr_rooms = [
        
        {"room_title": "Room 224",
         "room_picture": "room_images/graham-kerr-224.jpg"},
    ]
    
    
    hetherington_rooms = [
        
        {"room_title": "Room 118",
         "room_picture": "room_images/hetherington-118.jpg"},
        
        
        {"room_title": "Room 129",
         "room_picture": "room_images/hetherington-129.jpg"},
        
        
        {"room_title": "Room 130",
         "room_picture": "room_images/hetherington-130.jpg"},
        
        
        {"room_title": "Room 131",
         "room_picture": "room_images/hetherington-131.jpg"},
        
        
        {"room_title": "Room 133",
         "room_picture": "room_images/hetherington-133.jpg"},
        
        
        {"room_title": "Room 216",
         "room_picture": "room_images/hetherington-216.jpg"},
        
        
        {"room_title": "Room 317",
         "room_picture": "room_images/hetherington-317.jpg"},
    ]
    
    
    huntarian_art_gallery_rooms = [
        
        {"room_title": "Room 103",
         "room_picture": "room_images/huntarian-art-gallery-103.jpg"},
    ]
    
    
    jms_rooms = [
        
        {"room_title": "Room 407",
         "room_picture": "room_images/jms-407.jpg"},
        
        {"room_title": "Room 408",
         "room_picture": "room_images/jms-408.jpg"},
        
        
        {"room_title": "Room 429",
         "room_picture": "room_images/jms-429.jpg"},
        
        
        {"room_title": "Room 430",
         "room_picture": "room_images/jms-430.jpg"},
        
        
        {"room_title": "Room 438 (Saltire Lecture Theatre)",
         "room_picture": "room_images/jms-438.jpg"},
        
        
        {"room_title": "Room 507",
         "room_picture": "room_images/jms-507.jpg"},
        
        
        {"room_title": "Room 508",
         "room_picture": "room_images/jms-508.jpg"},
        
        
        {"room_title": "Room 548",
         "room_picture": "room_images/jms-548.jpg"},
        
        
        {"room_title": "Room 550",
         "room_picture": "room_images/jms-550.jpg"},
        
        
        {"room_title": "Room 607",
         "room_picture": "room_images/jms-607.jpg"},
        
        
        {"room_title": "Room 629",
         "room_picture": "room_images/jms-629.jpg"},
        
        
        {"room_title": "Room 630",
         "room_picture": "room_images/jms-630.jpg"},
        
        
        {"room_title": "Room 639",
         "room_picture": "room_images/jms-639.jpg"},
        
        
        {"room_title": "Room 641",
         "room_picture": "room_images/jms-641.jpg"},
        
        
        {"room_title": "Room 707",
         "room_picture": "room_images/jms-707.jpg"},
        
        
        {"room_title": "Room 733",
         "room_picture": "room_images/jms-733.jpg"},
        
        
        {"room_title": "Room 734",
         "room_picture": "room_images/jms-734.jpg"},
        
        
        {"room_title": "Room 743",
         "room_picture": "room_images/jms-743.jpg"},
        
        
        {"room_title": "Room 745",
         "room_picture": "room_images/jms-745.jpg"},
    ]
    
    
    james_watt_rooms = [
        
        {"room_title": "Room 355",
         "room_picture": "room_images/james-watt-355.jpg"},
        
        
        {"room_title": "Room 361",
         "room_picture": "room_images/james-watt-361.jpg"},
        
        
        {"room_title": "Room 375",
         "room_picture": "room_images/james-watt-375.jpg"},
        
        
        {"room_title": "Room 811",
         "room_picture": "room_images/james-watt-811.jpg"},
    ]
    
    
    joseph_black_rooms = [
        
        {"room_title": "Room A504 (Theoretical)",
         "room_picture": "room_images/joseph-black-A504.jpg"},
        
        
        {"room_title": "Room B408 (Physical)",
         "room_picture": "room_images/joseph-black-B408.jpg"},
        
        
        {"room_title": "Room B419",
         "room_picture": "room_images/joseph-black-B419.jpg"},
        
        
        {"room_title": "Room C305 (Carnegie)",
         "room_picture": "room_images/joseph-black-C305.jpg"},
        
        
        {"room_title": "Room C407 (Agricultural)",
         "room_picture": "room_images/joseph-black-C407.jpg"},
    ]
    
    
    kelvin_rooms = [
        
        {"room_title": "Room 222",
         "room_picture": "room_images/kelvin-222.jpg"},
        
        
        {"room_title": "Room 257",
         "room_picture": "room_images/kelvin-257.jpg"},
        
        
        {"room_title": "Room 312",
         "room_picture": "room_images/kelvin-312.jpg"},
    ]
    
    
    kelvin_hall_rooms = [
        
        {"room_title": "Room G53 (Seminar Room 2)",
         "room_picture": "room_images/kelvin-hall-G53.jpg"},
        
        
        {"room_title": "Room G56 (Seminar Room 1)",
         "room_picture": "room_images/kelvin-hall-G56.jpg"},
         
         
        {"room_title": "Room G59",
         "room_picture": "room_images/kelvin-hall-G59.jpg"},
          
          
        {"room_title": "Foyer",
         "room_picture": "room_images/kelvin-hall-Foyer.jpg"},
    ]
    
    
    main_building_rooms = [
        
        {"room_title": "Room 132",
         "room_picture": "room_images/main-132.jpg"},
        
        
        {"room_title": "Room 134",
         "room_picture": "room_images/main-134.jpg"},
        
        
        {"room_title": "Room 219 (Robing Room)",
         "room_picture": "room_images/main-219.jpg"},
        
        
        {"room_title": "Room 220A (Hunter Halls West)",
         "room_picture": "room_images/main-220A.jpg"},
        
        
        {"room_title": "Room 220B (Hunter Halls East)",
         "room_picture": "room_images/main-220B.jpg"},
        
        
        {"room_title": "Room 226 (East Quad Lecture Theatre)",
         "room_picture": "room_images/main-226.jpg"},
        
        
        {"room_title": "Room 250",
         "room_picture": "room_images/main-250.jpg"},
        
        
        {"room_title": "Room 251",
         "room_picture": "room_images/main-251.jpg"},
        
        
        {"room_title": "Room 253",
         "room_picture": "room_images/main-253.jpg"},
        
        
        {"room_title": "Room 255 (Humanity Lecture Theatre)",
         "room_picture": "room_images/main-255.jpg"},
        
        
        {"room_title": "Room 256 (Fore Hall)",
         "room_picture": "room_images/main-256.jpg"},
        
        
        {"room_title": "Room 355",
         "room_picture": "room_images/main-355.jpg"},
        
        
        {"room_title": "Room 356",
         "room_picture": "room_images/main-356.jpg"},
        
        
        {"room_title": "Room 358",
         "room_picture": "room_images/main-358.jpg"},
        
        
        {"room_title": "Room 413 (Kelvin Gallery)",
         "room_picture": "room_images/main-413.jpg"},
        
        
        {"room_title": "Room 420 (Bute Hall)",
         "room_picture": "room_images/main-420.jpg"},
        
        
        {"room_title": "Room 456 (Turnbull Room)",
         "room_picture": "room_images/main-456.jpg"},
        
        
        {"room_title": "Room 458 (Melville Room)",
         "room_picture": "room_images/main-458.jpg"},
        
        
        {"room_title": "Room 460 (Carnegie Room)",
         "room_picture": "room_images/main-460.jpg"},
        
        
        {"room_title": "Room 461 (Senate Room)",
         "room_picture": "room_images/main-461.jpg"},
        
        
        {"room_title": "Room 466",
         "room_picture": "room_images/main-466.jpg"},
        
        
    ]
    
    
    mcintryre_rooms = [
        
        {"room_title": "Room 201",
         "room_picture": "room_images/mcintyre-201.jpg"},
        
        {"room_title": "Room 208",
         "room_picture": "room_images/mcintyre-208.jpg"},
    ]
    
    
    molema_rooms = [
        
        {"room_title": "Room 109",
         "room_picture": "room_images/molema-109.jpg"},
    ]


    oakfield_avenue_59_rooms = [
        
        {"room_title": "Room 302",
         "room_picture": "room_images/oakfield-avenue-59-302.jpg"},
    ]
    
    
    professors_square_rooms = [
        
        {"room_title": "Room 131",
         "room_picture": "room_images/prof-sqr-131.jpg"},
        
        
        {"room_title": "Room 330 (Gloag Lecture Theatre)",
         "room_picture": "room_images/prof-sqr-330.jpg"},
        
        
        {"room_title": "Room 230",
         "room_picture": "room_images/prof-sqr-230.jpg"},
        
        
        {"room_title": "Room 329 (Walker)",
         "room_picture": "room_images/prof-sqr-329.jpg"},
        
        
        {"room_title": "Room 227",
         "room_picture": "room_images/prof-sqr-227.jpg"},
        
        
        {"room_title": "Room 324 (Cosgrove)",
         "room_picture": "room_images/prof-sqr-324.jpg"},
        
        
        {"room_title": "Room 221",
         "room_picture": "room_images/prof-sqr-221.jpg"},
        
        
        {"room_title": "Room 222",
         "room_picture": "room_images/prof-sqr-222.jpg"},
    ]
    
    
    rankine_rooms = [
        
        {"room_title": "Room 106",
         "room_picture": "room_images/rankine-106.jpg"},
        
        
        {"room_title": "Room 107",
         "room_picture": "room_images/rankine-107.jpg"},
        
        
        {"room_title": "Room 108",
         "room_picture": "room_images/rankine-108.jpg"},
        
        
        {"room_title": "Room 408 (Alistair Frame Lecture Theatre)",
         "room_picture": "room_images/rankine-408.jpg"},
    ]
    
    
    alexander_stone_rooms = [
        
        {"room_title": "Room 204",
         "room_picture": "room_images/alexander-stone-204.jpg"},
        
        
        {"room_title": "Room 206",
         "room_picture": "room_images/alexander-stone-206.jpg"},
        
        
        {"room_title": "Room 208",
         "room_picture": "room_images/alexander-stone-208.jpg"},
        
        
        {"room_title": "Room 210",
         "room_picture": "room_images/alexander-stone-210.jpg"},
        
        
        {"room_title": "Room 212A",
         "room_picture": "room_images/alexander-stone-212A.jpg"},
        
        
        {"room_title": "Room 212B",
         "room_picture": "room_images/alexander-stone-212B.jpg"},
        
        
        {"room_title": "Room 213",
         "room_picture": "room_images/alexander-stone-213.jpg"},
        
        
        {"room_title": "Room 214A",
         "room_picture": "room_images/alexander-stone-214A.jpg"},
        
        
        {"room_title": "Room 214B",
         "room_picture": "room_images/alexander-stone-214B.jpg"},
        
        
        {"room_title": "Room 302B",
         "room_picture": "room_images/alexander-stone-302B.jpg"},
        
        
        {"room_title": "Room 303",
         "room_picture": "room_images/alexander-stone-303.jpg"},
        
        
        {"room_title": "Room 307",
         "room_picture": "room_images/alexander-stone-307.jpg"},
        
        
        {"room_title": "Room 309",
         "room_picture": "room_images/alexander-stone-309.jpg"},
        
        
        {"room_title": "Room 313",
         "room_picture": "room_images/alexander-stone-313.jpg"},
        
        
        {"room_title": "Room 316",
         "room_picture": "room_images/alexander-stone-316.jpg"},
        
        
        {"room_title": "Room 327",
         "room_picture": "room_images/alexander-stone-327.jpg"},
        
        
        {"room_title": "Room 328",
         "room_picture": "room_images/alexander-stone-328.jpg"},
        
        
        {"room_title": "Room 329",
         "room_picture": "room_images/alexander-stone-329.jpg"},
        
        
        {"room_title": "Room 403",
         "room_picture": "room_images/alexander-stone-403.jpg"},
        
        
        {"room_title": "Room 404",
         "room_picture": "room_images/alexander-stone-404.jpg"},
        
        
        {"room_title": "Room 409",
         "room_picture": "room_images/alexander-stone-409.jpg"},
    ]
    
    
    charles_wilson_rooms = [
        
        {"room_title": "Room 101A",
         "room_picture": "room_images/charles-wilson-101A.jpg"},
        
        
        {"room_title": "Room 101B",
         "room_picture": "room_images/charles-wilson-101B.jpg"},
        
        
        {"room_title": "Room 201",
         "room_picture": "room_images/charles-wilson-201.jpg"},
        
        
        {"room_title": "Foyer",
         "room_picture": "room_images/charles-wilson-foyer.jpg"},
    ]
    
    
    james_black_rooms = [
        
        {"room_title": "Room 222",
         "room_picture": "room_images/james-black-222.jpg"},
    ]
    
    
    southpark_terrace_15 = [
        
        {"room_title": "Room 301",
         "room_picture": "room_images/southpark-terrace-15-301.jpg"},
    ]
    
    
    st_andrews_rooms = [
        
        {"room_title": "Room 101",
         "room_picture": "room_images/st-andrews-101.jpg"},
        
        
        {"room_title": "Room 102",
         "room_picture": "room_images/st-andrews-102.jpg"},
        
        
        {"room_title": "Room 157 (Gymnasium)",
         "room_picture": "room_images/st-andrews-157.jpg"},
        
        
        {"room_title": "Room 201",
         "room_picture": "room_images/st-andrews-201.jpg"},
        
        
        {"room_title": "Room 202",
         "room_picture": "room_images/st-andrews-202.jpg"},
        
        
        {"room_title": "Room 213",
         "room_picture": "room_images/st-andrews-213.jpg"},
        
        
        {"room_title": "Room 218",
         "room_picture": "room_images/st-andrews-218.jpg"},
        
        
        {"room_title": "Room 221",
         "room_picture": "room_images/st-andrews-221.jpg"},
        
        
        {"room_title": "Room 224",
         "room_picture": "room_images/st-andrews-224.jpg"},
        
        
        {"room_title": "Room 227",
         "room_picture": "room_images/st-andrews-227.jpg"},
        
        
        {"room_title": "Room 230",
         "room_picture": "room_images/st-andrews-230.jpg"},
        
        
        {"room_title": "Room 234",
         "room_picture": "room_images/st-andrews-234.jpg"},
        
        
        {"room_title": "Room 237A",
         "room_picture": "room_images/st-andrews-237A.jpg"},
        
        
        {"room_title": "Room 237B",
         "room_picture": "room_images/st-andrews-237B.jpg"},
        
        
        {"room_title": "Room 257",
         "room_picture": "room_images/st-andrews-257.jpg"},
        
        
        {"room_title": "Room 337",
         "room_picture": "room_images/st-andrews-337.jpg"},
        
        
        {"room_title": "Room 338",
         "room_picture": "room_images/st-andrews-338.jpg"},
        
        
        {"room_title": "Room 345",
         "room_picture": "room_images/st-andrews-345.jpg"},
        
        
        {"room_title": "Room 347 (Teaching Lab)",
         "room_picture": "room_images/st-andrews-347.jpg"},
        
        
        {"room_title": "Room 352 (Teaching Lab)",
         "room_picture": "room_images/st-andrews-352.jpg"},
        
        
        {"room_title": "Room 357 (IT Lab)",
         "room_picture": "room_images/st-andrews-357.jpg"},
        
        
        {"room_title": "Room 368",
         "room_picture": "room_images/st-andrews-368.jpg"},
        
        
        {"room_title": "Room 432",
         "room_picture": "room_images/st-andrews-432.jpg"},
        
        
        {"room_title": "Room 433AB",
         "room_picture": "room_images/st-andrews-433AB.jpg"},
        
        
        {"room_title": "Room 435",
         "room_picture": "room_images/st-andrews-435.jpg"},
        
        
        {"room_title": "Room 518",
         "room_picture": "room_images/st-andrews-518.jpg"},
        
        
        {"room_title": "Room 519",
         "room_picture": "room_images/st-andrews-519.jpg"},
        
        
        {"room_title": "Room 559B",
         "room_picture": "room_images/st-andrews-559B.jpg"},
        
    ]
    
    
    thomson_rooms = [
        
        {"room_title": "Room 236",
         "room_picture": "room_images/thomson-236.jpg"},
    ]
    
    
    university_gardens_rooms = [
        
        {"room_title": "Room 208",
         "room_picture": "room_images/university-gardens-208.jpg"},
        
        
        {"room_title": "Room 209",
         "room_picture": "room_images/university-gardens-209.jpg"},
        
        
        {"room_title": "Room 202",
         "room_picture": "room_images/university-gardens-202.jpg"},
        
        
        {"room_title": "Room 101 (4 University Gardens)",
         "room_picture": "room_images/university-gardens-101A.jpg"},
        
        
        {"room_title": "Room 101 (7 University Gardens)",
         "room_picture": "room_images/university-gardens-101B.jpg"},
        
        
        {"room_title": "Room 206",
         "room_picture": "room_images/university-gardens-206.jpg"},
        
        
        {"room_title": "Room 203",
         "room_picture": "room_images/university-gardens-203.jpg"},
        
        {"room_title": "Room 201 (George Service House)",
         "room_picture": "room_images/university-gardens-201.jpg"},
        
        
        {"room_title": "Room 101 (12 University Gardens)",
         "room_picture": "room_images/university-gardens-101C.jpg"},
    ]
    
    
    wolfson_medical_rooms = [
        
        {"room_title": "Room 248 (Seminar Room 3 - Gannochy)",
         "room_picture": "room_images/wolfson-medical-248.jpg"},
        
        
        {"room_title": "Room 253 (Seminar Room 1 - Yudowitz)",
         "room_picture": "room_images/wolfson-medical-253.jpg"},
        
        
        {"room_title": "Room 257 (Hugh Fraser)",
         "room_picture": "room_images/wolfson-medical-257.jpg"},
        
        
        {"room_title": "Room 331",
         "room_picture": "room_images/wolfson-medical-331.jpg"},
        
        
        {"room_title": "Room 332",
         "room_picture": "room_images/wolfson-medical-332.jpg"},
        
        
        {"room_title": "Room 333",
         "room_picture": "room_images/wolfson-medical-333.jpg"},
        
        
        {"room_title": "Room 343",
         "room_picture": "room_images/wolfson-medical-343.jpg"},
        
        
        {"room_title": "Room 344",
         "room_picture": "room_images/wolfson-medical-344.jpg"},
        
        
        {"room_title": "Room 345",
         "room_picture": "room_images/wolfson-medical-345.jpg"},
        
        
        {"room_title": "Room 346",
         "room_picture": "room_images/wolfson-medical-346.jpg"},
        
        
        {"room_title": "Room 347",
         "room_picture": "room_images/wolfson-medical-347.jpg"},
        
        
        {"room_title": "Room 348",
         "room_picture": "room_images/wolfson-medical-348.jpg"},
        
        
        {"room_title": "Room 349",
         "room_picture": "room_images/wolfson-medical-349.jpg"},
        
        
        {"room_title": "Room 350",
         "room_picture": "room_images/wolfson-medical-350.jpg"},
        
        
        {"room_title": "Atrium",
         "room_picture": "/room_images/wolfson-medical-atrium.jpg"},
    ]
    
    
    buildings_with_rooms = {
        
        "Adam Smith Building": adam_smith_rooms,
        "Advanced Research Centre (ARC)": arc_rooms,
        "Adam Smith Business School & Postgraduate Hub (ASBS & PGT Hub)": asbs_rooms,
        "Boyd Orr Building": boyd_orr_rooms,
        "25 Bute Gardens": bute_gardens_rooms,
        "Clarice Pears SHW Building": clarice_pears_rooms,
        "Davidson Building": davidson_rooms,
        "GilmoreHill Halls": gilmorehill_halls_rooms,
        "Graham Kerr Building": graham_kerr_rooms,
        "Hetherington Building":hetherington_rooms,
        "Huntarian Art Gallery": huntarian_art_gallery_rooms,
        "James McCune Smith Building (JMS)":jms_rooms,
        "James Watt South Building": james_watt_rooms,
        "Joseph Black Building": joseph_black_rooms,
        "Kelvin Building": kelvin_rooms,
        "Kelvin Hall": kelvin_hall_rooms,
        "Main Building (Gilbert Scott)": main_building_rooms,
        "McIntyre Building": mcintryre_rooms,
        "Molema Building": molema_rooms,
        "59 Oakfield Avenue": oakfield_avenue_59_rooms,
        "Professors' Square": professors_square_rooms,
        "Rankine Building": rankine_rooms,
        "Sir Alexander Stone Building": alexander_stone_rooms,
        "Sir Alwyn Williams Building": [],
        "Sir Charles Wilson Building": charles_wilson_rooms,
        "Sir James Black Building": james_black_rooms,
        "15 Southpark Terrace": southpark_terrace_15,
        "St Andrew's Building": st_andrews_rooms,
        "Thomson Building": thomson_rooms,
        "University Library": [],
        "University Gardens": university_gardens_rooms,
        "Wolfson Medical School": wolfson_medical_rooms
        
    }
    
    
    for build, rooms in buildings_with_rooms.items():
        
        for item in buildings:
            if item["building_name"] == build:
                
                b = add_building(build,
                                 item["building_description"],
                                 item["building_image"],
                                 item["google_map"],
                                 item["building_instagram"],
                                 item["building_website"],)
                
        
        for item in rooms:
        
            r = add_room(b, item["room_title"], item["room_picture"])
        
        
                
        
    
    
def add_building(name, description, image, google_map, instagram, website, views = 0, likes = 0):
        
    b = Building.objects.get_or_create(building_name = name)[0]
    
    b.building_description = description
    b.building_image = image
    b.google_map = google_map
    b.building_instagram = instagram
    b.building_website = website
    b.building_likes = likes
    b.building_views = views
        
    b.save()
        
    return b
    
    
def add_room(building, title, picture, views = 0, likes = 0):
        
    r = BuildingRooms.objects.get_or_create(building = building, 
                                            room_title = title)[0]
    
    r.room_picture = picture
    r.room_views = views
    r.room_likes = likes
        
    r.save()
        
    return r



if __name__ == '__main__':
    
    print("Starting Reveiw population script...")
    populate()