# encoding: utf-8 
# usamos esta codificacion ya que en algunos casos nos dio error.
import sys
import string
import time
from tweepy import Stream
from tweepy.streaming import StreamListener
#get_twitter_auth.py esto lo llamamos es como el include en c/c++.
from twitter_client import get_twitter_auth

class CustomListener(StreamListener):

    def __init__(self, fname):
        safe_fname = format_filename(fname)
        #nombre del archivo streaam
        self.outfile = "miStream.json"

    def on_data(self, data):
		
        try:
			print(data);
			# el 'a' anadir  es que cualquier dato a guardar se va al final de archivo.
			with open(self.outfile, 'a') as f:
				f.write(data)
				return True
        except BaseException as e:
            sys.stderr.write("Error en esta dato: {}\n".format(e))
            time.sleep(5)
        return True

    def on_error(self, status):
        if status == 420:
            sys.stderr.write("se ha accedido el limite\n".format(status))
            return False
        else:
			# en caso que ocurrar un error, esto nos paso cuando era otro idioma.
            sys.stderr.write("Error {}\n".format(status))
            return True

def format_filename(fname):
    return ''.join(convert_valid(one_char) for one_char in fname)


def convert_valid(one_char):
    valid_chars = "-_.%s%s" % (string.ascii_letters, string.digits)
    if one_char in valid_chars:
        return one_char
    else:
        return '_'

if __name__ == '__main__':
	#colocar todo lo que se desea buscar hay que recordar que twitter no identifica los tildes, papa ==  papá ambos son iguales
    query = [
    'guatemala',
    'nomadagt',
    'prensalibre'
    ]
    query_fname = ' '.join(query)
    auth = get_twitter_auth()
    twitter_stream = Stream(auth, CustomListener(query_fname))
    # async funcion que hace que sea asingrono asi nunca nos aparecera que abusamos del api.
    twitter_stream.filter(track=query,languages=['es'], async=True)
