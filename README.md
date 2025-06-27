# topnienie_lodu

Program symuluje topnienie lodu w skali mikro. Przedstawia sytuację, w której w kostkę lodu uderzają cząstki energii. Kostka jest przedstawiona w 2D - kwadrat n x n. Kwadrat ten to siatka złożona z cząstek wody połączonych wiązaniami wodorowymi. 
W cząstki wody uderzają cząstki energii, które nadlatują z różnych stron ekranu pod różnym kątem i wprawiają w drgania cząstki wody. Jeżeli cząstka wody oddali się za bardzo od innej, z którą jest połączona, to dochodzi do zerwania wiązania wodorowego między nimi. Jeśli cząstka nie ma żadnych wiązań wodorowych, to odrywa się i znika z ekranu.

settings.py - odpowiedzialny za podstawowe ustawienia: wielkość siatki, wielkość okna, liczba nadlatujących cząstek energii, kolory elementów;

grid.py - odpowiada za generowanie siatki;

energy_el.py - odpowiada za cząstkę nadlatującej energii;

point.py - odpowiada za cząstkę wody;

connection.py - odpowiada za wiązania wodorowe;

views.py - odpowiada za to, co się dzieje na ekranie;

main.py - uruchamiając ten plik, uruchamiamy program i ustawiamy ilość krawędzi ekranu, z których nadlatują cząstki energii (od 1 do 4). 
