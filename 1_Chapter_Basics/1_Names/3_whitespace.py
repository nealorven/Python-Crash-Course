# lang_py = lang_py.strip(" Python ") | Усеченное значение
# \t - tab
# \n - new row

lang = "Languages:\n\tPython\n\tC\n\tJavaScript"
print(lang)

# Languages:
#        Python
#        C
#        JavaScript

lang_py = " Python "
print(lang_py.lstrip())
print(lang_py.rstrip())
print(lang_py.strip())

# "Python_"
# "_Python"
# "Python"
