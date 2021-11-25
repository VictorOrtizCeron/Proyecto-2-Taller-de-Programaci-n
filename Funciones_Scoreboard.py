from os import close


def get_datas(current_score):
    scores = read_data_recurse(open("scores.txt",'r').readlines())
    scores.sort(key=lambda x: int(x[1]))
    scores = list(reversed(scores))

    if len(scores) > 10:
        scores = scores[:10]

    def format_name(name,score):
        if len(name) > 10:
            name = name[:10] + "..."
        goal = 13 - len(name)
        total_name = name+" "*goal
        return f"NAME: {total_name} | SCORE: {score}"

    scores = "\n".join(format_name(n,s) for n, s in scores)
    scores_formatted = f"""
{scores}
    """
    return scores_formatted
    

def read_data_recurse(lines, scores=[]):
  if len(lines) == 0:
    return scores
  elif len(scores) > 10:
    return scores
  else:
    n = lines[0]
    if len(n) >= 4:
      scores.append(n.split("__"))
    return read_data_recurse(lines[1:],scores)
#save_data es una funcion para poder guardar los datos en el archivo de texto
def save_data(name, score):
    name_info = name

    with open("scores.txt", "r") as f:
        datas = f.read()
        #leer el archivo de texto y guardarlo en una variable
    datas += name_info + "__" + str(score) + "\n"
    #concatenar la informacion del nombre y el puntaje

    with open("scores.txt", "w") as f:
        f.write(datas)
        #escribir la informacion en el archivo de texto

"""
 Instituto Tecnológico de Costa Rica
                    Ingeniería en Computadores

    Lenguaje: Python 3.9.6
    Autores:  Victor Ortiz Ceron(vortiz@estudiantec.cr) , José Ignacio Castillo()
    Tutor: Ramses Gutiérrez
    Versión: 1.0
    Fecha última Modificación: 24/11/2021
    Módulo: Funciones_Scoreboard.py
    Descripción del módulo: Este modulo se encarga de poder hacer que la scoreboard funcione, en este caso usando get datas y read data para poder extraer la informacion de puntajes y
    ordenarla para el display que lo hace el scoreboard.py, 
    Entradas: Score, Name y scores.txt
    Salidas: Escribir en scores.txt, y retornar la informacion de los puntajes en formato de string.
"""