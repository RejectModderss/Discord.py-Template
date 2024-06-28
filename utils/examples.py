# Examples for using Embeds from utils.

from utils import *

# This will only import the embed classes as so defined in the utils/__init__.py
# The "__all__" overwrites what all "*" imports.

# Alternatively you can also do-
# from utils import MainEmbed, SuccessEmbed, ErrorEmbed

embed = MainEmbed(title="Whatever", description="XYZ")
# Color and footer and timestamp have been added inside the class
# You can add fields and images or thumbnail like u do with normal embeds

embed.add_field(name="Field Name", value="Field Value", inline=False)
embed.set_author(name="Author Name", icon_url="Author Icon URL")
embed.set_thumbnail(url="Thumbnail URL")


embed2 = MainEmbed("I love gambling")
# Also the title argument is optional so you can make title-less embeds
# `embed2` will only have a description of "I love gambling".
