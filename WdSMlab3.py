# Generowanie dlugosci rozmowy zgodnie z rozkladem Gaussa
# Parametry: srednia, odchylenie, min, max

def gaussian_call(mean,std,min_val,max_val):
    while True:
        t=random.gauss(mean,std)  # rozklad normalny (Gauss)
        if min_val<=t<=max_val:
            return int(t)

# START SYMULACJI

def start():
    # PARAMETRY SYMULACJI (z treści zadania)

    channels=int(entry_channels.get())      # liczba kanalow S
    lambda_rate=float(entry_lambda.get())   # λ – natezenie ruchu (Poisson)
    mean_call=float(entry_mean.get())       # N – srednia dlugosc rozmowy
    std_call=float(entry_std.get())         # σ – odchylenie standardowe
    min_call=int(entry_min.get())           # minimalna dlugosc rozmowy
    max_call=int(entry_max.get())           # maksymalna dlugosc rozmowy
    queue_limit=int(entry_queue.get())      # dlugosc kolejki
    simulation_time=int(entry_time.get())   # czas symulacji

    # Stan systemu

    channels_state=[0]*channels   # tablica kanalow (czas rozmowy w kanalach)
    queue=[]                      # kolejka oczekujacych

    served=0                      # liczba obsluzonych polaczen
    rejected=0                    # liczba odrzuconych polaczen

    # listy do wykresow
    Q_values=[]
    W_values=[]
    rho_values=[]

    queue_lengths=[]
