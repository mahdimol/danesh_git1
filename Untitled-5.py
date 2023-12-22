# این یک کد پایتونی است
# این یک نظر است و توسط پایتون اجرا نمی‌شود

# تعریف یک دیکشنری برای ترجمه کلمات انگلیسی به فارسی
dictionary = {
    "hello": "salam",
    "goodbye": "khodafez",
    "say": "goftan",
    "we": "ma",
    "you": "shoma"
}

# چاپ یک پیام خوش‌آمدگویی
print("Hello, this is a Python program.")

# دریافت یک کلمه انگلیسی از کاربر
word = input("Please enter an English word: ")

# بررسی اینکه کلمه در دیکشنری وجود دارد یا خیر
if word in dictionary:
    # چاپ ترجمه فارسی کلمه
    print("The Persian translation of " + word + " is " + dictionary[word] + ".")
else:
    # چاپ پیامی که کلمه یافت نشد
    print("Sorry, the word " + word + " is not in the dictionary.")

# چاپ یک جمله انگلیسی و ترجمه فارسی آن
sentence = "We say goodbye to you tonight."
print(sentence)
translation = dictionary["we"] + " " + dictionary["say"] + " " + dictionary["goodbye"] + " " + dictionary["you"] + " tonight."
print(translation)
