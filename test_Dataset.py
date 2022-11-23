import Dataset
from colorama import Fore, Back, Style


# def test_getFields():
#     ds = Dataset(fields="nom_methode_dpe", size=10)
#     assert ds.getFields() == [
#         "nom_methode_dpe",
#         "version_methode_dpe",
#         "date_etablissement_dpe",
#         "consommation_energie",
#         "classe_consommation_energie",
#         "estimation_ges",
#         "classe_estimation_ges",
#         "annee_construction",
#         "surface_thermique_lot",
#         "latitude",
#         "longitude",
#         "tr001_modele_dpe_type_libelle",
#         "tr002_type_batiment_description",
#         "code_insee_commune_actualise",
#         "tv016_departement_code",
#     ]

# test to evaluate the capacity of the dataset to catch the size error
def test_getSize():
    ds = Dataset(fields="nom_methode_dpe", size=10)
    assert ds.getSize() == 10, "size should be 10"
    print(Fore.GREEN + "test_Dataset.py(size): test passed")

# test to evaluate the capacity of the dataset to catch the select error
def test_getSelect():
    ds = Dataset(select="nom_methode_dpe", size=10)
    assert ds.getSelect() == "nom_methode_dpe", "select shouldn't be empty"
    print(Fore.GREEN + "test_Dataset.py(select): test passed")


