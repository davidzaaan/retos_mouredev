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
import re

CELSIUS = "c"
FAHRENHEIT = "f"


def main() -> None:
    degrees: str = parse_degrees(sys.argv)

    if not degrees:
        print(generate_err_msg())
        return
    
    print(calc_degrees(degrees))


def calc_degrees(degrees: str) -> str:
    """
        Returns the calculated degrees in a string formatted object

        degrees [str]
            The degrees string parsed to calculate
        
        Returns:
            String with the degrees calculated either Fahrenheit or Celsius accordingly
    """
    unity_measure: str = degrees.split("°")[-1].lower() # C (Celsius) or F (Fahrenheit)
    degrees_to_convert: str = int(degrees.split("°")[0]) # Separator

    if unity_measure == CELSIUS:
        converted_degrees: int = fahrenheit(degrees_to_convert)

        if converted_degrees > 78:
            return f"{degrees} = {converted_degrees}°F \n{heat_comments()}"
        elif converted_degrees < 56:
            return f"{degrees} = {converted_degrees}°F \n{cold_comments()}"
        
        return f"{degrees} = {converted_degrees}°F"

    elif unity_measure == FAHRENHEIT:
        converted_degrees: int = celsius(degrees_to_convert)

        if converted_degrees > 21:
            return f"{degrees} = {converted_degrees}°C \n{heat_comments()}"
        elif converted_degrees < 14:
            return f"{degrees} = {converted_degrees}°C \n{cold_comments()}"
        
        return f"{degrees} = {converted_degrees}°C"


def parse_degrees(params: str) -> str | None:
    """
        Parse the arguments given by the user via command-line

        params
            The command-line argv
        
        Return
            Parsed degrees in the format of 000°[C|F] or None if none valid arguments were given
    """
    if not len(params) != 2:
        # Checking that the params given are valid to make calculations
        _ = re.search("[0-9]+°[C|F]$", params[-1], re.IGNORECASE) # Looking for patterns i.e: 000°[C|F]

        if not _:
            return None
        else:
            return _.string # String form of the re.Match object
    else:
        return None


def celsius(degrees: str) -> float:
    """
        Function that return degrees given to Celsius degrees

        Param
            String containing the degrees to convert
    """
    return (degrees - 32) * (5 / 9)


def fahrenheit(degrees: str) -> float:
    """
        Function that return degrees given to Fahrenheit degrees

        Param
            String containing the degrees to convert
    """
    return (degrees * (9 / 5)) + 32


def generate_err_msg() -> str:
    """
        Function that generate random error messages
    """
    ERROR_WORDS = [
        "Oops, you mean apples?",
        "????",
        "Sorry I didn't get it. Could you try again? 😔",
        "Beep boop beep?",
        "Still not getting it 😿",
        "I think I get it, Try adding a '°' sign at the end 🤔💭"
        "Oops, Try adding a '°' sign at the end"
    ]

    return random.choice(ERROR_WORDS)


def cold_comments() -> str:
    """
        Function that returns random quotes if the degrees are low
    """
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
    """
        Function that returns random comments if the degrees are too high
    """
    HOT_WEATHER_COMMENTS = [
        "Finally summer baby 😎",
        "Hey wanna go to the beach? 🌴☀️",
        "What about some Coke? 🤤",
        "🥵",
        "Beep boop b...",
        "Lemonade please 🙏",
        "Summer means happy times and good sunshine ☀️😎",
        "If you're not barefoot, then you're overdressed 🥵",
        "Friends, sun... sun, and sun, that sounds like a summer to me 🤔💭"
    ]

    return random.choice(HOT_WEATHER_COMMENTS)



if __name__ == '__main__':
    main()