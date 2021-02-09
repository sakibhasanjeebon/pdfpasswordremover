import pikepdf

# write the pdf name without suffix (.pdf)
pdf__name = "11"

# path of the file where pdf is right now
path = "C:\\Users\\Sakib\\Desktop\\"

# source path of pdf
pdf_name = path + pdf__name+".pdf"

# output path of pdf
pdf_name_output = path + pdf__name + "_unsecured.pdf"

# import of pdf file
pdf = pikepdf.open(pdf_name)

# output of pdf file
pdf.save(pdf_name_output)
