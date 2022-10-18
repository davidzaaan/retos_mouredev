"""
/*
 * Enunciado: Crea una función que transforme grados Celsius en Fahrenheit
 * y viceversa.
 *
 * - Para que un dato de entrada sea correcto debe poseer un símbolo "°" 
 *   y su unidad ("C" o "F").
 * - En caso contrario retornará un error.
 * - ¿Quieres emplear lo aprendido en este reto?
 *   Revisa el reto mensual y crea una App: 
 *   https://retosdeprogramacion.com/mensuales2022
 */
"""
import random
import sys


def main() -> None:
    degrees: float = parse_degrees(sys.argv)
    # TODO
    # Add logic to play with the comments



def parse_degrees(degrees: str) -> str | None:
    # TODO
    # Parse the command line arguments that will come with flags
    # i.e python reto_42.py 45° to [c|C]|[f|F]


    if not degrees.endswith("°") or \
       not degrees[:-1].isdigit():
        return None

    return degrees[:-1] # returning the numeric part


def celsius(degrees: str) -> float:
    return (degrees - 32) * (5 / 9)


def fahrenheit(degrees: str) -> float:
    return (degrees * (9 / 5)) + 32


def generate_err_msg(text: str) -> str:
    ERROR_WORDS = [
        "Oops, you mean apples?",
        f"{text} Bananas?",
        "Sorry I didn't get it. Could you try again? 😔",
        f"Beep boop beep?",
        "Still not getting it 😿",
        "I think I get it, Try adding a '°' sign at the end 🤔💭"
        "Oops, Try adding a '°' sign at the end"
    ]

    return random.choice(ERROR_WORDS)


def cold_comments() -> str:
    COLD_WEATHER_COMMENTS = [
        "Sheesh, its freezing here 🥶❄️",
        "Hey if you make chocolate, I don't mind if you bring me a bit 😳🥺",
        "Can somebody turn off the A/C?",
        "Ice cold baby 💎",
        "I wish I was a penguin 🐧😔",
        "Could you bring me some blanket? 🥺",
        "Nothing burns like the cold \n George R.R Martin ☃️",
        "Ho Ho Ho is coming"
    ]

    return random.choice(COLD_WEATHER_COMMENTS)


def heat_comments() -> str:
    HOT_WEATHER_COMMENTS = [
        "Finally summer baby 😎",
        "Hey wanna go to the beach? 🌴☀️",
        "What about some Coke? 🤤",
        "🥵",
        "Beep boop b...",
        "Lemonade please 🙏",
        "Summer means happy times and good sunshine ☀️😎",
        "If you're not barefoot, then you're overdressed 🥵",
        "Friends, sun, sun, and sun, that sounds like a summer to me 🤔💭"
    ]

    return random.choice(HOT_WEATHER_COMMENTS)



if __name__ == '__main__':
    main()