
import pickle
import requests
from bs4 import BeautifulSoup

def create_places_pickle():
    places = [
        "دانشگاه صنعتی",
        "مجموعه ورزشی",
        "مغازه",
        "نمایشگاه",
        "سینما",
        "سینمای",
        "پارک",
        "موزه",
        "ورزشگاه",
        "باشگاه",
        "رستوران",
        "کافه",
        "پاساژ",
        "کترینگ",
        "شرکت",
        "دانشگاه",
        "مدرسه",
        "مسجد",
        "راسته",
        "تیمچه",
        "بازار",
        "درمانگاه",
        "بیمارستان",
        "حسینیه",
        "دبستان",
        "دبیرستان",
        "دانشکده",
        "آزمایشگاه",
        "تعمیرگاه",
        "مکانیکی",
        "آتلیه",
        "رادیولوژی",
        "سونو",
        "گرافی",
        "نانوایی",
        "بولینگ",
        "تولیدی",
        "کارخانه",
        "قهوه خانه",
        "چای خانه",
        "سفره خانه",
        "فودکورت",
        "مجتمع تجاری",
        "داروخانه",
        "مجلس شورای",
        "ریاست",
        "قوه",
        "دادگاه",
        "دادسرای",
        "بیت ",
        "دفتر",
        "حوزه ی علمیه",
        "حرم",
        "فدراسیون",
    ]
    return places

def create_cities_phone_pickle(): 
    cities_phone = [
        41,
        44,
        45,
        31,
        84,
        77,
        21,
        38,
        51,
        56,
        58,
        61,
        24,
        23,
        54,
        71,
        26,
        25,
        28,
        87,
        34,
        83,
        74,
        17,
        13,
        66,
        11,
        86,
        76,
        81,
    ]
    return cities_phone

def create_countries_pickle():
    countries = [
        "آندورا",
        "امارات متحده عربی",
        "افغانستان",
        "آنتیگوا",
        "باربودا",
        "آنگویلا",
        "آلبانی",
        "ارمنستان",
        "آنگولا",
        "جنوبگان",
        "آرژانتین",
        "ساموآی آمریکا",
        "اتریش",
        "استرالیا",
        "آروبا",
        "جزایر آلند",
        "جمهوری آذربایجان",
        "بوسنی و هرزگوین",
        "باربادوس",
        "بنگلادش",
        "بلژیک",
        "بورکینا فاسو",
        "بلغارستان",
        "بحرین",
        "بوروندی",
        "بنین",
        "سنت بارثلمی",
        "برمودا",
        "برونئی",
        "بولیوی",
        "هلند کارائیب",
        "برزیل",
        "باهاما",
        "بوتان",
        "جزیره بووه",
        "بوتسوانا",
        "بلاروس",
        "بلیز"
        "کانادا"
        "جزایر کوکوس",
        "جمهوری دموکراتیک کنگو",
        "جمهوری آفریقای مرکزی",
        "جمهوری کنگو",
        "سوئیس",
        "ساحل عاج",
        "جزایر کوک",
        "شیلی",
        "کامرون",
        "چین",
        "کلمبیا",
        "کاستاریکا",
        "کوبا",
        "کیپ ورد",
        "کوراسائو",
        "جزیره کریسمس",
        "قبرس",
        "جمهوری چک",
        "آلمان",
        "جیبوتی",
        "دانمارک",
        "دومینیکا",
        "دومینیکا",
        "الجزایر",
        "اکوادور",
        "استونی",
        "مصر",
        "صحرای غربی",
        "اریتره",
        "اسپانیا",
        "اتیوپی",
        "فنلاند",
        "فیجی",
        "جزایر فالکلند",
        "ایالات فدرال میکرونزی",
        "جزایر فارو",
        "فرانسه",
        "گابن",
        "انگلستان",
        "انگلیس",
        "گرانادا",
        "گرجستان",
        "گویان",
        "فرانسه",
        "گرنزی",
        "غنا",
        "جبل الطارق",
        "گرینلند",
        "گامبیا",
        "گینه",
        "جزیره گوادلوپ",
        "گینه استوایی",
        "یونان",
        "جزایر جورجیای جنوبی و ساندویچ جنوبی",
        "گواتمالا",
        "گوام",
        "گینه بیسائو",
        "گویان",
        "هنگ کنگ",
        "جزیره هرد و جزایر مک دونالد",
        "هندوراس",
        "کرواسی",
        "هائیتی",
        "مجارستان",
        "اندونزی",
        "جمهوری ایرلند",
        "جزیره منهند",
        "قلمروی ",
        "اقیانوس هند بریتانیا",
        "عراق",
        "ایران",
        "ایسلند",
        "ایتالیا",
        "ادبیات",
        "جامائیکا",
        "اردن",
        "ژاپن",
        "کنیا",
        "قرقیزستان",
        "کامبوج",
        "کیریباتی",
        "کومور",
        "سنت کیتس و نویس",
        "کره شمالی",
        "کره جنوبی",
        "کویت",
        "جزایر کیمن",
        "قزاقستان",
        "لائوس",
        "لبنان",
        "سنت لوسیا",
        "لیختن اشتاین",
        "سری لانکا",
        "لیبریا",
        "لسوتو",
        "لیتوانی",
        "لوکزامبورگ",
        "لتونی",
        "لیبی",
        "مراکش",
        "موناکو",
        "مولداوی",
        "مونته نگرو",
        "سنت مارتین فرانسه",
        "ماداگاسکار",
        "جزایر مارشال",
        "جمهوری مقدونیه",
        "مالی",
        "میانمار",
        "مغولستان",
        "ماکائو",
        "جزایر ماریانای شمالی",
        "مارتینیک",
        "موریتانی",
        "مونتسرات",
        "مالت",
        "موریس",
        "مالدیو",
        "مالاوی",
        "مکزیک",
        "مالزی",
        "موزامبیک",
        "نامیبیا",
        "کالدونیای جدید",
        "نیجر",
        "جزیره نورفولک",
        "نیجریه",
        "نیکاراگوئه",
        "هلند",
        "نروژ",
        "نپال",
        "نائورو",
        "نیوئه",
        "نیوزلند",
        "عمان",
        "پاناما",
        "پرو",
        "پلینزی فرانسه",
        "پاپوآ گینه نو",
        "فیلیپین",
        "پاکستانلهستان",
        "سنت پیر و ماژلان",
        "جزایر پیت کرن",
        "پورتوریکو",
        "فلسطین",
        "پرتغال",
        "پالائو",
        "پاراگوئه",
        "قطر",
        "ریونیون",
        "رومانی",
        "صربستان",
        "روسیه",
        "رواندا",
        "عربستان سعودی",
        "جزایر سلیمان",
        "سیشل",
        "سودان",
        "سوئد",
        "سنگاپور",
        "سینت هلینا",
        "اسلوونی"
        "سوالبارد و یان ماین",
        "اسلواکی",
        "سیرالئون",
        "سن مارینو",
        "سنگالسومالی",
        "سورینام",
        "سائوتومه و پرینسیپ",
        "السالوادور",
        "سنت مارتین هلند",
        "سوریه",
        "سوازیلند",
        "جزایر تورکس و کایکوس",
        "چاد",
        "سرزمین های قطب جنوب و جنوبی فرانسه",
        "توگو",
        "تایلند",
        "تاجیکستان",
        "توکلائو",
        "تیمور شرقی",
        "ترکمنستان",
        "تونس",
        "تونگا",
        "ترکیه",
        "ترینیداد و توباگو",
        "تووالو",
        "تایوان",
        "تانزانیا",
        "اوکراین",
        "اوگاندا",
        "جزایر کوچک حاشیه ای آمریکا",
        "ایالات متحده",
        "اروگوئه",
        "ازبکستان",
        "شهر واتیکان",
        "سنت وینسنت و گرنادین",
        "ونزوئلا",
        "بریتانیا",
        "بریتانیای کبیر",
        "جزایر ویرجین بریتانیا",
        "جزایر ویرجین ایالات متحده آمریکا",
        "ویتنام",
        "وانواتو",
        "والیس و فوتونا",
        "ساموآ",
        "یمن",
        "مایوت",
        "آفریقای جنوبی",
        "زامبیا",
        "زیمبابوه",
    ]
    return countries

