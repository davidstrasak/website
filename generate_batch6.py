import re
import os

content = """
22.01.2024

<a href="https://www.goodreads.com/book/show/25887246-the-witcher-vol-2" style="float: left; padding-right: 20px"><img border="0" alt="The Witcher, Vol. 2: Fox Children" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1554458251l/25887246._SX98_.jpg" /></a><a href="https://www.goodreads.com/book/show/25887246-the-witcher-vol-2">The Witcher, Vol. 2: Fox Children</a> by <a href="https://www.goodreads.com/author/show/440975.Paul_Tobin">Paul Tobin</a><br/>
My rating: <a href="https://www.goodreads.com/review/show/5775258974">4 of 5 stars</a><br /><br />
A nice read with interesting main characters and a nice plot. I liked the character of the dwarf.<br />Unfortunately the main villain seemed a bit lacking and I didn't really get the final twist, but other than that it was fun to read.
<br/><br/>
<a href="https://www.goodreads.com/review/list/163394279-david-stra-k">View all my reviews</a>


04.03.2023

<a href="https://www.goodreads.com/book/show/37903770-norse-mythology" style="float: left; padding-right: 20px"><img border="0" alt="Norse Mythology" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1516128292l/37903770._SX98_.jpg" /></a><a href="https://www.goodreads.com/book/show/37903770-norse-mythology">Norse Mythology</a> by <a href="https://www.goodreads.com/author/show/1221698.Neil_Gaiman">Neil Gaiman</a><br/>
My rating: <a href="https://www.goodreads.com/review/show/5390217562">5 of 5 stars</a><br /><br />
Stories of the Norse gods, but it's put into an entertaining concept and it's written like a great book.<br />I love that there are a lot of the stories - that way you really learn a lot from different aspects of the culture.
<br/><br/>
<a href="https://www.goodreads.com/review/list/163394279-david-stra-k">View all my reviews</a>


14.01.2024

<a href="https://www.goodreads.com/book/show/36195248-critical-role" style="float: left; padding-right: 20px"><img border="0" alt="Critical Role: Vox Machina Origins Volume I" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1526604430l/36195248._SX98_.jpg" /></a><a href="https://www.goodreads.com/book/show/36195248-critical-role">Critical Role: Vox Machina Origins Volume I</a> by <a href="https://www.goodreads.com/author/show/15587365.Matthew_Mercer">Matthew Mercer</a><br/>
My rating: <a href="https://www.goodreads.com/review/show/6078235588">5 of 5 stars</a><br /><br />
A nice and funny comic that isn't too long, reads well and is overall interesting. It sets up the characters well and shows us their first story.<br />Made me interested for the second issue, so that's a plus :D.<br />And as a bonus it has enemy sheets for the big bad guys for dnd 5e, so it's cool that I could use these characters for my own dnd campaign if I wanted.
<br/><br/>
<a href="https://www.goodreads.com/review/list/163394279-david-stra-k">View all my reviews</a>


26.07.2024

<a href="https://www.goodreads.com/book/show/42792176-the-necronomicon-gamebook" style="float: left; padding-right: 20px"><img border="0" alt="The Necronomicon Gamebook: Dagon" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1542236904l/42792176._SX98_.jpg" /></a><a href="https://www.goodreads.com/book/show/42792176-the-necronomicon-gamebook">The Necronomicon Gamebook: Dagon</a> by <a href="https://www.goodreads.com/author/show/6535743.Valentino_Sergi">Valentino Sergi</a><br/>
My rating: <a href="https://www.goodreads.com/review/show/6703415288">5 of 5 stars</a><br /><br />
A very fun gamebook!<br /><br />Most gamebooks I've read did the things where they send you to run a bunch of errands in order to get to the final boss and if you forget one thing it's over. This gamebook here does none of that!<br /><br />The gamebook is more like a non linear story, where you could get to the final boss after like 10 pages, but you will probably die - it's a gamebook where if you do all the good decisions, you will be able to finish it in one or two tries.<br /><br />In my opinion that's awesome and that's how gamebooks should be!<br /><br />In addition to that the concepts were cool (obtaining the necklace is very cool), and after a while I understood the story - even though it's written pretty ambiguously. That goes for most of these Lovcraftian books though and it's a part of the aesthetic. <br /><br />Overall 5/5. It's a quick gamebook and it was a lot of fun!
<br/><br/>
<a href="https://www.goodreads.com/review/list/163394279-david-stra-k">View all my reviews</a>


26.12.2023

<a href="https://www.goodreads.com/book/show/44363173-critical-role" style="float: left; padding-right: 20px"><img border="0" alt="Critical Role: Vox Machina Origins Volume II" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1571075067l/44363173._SX98_.jpg" /></a><a href="https://www.goodreads.com/book/show/44363173-critical-role">Critical Role: Vox Machina Origins Volume II</a> by <a href="https://www.goodreads.com/author/show/15587365.Matthew_Mercer">Matthew Mercer</a><br/>
<br /><br />

<br/><br/>
<a href="https://www.goodreads.com/review/list/163394279-david-stra-k">View all my reviews</a>


09.04.2024

<a href="https://www.goodreads.com/book/show/52160928-fangs-of-the-rustwood" style="float: left; padding-right: 20px"><img border="0" alt="Fangs of the Rustwood (Warhammer Age of Sigmar)" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1566212081l/52160928._SX98_SY160_.jpg" /></a><a href="https://www.goodreads.com/book/show/52160928-fangs-of-the-rustwood">Fangs of the Rustwood</a> by <a href="https://www.goodreads.com/author/show/6559241.Evan_Dicken">Evan Dicken</a><br/>
My rating: <a href="https://www.goodreads.com/review/show/6414206422">3 of 5 stars</a><br /><br />

<br/><br/>
<a href="https://www.goodreads.com/review/list/163394279-david-stra-k">View all my reviews</a>


09.04.2024

<a href="https://www.goodreads.com/book/show/48611611-a-tithe-of-bone" style="float: left; padding-right: 20px"><img border="0" alt="A Tithe of Bone (Warhammer Age of Sigmar)" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1572262103l/48611611._SX98_.jpg" /></a><a href="https://www.goodreads.com/book/show/48611611-a-tithe-of-bone">A Tithe of Bone</a> by <a href="https://www.goodreads.com/author/show/7035308.Michael_R_Fletcher">Michael R. Fletcher</a><br/>
My rating: <a href="https://www.goodreads.com/review/show/6415516709">5 of 5 stars</a><br /><br />
An amazing short story that really kept me excited and interested. And honestly, I love the bonereapers. I love that they have something in their heads and they have a personality, which is revealed. And even so during this it still made sense.
<br/><br/>
<a href="https://www.goodreads.com/review/list/163394279-david-stra-k">View all my reviews</a>


28.03.2024

<a href="https://www.goodreads.com/book/show/49085628-reflections-in-steel" style="float: left; padding-right: 20px"><img border="0" alt="Reflections in Steel (Black Library Advent Calendar 2019 #3)" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1575395929l/49085628._SX98_.jpg" /></a><a href="https://www.goodreads.com/book/show/49085628-reflections-in-steel">Reflections in Steel</a> by <a href="https://www.goodreads.com/author/show/22087105.C_L_Werner">C.L.   Werner</a><br/>
My rating: <a href="https://www.goodreads.com/review/show/6382528044">4 of 5 stars</a><br /><br />
An interesting short story about the khorne marauder warriors with a really cool overall direction of the story.
<br/><br/>
<a href="https://www.goodreads.com/review/list/163394279-david-stra-k">View all my reviews</a>


09.04.2024

<a href="https://www.goodreads.com/book/show/49127226-strong-bones" style="float: left; padding-right: 20px"><img border="0" alt="Strong Bones (Black Library Advent Calendar 2019 #8)" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1575810298l/49127226._SX98_.jpg" /></a><a href="https://www.goodreads.com/book/show/49127226-strong-bones">Strong Bones</a> by <a href="https://www.goodreads.com/author/show/7035308.Michael_R_Fletcher">Michael R. Fletcher</a><br/>
My rating: <a href="https://www.goodreads.com/review/show/6414205845">5 of 5 stars</a><br /><br />
Top Tier short story.
<br/><br/>
<a href="https://www.goodreads.com/review/list/163394279-david-stra-k">View all my reviews</a>


04.03.2023

<a href="https://www.goodreads.com/book/show/50259247-cyberpunk-odrodzenie" style="float: left; padding-right: 20px"><img border="0" alt="Cyberpunk. Odrodzenie" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1580377071l/50259247._SX98_.jpg" /></a><a href="https://www.goodreads.com/book/show/50259247-cyberpunk-odrodzenie">Cyberpunk. Odrodzenie</a> by <a href="https://www.goodreads.com/author/show/955973.Andrzej_Ziemia_ski">Andrzej Ziemiański</a><br/>
My rating: <a href="https://www.goodreads.com/review/show/5390214278">4 of 5 stars</a><br /><br />

<br/><br/>
<a href="https://www.goodreads.com/review/list/163394279-david-stra-k">View all my reviews</a>


24.2.2024

<a href="https://www.goodreads.com/book/show/56653392-the-ultimate-rpg-game-master-s-worldbuilding-guide" style="float: left; padding-right: 20px"><img border="0" alt="The Ultimate RPG Game Master's Worldbuilding Guide: Prompts and Activities to Create and Customize Your Own Game World (Ultimate Role Playing Game Series)" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1610515391l/56653392._SX98_.jpg" /></a><a href="https://www.goodreads.com/book/show/56653392-the-ultimate-rpg-game-master-s-worldbuilding-guide">The Ultimate RPG Game Master's Worldbuilding Guide: Prompts and Activities to Create and Customize Your Own Game World</a> by <a href="https://www.goodreads.com/author/show/17977620.James_D_Amato">James D’Amato</a><br/>
My rating: <a href="https://www.goodreads.com/review/show/5914136269">1 of 5 stars</a><br /><br />
I've got to say, if you are looking for a book that teaches you world building, this is not the book for you.<br />The book has prompts - only prompts. Lots of them. They are great, but they take up a lot of space. Every prompt has tons of possible outcomes written, so every topic takes up 5 pages of this book.<br />Sadly because of that this means that the book does not cover so many topics. In addition to that the book has 5 subtopics that may not be relevant to the world you are trying to build (so if you are building a cyberpunk world, only two of 5 sections are relevant, which is suddenly just 40% of the book).<br />It is basically just giving you points to start from, but none of them are particularly good, so mostly I was just reading through all the possible prompts to hope to find one that was good.<br /><br />I don't think I will use this book again. <br />If you want to learn how to worldbuild, there are better books out there. My personal recommendation would be ICRPG rules and if you want world building prompts, use AI - it will give you more for free.
<br/><br/>
<a href="https://www.goodreads.com/review/list/163394279-david-stra-k">View all my reviews</a>
"""

