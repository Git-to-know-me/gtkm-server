from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 

# Placeholder data

name = "Jan"
surname = "Buduj"
username = "janbudujarch"

stat_1_name = "Number of public repos:"
stat_1_value = 4

stat_2_name = "Number of forks:"
stat_2_value = 5

stat_3_name = "Number of earned stars:"
stat_3_value = 6

# Generating profile badge

img = Image.open("gtkm/static/images/profile-badge-background.png")
draw = ImageDraw.Draw(img)

name_font = ImageFont.truetype("gtkm/static/font/Lato-Bold.ttf", 20)
username_font = ImageFont.truetype("gtkm/static/font/Lato-Bold.ttf", 14)
stats_font = ImageFont.truetype("gtkm/static/font/Lato-Bold.ttf", 12)

draw.text((120, 40),f"{name} {surname}",(255,255,255),font=name_font)
draw.text((120, 66),f"@{username}",(255,255,255),font=username_font)

draw.text((30, 120),f"{stat_1_name}",(255,255,255),font=stats_font)
draw.text((200, 120),f"{stat_1_value}",(255,255,255),font=stats_font)


draw.text((30, 160),f"{stat_2_name}",(255,255,255),font=stats_font)
draw.text((200, 160),f"{stat_2_value}",(255,255,255),font=stats_font)

draw.text((30, 200),f"{stat_3_name}",(255,255,255),font=stats_font)
draw.text((200, 200),f"{stat_3_value}",(255,255,255),font=stats_font)

# Show profile badge

img.show()