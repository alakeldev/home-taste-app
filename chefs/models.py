from django.db import models
from django.contrib.auth.models import User
from djrichtextfield.models import RichTextField
from cloudinary.models import CloudinaryField
from django.db.models.signals import post_save
from django.utils.text import slugify

# Create your models here.

GENDER = (("Female", "Female"), ("Male", "Male"), ("Not Set", "Not Set"))

REGION = (
    ("Africa", "Africa"),
    ("Asia", "Asia"),
    ("Caribbean", "Caribbean"),
    ("Central America", "Central America"),
    ("Europe", "Europe"),
    ("North America", "North America"),
    ("Oceania", "Oceania"),
    ("South America", "South America"),
)


class Profile(models.Model):
    """
    Represents profile table inside the DB
    and the fields within this model define the columns of the profile table.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(
        ("Name"),
        max_length=20,
        help_text="You can enter a different name from your username.",
    )
    image = CloudinaryField(
        "Profile Picture",
        folder="profile/",
        format="webp",
        transformation={"quality": 75},
        blank=True,
        null=True,
        help_text="Please upload your profile picture.",
    )
    email = models.EmailField(
        ("Contact Email"),
        max_length=50,
        blank=True,
        null=True,
        help_text=(
            "You can enter a different email "
            "from the one used during registration."
        ),
    )
    phone_number = models.CharField(
        ("Phone Number"),
        max_length=25,
        blank=True,
        null=True,
        help_text="Please provide your contact phone/mobile number.",
    )
    cuisine_specialization = models.CharField(
        ("Cuisine Type"),
        max_length=25,
        blank=True,
        null=True,
        help_text=(
            "Please specify one or two cuisines from your "
            "culinary expertise (e.g., Indian, Syrian, Italian)"),
    )
    Region = models.CharField(
        ("Region"),
        choices=REGION,
        default="Europe",
        help_text="Please specify your region.",
    )
    country = models.CharField(
        ("Country"),
        max_length=12,
        blank=True,
        null=True,
        help_text=(
            "Please enter your country of "
            "residence (use abbreviations if it's long)."),
    )
    city = models.CharField(
        ("City"),
        max_length=12,
        blank=True,
        null=True,
        help_text=(
            "Please enter your city of "
            "residence (use abbreviations if it's long)."),
    )
    created_on = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(blank=True, null=True)
    gender = models.CharField(
        choices=GENDER,
        help_text="Please specify your gender.",
        default="Not Set",
    )
    instructions = RichTextField(
        ("Please Share Below Your Cook Instructions/Schedules"),
        blank=True,
        null=True,
        max_length=6000,
    )
    facebook_link = models.URLField(
        ("Facebook URL"),
        blank=True,
        null=True,
        help_text="Please enter the URL of your Facebook account.",
    )
    instagram_link = models.URLField(
        ("Instagram URL"),
        blank=True,
        null=True,
        help_text="Please enter the URL of your Instagram account.",
    )
    youtube_link = models.URLField(
        ("Youtube URL"),
        blank=True,
        null=True,
        help_text="Please enter the URL of your Youtube channel.",
    )
    tiktok_link = models.URLField(
        ("Tiktok URL"),
        blank=True,
        null=True,
        help_text="Please enter the URL of your Tiktok account.",
    )
    dish1 = CloudinaryField(
        "Dish Image-1",
        folder="dishes/",
        format="webp",
        transformation={"quality": 75, "width": 600, "height": 600, "crop": "limit"},
        blank=True,
        null=True,
        help_text="Please upload a photo of your culinary masterpiece.",
    )
    dish2 = CloudinaryField(
        "Dish Image-2",
        folder="dishes/",
        format="webp",
        transformation={"quality": 75, "width": 600, "height": 600, "crop": "limit"},
        blank=True,
        null=True,
        help_text="Please upload a photo of your culinary masterpiece.",
    )
    dish3 = CloudinaryField(
        "Dish Image-3",
        folder="dishes/",
        format="webp",
        transformation={"quality": 75, "width": 600, "height": 600, "crop": "limit"},
        blank=True,
        null=True,
        help_text="Please upload a photo of your culinary masterpiece.",
    )
    dish4 = CloudinaryField(
        "Dish Image-4",
        folder="dishes/",
        format="webp",
        transformation={"quality": 75, "width": 600, "height": 600, "crop": "limit"},
        blank=True,
        null=True,
        help_text="Please upload a photo of your culinary masterpiece.",
    )
    dish5 = CloudinaryField(
        "Dish Image-5",
        folder="dishes/",
        format="webp",
        transformation={"quality": 75, "width": 600, "height": 600, "crop": "limit"},
        blank=True,
        null=True,
        help_text="Please upload a photo of your culinary masterpiece.",
    )

    def save(self, *args, **kwargs):
        """
        If the 'slug' field is not set, generate it by
        slugifying the user's username.
        """
        if not self.slug:
            self.slug = slugify(self.user.username)
        super(Profile, self).save(*args, **kwargs)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.user.username}"


def create_profile(sender, **kwargs):
    """
    Creates profile when a new user is created.
    connect create function to user model using signal post_save.
    """
    if kwargs["created"]:
        Profile.objects.create(user=kwargs["instance"])


post_save.connect(create_profile, sender=User)


class Comment(models.Model):
    """
    Represents comment table inside the DB.
    and the fields within this model define the columns of comment table.
    """

    chef = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, help_text="Please Enter Your Name.")
    email = models.EmailField(
        max_length=50, help_text="Please Enter Your Email."
    )
    comment = models.TextField(
        max_length=200, help_text="Please Enter Your Comment."
    )
    created_at = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f"Comment by {self.name} on {self.chef}"
