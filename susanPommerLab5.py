###########################################################
# Course:  CS21B Python Programming: Lab #5
# Name:  Susan Pommer
#
# Description:  This program scrapes the website
# http://www.nasonline.org
# Site is downloaded and parsed to compute the
# the number of instances of select topics.
#
# This program does not capture:
#  Text which is embedded within an image
# "Mental visualization in birds" (could not solve)
#
# Note -- some small tiles in carousel are not
# tagged with the text seen on the page

# Program assumes search for a topic regardless of
# word capitalization

# File name:  susanPommerLab5.py
# Date:  February 20, 2018
###########################################################

# Import datetime module
import datetime

# Import Regression Expression
import re

# Import urllib
from urllib.request import urlopen

## ------- DEFINE MAIN PROGRAM ------- ##

def main():

    # Print today's date
    todays_date = datetime.date.today()
    print("Today's date is " + str(todays_date) + "\n")

    # Request and receive HTML document
    # Object returned is type HTTPResponse
    response = urlopen("http://www.nasonline.org")

    # Return an object of type bytes
    website_content_bytes = response.read()

    # Convert bytes to string
    website_content_string = website_content_bytes.decode()


    ## REGEX PATTERNS
    # Pattern to find paragraphs content
    pattern_p1= '\s<p>(.*)</p>'

    # Pattern to find paragraphs content of other format
    pattern_p2 = '<p><strong>(.*)</p>'

    # Pattern to find h1 headers content
    pattern_h1 = '<h1>(.*)</h1>'

    # Pattern to find h2 headers content
    pattern_h2 = '<h2><a href="\S+">(.*)</a></h2>'

    # 2nd Pattern to find h2 headers content
    pattern_h2_2 = '<h2><a href="\S+"\starget="_blank">(.*)</a></h2>'

    # Pattern to find li in class = first
    pattern_li_first = '<li class="first"><a href="\S+">(.*)</a>'

    # Pattern to find li which span two lines
    pattern_li_two_lines = '<li class="two_lines"><a href="\S+">(.*)</a>'

    # Pattern to find li in class = last
    pattern_li_last = '<li class="last"><a href="\S+">(.*)</a>'

    # Pattern to find li content with a href
    pattern_li = '<li><a href="\S+">(.*)</a>'

    # Pattern to find <a>text</a>  (Footer list headers)
    pattern_a = '<a>.*</a>'

    # Pattern to find text on small carousel tiles
    pattern_img = '<img u="thumb"\salt=(.*)'

    # Pattern to find PNAS footnote ("Current Issue: ...)
    # Cheated a little here as could not figure out how to uniquely pull this line
    pattern_footnote = '<strong>Current Issue:</strong>'

    # Pattern to find PNAS footnote 2 : "mental visualization in birds"
    # Could not get the following targeted match to work to pick up
    # pattern_footnote2 = '</strong><a href="\S+"\starget="_blank">(.*)</a>'
    # Others patterns tried:
    # pattern_footnote2 = '<a href="http://www.pnas.org/content/115/7/1541.short? \
                        # rss=1" target="_blank">(.*)</a>'
    # pattern_footnote2 = '<a href="http://www.pnas.org/content/115/7/1541.short?' \
    #                     'rss=1"\starget="_blank">(.*)</a>'


    ## Initialize list of strings less HTML tags
    strings_less_html = []

    ## REGEX TO FIND TEXT CONTENT

    # Find all footnotes of text
    footnote = re.findall(pattern_footnote, website_content_string)
    # Run each string through a function to strip html tags
    for each_p in footnote:
        master_list = add_to_master_list(each_p, strings_less_html)

    # Look for footnotes 2 of text)
    #footnote2 = re.match(pattern_footnote2, website_content_string)
    # Run each string through a function to strip html tags
    #for each_p in footnote2:
        #add_to_master_list(each_p, strings_less_html)

    # Look for paragraphs of text
    paragraphs = re.findall(pattern_p1, website_content_string)
    # Run each string through a function to strip html tags
    for each_p in paragraphs:
        master_list = add_to_master_list(each_p, strings_less_html)

    # Look for paragraphs_2 of text
    paragraphs_2 = re.findall(pattern_p2, website_content_string)
    # Run each string through a function to strip html tags
    for each_p in paragraphs_2:
        master_list = add_to_master_list(each_p, strings_less_html)

    # Look for header1 text
    header1_string = re.findall(pattern_h1, website_content_string)
    # Run each string through a function to strip html tags
    for each_p in header1_string:
        master_list = add_to_master_list(each_p, strings_less_html)

    # Look for header2 text
    header2_string = re.findall(pattern_h2, website_content_string)
    # Run each string through a function to strip html tags
    for each_p in header2_string:
        master_list = add_to_master_list(each_p, strings_less_html)

    # Look for header2_2 text
    header2_2_string = re.findall(pattern_h2_2, website_content_string)
    # Run each string through a function to strip html tags
    for each_p in header2_2_string:
        master_list = add_to_master_list(each_p, strings_less_html)

    # Look for li class = first text
    li_string_first = re.findall(pattern_li_first, website_content_string)
    # Run each string through a function to strip html tags
    for each_p in li_string_first:
        master_list = add_to_master_list(each_p, strings_less_html)

    # Look for li class = last text
    li_string_last = re.findall(pattern_li_last, website_content_string)
    # Run each string through a function to strip html tags
    for each_p in li_string_last:
        master_list = add_to_master_list(each_p, strings_less_html)

    # Look for li class = two_lines
    li_string_two_lines = re.findall(pattern_li_two_lines, website_content_string)
    # Run each string through a function to strip html tags
    for each_p in li_string_two_lines:
        master_list = add_to_master_list(each_p, strings_less_html)

    # Look for li content text
    li_string = re.findall(pattern_li, website_content_string)
    # Run each string through a function to strip html tags
    for each_p in li_string:
        master_list = add_to_master_list(each_p, strings_less_html)

    # Look for <a> text
    string_a = re.findall(pattern_a, website_content_string)
    # Run each string through a function to strip html tags
    for each_p in string_a:
        master_list = add_to_master_list(each_p, strings_less_html)

    # Look for text on small carousel images
    carousel_img_text = re.findall(pattern_img, website_content_string)
    # Run each string through a function to strip html tags
    for each_p in carousel_img_text:
        master_list = add_to_master_list(each_p, strings_less_html)


