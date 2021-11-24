
def get_datas(current_score):
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
{scores}
    """
    return scores_formatted


def save_data(name, score):
    name_info = name

    with open("scores.txt", "r") as f:
        datas = f.read()

    datas += name_info + "__" + str(score) + "\n"

    with open("scores.txt", "w") as f:
        f.write(datas)