entries = re.split(r'(?=\n\d{1,2}\.\d{1,2}\.\d{4}\n)', '\n' + content)
blocks = [b.strip() for b in entries if b.strip()]

for block in blocks:
    lines = block.split('\n', 1)
    date_str = lines[0].strip()
    html_content = lines[1].strip() if len(lines) > 1 else ""
    
    title_match = re.search(r'<a href="[^"]*">([^<]+)</a> by', html_content)
    if not title_match: continue
    title = title_match.group(1)
    
    author_match = re.search(r'by <a href="[^"]*">([^<]+)</a>', html_content)
    author = author_match.group(1) if author_match else ""
    author = " ".join(author.split())
    
    rating_match = re.search(r'(\d+) of 5 stars', html_content)
    rating = int(rating_match.group(1)) if rating_match else 0
    
    img_match = re.search(r'src="([^"]+)"', html_content)
    if not img_match: continue
    img_url = img_match.group(1)
    
    img_url = re.sub(r'_[SXY]\w+_', '_SY475_', img_url)
    html_content = re.sub(r'_[SXY]\w+_', '_SY475_', html_content)
    
    parts = date_str.split('.')
    day = parts[0].zfill(2)
    month = parts[1].zfill(2)
    year = parts[2]
    iso_date = f"{year}-{month}-{day}T12:00:00+00:00"
    
    filename = title.lower()
    filename = re.sub(r'[^a-z0-9\s-]', '', filename)
    filename = re.sub(r'[\s-]+', '_', filename) + '.md'
    
    tags = '["book", "review"]'
    if "warhammer" in filename or "sisters_of_battle" in filename or "fangs_of_the_rustwood" in filename or "tithe_of_bone" in filename or "reflections_in_steel" in filename or "strong_bones" in filename:
        tags = '["book", "review", "warhammer", "sci-fi", "fantasy"]'
    if "cyberpunk" in filename:
        tags = '["book", "review", "cyberpunk", "sci-fi"]'
    if "necronomicon" in filename or "lovecraft" in html_content.lower():
        tags = '["book", "review", "horror", "gamebook"]'
    if "critical_role" in filename or "rpg" in filename:
        tags = '["book", "review", "fantasy", "rpg"]'
        
    md_content = f"""+++
date = '{iso_date}'
title = '{title}'
author = '{author}'
rating = {rating}
cover_image = '{img_url}'
tags = {tags}
+++
{html_content}
"""
    
    filepath = os.path.join('content/book', filename)
    with open(filepath, 'w', encoding='utf-8') as out:
        out.write(md_content)
    print(f"Created {filepath}")