###  COUNTING OCCURANCES OF KEY WORDS

    # List of topics being tracked for marketing
    review_topics = ['research', 'climate', 'evolution', 'cultural', \
                    'leadership', 'Kavli', 'dog', 'Sackler', 'olympics']

    # Calculate number of topics in the review topic list
    number_topics = len(review_topics)

    # Loop through each topic on the list to count references
    for i in range (0, number_topics):

        # Initialize empty match list
        match_list = []

        # Convert search topic to lower case
        pattern_s = review_topics[i].lower()

        # Loop through each item on master list for matches
        for j in range (0, len(master_list)):

            # Search string
            string_to_search = master_list[j]

            # RegExp search for topic
            regexp = re.search(pattern_s, string_to_search.lower())

            # If finds topic match, add to match_list
            if (regexp == None):
                continue
            else:
                match_list = add_to_list(regexp, match_list)

        # Count number of matches
        match_count = len(match_list)

        # Print output statement per topic
        print(review_topics[i] + " appears " + str(match_count) + " times. \n")


######  FUNCTIONS #############

# Function to "cleanse" the strings
def clean_string(string):
    # Remove all remaining HTML tags from parsed strings
    stripped_htmlp = re.sub('<p>', '', string)
    stripped_htmlp2 = re.sub('</p>', '', stripped_htmlp)
    stripped_span = re.sub('<span>\S+</span>\s<a href="\S+"\starget="_blank">', '', stripped_htmlp2)
    stripped_span2 = re.sub('<span\sstyle(\S+>)', '', stripped_span)
    stripped_url = re.sub('<a href=\S+>','', stripped_span2)
    stripped_url2 = re.sub('<a href="\S+"\starget="_blank">', '', stripped_url)
    stripped_img = re.sub('<img\ssrc="\S+"\s/>', '', stripped_url2)
    stripped_strong1 = re.sub('<strong>','', stripped_img)
    stripped_strong2 = re.sub('</strong>', '', stripped_strong1)
    stripped_em = re.sub('<em>', '', stripped_strong2)
    stripped_em2 = re.sub('</em>', '', stripped_em)
    stripped_a = re.sub('<a>', '', stripped_em2)
    stripped_a2 = re.sub('</a>', '', stripped_a)
    stripped_br = re.sub('<br>', '', stripped_a2)
    stripped_br2 = re.sub('<br />', '', stripped_br)
    stripped_src = re.sub('src="\S+"\s/>', '', stripped_br2)

    # Substitution to replace &amp with &
    sub_amp = re.sub('&amp;', '&', stripped_src)

    # Substitution to remove any quotes
    removed_quotes = re.sub('"', '', sub_amp)

    # Return string stripped of all html tags
    return(removed_quotes)

# Function to append stripped strings to master list
def add_to_master_list(string, strings_less_html):
    stripped = clean_string(string)
    strings_less_html.append(stripped)
    return(strings_less_html)

# Function to append found matches to match list
def add_to_list(string, match_list):
    match_list.append(string)
    return(match_list)


# Call main function
main()

## -------------------- SAMPLE RUN --------------------------- ##
#"C:\Users\Susan Dog\venv\Scripts\python.exe" "C:/Pommer Files/CLASSES/FHC CS21B/susanPommerLab5.py"
#Today's date is 2018-02-19
#
#research appears 3 times.
#
#climate appears 2 times.
#
#evolution appears 2 times.
#
#cultural appears 4 times.
#
#leadership appears 2 times.
#
#Kavli appears 3 times.
#
#dog appears 0 times.
#
#Sackler appears 7 times.
#
#olympics appears 0 times.
#
#
#Process finished with exit code 0
## -------------------------------------------------------------##
