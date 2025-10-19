from app import create_app, db
from models.db_models import Festival, Book, Temple, Food

app = create_app()

with app.app_context():
    # Clear existing data to prevent duplicates
    db.session.query(Festival).delete()
    db.session.query(Book).delete()
    db.session.query(Temple).delete()
    db.session.query(Food).delete()

    # --- Seed Festivals ---
    festivals_to_add = [
        Festival(
            name="Onam",
            date="August 26 – September 5",
            description="Onam is Kerala’s grand harvest festival celebrating the legendary King Mahabali.",
            image_url="onam.jpg",
        ),
        Festival(
            name="Ganesh Visarjan",
            date="September 6",
            description="Ganesh Visarjan marks the farewell of Lord Ganesha at the end of Ganesh Chaturthi.",
            image_url="ganesh.jpg",
        ),
        Festival(
            name="Shardiya Navratri",
            date="Beginning September 22",
            description="A nine-day festival dedicated to Goddess Durga, celebrating the victory of good over evil.",
            image_url="navaratri.jpg",
        ),
    ]

    # --- Seed Books ---
    books_to_add = [
        Book(
            title="The Ramayana",
            author="Valmiki",
            religion="Hinduism",
            description="An ancient Indian epic which narrates the struggle of the divine prince Rama to rescue his wife Sita from the demon king Ravana.",
            image_url="https://sanatandharmaa.com/wp-content/uploads/2024/03/Ramayana-Book.webp",
        ),
        Book(
            title="The Mahabharata",
            author="Vyasa",
            religion="Hinduism",
            description="One of the two major Sanskrit epics of ancient India, it is a narrative of the Kurukshetra War and the fates of the Kaurava and the Pandava princes.",
            image_url="https://cdn01.sapnaonline.com/product_media/9788181334718/md_9788181334718.jpg",
        ),
        Book(
            title="The Guru Granth Sahib",
            religion="Sikhism",
            description="The central religious scripture of Sikhism, regarded by Sikhs as the final, sovereign, and eternal living Guru.",
            image_url="https://tse1.mm.bing.net/th/id/OIP.6liSXHbOGsYzt1MU7qJBlwHaE6?cb=12&rs=1&pid=ImgDetMain&o=7&rm=3",
        ),
    ]

    # --- Seed Temples ---
    temples_to_add = [
        Temple(
            name="Tirumala Venkateswara Temple",
            location="Tirupati, Andhra Pradesh",
            description="A landmark Vaishnavite temple situated in the hill town of Tirumala. It is one of the richest temples in the world.",
            image_url="https://tse4.mm.bing.net/th/id/OIP.xM0mE6JM1EtR2u_SdjgWywHaE0?cb=12&rs=1&pid=ImgDetMain&o=7&rm=3",
        ),
        Temple(
            name="Golden Temple (Harmandir Sahib)",
            location="Amritsar, Punjab",
            description="The holiest Gurdwara and the most important pilgrimage site of Sikhism.",
            image_url="https://images.pexels.com/photos/12193697/pexels-photo-12193697.jpeg?cs=srgb&dl=pexels-inder-singh-922704-12193697.jpg&fm=jpg",
        ),
        Temple(
            name="Meenakshi Amman Temple",
            location="Madurai, Tamil Nadu",
            description="A historic Hindu temple dedicated to Meenakshi, a form of Parvati, and her consort, Sundareshwar, a form of Shiva.",
            image_url="https://www.savaari.com/blog/wp-content/uploads/2022/11/Temple_de_Minakshi01.jpg",
        ),
    ]

    # --- Seed Foods ---
    foods_to_add = [
        Food(
            name="Hyderabadi Biryani",
            region="Hyderabad",
            description="A famous Indian dish made with basmati rice, spices, and goat or chicken meat.",
            image_url="https://tse1.mm.bing.net/th/id/OIP.PNjMUVWb4ic5xEMjf48u-wHaFj?cb=12&rs=1&pid=ImgDetMain&o=7&rm=3",
        ),
        Food(
            name="Masala Dosa",
            region="South India",
            description="A popular South Indian breakfast pancake made from a fermented batter of rice and lentils, served with sambar and chutney.",
            image_url="https://png.pngtree.com/thumb_back/fh260/background/20230613/pngtree-an-indian-dosa-is-sitting-on-a-plate-image_2892702.jpg",
        ),
        Food(
            name="Dhokla",
            region="Gujarat",
            description="A savoury steamed cake made from a fermented batter derived from rice and split chickpeas.",
            image_url="https://image.freepik.com/free-photo/gujarati-khaman-dhokla-made-using-chana-dal-served-with-green-chutney-selective-focus_466689-71719.jpg",
        ),
    ]

    # Add all new data to the session and commit
    db.session.add_all(festivals_to_add)
    db.session.add_all(books_to_add)
    db.session.add_all(temples_to_add)
    db.session.add_all(foods_to_add)
    db.session.commit()

    print("✅ Database has been seeded with Festivals, Books, Temples, and Foods!")
