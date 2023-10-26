import tkinter as tk


# Nous allons créer une claculatrice avec tkinter(une dépendace permettant de créer des interfaces graphiques)

# La variable qui contient le calcul
calcul = ""

# fonction permettant l'afficahe des chiffres contenue dans le calcul dans l'interface graphique
def afficher_chiffre():
    global calcul
    text_resultat.delete(1.0, tk.END)
    text_resultat.insert(tk.END, calcul)

# cette fonction qui va permettre d'ajouter un caractère au calcul
def add_to_calcul(caractere):
    global calcul
    calcul = calcul + str(caractere)
    afficher_chiffre()


# une fois les caractères ajoutés on va réaliser le calcul et renvoyer un résultat à l'aide de cette fonction
def eval_calcul():
    global calcul
    try:
        calcul = str(eval(calcul))
        afficher_chiffre()
    except:
        clear_calcul()
        text_resultat.insert(tk.END, "Erreur")


# cette fonction va permettre de supprimer le dernier caractère du calcul
def clear_calcul():
    global calcul
    calcul = ""
    afficher_chiffre()

# création de la fenêtre et ajout des spécifications
root = tk.Tk()
root.title("Calculatrice")
root.geometry("325x410")

text_resultat = tk.Text(root, height=2, width=20, font=("Arial", 20))
text_resultat.grid(columnspan=5)

# création des boutons
button_values = list(range(1, 10))
for i, value in enumerate(button_values):
    row = (i // 3) + 1
    col = i % 3
    btn = tk.Button(root, text=str(value), command=lambda value=value: add_to_calcul(value), height=2, width=2, font=("Arial", 20))
    btn.grid(row=row, column=col, padx=5, pady=5)

#bouton pour le 0
btn = tk.Button(root, text="0", command=lambda: add_to_calcul(0), height=2, width=2, font=("Arial", 20))
btn.grid(row=4, column=1, padx=5, pady=5)

#bouton pour les opérations + paranthèses
operations = ["+", "-", "*", "/", "(", ")"]
for i, value in enumerate(operations):
    btn = tk.Button(root, text=value, command=lambda value=value: add_to_calcul(value), height=2, width=2, font=("Arial", 20))
    btn.grid(row=i, column=5, padx=5, pady=5)

#bouton pour le =
btn = tk.Button(root, text="=", command=lambda: eval_calcul(), height=2, width=2, font=("Arial", 20) )
btn.grid(row=4, column=2, padx=5, pady=5)

#bouton pour le clear
btn = tk.Button(root, text="C", command=lambda: clear_calcul(), height=2, width=2, font=("Arial", 20))
btn.grid(row=4, column=0, padx=5, pady=5)

#bouton pour le .
btn = tk.Button(root, text=".", command=lambda: add_to_calcul("."), height=2, width=2, font=("Arial", 20))
btn.grid(row=5, column=2, padx=5, pady=5)


root.mainloop()