



from Ingame import Score, name


def show_scores(current_score):
    #Funcion para printear resultados en la pantalla despues del juego y poder volver al menu principal
    global name
    Nombre = name.get()
    Punt_fin = f"""
    Gracias por 
    
    jugar Submarine escape! 
    
    He aca los datos de su partida
    
    Puntaje:
    {current_score}
    
    Nombre:
    {Nombre}
    """

    return Punt_fin

def get_datas(current_score):
    save_data()
    with open("scores.txt", "r") as file:
        # Leer y dividir la informacion para dar formato
        scores = [n.split("__") for n in file.read().split("\n") if len(n) >= 4]
        # Organizar la lista de puntajes
        scores.sort(key=lambda i: int(i[1]))
        # Arreglo para invertir la lista de puntajes, para asi poder mostrar de mayor a menor
        scores = list(reversed(scores))

    if len(scores) > 10:
        scores = scores[:10]
        #aca, se hace que el programa se muestre solo los 10 mejores resultados

    def format_name(name,score):
        if len(name) > 10:
            name = name[:10] + "..."
        goal = 13 - len(name)
        total_name = name+" "*goal
        return f"NAME: {total_name} | SCORE: {score}"

    scores = "\n".join(format_name(n,s) for n, s in scores)
    scores_formatted = f"""
    Felicidades, su puntaje es de: {current_score}
{scores}
    """
    return scores_formatted


def save_data():
    global name, Score 
    name_info = name.get()

    with open("scores.txt", "r") as f:
        datas = f.read()

    datas += name_info + "__" + str(Score) + "\n"

    with open("scores.txt", "w") as f:
        f.write(datas)

