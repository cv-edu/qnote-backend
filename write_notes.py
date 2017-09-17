# Takes note information and creates a class directory and stores notes in .txt files.
# @param: clss, date, title, body
# @date_created: 9/17/17
import os
import upload_image
import categorize


# Using upload_image and categorize tools to convert notes to separate String variables.
def write(contents):
    clss = categorize.class_text(contents["class"])
    date = categorize.date_text(contents["date"])
    title = categorize.title_text(contents["name"])
    body = categorize.body_text(contents["body"])

    crt_class(clss)
    write_txt(clss, date, title, body)

# Checks if class folder exists and makes new directory if it doesn't.
def crt_class(clss):
    if not os.path.exists(clss):
        os.makedirs(clss)

# Writes String notes into .txt file.
def write_txt(clss, date, title, body):
    note = open(clss + "/" + date + " " + title +  ".txt", "w")
    note.write(date + " " + title + "\n")
    note.write(body)

# Main method to run the functions.
if __name__ == '__main__':
    clss_in = "BigRed"
    date_in = "9-17-17"
    title_in = "QNote"
    body_in = "Created at BigRed//Hacks 2017!"
    crt_class(clss_in)
    write_txt(clss_in, date_in, title_in, body_in)
