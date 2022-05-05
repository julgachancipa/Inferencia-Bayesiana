import pandas as pd


def create_red_bay():
    red_bay = {}
    new_node = True

    print("¿Deseas añadir un nuevo nodo? (si-no)")
    new_node = input().lower()
    new_node = True if new_node == "si" else False

    while new_node:

        print("Ingresa el nombre del nodo:")
        node = input().lower()

        depende = True
        dependencias = []
        while depende:
            print("¿Depende de otro nodo? (si-no)")
            depende = input().lower()
            depende = True if depende == "si" else False

            if not depende:
                continue

            print("¿Cual?")
            dependencia = input().lower()
            dependencias.append(dependencia)

        red_bay[node] = dependencias

        print(red_bay)

        print("¿Deseas añadir un nuevo nodo? (si-no)")
        new_node = input().lower()
        new_node = True if new_node == "si" else False

    return red_bay


def create_df_nodos(red_bay):
    df_nodos = {}

    for node in red_bay.keys():
        df_nodos[node] = pd.read_csv(f"./data/{node}.csv")

    return df_nodos


def create_consulta(nodos):
    consulta = {}

    print("Probabilidad de ... si ...")
    for nodo in nodos:
        print(f"{nodo}: ", end="")
        consulta[nodo] = input().lower()

    return consulta

def calculate_probabilidad(consulta, red_bay, df_nodos):
    p = 1

    for nodo in consulta.keys():
        # print(">>", nodo)
        df_nodo = df_nodos[nodo]
        # print(df_nodo)
        for dependencia in red_bay[nodo]:
            # print(">>>", dependencia)
            df_nodo = df_nodo[df_nodo[dependencia]==consulta[dependencia]]
            print(df_nodo)

        p = p * float(df_nodo[consulta[nodo]])
        
    return p

    

if __name__ == "__main__":
    print("Inferencia Bayesiana")

    # red_bay = create_red_bay()
    red_bay = {
        "rain": [],
        "maintenance": ["rain"],
        "train": ["rain", "maintenance"],
        "appointment": ["train"],
    }
    print(red_bay)

    df_nodos = create_df_nodos(red_bay)
    # print(df_red_bay)

    consulta = create_consulta(list(red_bay.keys()))
    print(consulta)

    p = calculate_probabilidad(consulta, red_bay, df_nodos)

    print(p)