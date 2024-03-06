from aiogram import Bot, Dispatcher, executor, types
from deep_translator import GoogleTranslator
import config
import logging
import re

logging.basicConfig(level=logging.INFO)

#initialization of the bot
bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)

 
language_dict = {
    "афарский": "aa",
    "абхазский": "ab",
    "авестийский": "ae",
    "африкаанс": "af",
    "аймара": "ay",
    "азербайджанский": "az",
    "башкирский": "ba",
    "белорусский": "be",
    "болгарский": "bg",
    "бишнуприйский": "bi",
    "бамбара": "bm",
    "бенгальский": "bn",
    "тибетский": "bo",
    "бретонский": "br",
    "боснийский": "bs",
    "каталанский": "ca",
    "чеченский": "ce",
    "чаморро": "ch",
    "корсиканский": "co",
    "креольский": "cr",
    "чешский": "cs",
    "чувашский": "cv",
    "валлийский": "cy",
    "датский": "da",
    "немецкий": "de",
    "дзонг-кейский": "dz",
    "эве": "ee",
    "греческий": "el",
    "английский": "en",
    "эсперанто": "eo",
    "испанский": "es",
    "эстонский": "et",
    "баскский": "eu",
    "персидский": "fa",
    "фулах": "ff",
    "финский": "fi",
    "фиджийский": "fj",
    "фарерский": "fo",
    "французский": "fr",
    "фризский": "fy",
    "ирландский": "ga",
    "гэльский": "gd",
    "галисийский": "gl",
    "гуарани": "gn",
    "гуджарати": "gu",
    "маньский": "gv",
    "гаитянский креольский": "ht",
    "хауса": "ha",
    "хинди": "hi",
    "хиримото": "ho",
    "хорватский": "hr",
    "венгерский": "hu",
    "армянский": "hy",
    "интерлингва": "ia",
    "интерлингве": "ie",
    "инуктитут": "iu",
    "индонезийский": "id",
    "исландский": "is",
    "итальянский": "it",
    "ингушский": "inh",
    "игбо": "ig",
    "японский": "ja",
    "яванский": "jv",
    "грузинский": "ka",
    "конго": "kg",
    "каннада": "kn",
    "казахский": "kk",
    "гренландский": "kl",
    "кхмерский": "km",
    "корейский": "ko",
    "кашубский": "csb",
    "курук": "ku",
    "киргизский": "ky",
    "латинский": "la",
    "люксембургский": "lb",
    "ганда": "lg",
    "лимбургский": "li",
    "лингала": "ln",
    "лаосский": "lo",
    "литовский": "lt",
    "латышский": "lv",
    "малагасийский": "mg",
    "маршалльский": "mh",
    "маори": "mi",
    "македонский": "mk",
    "малайский": "ms",
    "малаялам": "ml",
    "монгольский": "mn",
    "маратхи": "mr",
    "мальтийский": "mt",
    "бирманский": "my",
    "науру": "na",
    "норвежский (букмол)": "nb",
    "ндебеле, южный": "nr",
    "непальский": "ne",
    "нидерландский": "nl",
    "ндебеле, северный": "nd",
    "норвежский (нюнорск)": "nn",
    "ндонга": "ng",
    "непали": "ne",
    "чева": "ny",
    "окситанский": "oc",
    "оджибва": "oj",
    "ория": "or",
    "оромо": "om",
    "осетинский": "os",
    "панджаби": "pa",
    "пали": "pi",
    "польский": "pl",
    "пушту": "ps",
    "португальский": "pt",
    "кечуа": "qu",
    "ретороманский": "rm",
    "румынский": "ro",
    "рунди": "rn",
    "русский": "ru",
    "киньяруанда": "rw",
    "санскрит": "sa",
    "сардинский": "sc",
    "синдхи": "sd",
    "санго": "sg",
    "сербский": "sr",
    "гэльский": "gd",
    "сингальский": "si",
    "словацкий": "sk",
    "словенский": "sl",
    "самоанский": "sm",
    "шона": "sn",
    "сомали": "so",
    "албанский": "sq",
    "сербский": "sr",
    "свази": "ss",
    "сото, южный": "st",
    "сунданский": "su",
    "шведский": "sv",
    "суахили": "sw",
    "тамильский": "ta",
    "телугу": "te",
    "таджикский": "tg",
    "тайский": "th",
    "тигринья": "ti",
    "таитянский": "ty",
    "туркменский": "tk",
    "тагалог": "tl",
    "тсвана": "tn",
    "тонганский": "to",
    "турецкий": "tr",
    "тсонга": "ts",
    "татарский": "tt",
    "тви": "tw",
    "таитянский": "ty",
    "уйгурский": "ug",
    "украинский": "uk",
    "урду": "ur",
    "узбекский": "uz",
    "вьетнамский": "vi",
    "волапюк": "vo",
    "валлийский": "wa",
    "волоф": "wo",
    "коса": "xh",
    "идиш": "yi",
    "янгбене": "yo",
    "юоруба": "yo",
    "коса": "za",
    "зулусский": "zu"
}
 
@dp.message_handler()
async def main(message: types.Message):
        if message.text.lower().startswith("/info t"):
         await bot.send_message(message.chat.id, "<b>Приветствую! Я бот-переводчик ваших сообщений!\nЕсли вам нужно что-то перевести, напишите: <i>/t  'текст для перевода' 'язык, на который перевести'</i></b>",  parse_mode=types.ParseMode.HTML)
        if message.text.lower().startswith("/start"):
         await bot.send_message(message.chat.id, "<b>Приветствую! Я бот-переводчик ваших сообщений!\nЕсли вам нужно что-то перевести, напишите: <i>\n/t  'текст для перевода' 'язык, на который перевести'</i></b>",  parse_mode=types.ParseMode.HTML)
        if message.text.lower().startswith("/t"):
         message_for_translate = message.text.lower().split()
         text_to_translate = message_for_translate[1:][:-1]
         language = message_for_translate[-1]
         target_language = language_dict.get(language)
         translate_text = ' '.join(text_to_translate)
         # Текст, который нужно перевести
         print(message_for_translate)
         print(text_to_translate)
         print(translate_text)
         print(target_language)
         


#translation from English into the specified one
         translated_text = GoogleTranslator(source='auto', target=target_language).translate(translate_text)

#output of the translated text
         print("Translated Text:", translated_text) 
         await bot.send_message(message.chat.id, translated_text, reply_to_message_id=message.message_id)

        
  
if __name__ =="__main__":
    executor.start_polling(dp, skip_updates=True)