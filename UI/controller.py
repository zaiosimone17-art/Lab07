import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.biblioteca_selezionata = None
        self.genere_selezionato = None

    # POPOLA DROPDOWN
    def populate_dropdowns(self):
        self._view.dd_biblioteca.options.append(ft.dropdown.Option(key="NONE", text="Nessun filtro"))
        biblioteche = self._model.get_biblioteche()
        if biblioteche:
            for b in biblioteche:

                self._view.dd_biblioteca.options.append(ft.dropdown.Option(key=str(b.id), text=b.nome))

        self._view.dd_genere.options.append(ft.dropdown.Option(key="NONE", text="Nessun filtro"))
        generi = self._model.get_generi()
        if generi:
            for g in generi:
                self._view.dd_genere.options.append(ft.dropdown.Option(key=g, text=g))

    # CALLBACKS DROPDOWN
    def read_biblioteca(self, e):
        valore = self._view.dd_biblioteca.value
        if valore == "NONE" or valore is None:
            self.biblioteca_selezionata = None
        else:
            self.biblioteca_selezionata = int(valore)

    def read_genere(self, e):
        valore = self._view.dd_genere.value
        if valore == "NONE" or valore is None:
            self.genere_selezionato = None
        else:
            self.genere_selezionato = valore

    # AZIONE: MOSTRA LIBRI
    def handle_mostra_libri(self, e):
        self._view.lst_libri.controls.clear()


        libri = self._model.get_libri_filtrati(self.biblioteca_selezionata, self.genere_selezionato)

        if not libri or len(libri) == 0:
            self._view.show_alert("Nessun libro trovato con i criteri selezionati.")
        else:
            for l in libri:
                self._view.lst_libri.controls.append(ft.Text(str(l)))

        self._view.update()