def create_province_pickle():
    provinces_list = [
        "اذربایجان",
        "آذربایجان",
        "اذربایجان شرقی",
        "آذربایجان شرقی",
        "اذربایجان غربی",
        "آذربایجان غربی",
        "اردبیل",
        "اصفهان",
        "البرز",
        "ایلام",
        "بوشهر",
        "تهران",
        "چهارمحال و بختیاری"
        "چهارمحال"
        "خراسان جنوبی",
        "خراسان رضوی",
        "خراسان",
        "خراسان شمالی",
        "خوزستان",
        "زنجان",
        "سمنان",
        "سیستان و بلوچستان",
        "سیستان",
        "بلوچستان",
        "فارس",
        "قزوین",
        "قم",
        "کردستان",
        "کرمان",
        "کرمانشاه",
        "کهگیلویه و بویر احمد",
        "کهگیلویه و بویراحمد",
        "کهگیلویه",
        "گلستان",
        "لرستان",
        "گیلان",
        "مازندران",
        "مرکزی",
        "هرمزگان",
        "همدان",
        "یزد",
    ] 
    return provinces_list

def create_cities_pickle():
    cities = [
    "تبریز",
    "ارومیه",
    "اردبیل",
    "اصفهان",
    "کرج",
    "ایلام",
    "بوشهر",
    "تهران",
    "شهرکرد",
    "بیرجند",
    "مشهد",
    "بجنورد",
    "اهواز",
    "زنجان",
    "سمنان",
    "زاهدان",
    "شیراز",
    "قزوین",
    "قم",
    "سنندج",
    "کرمان",
    "کرمانشاه",
    "یاسوج",
    "خرم آباد",
    "رشت",
    "ساری",
    "اراک",
    "بندر عباس",
    "همدان",
    "یزد",
    ]
    
    URL = "https://fa.wikipedia.org/wiki/%D8%B4%D9%87%D8%B1%D8%B3%D8%AA%D8%A7%D9%86%E2%80%8C%D9%87%D8%A7%DB%8C_%D8%A7%DB%8C%D8%B1%D8%A7%D9%86"
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib
    tables = []
    divs = soup.table.select('a', )
    return cities


if __name__ == "__main__":
    res = create_places_pickle()
    with open("places.pickle", "wb") as f:
        pickle.dump(res, f, protocol=pickle.HIGHEST_PROTOCOL)